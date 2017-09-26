from csv import DictReader
import os
import sys
import csv
import pandas as pd
import numpy as np
import math

def calculateSigmoid(x):
    x_array=np.array([-x])
    sig=1/(1+np.exp(x_array))
    #sig=1/(1+np.exp(x))
    #print("value of sig is "+str(sig))
    return sig

def calculateAccuracy(goldLabels,PredecitedLabels):
    correctCount=0;
    totalCount=0
    for i, (gold, pred) in enumerate(zip(goldLabels, PredecitedLabels)):
        totalCount=totalCount+1
        #print(gold,pred)
        if gold == pred:
            correctCount=correctCount+1
    #print(correctCount,totalCount)
    accuracy=(correctCount*100)/totalCount
    return accuracy


