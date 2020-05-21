import ntutrun
import os
retval = os.getcwd()
ProjectPath="C:/Jenkins/workspace/mark_1"
commandOPtions="-P ./ -P ./Project"
commitID="ad9861b3f5c7ae65e1e91ae4f2c6bbb71b0ea613"
commitID2="0fb60c0ec276108be1592059dc59afcbe2960e8b"
ntutrun.exe(ProjectPath, outpath=retval, precommitId=commitID, cmpcommitId=commitID2,commandOPt=commandOPtions, autoRun=True)
# ntutrun.exe(ProjectPath, outpath=retval, precommitId=commitID, commandOPt=commandOPtions, autoRun=True)