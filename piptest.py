# import ntutrun
# import os
# retval = os.getcwd()
# ProjectPath="C:/Users/mark/Desktop/RobotTestThsis"
# commandOPtions='-P ./ -P ./Project'
# # print(commandOPtions.split())
# ntutrun.exe(ProjectPath,outpath=retval,userXmlFileXpath="C:/Users/mark/Desktop/output.xml",commandOPt=commandOPtions)


import ntutrun
import os
retval = os.getcwd()
ProjectPath="C:/Users/mark/Desktop/test_automation"
commandOPtions='-P ./ -P ./RobotTests --listener ./dctlib/listeners/no_rush.py -v dcTrackURL:https://140.124.181.125 '
# print(commandOPtions.split())
runUnderPath="RobotTests"

ntutrun.exe(ProjectPath,runUnderPath=runUnderPath,outpath=retval, precommitId="c0dfcf4ab128b8033f76b2961b2068f7d22269de",commandOPt=commandOPtions, autoRun=False)






# import os
# ProjectPath="C:/Users/mark/Desktop/test_automation"
# runUnderPath="RobotTests"
# retval = os.getcwd()
# ntutrun.exe(ProjectPath, runUnderPath, retval)