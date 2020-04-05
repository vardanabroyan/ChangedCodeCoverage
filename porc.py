import Test
import os
import sys
import re
import coverage
import numpy as np
import Utils
import DataFIle



list_Line = []
if  len( sys.argv) == 1:
    cov = coverage.Coverage()
    utils = Utils.Utils()
    allTestModules = ["Test","Test1","Test2"]
    #allTestModules = ["Test"]
    for module in allTestModules:
        utils.run_all_functions(cov,module)
    utils.run_all_functions(cov,"Test")
    allFiles = ["C:\\Users\\arsen\\Desktop\\porc\\Kod.py"]
    data = cov.get_data()

    contexts = data.measured_contexts()
    arrayToInsert = []
    arrayToUpdate = []
    rows = DataFIle.getLogs()
    keys= [row[1] for row in rows]

    for context in contexts:
        if context :
            print(context)
            data.set_query_context(context);
            for file in allFiles:
                lines = data.lines(file)
                print(lines)
                if context in keys:
                    tuple = (context,str(lines).strip('[]'),file)
                    arrayToUpdate.append(tuple)
                else:
                    tuple = (context,str(lines).strip('[]'),file)
                    arrayToInsert.append(tuple)

    if len(arrayToInsert)!=0:
        print ("arrayToInsert")
        print (arrayToInsert)
        DataFIle.insertSqliteTable(arrayToInsert)
    
    if len(arrayToUpdate)!=0:
        print ("arrayToUpdate")
        print (arrayToUpdate)
        DataFIle.updateSqliteTable(arrayToUpdate)
   
elif not len( sys.argv) == 1:
    list_Line = sys.argv[1::]
    for i in list_Line:
        ScanLineNumber(int(i))
print("###############################################################################################\n")
print ("es silkov kkardas ->  https://coverage.readthedocs.io")
print("###############################################################################################\n")

#coverage run test_mymath.py
#coverage report -m
#coverage html