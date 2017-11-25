from utils.readData import readSpam
import os

trainingData="train.tagged"
devData="dev.tagged"
testingData="test.tagged"

cwd = os.getcwd()
posTrain=readSpam(cwd,trainingData)
print(posTrain["word"][0])
print(posTrain["tag"][0])
