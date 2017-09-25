from __future__ import division
import nltk, string
import os
import sys;
import utils;
import csv;
import collections
import numpy as np
import math
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





def train(filename,miniBatchSize,noOfEpochs):

    start_time = time.time()


    try:


        cwd = os.getcwd()

        base_dir_name = os.path.dirname(os.path.abspath(sys.argv[0]))
        #print("base directory is:" + base_dir_name)
        if(base_dir_name != cwd):
            os.chdir(base_dir_name)



        # #Do training for 2 classes related-unrelated

        print ("going to train on data for related-unrelated splitting aka phase1")



        training_data= utils.read_data.readSpam(cwd,filename)
        print("size of entire_corpus is:" + str((training_data.shape)))
        featureVector,vectorizer=tokenize(training_data["data"] )
        labels=training_data["label"]
        print("size of tokenized corpus is:" + str((featureVector.shape)))
        rowCount=featureVector.shape[0]
        noOfFeatures=featureVector.shape[1]

        #create3 a theta/weight vector which has same number of rows, but one column
        theta=np.random.rand(noOfFeatures,1)

        #add a bias value place holder
        print("shape of the numpy array theta before bias:"+str((theta.shape)))

        #theta = np.insert(theta,noOfFeatures,0.5,axis=0)

        # print("shape of the numpy array theta after bias:"+str((theta.shape)))
        # print("bias before all iterations"+str(theta[noOfFeatures][0]))
        #
        #
        labelCounter=0;
        # biasForX=np.array([[1]])
        # biasForX[0][0]=-1
        # print("shape of the biasForX:"+str((biasForX.shape)))
        # biasForX=np.mat(biasForX)
        # print("shape of the biasForX after matrix:"+str((biasForX.shape)))
        #for each of the message calculate theta.X
        #print("first row of feature vector :"+str(featureVector[0:1,:]))

        #do a shuffle at the beginning of each epoch. Note that theta doesnt change.
        for epoch in range(0,noOfEpochs):

            #featureVector=np.random.shuffle(featureVector)
            #to shuffle a sparse matrix
            index = np.arange(np.shape(featureVector)[0])
            np.random.shuffle(index)
            featureVector= featureVector[index, :]
            #print("first row of feature vector :"+str(featureVector[0:1,:]))
            sys.exit(1)

            batchStartIndex=0
            batchendIndex=batchStartIndex+miniBatchSize

            #if the number of data points is not a multiple of the batchsize, ignore the last batch.
            #i.e run for only one batch less
            noOfBatches=0
            if((rowCount%miniBatchSize)>0):
                noOfBatches=math.floor(rowCount/miniBatchSize)
            else:
                noOfBatches=(rowCount/miniBatchSize)

            print("rowCount:"+str(rowCount))
            print("miniBatchSize:"+str(miniBatchSize))
            print("noOfBatches:"+str(noOfBatches))



            print("value of a random eleement in theta before one batch started"+str(theta[5821][0]))

            print("shape of the featureVector is:"+str(featureVector.shape))
            #run this for all the number of batches
            for batchCount in range (0,int(noOfBatches)):

                #print("value of a batchStartIndex is:"+str(batchStartIndex))
                #print("value of a miniBatchSize is:"+str(miniBatchSize))
                minibatch=featureVector[batchStartIndex:batchendIndex,:]
                #print("shape of the minibatch is:"+str(minibatch.shape))



                #for each of this element in a mini batch, run through each item
                #print("size of minibatch:"+str(minibatch.shape))


                #create a delta like the same shape of theta, but it will be initialized to all zeroes. this is initialized to zeroes for all batches
                delta=np.zeros((noOfFeatures,1))

                #print("size of delta is :"+str(delta.shape))
                #print("value of a random eleement in theta before one batch started"+str(theta[5821][0]))
                #print("value of a random eleement in delta before one batch started"+str(delta[5821][0]))

                #calculate delta for each entry in the minibatch. This is basically one data point, with 6054 features
                for x in minibatch:


                    #print("This is item number"+str(labelCounter)+" in Batch number:"+str(batchCount))
                    #add a fake feature
                    # print("shape of the xT array before bias:"+str((x.T.shape)))
                    # #newx=np.stack([x.T,biasForX],axis=0)
                    # print("shape of the x array after bias:"+str((newx.shape)))

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

                    #do yi-hi (this is a scalar value)
                    diff=labelInt-sigint
                   # print("value of labelInt is:"+str(labelInt))
                    #print("value of diff is:"+str(diff))

                    #feature_vector_this= np.array([[]])
                    #feature_vector_this=feature_vector_this.reshape(-1, 1)
                    #feature_vector_this=np.asarray(x.transpose()).reshape(-1)
                    #print(str(feature_vector_this))
                    #print(str(feature_vector_this.shape))

                    fvProduct=(x.T)*diff

                    #add this product thing to delta
                    delta=delta+fvProduct;

                    #fvProduct=np.multiply((x.transpose()),diff)
                    #print("fvProduct "+str(fvProduct))
                    #if(labelCounter==1):
                    #print("theta value of a random element before"+str(theta[5821][0]))
                    #print("delta value of a random element before"+str(delta[5821][0]))





                    #new theta value is old theta plus this new fVproduct(vector)
                    #update, do this after teh end of every batch, but with the average fvProduct from the given batch
                    #add this new delta to the theta

                    #print("one element finished running")
                    #print("theta value of a random element before"+str(theta[5821][0]))
                    #print("delta value of a random element before"+str(delta[5821][0]))
                    #sys.exit(1)

                    #if(labelCounter==1):

                print("done with batch number:"+str(batchCount))

                #print("one batch finished running")
                #at the end of each batch divdide the delta by the batch size
                delta =delta/(miniBatchSize)

                #print("value of a random eleement in delta after one batch "+str(delta[5821][0]))
                theta=theta+delta

                #after every batch increase the start index by batch size
                batchStartIndex=batchStartIndex+miniBatchSize
                batchendIndex=batchStartIndex+miniBatchSize

                #print("theta after one batch for a random eleement"+str(theta[5821][0]))


                #print("shape of thetat is:"+str(theta.shape))

            print("done with all batches. value of batch count is:"+str(batchCount))




        print("theta after all iterations"+str(theta[5821][0]))
        print("value of labelCounter is:"+str(labelCounter))
        #print("bias after all iterations"+str(theta[noOfFeatures][0]))
        return theta,vectorizer


    except:
        import traceback
        print('generic exception: ' + traceback.format_exc())
        elapsed_time = time.time() - start_time
        print("time taken:" + str(elapsed_time))


