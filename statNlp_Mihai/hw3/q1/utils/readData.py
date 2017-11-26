from csv import DictReader
import os
import sys
import csv
import pandas as pd


#return each data in this format

# training_data = [
#     ("The dog ate the apple".split(), ["DET", "NN", "V", "DET", "NN"]),
#     ("Everybody read that book".split(), ["NN", "V", "DET", "NN"])
# ]

training_data =[]

def read_without_space(cwd, inputFile):
    path = cwd+"/data/"
    df =pd.read_csv(path  + inputFile,sep='\t',header=None,names=['words','tags'])
    return df;


