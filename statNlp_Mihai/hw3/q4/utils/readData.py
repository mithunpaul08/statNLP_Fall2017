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


    print(str(len(training_data)))
    return training_data




def read_test_data_with_blank_lines(cwd, inputFile):
    all_sentences=[]
    tags=["START"]
    mywords=[]
    rowcounter=0;
    path = cwd+"/data/"
    spamReader = csv.reader(open(path+inputFile, newline=''), delimiter='\t', quotechar='|')
    for row in spamReader:
        rowcounter=rowcounter+1
        if(row==[]):
            tags.append("END")
            all_sentences.append([[mywords],[tags]])
            #send tags to calculate bigrams
            #attach to a bigram list
            tags=["START"]
            mywords=[]
        else:
            mywords.append(row[0])
            tags.append(row[1])



    return all_sentences

