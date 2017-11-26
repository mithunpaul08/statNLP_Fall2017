from utils.readData import readSpam
from utils.lstm import startLstm
import os

trainingData="train.tagged"
devData="dev.tagged"
testingData="test.tagged"

cwd = os.getcwd()
posTrain=readSpam(cwd,trainingData)
startLstm(posTrain)
