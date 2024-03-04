#Importing pyautogui and time. 
import pyautogui as pya 
import time as tm

#This code is for process automation using the python library: Pyautogui

pya.click(x=800, y=1057)
tm.sleep(1)
pya.write("edge")
pya.press("enter")
pya.click(x=1252, y=59)
pya.write("Youtube.com")

#with this code, is possible any automation process, like: Send emails, send messages...