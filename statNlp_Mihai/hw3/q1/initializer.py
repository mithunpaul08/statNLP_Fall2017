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

#find all tags and the number of times the tag occurs

tagCounter={}
for tag in tqdm(posTrain["tags"],total=len(posTrain["tags"]),desc="all_tags :"):

    if tag in tagCounter:
        tagCounter[tag] += 1
    else:
        tagCounter[tag] = 1

#print("size of tags is:"+str(len(tagCounter)))

#to find the number of times each word occurs with its corresponding tag

wordTagCounter={}

for index, row in tqdm(posTrain.iterrows(),total=len(posTrain["tags"]),desc="word_tag :"):
    word=row[0]
    tag=row[1]
    #combine and store it to a hashtable
    combined=word+"_"+tag
    if combined in wordTagCounter:
        wordTagCounter[combined] += 1
    else:
        wordTagCounter[combined] = 1



print(wordTagCounter["committee_NN"])


#get counts of START_NNP etc
tagsPerSentence=read_with_space(cwd,trainingData)

#for each tag find the number of times it occurs with the previous tag
bigramTagCounter=calculate_bigrams(tagsPerSentence)
#print(bigramTagCounter["START_NNP"])


#predict for a sample sentence CHAIRMAN OF

scoresPerWord=[]
highestScoreSoFar=0;
predicted_tag=""

for thisTag, freq in tagCounter.items():
    word_tag="chairman"+"_"+thisTag

    wordTagCount=0
    #for each of the tags, find the number of times this word occurs with that tag
    if word_tag in wordTagCounter:
        wordTagCount=wordTagCounter[word_tag]


    #for each of this tag, find the count of the tag and teh previous tag
    tatTagcounter=0
    tag_tag_combined="START"+"_"+thisTag
    if tag_tag_combined in bigramTagCounter:
        tatTagcounter=bigramTagCounter[tag_tag_combined]



    #
    # if tag_tag_combined in bigramTagCounter:
    #     #print(tag_tag_combined+":"+str(bigramTagCounter[tag_tag_combined]))
    # else:
    #     #print(tag_tag_combined+":"+str(0))

    # find emission prob:p(wi/ti)=count(ti,wi)/count(ti)
    #find the total number of times this tag occurs in the corpus=freq
    #i.e wordTagCount/freq

    # print("wordTagCount:"+str(wordTagCount))
    # print("freq:"+str(freq))
    emission_prob=wordTagCount/freq
    # if(emission_prob>0):
    #     print("emission probability of word,tag:"+word_tag+"="+str(emission_prob))

    # print("tatTagcounter:"+str(tatTagcounter))

    transition_prob=tatTagcounter/freq
    # print("transition_prob  word,tag:"+tag_tag_combined+"="+str(transition_prob))


    #multiply both if
    score=emission_prob*transition_prob
    if(score>highestScoreSoFar):
        highestScoreSoFar=score;
        predicted_tag=thisTag

    scoresPerWord.append(score)
    # #print(tag_tag_combined+":"+str(bigramTagCounter[tag_tag_combined]))

print(str(len(scoresPerWord)))
print(str(highestScoreSoFar))
print(predicted_tag)

#sort and pick the tag with highest value. Find its index


        #find transition prob






sys.exit(1)



print("--- %s seconds ---" % (time.time() - start_time))
