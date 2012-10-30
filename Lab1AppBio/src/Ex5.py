'''
Created on 30 Okt 2012

@author: maryger
'''
import re




def printStringInFarsta(string):
    re1 = '^(p)'  # Any Single Word Character (Not Whitespace) 1
    re2 = '(r)'  # Any Single Word Character (Not Whitespace) 2
    re3 = '(o)'  # Any Single Word Character (Not Whitespace) 3
    re4 = '(t)'  # Any Single Word Character (Not Whitespace) 4
    re5 = '(\\d+)'  # Integer Number 1
    re6 = '(   )'  # White Space 1
    re7 = '((?:[a-z][a-z]+))'  # Word 1
    pattern = re1 + re2 + re3 + re4 + re5 + re6 + re7
    rg = re.compile(pattern, re.IGNORECASE | re.DOTALL)
    result = rg.search(string)
    if result is None:
        pass
    else:
        print result.group(0)
        print constructFarstaBlocks(result.group(1))

def constructFarstaBlocks(string):    
    Line = ''
    for i in range(1,len(string)):
        Line += string[i]
        if i ==  len(string)-1 or i%60==0:
            Line +='\n'
    else: return Line 

def readStringSequences():
    input_var = raw_input("Enter the file name you want to read: ") + ".txt"
    f = open ("../" + input_var, "r")
    line = f.readline()
    while line:
        printStringInFarsta(line)
        line = f.readline()
        


#Main part block
readStringSequences()
