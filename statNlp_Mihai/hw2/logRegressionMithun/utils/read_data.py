from csv import DictReader
import os
import sys
import csv
import pandas as pd

def readSpam(cwd, inputFile):

    path = cwd+"/data/"

    #df =pd.read_csv("~/fall2017/statNlp_Mihai/hw2/logRegressionMithun/data/SMSSpamCollection.train" ,sep='\t',header=None,names=['label','data'])

    df =pd.read_csv(path  + inputFile,sep='\t',header=None,names=['label','data'])
    #print("done reading spamData")

    return df;


