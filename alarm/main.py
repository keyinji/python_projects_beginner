import tkinter as tk
import time
import threading
import winsound

def alarm():
    global alarm_time
    while True:
        time.sleep(1)
        if alarm_time > 0:
            alarm_time -= 1
        else:
            break
    winsound.Beep(500, 2000)  # Beep for 2 seconds
    print("Time's up!")

def set_alarm():
    global alarm_time
    alarm_time = int(seconds.get())
    threading.Thread(target=alarm).start()

def update_display():
    global alarm_time
    if alarm_time > 0:
        time_label.config(text=f"Time remaining: {alarm_time} seconds")
    else:
        time_label.config(text="Set your timer")
    clock.after(10, update_display)

# GUI setup
clock = tk.Tk()
clock.title("Alarm Clock")
clock.geometry("300x150")

alarm_time = 0  # global variable to keep track of the alarm time in seconds

time_label = tk.Label(clock, text="Set your timer", font=("Arial", 12))
time_label.pack()

seconds = tk.StringVar()
seconds_entry = tk.Entry(clock, textvariable=seconds)
seconds_entry.pack()

set_button = tk.Button(clock, text="Set Alarm", command=set_alarm)
set_button.pack()

update_display()

clock.mainloop()

