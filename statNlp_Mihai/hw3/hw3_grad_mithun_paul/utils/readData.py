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

def readPOS(cwd, inputFile):
    words=[]
    tags=[]
    rowcounter=0;
    path = cwd+"/data/"
    spamReader = csv.reader(open(path+inputFile, newline=''), delimiter='\t', quotechar='|')
    for row in spamReader:
        rowcounter=rowcounter+1
        if(row==[]):
            training_data.append([words,tags])
            words=[]
            tags=[]
        else:
            words.append(row[0])
            tags.append(row[1])

        if(rowcounter==50):
            print(training_data)
            sys.exit(1)

