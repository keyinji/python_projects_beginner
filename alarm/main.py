from tkinter import *
import datetime
import time
import winsound
import threading

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        if now == set_alarm_timer:
            print("Wake Up!")
            winsound.Beep(500, 2000)
            break

def actual_time():
    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M:%S")
    time_label.config(text=now)
    clock.after(1000, actual_time)

def set_alarm():
    alarm_time = f"{hour.get()}:{min.get()}:{sec.get()}"
    threading.Thread(target=alarm, args=(alarm_time,)).start()

clock = Tk()
clock.title("Digital Clock")
clock.geometry("400x200")

time_label = Label(clock, font="Arial 15 bold")
time_label.pack()

time_format = Label(clock, text="Enter time in 24 hour format!", fg="red", font="Arial 10 bold")
time_format.pack()

addTime = Label(clock, text="Hour  Min   Sec", font="Arial 10 bold")
addTime.pack()

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(clock, textvariable=hour, width=15)
hourTime.pack()

minTime = Entry(clock, textvariable=min, width=15)
minTime.pack()

secTime = Entry(clock, textvariable=sec, width=15)
secTime.pack()

setAlarm = Button(clock, text="Set Alarm", fg="white", bg="blue", command=set_alarm)
setAlarm.pack()

actual_time()

clock.mainloop()

