# import libraries
import pyactup

# import scripts
import parameters as P
import functions as F

# functions
def trainACTR(chunk):
    
    dlTarget_t, dlOpen_t, clOpen_t, prevChunks = F.unpackChunkOuter(chunk)

    for n in range(P.N):
        dlTarget_tn, dlOpen_tn, clOpen_tn, clHigh_tn, clLow_tn, clClose_tn, clAdjClose_tn, clVolume_tn = F.unpackChunkInner(prevChunks[n])

        # TODO: Do stuff here updating based on t - 1.  You can do this in the loop for each previous timestep's data, or you can do it all at once outside this loop depending on your algorithm treating all data in "prevChunks", "dlOpen_t", and "clOpen_t" as athe training data.

    P.workingMemory = [] # update working memory accordingly along the way

def testACTR(dlTarget_t, dlOpen_t, clOpen_t, prevChunks):
    actualValue = chunk[-1]
    predictedValue = ...

    return actualValue - predictedValue
