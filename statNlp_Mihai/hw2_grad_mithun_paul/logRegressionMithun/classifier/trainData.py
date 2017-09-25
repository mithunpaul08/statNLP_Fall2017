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
from classifier.testData import testWithGivenPickle
from utils.process_input_data import tokenizeWithBigrams
from utils.process_input_data import tokenizeWithBothUniBigrams
import pandas as pd
import pickle as pk


import time


#in phase 1, we split teh data set to related- unrelated
do_training_phase1=False;
do_training_phase2=True;

do_validation_phase1=False;
do_validation_phase2=False;

do_testing_phase1=True;
do_testing_phase2=True;


def trainWithPickle(testingData,trainingData,maxNoOfEpochsStr,maxMiniBatchSizeStr):
    maxMiniBatchSize=int(maxMiniBatchSizeStr)
    maxNoOfEpochs=int(maxNoOfEpochsStr)
    doDev=False;
    maxMiniBatchSizeStr="1";
    maxNoOfEpochsStr="1";



    cwd = os.getcwd()

    base_dir_name = os.path.dirname(os.path.abspath(sys.argv[0]))
    #print("base directory is:" + base_dir_name)
    if(base_dir_name != cwd):
        os.chdir(base_dir_name)

    #print ("going to train on data")



    #to tune on dev data

    #tuning batch size. For each of the batch size. #print accuracy alone
    for miniBatchSize in range(1,maxMiniBatchSize+1):
        print("*******Starting a new run with miniBatchSize:"+str(miniBatchSize))
        miniBatchSize=10

        trainedWeights,vectorizer=train(trainingData,miniBatchSize,maxNoOfEpochs)
        print("done with training. Going to save to pickle")

        file1="trainedWeights.pkl"
        file2="vectorizer.pkl"

        fileObject_trainedWeights = open(file1,'wb')
        pk.dump(trainedWeights, fileObject_trainedWeights)
        fileObject_trainedWeights.close()

        fileObject_vectorizer = open(file2,'wb')
        pk.dump(vectorizer, fileObject_vectorizer)
        fileObject_vectorizer.close()
        print("done training. Stored pickles as:"+file2+":and:"+file1+". Going to test with them")
        testWithGivenPickle(testingData,file1,file2)

    #print("done with training and Testing . Going to main menu")

# def print_top10(vectorizer, clf, class_labels):
#
#     """#prints features with the highest coefficient values, per class"""
#     feature_names = vectorizer.get_feature_names()
#     for i, class_label in enumerate(class_labels):
#         top10 = np.argsort(clf.coef_[0])[-10:]
#         print("%s: %s" % (class_label,
#               " ".join(feature_names[j] for j in top10)))

