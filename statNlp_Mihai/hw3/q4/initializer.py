from utils.readData import readPOS
from utils.lstm import startLstm
#from utils.lstm import prepare_training_data
import os

import time

start_time = time.time()

trainingData="train.tagged"
devData="dev.tagged"
testingData="test.tagged"

cwd = os.getcwd()
training_data=readPOS(cwd,trainingData)

#print(training_data[0])
#prepare_training_data(posTrain)

startLstm(training_data)
print("--- %s minutes ---" % ((time.time() - start_time)/60)
