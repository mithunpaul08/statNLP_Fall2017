from __future__ import division
import nltk, string
import os
import sys;
import utils;
import csv;
import collections
import numpy as np

import itertools
from utils.read_data import readSpam
from utils.process_input_data import tokenize
from utils.mathStuff import calculateSigmoid
from classifier.trainData import train
from classifier.testData import test
from utils.mathStuff import calculateAccuracy
import pickle


import time






LABELS = ['agree', 'disagree', 'discuss', 'unrelated']
LABELS_RELATED = ['unrelated','related']
RELATED = LABELS[0:3]

#acccording to FNC guys, this is the mapping of classes to labels
#agree:0
#disagree:1
#discuss:2
#unrelated:3
toaddr="mithunpaul08@gmail.com"
#toaddr="mithunpaul@email.arizona.edu"

start_time = time.time()
#writeToOutputFile("start time:"+str(start_time), "logfile")

#or if its just 2 classes
#unrelated:0
#related=1
if __name__ == "__main__":
    try:

        #sys.exit(1)
        miniBatchSize=5;
        noOfEpochs=10;

        #nltk.download("wordnet", "whatever_the_absolute_path_to_myapp_is/nltk_data/")
        print("number of arguments is"+ str(len(sys.argv)))




        if(len(sys.argv)>1):
            toaddr=sys.argv[1]



        #make sure that the current working directory is the starting level


        cwd = os.getcwd()

        base_dir_name = os.path.dirname(os.path.abspath(sys.argv[0]))
        #print("base directory is:" + base_dir_name)
        if(base_dir_name != cwd):
            os.chdir(base_dir_name)

        print ("going to train on data")

        trainingData="SMSSpamCollection.train"
        testFile="SMSSpamCollection.test"
        trainedWeights,vectorizer=train(trainingData,miniBatchSize)
        pred_labels,gold_labels=test(trainedWeights,testFile,vectorizer)


        #print(str(pred_labels))
        #print(str(gold_labels))

        print("size of result data ste is"+str(len(pred_labels)))
        print("size of result data ste is"+str(len(gold_labels)))
        accuracy=calculateAccuracy(gold_labels,pred_labels)
        print("value of accuracy is is"+str((accuracy)))




    except:
        import traceback
        print('generic exception: ' + traceback.format_exc())
        elapsed_time = time.time() - start_time
        print("time taken:" + str(elapsed_time))


