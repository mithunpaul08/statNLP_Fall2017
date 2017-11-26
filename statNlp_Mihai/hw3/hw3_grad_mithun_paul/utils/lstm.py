import sys
import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from tqdm import tqdm
import re
torch.manual_seed(1)

#create a dictionary (which will be filled later, to store the unique words and its indexes)
wordsAndIndices = {}


#create a similar hash table for all the pos tags and give it an index
tagsAndIndices = {}


def prepare_sequence(seq, to_ix):
    idxs = [to_ix[w] for w in seq]
    tensor = torch.LongTensor(idxs)
    return autograd.Variable(tensor)



def getIndex(w, to_ix):
    #idxs=[0, 1, 2, 3, 4]
    #print(w)
    idxs = [to_ix[w]]
    #print(idxs)
    #print("just printed indices")
    tensor = torch.LongTensor(idxs)
    return autograd.Variable(tensor)

# def prepare_sequence():
#     idxs=[0, 1, 2, 3, 4]
#     #idxs = [to_ix[w] for w in seq]
#     tensor = torch.LongTensor(idxs)
#     return autograd.Variable(tensor)

#an array of sentences
sentence_collection=[]
# def prepare_training_data(posTrain):
#
#     #assign a unique id to each of the words
#     for word in posTrain["words"]:
#             if word not in wordsAndIndices:
#                 wordsAndIndices[word] = len(wordsAndIndices)
#
#
#
#     #assign a unique id to each of the words
#     for tag in posTrain["tags"]:
#             if tag not in tagsAndIndices:
#                 tagsAndIndices[tag] = len(tagsAndIndices)
#
#     print(tagsAndIndices)


EMBEDDING_DIM = 6
HIDDEN_DIM = 6

#
class LSTMTagger(nn.Module):

    def __init__(self, embedding_dim, hidden_dim, vocab_size, tagset_size):
        super(LSTMTagger, self).__init__()
        self.hidden_dim = hidden_dim

        self.word_embeddings = nn.Embedding(vocab_size, embedding_dim)
        print("size of word embeddings now is:")
        print((self.word_embeddings))

        self.lstm = nn.LSTM(embedding_dim, hidden_dim)

        self.hidden2tag = nn.Linear(hidden_dim, tagset_size)
        self.hidden = self.init_hidden()

    def init_hidden(self):
        return (autograd.Variable(torch.zeros(1, 1, self.hidden_dim)),
                autograd.Variable(torch.zeros(1, 1, self.hidden_dim)))

    def forward(self, sentence):
        embeds = self.word_embeddings(sentence)
        lstm_out, self.hidden = self.lstm(
            embeds.view(len(sentence), 1, -1), self.hidden)
        tag_space = self.hidden2tag(lstm_out.view(len(sentence), -1))
        tag_scores = F.log_softmax(tag_space)
        return tag_scores


def startLstm(posTrain):

    training_data=prepare_training_data(posTrain)
    model = LSTMTagger(EMBEDDING_DIM, HIDDEN_DIM, len(wordsAndIndices), len(tagsAndIndices))
    loss_function = nn.NLLLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.1)

    #temporarily check the weight scores that the model has learned. just to compare with later
    inputs = getIndex("every",wordsAndIndices)
    tag_scores = model(inputs)
    #print("weights before training:")
    #print(tag_scores)
    #sys.exit(1)

    counter=0

    #the actual training part
    #for epoch in range(300):
     #for sentence, tags in training_data:
    for index, row in tqdm(posTrain.iterrows(),total=len(posTrain)):

        #for word, tag in posTrain.items():
        model.zero_grad()
        model.hidden = model.init_hidden()
        word=row["words"]
        tag=row["tags"]
        #print("value of word is:"+word)
        #print("size of wordsAndIndices is:"+str(len(wordsAndIndices)))

        sentence_in = getIndex(word, wordsAndIndices)
        #print("value of sentence_in is:")
        #print(sentence_in.data)

        #print("value of tag is:"+tag)
        #print("size of tagsAndIndices is:"+str(len(tagsAndIndices)))


        targets = getIndex(tag, tagsAndIndices)
        #print("value of targets is:")
        #print(targets.data)


        tag_scores = model(sentence_in)

        loss = loss_function(tag_scores, targets)
        loss.backward()
        optimizer.step()

    #dev part
    inputs = getIndex("every",wordsAndIndices)
    tag_scores = model(inputs)
    #print("weights after training:")
    #print(tag_scores)
    values, indices = tag_scores.max(0)
    print("values:")
    print(values)
    print("indices:")
    print(indices)

    predicted_tag=tagsAndIndices[indices]
    print("predicted_tag:")
    print(predicted_tag)

    # #testing part
    # inputs = getIndex(testing_data[0], wordsAndIndices)
    # tag_scores = model(inputs)
    # print("weights after training:")
    #
    # print(tag_scores)

