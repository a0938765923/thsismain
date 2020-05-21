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

# print(a[1])
# print(commandOPtions.split())
# userXmlFileXpath="C:/Users/mark/Desktop/output.xml"
retval = os.getcwd()
path="C:/Jenkins/workspace/mark_1"
commandOPtions='-P ./ -P ./Project'
precommitId="ad9861b3f5c7ae65e1e91ae4f2c6bbb71b0ea613"

# ntutrun.exe(ProjectPath=path, outpath=retval, commandOPt=commandOPtions, autoRun=True)
ntutrun.exe(**opt, outpath=retval)