import sys
import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

torch.manual_seed(1)

def prepare_sequence(seq, to_ix):
    idxs = [to_ix[w] for w in seq]
    tensor = torch.LongTensor(idxs)
    return autograd.Variable(tensor)


def prepare_training_data(posTrain):

    #create a dictionary (which will be filled later, to store the unique words and its indexes)
    word_to_ix = {}

    #assign a unique id to each of the words
    for word in posTrain["words"]:
            if word not in word_to_ix:
                word_to_ix[word] = len(word_to_ix)



    #create a similar hash table for all the pos tags and give it an index
    tag_to_ix = {}

    #assign a unique id to each of the words
    for tag in posTrain["tags"]:
            if tag not in tag_to_ix:
                tag_to_ix[tag] = len(tag_to_ix)

    print(tag_to_ix)
    sys.exit(1)

EMBEDDING_DIM = 6
HIDDEN_DIM = 6

#
class LSTMTagger(nn.Module):

    def __init__(self, embedding_dim, hidden_dim, vocab_size, tagset_size):
        super(LSTMTagger, self).__init__()
        self.hidden_dim = hidden_dim

        self.word_embeddings = nn.Embedding(vocab_size, embedding_dim)

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


def startLstm():

    model = LSTMTagger(EMBEDDING_DIM, HIDDEN_DIM, len(word_to_ix), len(tag_to_ix))
    loss_function = nn.NLLLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.1)

    training_data=prepare_training_data()
    inputs = prepare_sequence(training_data[0][0], word_to_ix)
    tag_scores = model(inputs)
    print("weights before training:")
    print(tag_scores)


    #the actual training part
    for epoch in range(300):
        for sentence, tags in training_data:
            model.zero_grad()

            model.hidden = model.init_hidden()

            sentence_in = prepare_sequence(sentence, word_to_ix)
            targets = prepare_sequence(tags, tag_to_ix)
            tag_scores = model(sentence_in)

            loss = loss_function(tag_scores, targets)
            loss.backward()
            optimizer.step()

    #dev part

    # #testing part
    inputs = prepare_sequence(testing_data[0], word_to_ix)
    tag_scores = model(inputs)
    print("weights after training:")

    print(tag_scores)

