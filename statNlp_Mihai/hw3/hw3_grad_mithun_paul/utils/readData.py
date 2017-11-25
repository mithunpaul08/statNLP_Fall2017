from csv import DictReader
import os
import sys
import csv
import pandas as pd

def readSpam(cwd, inputFile):

    path = cwd+"/data/"

    df =pd.read_csv(path  + inputFile,sep='\s',header=None,names=['word','tag'],engine='python')
    #print("done reading spamData")

    return df;


