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

# import tkinter as tk
# import math

# window = tk.Tk()
# window.title('BMI App')
# window.geometry('800x600')
# window.configure(background='white')

# def calculate_bmi_number():
#     height = float(height_entry.get())
#     weight = float(weight_entry.get())
#     print(height)
#     print(weight)
#     bmi_value = round(weight / math.pow(height, 2.0), 2)
#     result = '你的 BMI 指數為：{} {}'.format(bmi_value, get_bmi_status_description(bmi_value))
#     result_label.configure(text=result)

# def get_bmi_status_description(bmi_value):
#     if bmi_value < 18.5:
#         return '體重過輕囉，多吃點！'
#     elif bmi_value >= 18.5 and bmi_value < 24:
#         return '體重剛剛好，繼續保持！'
#     elif bmi_value >= 24 :
#         return '體重有點過重囉，少吃多運動！'

# header_label = tk.Label(window, text='BMI 計算器', background='white')
# header_label.pack()

# height_frame = tk.Frame(window)
# height_frame.pack(side=tk.TOP)
# height_label = tk.Label(height_frame, text='專案路徑（Project Path）',background='white')
# height_label.pack(side=tk.LEFT)
# height_entry = tk.Entry(height_frame)
# height_entry.pack(side=tk.LEFT)

# weight_frame = tk.Frame(window)
# weight_frame.pack(side=tk.TOP)
# weight_label = tk.Label(weight_frame, text='執行專案的地方（Run Project Path）', background='white')
# weight_label.pack(side=tk.LEFT)
# weight_entry = tk.Entry(weight_frame)
# weight_entry.pack(side=tk.LEFT)

# result_label = tk.Label(window, background='white')
# result_label.pack()

# calculate_btn = tk.Button(window, text='馬上計算', command=calculate_bmi_number, background='white')
# calculate_btn.pack()

# window.mainloop()