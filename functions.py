# script imports
import parameters as P

# library imports
import csv
import random

# helper functions

def tryPrintBreak():
    if not P.debuggingMode:
        print("---------------")

def tryPrint(output):
    if not P.debuggingMode:
        print(output)

# data functions

def decodeCSV(filePath):
    with open(filePath, newline='') as csvfile:
        # Read the CSV file
        reader = csv.reader(csvfile)
        
        # Extract the rows
        rows = list(reader)
        
        # Check if there are at least two rows
        if len(rows) < 2:
            raise ValueError("CSV file must have at least two rows")
        
        # First row for keys, second row for values
        fields = rows[0]
        values = []
        for row in rows[1:]:
            values.append(row)

        return fields, values

def filterColumns(daTargetName, fieldNames, clData, daData):

    outerChunks = []

    T = len(clData) # total number of timesteps
    
    for t in range(P.N, T):

        # create outer chunk

        outerChunk = {
            "inputs" : [
                [daData[t][1], clData[t][1]]
            ],
            "target" : daData[t][fieldNames.index(daTargetName)]
        }

        # create inner chunk

        innerChunks = []

        for n in range(1, P.N): # n-back

            tn = t - n

            newList = []

            newList.append(daData[tn][fieldNames.index(daTargetName)]) # da_target
            newList.append(daData[tn][1])                              # da_open

            newList.append(clData[tn][1])                              # cl_open
            newList.append(clData[tn][2])                              # cl_high
            newList.append(clData[tn][3])                              # cl_low
            newList.append(clData[tn][4])                              # cl_close
            newList.append(clData[tn][5])                              # cl_adjclose
            newList.append(clData[tn][6])                              # cl_vol

            innerChunks.append(newList)
        
        outerChunk["inputs"].extend(innerChunks)
    
    return outerChunks

def splitRows():
    
    rand_ui = random.random()

    

# unpackChunkOuter(chunk) -> daTarget_t, daOpen_t, clOpen_t, innerChunk
def unpackChunkOuter(chunk):

    # daTarget_t, daOpen_t, clOpen_t, innerChunk
    return chunk["target"], chunk["inputs"][0][0], chunk["inputs"][0][1], chunk["inputs"][1:]

# unpackChunkInner(innerChunkn) -> daTarget_tn, daOpen_tn, clOpen_tn, clHigh_tn, clLow_tn, clClose_tn, clAdjClose_tn, clVolume_tn
def unpackChunkInner(innerChunkn):
    
    # daTarget_tn, daOpen_tn, clOpen_tn, clHigh_tn, clLow_tn, clClose_tn, clAdjClose_tn, clVolume_tn
    return innerChunkn[0], innerChunkn[1], innerChunkn[2], innerChunkn[3], innerChunkn[4], innerChunkn[5], innerChunkn[6], innerChunkn[7]
