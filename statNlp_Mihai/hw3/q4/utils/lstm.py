import sys
import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from tqdm import tqdm
import re
torch.manual_seed(1)

noofEpochs=1
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


def prepare_training_data(posTrain):

    for eachSent in tqdm(posTrain,total=len(posTrain),desc="test_data :"):
        # print("eachSent:")
        # print(eachSent)
        for eachWord in eachSent[0]:
                #print(eachWord)
                if eachWord not in wordsAndIndices:
                    wordsAndIndices[eachWord] = len(wordsAndIndices)

            #assign a unique id to each of the words
            # for tag in posTrain["tags"]:
            #         if tag not in tagsAndIndices:
            #             tagsAndIndices[tag] = len(tagsAndIndices)

    #print(tagsAndIndices)


def prepare_tags_data(posTrain):

    for eachSent in tqdm(posTrain,total=len(posTrain),desc="test_data :"):
        # print("eachSent:")
        # print(eachSent)
        for tag in eachSent[1]:
                if tag not in tagsAndIndices:
                    tagsAndIndices[tag] = len(tagsAndIndices)





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


def startLstm(training_data):

    prepare_tags_data(training_data)
    prepare_training_data(training_data)


    model = LSTMTagger(EMBEDDING_DIM, HIDDEN_DIM, len(wordsAndIndices), len(tagsAndIndices))
    loss_function = nn.NLLLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.1)

    # See what the scores are before training
    # Note that element i,j of the output is the score for tag j for word i.
    #print(training_data[0][0])
    #sys.exit(1)
    inputs = prepare_sequence(training_data[0][0], wordsAndIndices)
    tag_scores = model(inputs)
    #print(tag_scores)


    for epoch in tqdm(range(noofEpochs),total=noofEpochs,desc="epochs :"):
    #for epoch in range(1):
        sentenceCounter=0
        for sentence,tags in tqdm(training_data ,total=len(training_data),desc="sent:"):

        #for sentence, tags in training_data:


            # Step 1. Remember that Pytorch accumulates gradients.
            # We need to clear them out before each instance
            model.zero_grad()

            # Also, we need to clear out the hidden state of the LSTM,
            # detaching it from its history on the last instance.
            model.hidden = model.init_hidden()

            # Step 2. Get our inputs ready for the network, that is, turn them into
            # Variables of word indices.
            sentence_in = prepare_sequence(sentence, wordsAndIndices)
            targets = prepare_sequence(tags, tagsAndIndices)

            # Step 3. Run our forward pass.
            tag_scores = model(sentence_in)

            # Step 4. Compute the loss, gradients, and update the parameters by
            #  calling optimizer.step()
            loss = loss_function(tag_scores, targets)
            loss.backward()
            optimizer.step()

    # See what the scores are after training
    inputs = prepare_sequence(training_data[0][0], wordsAndIndices)
    tag_scores = model(inputs)
    # The sentence is "the dog ate the apple".  i,j corresponds to score for tag j
    #  for word i. The predicted tag is the maximum scoring tag.
    # Here, we can see the predicted sequence below is 0 1 2 0 1
    # since 0 is index of the maximum value of row 1,
    # 1 is the index of maximum value of row 2, etc.
    # Which is DET NOUN VERB DET NOUN, the correct sequence!
    print(tag_scores)


    # model = LSTMTagger(EMBEDDING_DIM, HIDDEN_DIM, len(wordsAndIndices), len(tagsAndIndices))
    # loss_function = nn.NLLLoss()
    # optimizer = optim.SGD(model.parameters(), lr=0.1)
    #
    # #temporarily check the weight scores that the model has learned. just to compare with later
    # inputs = getIndex("every",wordsAndIndices)
    # tag_scores = model(inputs)
    # #print("weights before training:")
    # #print(tag_scores)
    # #sys.exit(1)
    #
    # counter=0
    #
    # #the actual training part
    # #for epoch in range(300):
    #  #for sentence, tags in training_data:
    # for index, row in tqdm(posTrain.iterrows(),total=len(posTrain)):
    #
    #     #for word, tag in posTrain.items():
    #     model.zero_grad()
    #     model.hidden = model.init_hidden()
    #     word=row["words"]
    #     tag=row["tags"]
    #     #print("value of word is:"+word)
    #     #print("size of wordsAndIndices is:"+str(len(wordsAndIndices)))
    #
    #     sentence_in = getIndex(word, wordsAndIndices)
    #     #print("value of sentence_in is:")
    #     #print(sentence_in.data)
    #
    #     #print("value of tag is:"+tag)
    #     #print("size of tagsAndIndices is:"+str(len(tagsAndIndices)))
    #
    #
    #     targets = getIndex(tag, tagsAndIndices)
    #     #print("value of targets is:")
    #     #print(targets.data)
    #
    #
    #     tag_scores = model(sentence_in)
    #
    #     loss = loss_function(tag_scores, targets)
    #     loss.backward()
    #     optimizer.step()
    #
    # #dev part
    # inputs = getIndex("every",wordsAndIndices)
    # tag_scores = model(inputs)
    # #print("weights after training:")
    # #print(tag_scores)
    # values, indices = tag_scores.max(0)
    # print("values:")
    # print(values)
    # print("indices:")
    # print(indices)
    #
    # predicted_tag=tagsAndIndices[indices]
    # print("predicted_tag:")
    # print(predicted_tag)

    # #testing part
    # inputs = getIndex(testing_data[0], wordsAndIndices)
    # tag_scores = model(inputs)
    # print("weights after training:")
    #
    # print(tag_scores)