def train(filename,miniBatchSize,maxNoOfEpochs):

    start_time = time.time()


    try:


        cwd = os.getcwd()

        base_dir_name = os.path.dirname(os.path.abspath(sys.argv[0]))
        #print("base directory is:" + base_dir_name)
        if(base_dir_name != cwd):
            os.chdir(base_dir_name)



        # #Do training for 2 classes related-unrelated

        #print ("going to train on data for related-unrelated splitting aka phase1")



        training_data= utils.read_data.readSpam(cwd,filename)
        #print("size of entire_corpus is:" + str((training_data.shape)))
        #featureVector,vectorizer=tokenize(training_data["data"] )

        #featureVector,vectorizer=tokenizeWithBigrams(training_data["data"] )
        featureVector,vectorizer=tokenizeWithBothUniBigrams(training_data["data"] )

        # #print("done reading and tokenizing:")
        # #print(class_labels)
        # #print(featureVector.coef_[0])
        # sys.exit(1)
        #
        # class_labels=["spam","ham"]
        # #print_top10(vectorizer,featureVector,class_labels)

        # word_freq_df = pd.DataFrame({'term': vectorizer.get_feature_names(),
        #                              'occurrences':np.asarray(featureVector.sum(axis=0)).ravel().tolist()})
        # word_freq_df['frequency'] = word_freq_df['occurrences']/np.sum(word_freq_df['occurrences'])
        # #print(word_freq_df.sort('occurrences',ascending = False).head())

        #print("#printing ascending bectors:")
        #sys.exit(1)


        labels=training_data["label"]

        rowCount=featureVector.shape[0]
        noOfFeatures=featureVector.shape[1]

        #create3 a theta/weight vector which has same number of rows, but one column
        theta=np.random.rand(noOfFeatures,1)

        #add a bias value place holder
        print("shape of the numpy array theta before bias:"+str((theta)))


        #theta = np.insert(theta,noOfFeatures,0.5,axis=0)

        print("shape of the numpy array theta after bias:"+str((theta.shape)))
        # #print("bias before all iterations"+str(theta[noOfFeatures][0]))
        #
        #

        # biasForX=np.array([[1]])
        # biasForX[0][0]=-1
        # #print("shape of the biasForX:"+str((biasForX.shape)))
        # biasForX=np.mat(biasForX)
        # #print("shape of the biasForX after matrix:"+str((biasForX.shape)))
        #for each of the message calculate theta.X
        #print("first row of feature vector :"+str(featureVector[0:1,:]))

        #do a shuffle at the beginning of each epoch. Note that theta doesnt change.
        for epoch in range(0,maxNoOfEpochs):
            print("starting a new Epoch. This is Epoch Number:"+str(epoch+1))


            #combine the feature vector matrix and the labels so that when we shuffle we shuffle both together
            # #print("size of labels  is:" + str((labels.shape)))
            # labels=np.mat(labels)
            # #print("size of labels  is:" + str((labels.T.shape)))
            # #print("size of featureVector  is:" + str((featureVector.shape)))
            # combined_label_fv=np.concatenate((labels.T,featureVector),axis=1)
            # #print("size of combined_label_fv  is:" + str((combined_label_fv.shape)))


            #to shuffle a sparse matrix
            index = np.arange(np.shape(featureVector)[0])
            np.random.shuffle(index)
            featureVector= featureVector[index, :]

            #print("size of featureVector  is:" + str((featureVector.shape)))
            #sys.exit(1)
            #print("first row of feature vector :"+str(featureVector[0:1,:]))
            

            batchStartIndex=0
            batchendIndex=batchStartIndex+miniBatchSize

            #if the number of data points is not a multiple of the batchsize, ignore the last batch.
            #i.e run for only one batch less
            noOfBatches=0
            if((rowCount%miniBatchSize)>0):
                noOfBatches=math.floor(rowCount/miniBatchSize)
            else:
                noOfBatches=(rowCount/miniBatchSize)

            #print("rowCount:"+str(rowCount))
            #print("miniBatchSize:"+str(miniBatchSize))
            print("noOfBatches:"+str(noOfBatches))

            labelCounter=0;



            ##print("value of a random eleement in theta before one batch started"+str(theta[5821][0]))

            #print("shape of the featureVector is:"+str(featureVector.shape))
            #run this for all the number of batches
            for batchCount in range (0,int(noOfBatches)):

                print("#####starting a new batch with Batch number:"+str(batchCount))

                print("value of a batchendIndex is:"+str(batchendIndex))
                print("value of a batchStartIndex is:"+str(batchStartIndex))
                print("value of a miniBatchSize is:"+str(miniBatchSize))
                minibatch=featureVector[batchStartIndex:batchendIndex,:]
                #print("shape of the minibatch is:"+str(minibatch.shape))




                #for each of this element in a mini batch, run through each item
                print("shape of minibatch:"+str(minibatch.shape))


                #create a delta like the same shape of theta, but it will be initialized to all zeroes. this is initialized to zeroes for all batches
                delta=np.zeros((noOfFeatures,1))
                #print(" delta is :"+str(delta))
                print("size of delta is :"+str(delta.shape))
                ##print("value of a random eleement in theta before one batch started"+str(theta[5821][0]))
                ##print("value of a random eleement in delta before one batch started"+str(delta[5821][0]))


                #calculate delta for each entry in the minibatch. This is basically one data point, with 6054 features
                for x in minibatch:


                    print("start of This is item number"+str(labelCounter)+" in Batch number:"+str(batchCount))

                    #add a fake feature
                    # ####print("shape of the xT array before bias:"+str((x.T.shape)))
                    # #newx=np.stack([x.T,biasForX],axis=0)
                    # ###print("shape of the x array after bias:"+str((newx.shape)))

                    ##print("shape of the theta transpose is:"+str(theta.transpose().shape))
                    ###print("shape of the x transpose is is:"+str(x.transpose().shape))
                    ###print(theta.transpose().shape[-1] == x.transpose().shape[-2], theta.transpose().shape[1])
                    #d=np.dot(x,theta.transpose())
                    d=x*theta
                    ##print("shape of d:"+str(d.shape))
                    ###print(" of d:"+str(d))
                    dint=d[0][0]
                    ##print("value of dint is:"+str(dint))
                    sig=calculateSigmoid(dint)
                    sigint=sig[0]
                    thisLabel=str(labels[labelCounter])
                    #thisLabel=str(labels[2])
                    ##print("shape of labels is:"+str(labels.shape))
                    ##print("value of labelCounter is:"+str(labelCounter))
                    ###print("X is:"+str(x))
                    ##print("value of thisLabel is:"+thisLabel)


                    ##print("value of sigint is:"+str(sigint))
                    # ##print("sahpe of sig is:"+str(sig[0][0][0].shape))

                    labelInt=1;
                    labelCounter=labelCounter+1

                    #if its ham, call it label 0
                    ##print("theta value of a random element before"+str(theta[1311][0]))
                    if(thisLabel=="ham"):
                        labelInt=0


                    #find the value of y(i)-sigmoid

                    #do yi-hi (this is a scalar value)
                    diff=labelInt-sigint
                    ###print("value of labelInt is:"+str(labelInt))
                    ##print("value of diff is:"+str(diff))




                    #fvProduct=(x.T)*diff
                    fvProduct=np.multiply(x,diff)
                    ##print(str(delta))



                    print("value of fvProduct shape is:"+str(fvProduct.shape))
                    print("value of delta shape is:"+str(delta.shape))
                    ###print()
                    print("theta value of a random element before"+str(fvProduct.T[1311][0]))
                    print("theta value of a random element before"+str(delta[1311][0]))
                    print("value of delta dimenstions is:"+str(delta.ndim))

                    #add this product thing to delta
                    delta=np.add(delta,fvProduct.T)
                    #delta=delta+fvProduct
                    #delta=np.array(delta)
                    #delta = np.asarray(delta).reshape(-1)
                    print("value of delta dimenstions is:"+str(delta.ndim))

                    #print(str(delta))
                    print("fvProduct value of a random element after"+str(fvProduct.T[1311][0]))
                    #print("delta value of a random element after"+str(delta[1311][1686]))
                    print("one element in this batch finished running")
                    print("value of delta shape is:"+str(delta.shape))
                    print("end of This is item number"+str(labelCounter)+" in Batch number:"+str(batchCount))
                    #sys.exit(1)




                    #fvProduct=np.multiply((x.transpose()),diff)
                    ######print("fvProduct "+str(fvProduct))
                    #if(labelCounter==1):

                    ###print("delta value of a random element before"+str(delta[5821][0]))





                    #new theta value is old theta plus this new fVproduct(vector)
                    #update, do this after teh end of every batch, but with the average fvProduct from the given batch
                    #add this new delta to the theta


                   # ##print("theta value of a random element before"+str(theta[5821][0]))
                   # ##print("delta value of a random element before"+str(delta[5821][0]))
                    #sys.exit(1)

                    #if(labelCounter==1):

                print("done with batch number:"+str(batchCount))


                print("one batch finished running")
                print("value of miniBatchSize  is:"+str(miniBatchSize))
                print("shape of delta  is:"+str(delta.shape))
                print("delta value of a random element before"+str(delta[0,0]))

                #at the end of each batch divdide the delta by the batch size
                delta =delta/miniBatchSize

                print("miniBatchSize batch finished running")
                print("one batch finished running")


                print("value of a random eleement in delta after one batch "+str(delta[0][0]))
                print("theta value of a random element before"+str(theta[1311][0]))
                print("shape of theta  is:"+str(theta.shape))
                print("shape of delta  is:"+str(delta.shape))
                delta = np.asarray(delta).reshape(-1)
                theta = np.asarray(theta).reshape(-1)
                theta=theta+delta
                #theta=np.add(theta,delta)
                print("shape of theta  is:"+str(theta.shape))
                #print("theta value of a random element after"+str(theta[1311][0]))
                print("done addition going to exit")

                sys.exit(1)

                #after every batch increase the start index by batch size
                batchStartIndex=batchStartIndex+miniBatchSize
                batchendIndex=batchStartIndex+miniBatchSize



                print("end of batch Number:"+str(batchCount+1))


            print("end of Epoch Number:"+str(epoch+1))

                ##print("theta after one batch for a random eleement"+str(theta[5821][0]))


                #print("shape of thetat is:"+str(theta.shape))

            #print("done with all batches. value of batch count is:"+str(batchCount))




        ##print("theta after all epochs"+str(theta[5821][0]))
        #print("value of labelCounter is:"+str(labelCounter))
        ##print("bias after all iterations"+str(theta[noOfFeatures][0]))
        return theta,vectorizer


    except:
        import traceback
        #print('generic exception: ' + traceback.format_exc())
        elapsed_time = time.time() - start_time
        #print("time taken:" + str(elapsed_time))


