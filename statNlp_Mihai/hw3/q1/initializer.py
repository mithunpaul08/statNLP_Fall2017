from utils.readData import read_without_space
from utils.readData import read_with_space
from utils.calculations import calculate_bigrams

import sys
import os
import time
from tqdm import tqdm
start_time = time.time()

trainingData="train.tagged"
devData="dev.tagged"
testingData="test.tagged"

cwd = os.getcwd()
posTrain=read_without_space(cwd,trainingData)

# for word in posTrain["words"]:
#     print(word)

tagsPerSentence=read_with_space(cwd,trainingData)
calculate_bigrams(tagsPerSentence)

tagCounter={}
for tag in tqdm(posTrain["tags"],total=len(posTrain["tags"])):

    if tag in tagCounter:
        tagCounter[tag] += 1
    else:
        tagCounter[tag] = 1

#to find the number of times each word occurs with its corresponding tag


wordTagCounter={}

for index, row in tqdm(posTrain.iterrows(),total=len(posTrain["tags"])):
    word=row[0]
    tag=row[1]
    print(tag)
    if(index==25):
        sys.exit(1)
    #combine and store it to a hashtable
    combined=word+tag
    if combined in wordTagCounter:
        wordTagCounter[combined] += 1
    else:
        wordTagCounter[combined] = 1


print(wordTagCounter["committeeNN"])




#prepare_training_data(posTrain)

#startLstm(posTrain)
print("--- %s seconds ---" % (time.time() - start_time))
