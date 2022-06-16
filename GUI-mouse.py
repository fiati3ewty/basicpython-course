from tkinter import *
from tkinter import ttk
import pyautogui as pg
import webbrowser

GUI = Tk()
GUI.title("โปรแกรมสั่งกดปฏิทิน")
GUI.geometry("500x300")

def Calendar():
	pg.click(1873,1061)

def Google():
	webbrowser.open_new_tab("https://www.google.com")

B1 = Button(GUI,text="Calendar1",command=Calendar)
B1.pack(ipadx=20,ipady=10,pady=20)

B2 = ttk.Button(GUI,text="Calendar2",command=Calendar)
B2.pack(ipadx=20,ipady=10,pady=20)

B3 = ttk.Button(GUI,text="Google.com",command=Google)
B3.pack(ipadx=20,ipady=10,pady=20)

GUI.mainloop()