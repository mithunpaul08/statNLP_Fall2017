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
import pickle as pk


import time





start_time = time.time()

if __name__ == "__main__":
    try:

        doDev=False;
        maxMiniBatchSizeStr="1";
        maxNoOfEpochsStr="1";






        if(len(sys.argv)>2):
            maxMiniBatchSizeStr=sys.argv[1]
            maxNoOfEpochsStr=sys.argv[2]
            print("maxMiniBatchSize:"+ str(maxMiniBatchSizeStr))
            print("maxNoOfEpochs:"+ str(maxNoOfEpochsStr))

        else:
            print("Error: No max epoch and max batch size provided")
            sys.exit(1)

        userinput=input("Is it correct. press y or n:")
        if(userinput=="n"):
            sys.exit(1);
        else:




            maxMiniBatchSize=int(maxMiniBatchSizeStr)
            maxNoOfEpochs=int(maxNoOfEpochsStr)




            #make sure that the current working directory is the starting level


            cwd = os.getcwd()

            base_dir_name = os.path.dirname(os.path.abspath(sys.argv[0]))
            #print("base directory is:" + base_dir_name)
            if(base_dir_name != cwd):
                os.chdir(base_dir_name)

            print ("going to train on data")

            trainingData="SMSSpamCollection.train"
            testData="SMSSpamCollection.test"
            devData="SMSSpamCollection.devel"

            if(doDev==True):
                devData=devData
            else:
                devData=testData

            #to tune on dev data

            #tuning batch size. For each of the batch size. print accuracy alone
            for miniBatchSize in range(1,maxMiniBatchSize):
                 trainedWeights,vectorizer=train(trainingData,miniBatchSize,maxNoOfEpochs)
                 print("done with training. Going to save to pickle")

                 fileObject_trainedWeights = open("trainedWeights.pkl",'wb')
                 pk.dump(trainedWeights, fileObject_trainedWeights)
                 fileObject_trainedWeights.close()

                 fileObject_vectorizer = open("vectorizer.pkl",'wb')
                 pk.dump(vectorizer, fileObject_vectorizer)
                 fileObject_vectorizer.close()
                 sys.exit(1)

                 trainedWeights_from_pkl=pk.load('trainedWeights.pkl')
                 vectorizer_from_pkl=pk.load('vectorizer.pkl')




                 #print("size of trainedWeights is.:"+str(trainedWeights.shape))
                 #print("size of vectorizer is.:"+(vectorizer.))
                 pred_labels,gold_labels=test(trainedWeights,devData,vectorizer)
                 accuracy=calculateAccuracy(gold_labels,pred_labels)
                 print("miniBatchSize:"+str(miniBatchSize)+" accuracy:"+str((accuracy)))

            print("done with training and Testing . Going to exit")

##################################end of dev phase####################

        #to run on testing data
        #pred_labels,gold_labels=test(trainedWeights,testData,vectorizer)
        #
        # for miniBatchSize in range(1,maxMiniBatchSize):
        #          trainedWeights,vectorizer=train(trainingData,miniBatchSize,maxNoOfEpochs)
        #          print("done with training.")
        #          #print("size of trainedWeights is.:"+str(trainedWeights.shape))
        #          #print("size of vectorizer is.:"+(vectorizer.))
        #          pred_labels,gold_labels=test(trainedWeights,testData,vectorizer)
        #          accuracy=calculateAccuracy(gold_labels,pred_labels)
        #          print("miniBatchSize:"+str(miniBatchSize)+" accuracy:"+str((accuracy)))

        #print(str(pred_labels))
        #print(str(gold_labels))

        # print("size of result data ste is"+str(len(pred_labels)))
        # print("size of result data ste is"+str(len(gold_labels)))
        # accuracy=calculateAccuracy(gold_labels,pred_labels)
        # print("value of accuracy is is"+str((accuracy)))




    except:
        import traceback
        print('generic exception: ' + traceback.format_exc())
        elapsed_time = time.time() - start_time
        print("time taken:" + str(elapsed_time))


