import tkinter as tk
from tkinter import messagebox
import time

class AlarmClock(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Alarm Clock")
        self.geometry("300x200")

        self.label = tk.Label(self, text="Enter the time to set the alarm:")
        self.label.pack()

        self.time_entry = tk.Entry(self)
        self.time_entry.pack()

        self.set_alarm_button = tk.Button(self, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack()

        self.alarm_time = None

    def set_alarm(self):
        alarm_time_input = self.time_entry.get()

        if alarm_time_input:
            alarm_time_list = alarm_time_input.split(":")

            if len(alarm_time_list) == 2:
                hour, minute = alarm_time_list

                if 0 <= int(hour) <= 23 and 0 <= int(minute) <= 59:
                    self.alarm_time = alarm_time_input
                    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time_input}")
                else:
                    messagebox.showerror("Invalid Time", "Please enter a valid time")
            else:
                messagebox.showerror("Invalid Time", "Please enter a valid time")
        else:
            messagebox.showerror("Invalid Time", "Please enter a valid time")

    def check_alarm(self):
        while True:
            current_time = time.strftime("%H:%M")

            if self.alarm_time == current_time:
                messagebox.showwarning("Alarm", "Wake up! Wake up!")
                break

            time.sleep(60)

if __name__ == "__main__":
    alarm_clock = AlarmClock()
    alarm_clock.mainloop()