import ntutrun
import os
retval = os.getcwd()
ProjectPath="C:/Jenkins/workspace/mark_1"
commandOPtions='-P ./ -P ./Project'
# print(commandOPtions.split())
ntutrun.exe(ProjectPath,outpath=retval, userXmlFileXpath="C:/Users/mark/Desktop/output.xml", precommitId="ad9861b3f5c7ae65e1e91ae4f2c6bbb71b0ea613", commandOPt=commandOPtions, autoRun=False)