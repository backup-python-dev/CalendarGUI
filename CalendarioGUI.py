import tkinter as tk
import calendar as c
from tkinter import ttk 


root = tk.Tk()
root.title("CALENDARIO GUI")
frame=tk.Frame(root)
root.config(bg="black")
frame.config(bg="black")
anio=2020
a=tk.StringVar()
calendar_anio = c.calendar(anio)

def Prev():
    global anio
    anio-=1
    calendar_anio = c.calendar(anio)
    a.set(calendar_anio)
def Next():
    global anio
    anio+=1
    calendar_anio = c.calendar(anio)
    a.set(calendar_anio)

a.set(calendar_anio)

btn_Prev=tk.Button(frame,text="<",
bg="black",fg="white",command=Prev).grid(row=0,column=0,padx=10,pady=10)
btn_Next=tk.Button(frame,text=">",bg="black",fg="white",command=Next).grid(row=0,column=1,padx=10,pady=10)

frame.pack()
calendar_anios = tk.Label(root,textvariable=a,bg="black",fg="white",
justify=tk.LEFT,font="Arial 9").pack()
root.mainloop()