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
posTrain=readPOS(cwd,trainingData)

#prepare_training_data(posTrain)

#startLstm(posTrain)
print("--- %s seconds ---" % (time.time() - start_time))
