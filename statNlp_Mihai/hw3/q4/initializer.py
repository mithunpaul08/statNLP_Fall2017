from utils.readData import readPOS
from utils.lstm import startLstm
from utils.lstm import startLstmWithPickle
from utils.readData import read_test_data_with_blank_lines


#from utils.lstm import prepare_training_data
import os

import time

start_time = time.time()

trainingDataInput="train.tagged"
devData="dev.tagged"
testingDataInput="test.tagged"

cwd = os.getcwd()


#print(training_data[0])
#prepare_training_data(posTrain)

#startLstm(training_data)



while True:
            print("                      ")
            print("          ******            ")

            print("Welcome to LSTM Tagger. Please pick one of the following:")

            print("To train a model, save it and to test with it, Press:1")
            print("To test using an already trained saved model, Press:2")
            print("To exit Press:0")


            myInput=input("what is your choice:")
            if(myInput=="1"):
                testData=read_test_data_with_blank_lines(cwd, testingDataInput)
                training_data=readPOS(cwd,trainingDataInput)
                startLstm(training_data,testData)

            else:
                if(myInput=="0"):
                    print("******Good Bye")
                    break;
                else:
                    if(myInput=="3"):
                        trainAndTest(True)
                    else:

                        if (myInput == "2"):
                            testData=read_test_data_with_blank_lines(cwd, testingDataInput)
                            startLstmWithPickle(testData)




print("--- Took %s seconds---" % ((time.time() - start_time)*100/60))
