import sys


def calculate_bigrams(tagsAsSentence):
    bigramCounter={}
    rowcounter=0;
    #for each of the sentences
    for row in tagsAsSentence:
        rowcounter=rowcounter+1;
        #for each element in the row, take 2 at a time
        tagCounter=0;
        for eachTag in row:

            if(tagCounter>0):
                #concatenate me with the guy before me
                combined=row[tagCounter-1]+"_"+eachTag
                if combined in bigramCounter:
                    bigramCounter[combined] += 1
                else:
                    bigramCounter[combined] = 1

            tagCounter=tagCounter+1;



        if(rowcounter==2):
            print(bigramCounter)
            combined=""
            sys.exit(1)

