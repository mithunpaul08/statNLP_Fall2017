from __future__ import division
import nltk, string
import os
import sys;
import utils;
import csv;
import collections
import numpy as np
import pandas as pd
import itertools
from utils.read_data import readSpam
from utils.process_input_data import tokenize
from utils.mathStuff import calculateSigmoid

import pickle
from utils.mathStuff import calculateAccuracy

import time
import pickle as pk


def testWithGivenPickle(filename,trainedWeightsPkl,vectorizerPkl):
    fileObject_trainedWeights = open(trainedWeightsPkl,'rb')
    trainedWeights_from_pkl=pk.load(fileObject_trainedWeights)

    fileObject_vectorizer = open(vectorizerPkl,'rb')
    vectorizer_from_pkl=pk.load(fileObject_vectorizer)

    pred_labels,gold_labels=test(trainedWeights_from_pkl,filename,vectorizer_from_pkl)
    accuracy=calculateAccuracy(gold_labels,pred_labels)
    return accuracy
    ##print("accuracy:"+str((accuracy)))





def testWithAlreadyTrainedPickle(filename):
    #print("Going to load pickle:trainedWeights_golden.pkl")
    #print("Going to load pickle:vectorizer_golden.pkl")
    fileObject_trainedWeights = open('trainedWeights_golden.pkl','rb')
    trainedWeights_from_pkl=pk.load(fileObject_trainedWeights)

    fileObject_vectorizer = open('vectorizer_golden.pkl','rb')
    vectorizer_from_pkl=pk.load(fileObject_vectorizer)

    pred_labels,gold_labels=test(trainedWeights_from_pkl,filename,vectorizer_from_pkl)
    accuracy=calculateAccuracy(gold_labels,pred_labels)
    #print("accuracy:"+str((accuracy)))




def test(theta,filename,vectorizer):

    start_time = time.time()


    try:

        #sys.exit(1)

        #nltk.download("wordnet", "whatever_the_absolute_path_to_myapp_is/nltk_data/")
        #print("number of arguments is"+ str(len(sys.argv)))




        if(len(sys.argv)>1):
            toaddr=sys.argv[1]

        ###########################-DO NOT DELETE###########################

        #make sure that the current working directory is the starting level


        cwd = os.getcwd()

        base_dir_name = os.path.dirname(os.path.abspath(sys.argv[0]))
        ##print("base directory is:" + base_dir_name)
        if(base_dir_name != cwd):
            os.chdir(base_dir_name)



        # #Do training for 2 classes related-unrelated

        #print ("going to read test data ")



        testing_data= utils.read_data.readSpam(cwd,filename)
        #print("size of entire_corpus is:" + str((testing_data.shape)))
        featureVector=vectorizer.transform(testing_data["data"] )

        #print ("done reading and vectorizing test data ")





        gold_labels=testing_data["label"]
        #print("size of tokenized corpus is:" + str((featureVector.shape)))
        rowCount=featureVector.shape[0]
        noOfFeatures=featureVector.shape[1]

        #create3 a theta/weight vector which has same number of rows, but one column
        #theta=np.random.rand(noOfFeatures,1)

        #add a bias value place holder
        #print("shape of featureVector:"+str((featureVector.shape)))

        #theta = np.insert(theta,noOfFeatures,0.5,axis=0)

        # #print("shape of the numpy array theta after bias:"+str((theta.shape)))
        # #print("bias before all iterations"+str(theta[noOfFeatures][0]))
        #
        #
        labelCounter=0;
        predictedLabel=0;
        pred_int=[]
        gold_int=[]

        for x in featureVector:
            thisLabel=str(gold_labels[labelCounter])


            labelInt=1;
            labelCounter=labelCounter+1


            d=x*theta
            ##print("shape of d:"+str(d.shape))
            sig=calculateSigmoid(d)
            sigint=sig[0][0]
            ##print("sigint:"+str(sigint))
            if(sigint<0.5):
                predictedLabel=0
            else:
                predictedLabel=1;
            pred_int.append(predictedLabel)

            if(thisLabel=="ham"):
                labelInt=0

            gold_int.append(labelInt)




        return pred_int,gold_int


    except:
        import traceback
        #print('generic exception: ' + traceback.format_exc())
        elapsed_time = time.time() - start_time
        #print("time taken:" + str(elapsed_time))


