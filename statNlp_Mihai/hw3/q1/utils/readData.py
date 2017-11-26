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




def read_with_space(cwd, inputFile):
    training_data=[]
    tags=["START"]
    rowcounter=0;
    path = cwd+"/data/"
    spamReader = csv.reader(open(path+inputFile, newline=''), delimiter='\t', quotechar='|')
    for row in spamReader:
        rowcounter=rowcounter+1
        if(row==[]):
            #attach end
            tags.append("END")
            print(tags)
            sys.exit(1)
            #send tags to calculate bigrams
            #attach to a bigram list
            tags=["START"]
        else:
            tags.append(row[1])
