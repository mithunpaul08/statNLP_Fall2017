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



        training_data= utils.read_data.readSpam(cwd,"SMSSpamCollection.train")
        print("size of entire_corpus is:" + str((training_data.shape)))
        featureVector=tokenize(training_data["data"] )
        labels=training_data["label"]
        print("size of tokenized corpus is:" + str((featureVector.shape)))
        rowCount=featureVector.shape[0]
        noOfFeatures=featureVector.shape[1]

        #create3 a theta/weight vector which has same number of rows, but one column
        theta=np.random.rand(noOfFeatures,1)
        print("shape of the numpy array theta:"+str((theta.shape)))

        labelCounter=0;

        #for each of the message calculate theta.X
        for x in featureVector:




            #print("shape of the theta transpose is:"+str(theta.transpose().shape))
            #print("shape of the x transpose is is:"+str(x.transpose().shape))
            #print(theta.transpose().shape[-1] == x.transpose().shape[-2], theta.transpose().shape[1])
            #d=np.dot(x,theta.transpose())
            d=x*theta
            #print("shape of d:"+str(d.shape))
            sig=calculateSigmoid(d)
            sigint=sig[0][0][0]
            thisLabel=str(labels[labelCounter])
            # print("shape of labels is:"+str(labels.shape))
            # print("value of labelCounter is:"+str(labelCounter))
           # print("value of thisLabel is:"+thisLabel)
           # print("value of sig is:"+str(sig[0][0][0]))
            #print("sahpe of sig is:"+str(sig[0][0][0].shape))

            labelInt=1;
            labelCounter=labelCounter+1

            #if its ham, call it label 0
            if(thisLabel=="ham"):
                labelInt=0

            #find the value of y(i)-sigmoid
            diff=labelInt-sigint
           # print("value of labelInt is:"+str(labelInt))
            #print("value of diff is:"+str(diff))

            #feature_vector_this= np.array([[]])
            #feature_vector_this=feature_vector_this.reshape(-1, 1)
            #feature_vector_this=np.asarray(x.transpose()).reshape(-1)
            #print(str(feature_vector_this))
            #print(str(feature_vector_this.shape))

            fvProduct=(x.T)*diff
            #fvProduct=np.multiply((x.transpose()),diff)
            #print("fvProduct "+str(fvProduct))
            if(labelCounter==1):
                print("theta before"+str(theta[805][0]))

            #new theta value is old theta plus this new fVproduct
            theta=theta+fvProduct
            if(labelCounter==1):
                print("theta after for 1st eleement"+str(theta[805][0]))


        print("theta after all iterations"+str(theta[805][0]))


    except:
        import traceback
        print('generic exception: ' + traceback.format_exc())
        elapsed_time = time.time() - start_time
        print("time taken:" + str(elapsed_time))


