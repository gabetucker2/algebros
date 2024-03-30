# script imports
import functions as F
import parameters as P
import functions_MLR

# shell
F.tryPrintBreak()
F.tryPrint("MODEL START")

######################################################

# import training data
F.tryPrint("Importing training data")

fieldNames, clData = F.decodeCSV(P.clDataPath)
_, daData = F.decodeCSV(P.daDataPath)

# run main routine
totalEpochError = 0

for epoch in range(P.epochs):

    combinedChunks = F.combineChunks(fieldNames, clData, daData)
    trainChunks, testChunks = F.splitChunks(combinedChunks)

    # train
    for trainChunk in trainChunks:
        functions_MLR.trainMLRLoop(trainChunk)
    functions_MLR.trainMLRFinal(len(trainChunks))

    # test
    totalChunkError = 0
    for testChunk in testChunks:
        chunkError = functions_MLR.testMLR(testChunk)
        totalChunkError += chunkError
        # F.tryPrint(f"CHUNK ERROR: {chunkError}")
    epochError = totalChunkError / len(testChunks)
    totalEpochError += epochError

    F.tryPrint(f"EPOCH {epoch+1} ERROR: {epochError}")

averageEpochError = totalEpochError / P.epochs

F.tryPrint(f"AVERAGE ERROR ACROSS {P.epochs} EPOCHS: {averageEpochError}")

######################################################

# shell
F.tryPrint("MODEL STOP")
F.tryPrintBreak()
