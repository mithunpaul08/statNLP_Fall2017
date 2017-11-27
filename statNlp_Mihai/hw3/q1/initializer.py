from utils.readData import read_without_space
from utils.readData import read_tags_only_with_blank_lines
from utils.readData import read_data_with_blank_lines

from utils.calculations import calculate_bigrams


import sys
import os
import time
from tqdm import tqdm
start_time = time.time()

trainingData="train.tagged"
devDataInput="dev.tagged"
testingDataInput="test.tagged"

cwd = os.getcwd()



#read training data
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
tagsPerSentence=read_tags_only_with_blank_lines(cwd, trainingData)

#for each tag find the number of times it occurs with the previous tag
bigramTagCounter=calculate_bigrams(tagsPerSentence)
#print(bigramTagCounter["START_NNP"])


#predict for a sample sentence CHAIRMAN OF

scoresPerWord=[]

myWordCounter=0;
#take input as a collection of sentences and return the predicted tags
listOfPredTags=[]



#read the dev data
devData=read_data_with_blank_lines(cwd, devDataInput)

print("size of dev data is:"+str(len(devData)))
sys.exit(1)


dummy=["Pierre","Vinken","61","mithunpatti","old",",","will"]
for eachWord in dummy:
    myWordCounter=myWordCounter+1
    highestScoreSoFar=0;

    previous_tag="START"
    myTagCounter=0

    #initially the first tag of a sentences will be previous_tag
    # after each word, the predicted tag becomes the new previous_tag
    #TODO: change this START thing if you are already feeding in with START while reading dev or testing data

    if(myWordCounter>1):
        previous_tag=predicted_tag



    predicted_tag=""

    #for each of the tag in the entire tag collection
    for thisTag, freq in tagCounter.items():


        word_tag=eachWord+"_"+thisTag

        wordTagCount=0
        #for each of the tags, find the number of times this word occurs with that tag
        if word_tag in wordTagCounter:
            wordTagCount=wordTagCounter[word_tag]


        #for each of this tag, find the count of the tag and teh previous tag
        #here the value of predicted_tag will always contain the value of the tag i predicted
        # this is the greedy approach
        tatTagcounter=0
        tag_tag_combined=previous_tag+"_"+thisTag

        if tag_tag_combined in bigramTagCounter:
            tatTagcounter=bigramTagCounter[tag_tag_combined]

        #print(tag_tag_combined+":"+str(tatTagcounter))




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

    #after each word add the predicted tag to a list
    listOfPredTags.append(predicted_tag)

print((listOfPredTags))
#sort and pick the tag with highest value. Find its index


        #find transition prob






sys.exit(1)



print("--- %s seconds ---" % (time.time() - start_time))
