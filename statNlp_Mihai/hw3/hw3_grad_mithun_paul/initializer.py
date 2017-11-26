from utils.readData import readSpam
from utils.lstm import prepare_training_data
import os

trainingData="train.tagged"
devData="dev.tagged"
testingData="test.tagged"

cwd = os.getcwd()
posTrain=readSpam(cwd,trainingData)
prepare_training_data(posTrain)
