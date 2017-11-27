import sys
import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from tqdm import tqdm
import re
import pickle as pk

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


    file_Name2 = "wordsAndIndices.pkl"
    # open the file for writing
    fileObject2 = open(file_Name2,'wb')
    pk.dump(wordsAndIndices, fileObject2)



def prepare_tags_data(posTrain):

    for eachSent in tqdm(posTrain,total=len(posTrain),desc="test_data :"):
        # print("eachSent:")
        # print(eachSent)
        for tag in eachSent[1]:
                if tag not in tagsAndIndices:
                    tagsAndIndices[tag] = len(tagsAndIndices)

    file_Name1 = "tagsAndIndices.pkl"
    # open the file for writing
    fileObject1 = open(file_Name1,'wb')
    pk.dump(tagsAndIndices, fileObject1)





EMBEDDING_DIM = 6
HIDDEN_DIM = 6

#
class LSTMTagger(nn.Module):

    def __init__(self, embedding_dim, hidden_dim, vocab_size, tagset_size):
        super(LSTMTagger, self).__init__()
        self.hidden_dim = hidden_dim

        #read teh glove data

        # embedding = nn.Embedding(embeddings.size(0), embeddings.size(1))
        # embedding.weight = nn.Parameter(embeddings)

        self.word_embeddings = nn.Embedding(vocab_size, embedding_dim)
        # print("size of word embeddings now is:")
        # print((self.word_embeddings))

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


    inputs = prepare_sequence(training_data[0][0], wordsAndIndices)
    tag_scores = model(inputs)


    for epoch in tqdm(range(noofEpochs),total=noofEpochs,desc="epochs :"):
        sentenceCounter=0
        for sentence,tags in tqdm(training_data ,total=len(training_data),desc="sent:"):



            model.zero_grad()
            model.hidden = model.init_hidden()

            sentence_in = prepare_sequence(sentence, wordsAndIndices)
            targets = prepare_sequence(tags, tagsAndIndices)

            tag_scores = model(sentence_in)

            loss = loss_function(tag_scores, targets)
            loss.backward()
            optimizer.step()

    file_Name5 = "lstm.pkl"
    # open the file for writing
    fileObject5 = open(file_Name5,'wb')
    pk.dump(model, fileObject5)

    inputs = prepare_sequence(training_data[0][0], wordsAndIndices)
    tag_scores = model(inputs)
    print(tag_scores)


    for perWordScore in tag_scores:
        highestScoreSoFar=0
        highestIndex=0
        tagCounter=0;
        #go through each of the scores of 45 pos tags and pick the highest
        for score in perWordScore:
            if(score>highestScoreSoFar):
                highestScoreSoFar=score;
                highestIndex=tagCounter
        tagCounter=tagCounter+1


        for tag, index in tagsAndIndices.iteritems():
            if tagCounter == highestIndex:
                predicted_tag=tag

        #print(predicted_tag)


def startLstmWithPickle(training_data):

    fileObject_tagsAndIndices = open('tagsAndIndices.pkl','rb')
    tagsAndIndices=pk.load(fileObject_tagsAndIndices)

    fileObject_wordsAndIndices = open('wordsAndIndices.pkl','rb')
    wordsAndIndices=pk.load(fileObject_wordsAndIndices)

    fileObject_toatlVocabCounter = open('lstm.pkl','rb')
    model=pk.load(fileObject_toatlVocabCounter)

    inputs = prepare_sequence(training_data[0][0], wordsAndIndices)
    tag_scores = model(inputs)
    print(tag_scores)
    print(training_data[0][0])
    allTags=[]

    for perWordScore in tag_scores:
        print(perWordScore)
        highestScoreSoFar=0

        highestIndex=0
        tagCounter=0;
        predicted_tag="NN"
        scoreCOunter=0
        #go through each of the scores of 45 pos tags and pick the highest
        for score in perWordScore:
            scoreCOunter=scoreCOunter+1

            #print(score.data[0]);
            if(scoreCOunter==1):
                if((score.data[0]) < highestScoreSoFar):
                    highestScoreSoFar=score;
                    highestIndex=tagCounter
                else:
                    if((score.data[0]) > highestScoreSoFar):
                        highestScoreSoFar=score;
                        highestIndex=tagCounter

                tagCounter=tagCounter+1

        #print(tagsAndIndices)
        #print(highestIndex)

        for tag, index in tagsAndIndices.items():
            if index == highestIndex:
                predicted_tag=tag
                allTags.append(predicted_tag)
                break;

    #print(allTags)



