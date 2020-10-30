'''
Pre-requisites:
1. PyAutoGUI Introduction
2. How to capture Screenshot using python

*** Required Library: pip install PyAutoGUI

'''


#Without GUI
import pyautogui

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'C:\Users\Nasik\Desktop\python tutorial\screenshot1.png')


#With GUI
import pyautogui
import tkinter as tk

root = tk.Tk()
root.title('Screenshot Taker')


canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()


def myScreenshot():
   ss = pyautogui.screenshot()
   ss.save(r'C:\Users\Nasik\Desktop\python tutorial\screenshot8.png')


myButton = tk.Button(text='Take Screenshot', command=myScreenshot, bg='crimson',fg='white',font= 15)
canvas1.create_window(150, 150, window=myButton)

root.mainloop()