# script imports
import functions as F
import parameters as P

# shell
F.tryPrintBreak()
F.tryPrint("MODEL START")

######################################################

# import training data
F.tryPrint("Importing training data")

fields, clData = F.decodeCSV(P.clDataPath)
_, daData = F.decodeCSV(P.daDataPath)

# run main routine
averageError = 0

for epoch in P.epochs:

    error = 0
    
    for chunk in trainingData:
    # train
        train(F.unpackChunk(chunk))

    for chunk in testingData:
    # test
        totalError += ?
    
        error = totalError / nTestData

averageError = totalError / nEpochs

######################################################

# shell
F.tryPrint("MODEL STOP")
F.tryPrintBreak()
