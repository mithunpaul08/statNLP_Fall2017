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
from classifier.trainData import trainWithPickle


from classifier.testData import test
from classifier.testData import testWithAlreadyTrainedPickle

from utils.mathStuff import calculateAccuracy
import pickle as pk


import time





start_time = time.time()

if __name__ == "__main__":
    try:
        trainingData="SMSSpamCollection.train"
        testData="SMSSpamCollection.test"
        devData="SMSSpamCollection.devel"




        while True:
            print("                      ")
            print("          ******            ")

            print("Welcome to Spam Classifier. Please pick one of the following:")
            print("To test using an already trained classifier, Press:1")
            print("To train a model and test with it, Press:2")
            print("To exit Press:0")


            myInput=input("what is your choice:")
            if(myInput=="1"):
                testWithAlreadyTrainedPickle(testData)

            else:
                if(myInput=="0"):
                    print("******Good Bye")
                    break;
                else:
                    if(myInput=="2"):
                        maxNoOfEpochsStr=input("Enter a max epoch value:")
                        maxMiniBatchSizeStr=input("Enter a maximum minibatch size value:")
                        if(maxMiniBatchSizeStr!="" and maxNoOfEpochsStr!=""):
                            trainWithPickle(testData,trainingData,maxNoOfEpochsStr,maxMiniBatchSizeStr)






    ##################################end of dev phase####################
    except:
        import traceback
        print('generic exception: ' + traceback.format_exc())
        elapsed_time = time.time() - start_time
        print("time taken:" + str(elapsed_time))






