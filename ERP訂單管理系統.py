import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

win=Tk()
win.minsize(width=1025, height=480)
win.maxsize(width=1025, height=480)
win.resizable(width=False, height=False)


toolbar = tk.Frame(win,bd=1,  relief=tk.RAISED)
toolbar.pack(side='top', fill='x')
def funQuit():
    exit()
x=[]
y=[]
def printPlot():
    for i in orderList:
        x.append(i[1])
        y.append(i[2])
    plt.plot(x,y,'r')
    plt.ylabel('金額')
    plt.xlabel('商品')
    plt.show()
img = Image.open("exit.jpg")
eimg = ImageTk.PhotoImage(img)
pimg=Image.open('print.png')
pimg=pimg.resize((25,25))
pimg=ImageTk.PhotoImage(pimg)
printButton=Button(toolbar, image=pimg,command=printPlot)
printButton.pack(side=tk.LEFT, padx=2, pady=2)
exitButton = Button(toolbar, image=eimg, relief=tk.FLAT,command=funQuit)
exitButton.pack(side=tk.LEFT, padx=2, pady=2)

menubar=tk.Menu(win)
filemenu=tk.Menu(menubar)
filemenu.add_command(label="open")
filemenu.add_command(label='save')
filemenu.add_command(label='exit')
menubar.add_cascade(label='File',menu=filemenu)

filemenu = tk.Menu(menubar)
filemenu.add_command(label="Help")
filemenu.add_command(label="About")
menubar.add_cascade(label="Help", menu=filemenu)
win.config(menu=menubar)


Label(win,text='訂單編號').place(x=10, y=50)
sbVar=StringVar()
ttk.Spinbox(win,from_=0,to=100,textvariable=sbVar).place(x=80, y=50)
Label(win,text='商品名稱').place(x=10, y=80)
eVar1=StringVar()
Entry(win,textvariable=eVar1).place(x=80, y=80)
Label(win,text='金額').place(x=10, y=110)
eVar2=StringVar()
Entry(win,textvariable=eVar2).place(x=80, y=110)
Label(win,text='備註').place(x=10, y=140)
st=ScrolledText(win, width=20,  height=1)
st.place(x=80, y=140)

radioValue = tk.IntVar()
rdio1 = tk.Radiobutton(win, text='未處理',variable=radioValue, value=1).pack()
rdio2 = tk.Radiobutton(win, text='已寄出',variable=radioValue, value=2).pack()
rdio3 = tk.Radiobutton(win, text='已收到',variable=radioValue, value=3).pack()
rdio4 = tk.Radiobutton(win, text='結案',variable=radioValue, value=4).pack()


columns = ('訂單編號', '商品名稱','金額', '備註','訂單狀況')
tree=ttk.Treeview(win, columns=columns, show='headings')
tree.place(x=10, y=220)
tree.heading('訂單編號', text='訂單編號')
tree.heading('商品名稱', text='商品名稱')
tree.heading('金額', text='金額')
tree.heading('備註', text='備註')
tree.heading('訂單狀況', text='訂單狀況')


def printInfo():
    for selected_item in tree.selection():
        record = tree.item(selected_item)['values']
        print(record)
Button(win,text='print',command=printInfo).pack()


class ordenStatus:
    def __init__(self,number,name,price,remark,status):
        self.number=number
        self.name = name
        self.price = price
        self.remark = remark
        self.status = status

orderList=[[1,'apple',50,'none','shipped'],[2,'orange',100,'none','closed'],[3,'banana',75,'none','received'],
           [4,'melon',150,'none','unprocessed']]

for i in range(len(orderList)):
    tree.insert('', tk.END, values=orderList[i])

def item_selected(event):
    for selected_item in tree.selection():
        record = tree.item(selected_item)['values']
        sbVar.set(record[0])
        eVar1.set(record[1])
        eVar2.set(record[2])
        st.delete(1.0, END)
        st.insert(1.0,record[3])
        if record[4]=='unprocessed':
            radioValue.set(1)
        if record[4]=='shipped':
            radioValue.set(2)
        if record[4]=='received':
            radioValue.set(3)
        if record[4]=='closed':
            radioValue.set(4)

tree.bind('<<TreeviewSelect>>', item_selected)


win.mainloop()