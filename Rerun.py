import coverage
import DataFIle
import re
import Utils
def GetRunableTests(fileName, lines):
    functionsToRun=[]
    rows = DataFIle.getLogs(fileName)
    for row in rows:
        print(row[1] +" " + row[2])
        coveredLines=list(map(int, row[2].split(",")))
        for line in coveredLines:
            if line in lines:
                functionsToRun.append(row[1])
                break
    return functionsToRun

casesToRun = GetRunableTests(re.escape("C:\\Users\\arsen\\Desktop\\porc\\Kod.py"),[8,2,9])
cov = coverage.Coverage()
utils = Utils.Utils()
utils.run_tests(cov,casesToRun)