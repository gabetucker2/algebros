# import library
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller

# import scripts
import parameters as P
import functions as F

# functions
numChunks = 0

def trainMLRLoop(chunk):

    numChunks += 1

    X_train = []
    
    daTarget_t, daOpen_t, clOpen_t, innerChunkn = F.unpackChunkOuter(chunk)

    X_train.append(daOpen_t, clOpen_t)

    for n in range(P.N):
        daTarget_tn, daOpen_tn, clOpen_tn, clHigh_tn, clLow_tn, clClose_tn, clAdjClose_tn, clVolume_tn = F.unpackChunkInner(innerChunkn[n])
        X_train.append(daTarget_tn, daOpen_tn, clOpen_tn, clHigh_tn, clLow_tn, clClose_tn, clAdjClose_tn, clVolume_tn)

    Y_train = daTarget_t

    model = sm.OLS(Y_train, X_train).fit()

    alpha = model.params[0]
    betas = model.params[1:].values

    if len(P.workingMemory) == 0:
        P.workingMemory.append(alpha)
        P.workingMemory.extend(betas)
    else:
        P.workingMemory[0] += alpha
        for c in range(len(X_train)):
            P.workingMemory[c+1] += betas[c]

def trainMLRFinal():
    
    # average the coefficients across each chunk MLR was ran on

    for i in range(len(P.workingMemory)):
        P.workingMemory[i] /= numChunks
    
    numChunks = 0

def testMLR(chunk):

    X_train = []
    
    daTarget_t, daOpen_t, clOpen_t, innerChunkn = F.unpackChunkOuter(chunk)

    X_train.append(daOpen_t, clOpen_t)

    for n in range(P.N):
        daTarget_tn, daOpen_tn, clOpen_tn, clHigh_tn, clLow_tn, clClose_tn, clAdjClose_tn, clVolume_tn = F.unpackChunkInner(innerChunkn[n])
        X_train.append(daTarget_tn, daOpen_tn, clOpen_tn, clHigh_tn, clLow_tn, clClose_tn, clAdjClose_tn, clVolume_tn)

    actualValue = daTarget_t

    predictedValue = P.workingMemory[0]
    # dot product to calculate predicted value
    for i in range(len(P.workingMemory)):
        predictedValue += P.workingMemory[i+1] * X_train[i]

    return actualValue - predictedValue
