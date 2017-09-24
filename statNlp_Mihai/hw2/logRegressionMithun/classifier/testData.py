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

import pickle


import time


#in phase 1, we split teh data set to related- unrelated
do_training_phase1=False;
do_training_phase2=True;

do_validation_phase1=False;
do_validation_phase2=False;

do_testing_phase1=True;
do_testing_phase2=True;





def test(theta,filename):

    start_time = time.time()


    try:

        #sys.exit(1)

        #nltk.download("wordnet", "whatever_the_absolute_path_to_myapp_is/nltk_data/")
        print("number of arguments is"+ str(len(sys.argv)))




        if(len(sys.argv)>1):
            toaddr=sys.argv[1]

        ###########################-DO NOT DELETE###########################

        #make sure that the current working directory is the starting level


        cwd = os.getcwd()

        base_dir_name = os.path.dirname(os.path.abspath(sys.argv[0]))
        #print("base directory is:" + base_dir_name)
        if(base_dir_name != cwd):
            os.chdir(base_dir_name)



        # #Do training for 2 classes related-unrelated

        print ("going to train on data for related-unrelated splitting aka phase1")



        training_data= utils.read_data.readSpam(cwd,filename)
        print("size of entire_corpus is:" + str((training_data.shape)))
        featureVector=tokenize(training_data["data"] )
        labels=training_data["label"]
        print("size of tokenized corpus is:" + str((featureVector.shape)))
        rowCount=featureVector.shape[0]
        noOfFeatures=featureVector.shape[1]

        #create3 a theta/weight vector which has same number of rows, but one column
        #theta=np.random.rand(noOfFeatures,1)

        #add a bias value place holder
        print("shape of the numpy array theta before bias:"+str((theta.shape)))
        print("shape of the numpy array theta before bias:"+str((theta.shape)))

        #theta = np.insert(theta,noOfFeatures,0.5,axis=0)

        # print("shape of the numpy array theta after bias:"+str((theta.shape)))
        # print("bias before all iterations"+str(theta[noOfFeatures][0]))
        #
        #
        labelCounter=0;
        predictedLabel=0;
        pred_int=[]

        for x in featureVector:


            d=x*theta
            #print("shape of d:"+str(d.shape))
            sig=calculateSigmoid(d)
            sigint=sig[0][0][0]

            if(sigint>0.5):
                predictedLabel=1
            pred_int.append(predictedLabel)






        #print("bias after all iterations"+str(theta[noOfFeatures][0]))
        return pred_int


    except:
        import traceback
        print('generic exception: ' + traceback.format_exc())
        elapsed_time = time.time() - start_time
        print("time taken:" + str(elapsed_time))


