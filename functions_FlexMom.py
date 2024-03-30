# import scripts
import parameters as P
import functions as F

# functions
def trainACTR(chunk):
    
    dlTarget_t, dlOpen_t, clOpen_t, innerChunk = F.unpackChunkOuter(chunk)

    for n in range(P.N):
        dlTarget_tn, dlOpen_tn, clOpen_tn, clHigh_tn, clLow_tn, clClose_tn, clAdjClose_tn, clVolume_tn = F.unpackChunkInner(innerChunk[n])
        
    P.workingMemory = [] # update working memory accordingly along the way

def testACTR(dlTarget_t, dlOpen_t, clOpen_t, prevChunks):
    actualValue = chunk[-1]
    predictedValue = ...

    return actualValue - predictedValue
