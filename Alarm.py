from tkinter import *					# Python library used to create GUI interfaces
from tkinter import messagebox
import time, sys
from pygame import mixer
from PIL import Image, ImageTk


# Alarm Function
def alarm():

	alarm_time=user_input.get()

	if alarm_time=="":

		messagebox.askretrycancel("Error Message","Please Enter Value")

	else:

		while True:

			time.sleep(1)

			if (alarm_time==time.strftime("%H:%M")):

				playmusic()

# Alarm ringtone play when its Time for alarm to ring
def playmusic():
	mixer.init()
	mixer.music.load('D:/CodeClause/likki/assets/alarm.mp3')
	mixer.music.play()
	while mixer.music.get_busy():

		time.sleep(30)
		mixer.music.stop()
		sys.exit()

root=Tk()


# Creating the GUI wimndow
root.title("CodeClause | Task-2 - Alarm Clock")
root.geometry("600x380")
root.config(background = "#f28585")

header=Frame(root)
header.place(x=110,y=50)
box1=Frame(root)
box1.place(x=250,y=150)
box2=Frame(root)
box2.place(x=250,y=230)



my_label = Label(header, text="Python Alarm Clock",font=("Helvetica",34))
my_label.grid(row=1,column=1)

#Time taken by User as Input

user_input=Entry(box1,font=('Arial Narrow',20),width=8)
user_input.grid(row=0,column=2)

#Set Alarm Button

start_button=Button(box2,text="Set Alarm",font=('Arial Narrow',16,'bold'),command=alarm)
start_button.grid(row=2,column=2)





root.mainloop()