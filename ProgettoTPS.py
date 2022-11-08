from pandas import *
import os
import time
from Funzioni import *
LocatePoz = "DatabasePoz.xlsx"
LocateIng = "DatabaseIng.xlsx"

dfPoz =  DataFrame(read_excel(LocatePoz))
dfIng =  DataFrame(read_excel(LocateIng))
MostraPoz(dfPoz)
dfPoz = NewPozione(dfPoz,dfIng)