# script imports
import parameters as P

# library imports
import csv

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

def dataPipeline(dlTargetName, CLData, DLData):

    workingChunk1 = []
    t = 0

    def filterColumns():

        workingChunk1.append(t)        # t
        t += 1

        workingChunk1.append(CLData[?]) # cl_open
        workingChunk1.append(CLData[?]) # cl_high
        workingChunk1.append(CLData[?]) # cl_low
        workingChunk1.append(CLData[?]) # cl_close
        workingChunk1.append(CLData[?]) # cl_adjclose
        workingChunk1.append(CLData[?]) # cl_vol
                                    
        workingChunk1.append(DLData[?]) # dl_open
        workingChunk1.append(DLData[?]) # dl_target

    def splitRows():
        
        
    
    return ''

def makeChunk(t, dlTarget, data):

    innerChunks = []

    for  in :
        dlTarget_tn = data[t][?]

        innerChunk = dlTarget_tn, dlOpen_tn, clOpen_tn, clHigh_tn, clLow_tn, clClose_tn, clAdjClose_tn, clVolume_tn
        innerChunks.append(innerChunk)

    chunk = {
        "inputs" : [
            [data[t][]??]
        ],
        "target" : dlTarget
    }

    chunk["inputs"].extend(prevChunks)

    return chunk

# unpackChunkOuter(chunk) -> dlTarget_t, dlOpen_t, clOpen_t, innerChunk
def unpackChunkOuter(chunk):

    # dlTarget_t, dlOpen_t, clOpen_t, innerChunk
    return chunk["target"], chunk["inputs"][0][0], chunk["inputs"][0][1], chunk["inputs"][1:]

# unpackChunkInner(innerChunkn) -> dlTarget_tn, dlOpen_tn, clOpen_tn, clHigh_tn, clLow_tn, clClose_tn, clAdjClose_tn, clVolume_tn
def unpackChunkInner(innerChunkn):
    
    # dlTarget_tn, dlOpen_tn, clOpen_tn, clHigh_tn, clLow_tn, clClose_tn, clAdjClose_tn, clVolume_tn
    return innerChunkn[0], innerChunkn[1], innerChunkn[2], innerChunkn[3], innerChunkn[4], innerChunkn[5], innerChunkn[6], innerChunkn[7]
