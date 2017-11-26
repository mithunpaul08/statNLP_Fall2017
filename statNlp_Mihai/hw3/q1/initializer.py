from utils.readData import read_without_space

import os
import time
from tqdm import tqdm
start_time = time.time()

trainingData="train.tagged"
devData="dev.tagged"
testingData="test.tagged"

cwd = os.getcwd()
posTrain=read_without_space(cwd,trainingData)

# for word in posTrain["words"]:
#     print(word)


tagCounter={}
for tag in tqdm(posTrain["tags"],total=len(posTrain["tags"])):
    if tag in tagCounter:
        tagCounter[tag] += 1
    else:
        tagCounter[tag] = 1

wordTagCounter={}


#prepare_training_data(posTrain)

#startLstm(posTrain)
print("--- %s seconds ---" % (time.time() - start_time))
