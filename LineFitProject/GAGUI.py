import tkinter as tk
import GAEnvironment as GAE
import numpy as np
from matplotlib import animation


def findLine():
    x = list(map(int, e1.get().split(", ")))
    y = list(map(int, e2.get().split(", "))) 
    environment = GAE.Environment(x, y, 4, 0.005)
    """
    # Set up figure, axis, and plot element
    fig = plt.figure()
    ax = plt.axes(xlim=(min(self.x)*1.2, max(self.x)*1.2), ylim=(-999, 999))
    line, = ax.plot([], [], lw=2)

    # initialization function: plot the background of each frame
    def init():
        line.set_data([], [])
        return line,

    # animation function.
    def animate(i):
        x = np.linspace(0, np.amax(self.x)*1.2, 1000)
        y = np.sin(2 * np.pi * (x - 0.01 * i))
        line.set_data(x, y)
        return environment.drawPopulation()
    """
    while isEnd:
        environment.graphDots()
        environment.drawPopulation()
        environment.selection()
        environment.reproduction()

def end():
    isEnd = False
    plt.close('all')

isEnd = True
master = tk.Tk()
master.title('best fitline') 
master.geometry('300x300')
l1 = tk.Label(master, text='x axis values').grid(row=0) 
l2 = tk.Label(master, text='y axis values').grid(row=1) 
e1 = tk.Entry(master)
e2 = tk.Entry(master)
b1 = tk.Button(master, text='Generate', width=25, command=findLine)
b2 = tk.Button(master, text='Terminate', width=25, command=end)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e1.insert(0, '2, 55, 23')
e2.insert(0, '16, 40, 43')
b1.place(x=30, y=60)
b2.place(x=30, y=90)
master.mainloop()
