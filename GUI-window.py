# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 09:54:33 2021

@author: p35k
"""

import tkinter as tk
import tkinter.messagebox

window=tk.Tk()

window.title('我的第一個GUI')

window.geometry('300x300')

label=tk.Label(window,text="答答答~答答答~",bg="#0000FF",fg="#FF0000")
label.pack()

entry=tk.Entry(window,width=20)
entry.pack()


def clickMe():
    tkinter.messagebox.showinfo(title="提示",message="好痛")
    
button=tk.Button(window,text="這是按鈕",command=clickMe)
button.pack()
window.mainloop()