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




def read_tags_only_with_blank_lines(cwd, inputFile):
    all_sentences=[]
    tags=["START"]
    rowcounter=0;
    path = cwd+"/data/"
    spamReader = csv.reader(open(path+inputFile, newline=''), delimiter='\t', quotechar='|')
    for row in spamReader:
        rowcounter=rowcounter+1
        if(row==[]):
            #attach end
            tags.append("END")
            all_sentences.append(tags)
            #send tags to calculate bigrams
            #attach to a bigram list
            tags=["START"]
        else:
            tags.append(row[1])
    return all_sentences





def read__dev_data_with_blank_lines(cwd, inputFile):
    all_sentences=[]
    tags=["START"]
    mywords=[]
    rowcounter=0;
    path = cwd+"/data/"
    spamReader = csv.reader(open(path+inputFile, newline=''), delimiter='\t', quotechar='|')
    for row in spamReader:
        rowcounter=rowcounter+1
        print("word is:"+str(len(row[1])))
        if(len(row[1])==0):
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

