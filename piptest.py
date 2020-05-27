import ntutrun
import os
import sys

arguments = len(sys.argv) - 1
key=[]
value=[]
opt={}
position = 1
while (arguments >= position):
    if sys.argv[position].startswith("--"):
        key.append(sys.argv[position][2:])
    else:
        value.append(sys.argv[position])
    position = position + 1
    
for i in range(0,len(key)):
    opt[key[i]]=value[i]

retval = os.getcwd()
ntutrun.exe(**opt, outpath=retval)

# userXmlFileXpath="C:/Users/mark/Desktop/output.xml"