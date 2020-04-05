import Test
import os
import sys
import re
import coverage
import numpy as np
import Utils
import DataFIle
#  Test2.py   5  12  17  21
#  Test1.py   5  12
#  Test.py    17  21
#def Data_scan(CovRunFileName, file_name = "t.txt"):
#    flag_f = True
#    _FileN = open(file_name,'r')
#    fileData = _FileN.read()
#    for line in fileData.splitlines():
#        if re.findall("\%\s+",line) and flag_f == True:
#            covLineNumbers = line.split("%")[-1]
#            flag_f = False
#            data_file = open("CovrageLine.txt",'a+')
#            covLineNumbers = re.sub(",", " ", covLineNumbers)
#            data_file.write(CovRunFileName + covLineNumbers + "\n")
#            data_file.close()
#    _FileN.close()
#    return

def Data_scan(context, lineNumbers):
    data_file = open("CovrageLine.txt",'a+')
    data_file.write(context+ ":" + str(lineNumbers).strip('[]') + "\n")
    data_file.close()
    return

def ReadLinesInfo(fileName):
    file1 = open('CovrageLine.txt', 'r') 
    Lines = file1.readlines()
    lastLine =[]
    for line in Lines: 
        fName = line.split(':')[0]
        if fName == fileName:
            lastLine = line.split(":")[1]

    return lastLine

def GetResponsibleTestsForLines(fileName,changedLines):
    coverageFile = open('CovrageLine.txt', 'r') 
    Lines = coverageFile.readlines()
    print("Lines")
    print(Lines)
    testCases = []
    for line in Lines: 
        if fileName == line.split(':')[0]:
            coverageLines = list(map(int, line.split(':')[2].split(",")))
            #coverageLines = line.split(':')[1].split(',')
            print("coverageLines")
            print(coverageLines)
            for lineNumber in changedLines:
                if lineNumber in coverageLines:
                    testCases.append(line.split(':')[1])
                    break

    return testCases

def Upgrade(NameTest):
    
    
    #os.system("coverage html")
    flag_f = True
    data_file = open("CovrageLine.txt",'r+')
    Upgrade_File = open("Upgrade.txt",'w')
    fileData = data_file.read()

    for line in fileData.splitlines():
        if re.findall(NameTest+" ",line):
            os.system("coverage run"+ NameTest)
            os.system("coverage report -m > t.txt")
            os.system("coverage html")
            NewC = open('t.txt', 'r')
            NewCov = NewC.read()
            for li in NewCov.splitlines():
                if re.findall("\%\s+",li) and flag_f == True:
                    covNumbers = li.split("%")[-1]
                    flag_f = False
                    covNumbers = re.sub(",", " ", covNumbers)
                    line = NameTest + covNumbers
        Upgrade_File.write(line + "\n")
    
    #return

def ScanLineNumber(Number):
    Nu = []
    FlagObg = False
    data_file = open("CovrageLine.txt",'r+')
    fileD = data_file.read()
    for lines in fileD.splitlines():
        if re.findall("\s+",lines):
            CName = lines.split()[0]
            Nu = lines.split(CName)[1].split()
            
            j = 0
            for  i in Nu: #range(len(Nu)-1): int(Nu[i])
                if Number > int(i) or FlagObg == False:
                    FlagObg = True
                    if Number < int(i) and FlagObg == True:
                        print("*******************************************")
                        print(CName)
                        print("*******************************************")
                        print(lines)
                        print("*******************************************")
                        print("Upgrade data!")
                        print("*******************************************")
                        Upgrade(CName)

                    else:
                        FlagObg = False
               

    data_file.close()
    return

list_Line = []
if  len( sys.argv) == 1:
    cov = coverage.Coverage()
    utils = Utils.Utils()
    utils.run_all_functions(cov,"Test")
    
    
    data = cov.get_data()
    contexts = data.measured_contexts()
    dictToInsert = {}
    dictToUpdate = {}
    rows = DataFIle.getLogs()
    keys= [row[1] for row in rows]

    for context in contexts:
        if context :
            data.set_query_context(context);    
            lines = data.lines("C:\\Users\\arsen\\Desktop\\porc\\Kod.py")
            if context in keys:
                dictToUpdate[context]=str(lines).strip('[]')
            else:
                dictToInsert[context]=str(lines).strip('[]')

    if len(dictToInsert)!=0:
        print ("dictToInsert")
        print (dictToInsert)
        DataFIle.insertSqliteTable(dictToInsert)
    
    if len(dictToUpdate)!=0:
        print ("dictToUpdate")
        print (dictToUpdate)
        DataFIle.updateSqliteTable(dictToUpdate)
    

    #print ("Test.TestPow.test_Pow_zero")
    #data.set_query_context("Test.TestPow.test_Pow_zero");
    #lines = data.lines("C:\\Users\\arsen\\Desktop\\porc\\Kod.py")
    #print(lines)
    #---------------------------------------------------
    #os.system("coverage run Test.py")
    #os.system("coverage report -m > t.txt")
    #os.system("coverage html")

    
    #Data_scan("Test.py","test_Pow_zero",data)
    
    #data = GetResponsibleTestsForLines("Test.py",[1,8])
    
    #os.system("coverage run Test1.py")
    #os.system("coverage report -m > t.txt")
    #os.system("coverage html")
    #Data_scan("Test1.py")

   # os.system("coverage run Test2.py")
   # os.system("coverage report -m > t.txt")
   # os.system("coverage html")
   # Data_scan("Test2.py")
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