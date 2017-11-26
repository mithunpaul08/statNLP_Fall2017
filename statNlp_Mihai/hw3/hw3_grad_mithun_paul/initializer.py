from utils.readData import readSpam
from utils.lstm import startLstm
import os

import time

start_time = time.time()

trainingData="train.tagged"
devData="dev.tagged"
testingData="test.tagged"

cwd = os.getcwd()
posTrain=readSpam(cwd,trainingData)
startLstm(posTrain)
print("--- %s seconds ---" % (time.time() - start_time))
