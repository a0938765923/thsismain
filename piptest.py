import ntutrun
import os
import sys
sys.path.append(r'C:\Users\asus\Downloads\RobotTestThsis\RobotTestThsis\Project')
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
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
from git import Repo



window = tk.Tk()
window.title('測試案例選擇工具')
window.geometry('1000x800')
window.configure(background='white')

x=0

def selectPath():
    path_=askdirectory()
    path.set(path_)

def get_value():
    opt={}
    opt["ProjectPath"]=height_entry.get()
    opt["commandOPt"]=weight_entry.get()
    opt["autoRun"]=variable.get()
    print(opt)
    retval = os.getcwd()
    print(retval)
    x=ntutrun.exe(**opt, outpath=retval)
    print("ans",x)
    txtarea.delete('1.0','end')
    path = 'C://Users//asus//Desktop//mytree.txt'  # 文件路径
    f = open(path,encoding="utf-8")
    # print()
    txtarea.insert(END, f.read())
    # txtarea.configure(state='disabled')
    f.close()
    if os.path.exists(path):  # 如果文件存在
        os.remove(path)
    
    if x == 1:
        m.set(x)
        header_label1.config( background='green')
        
        RunBtn1.pack()
    else:
        header_label1.config( background='red')


def push():
    print("------",m.get())
    print("------",path.get())
    msg = tk.simpledialog.askstring(title = '獲取資訊',prompt='請輸入Commit msg：',initialvalue = '')
    repo= Repo(path.get())
    repo.git.add('.')
    repo.git.commit("-m " + msg)
    repo.git.push()


m=StringVar() 
path=StringVar()
print(path)
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
RunBtn1=tk.Button(text="push",command = push)

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

push_frame = tk.Frame(window)
push_frame.pack(side=tk.TOP)

header_label1 = tk.Label(window,text="Status",width=30,height=10)
header_label1.pack()
window.mainloop()