import tkinter as tk
import twoDLinearLineFit as lf

def findLine():
    x = list(map(int, e1.get().split(", ")))
    y = list(map(int, e2.get().split(", "))) 
    graph = lf.LineFit(x, y)
    graph.findReg()

master = tk.Tk()
master.title('best fitline') 
master.geometry('300x300')
l1 = tk.Label(master, text='x axis values').grid(row=0) 
l2 = tk.Label(master, text='y axis values').grid(row=1) 
e1 = tk.Entry(master)
e2 = tk.Entry(master)
b1 = tk.Button(master, text='Find', width=25, command=findLine)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e1.insert(0, '2, 55, 23')
e2.insert(0, '16, 40, 43')
b1.place(x=30, y=60)
master.mainloop()











