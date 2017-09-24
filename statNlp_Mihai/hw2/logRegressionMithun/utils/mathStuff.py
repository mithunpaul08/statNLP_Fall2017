from csv import DictReader
import os
import sys
import csv
import pandas as pd
import numpy as np

def calculateSigmoid(x):
    x_array=np.array([-x])
    sig=1/(1+np.exp(x_array))
    print("value of sig is "+str(sig))
    return sig
