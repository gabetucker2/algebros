# script imports
import functions as F
import parameters as P

# library imports
# TODO: add

# shell
F.tryPrintBreak()
F.tryPrint("TEST START")

######################################################

fields, CLValues = F.decodeCSV(P.clDataPath)
_, DLValues = F.decodeCSV(P.dlDataPath)

print(CLValues)

######################################################

# shell
F.tryPrint("TEST STOP")
F.tryPrintBreak()
