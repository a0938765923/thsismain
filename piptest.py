from re import M
import ntutrun
import os
from git import Repo

# import sys
# sys.path.append(r'C:\Users\User\Desktop\RobotTestThsis')
# sys.path.append(r'C:\Users\User\Desktop\test_automation\RobotTests')
# arguments = len(sys.argv) - 1
# key=[]
# value=[]
# opt={}
# position = 1
# while (arguments >= position):
#     if sys.argv[position].startswith("--"):
#         key.append(sys.argv[position][2:])
#     else:
#         value.append(sys.argv[position])
#     position = position + 1
    
# for i in range(0,len(key)):
#     # print("key[i]",key[i])
#     # print("value[i]",value[i])
#     opt[key[i]]=value[i]
# print(opt)
# retval = os.getcwd()
# ntutrun.exe(**opt, outpath=retval)

# userXmlFileXpath="C:/Users/mark/Desktop/output.xml"

import tkinter as tk
import os
from tkinter.filedialog import askdirectory, askopenfilename
from tkinter import *
from tkinter import filedialog



window = tk.Tk()
window.title('測試案例選擇工具')
window.geometry('800x600')
window.configure(background='white')

def selectPath():
    path_=askdirectory()
    path.set(path_)
    # print(path)


def get_value():
    print("this is my show")
    opt={}
    opt["ProjectPath"]=height_entry.get()
    opt["commandOPt"]=weight_entry.get()
    opt["autoRun"]=variable.get()
    print(opt)
    retval = os.getcwd()
    print(retval)
    txtarea.delete('1.0','end')
    ntutrun.exe(**opt, outpath=retval)
    path = 'C://Users//asus//Desktop//mytree.txt'   # 文件路徑
    f = open(path,encoding="utf-8")
    # print()
    txtarea.insert(END, f.read())
    # txtarea.configure(state='disabled')
    f.close()
    if os.path.exists(path):  # 如果文件存在
        os.remove(path)  
    # print("--ProjectPath "+height_entry.get()+" --commandOPt "+weight_entry.get()+" --autoRun "+variable.get())

def push(path, msg):
    repo= Repo(path)
    # 'C:\\Users\\asus\\Desktop\\RobotTestThsis\\RobotTestThsis'
    print(repo.git.add('.')) 
    # repo.git.commit('-m test')
    repo.git.commit("-m " + msg)
    repo.git.push()

path=StringVar()
# print(path)
header_label = tk.Label(window, text='測試案例選擇工具', background='white')
header_label.pack()

height_frame = tk.Frame(window)
height_frame.pack(side=tk.TOP)

height_label = tk.Label(height_frame, text='專案路徑（Project Path）',background='white')
height_label.pack(side=tk.LEFT)
height_entry = tk.Entry(height_frame,textvariable=path)
height_entry.pack(side=tk.LEFT)
btn=tk.Button(height_frame,text="路徑選擇",command=selectPath)
btn.pack(side=tk.LEFT)

weight_frame = tk.Frame(window)
weight_frame.pack(side=tk.TOP)
weight_label = tk.Label(weight_frame, text='Command Opt', background='white')
weight_label.pack(side=tk.LEFT)
weight_entry = tk.Entry(weight_frame)
weight_entry.pack(side=tk.LEFT)

OptionList = [
"True",
"False"
] 
Auto_Run_frame = tk.Frame(window)
Auto_Run_frame.pack(side=tk.TOP)
Auto_Run_label = tk.Label(Auto_Run_frame, text='Auto Run', background='white')
Auto_Run_label.pack(side=tk.LEFT)
variable = tk.StringVar(Auto_Run_frame)
variable.set(OptionList[0])
opt = tk.OptionMenu(Auto_Run_frame, variable, *OptionList)
opt.pack(side=tk.LEFT)

Run_frame = tk.Frame(window)
Run_frame.pack(side=tk.TOP)
RunBtn=tk.Button(Run_frame,text="執行",command=get_value)
RunBtn.pack(side=tk.LEFT)

text_frame = tk.Frame(window)
text_frame.pack(side=tk.TOP)
txtarea = tk.Text(text_frame)
txtarea.pack(side=tk.LEFT)


result_label = tk.Label(window, background='white')
result_label.pack()
RunBtn1=tk.Button(window,text="push",command=push(path.get(),"commitTest"))
# print(path)
RunBtn1.pack(side=tk.TOP)

window.mainloop()