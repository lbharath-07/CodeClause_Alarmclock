import datetime
import tkinter as tk
import winsound

class AlarmClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Alarm Clock")

        # set up time input fields
        self.hour_input = tk.Entry(self.root, width=2, font=("Arial", 20))
        self.colon_label = tk.Label(self.root, text=":", font=("Arial", 20))
        self.minute_input = tk.Entry(self.root, width=2, font=("Arial", 20))

        # set up alarm button
        self.set_alarm_button = tk.Button(self.root, text="Set Alarm", command=self.set_alarm)

        # pack the widgets
        self.hour_input.pack(side=tk.LEFT)
        self.colon_label.pack(side=tk.LEFT)
        self.minute_input.pack(side=tk.LEFT)
        self.set_alarm_button.pack(side=tk.LEFT)

        self.alarm_time = None

    def set_alarm(self):
        try:
            hour = int(self.hour_input.get())
            minute = int(self.minute_input.get())
            self.alarm_time = datetime.time(hour, minute)           #stores the input alarm time
            print(f"Alarm set for {self.alarm_time.strftime('%I:%M %p')}")
        except ValueError:
            print("Please enter a valid time")

    def check_alarm(self):
        current_time = datetime.datetime.now().time()               #stores the current value of time
        if self.alarm_time and current_time >= self.alarm_time:
            self.play_alarm()

    def play_alarm(self):
        for i in range(3):
            winsound.Beep(440, 500)
            winsound.Beep(880, 500)
        self.alarm_time = None

    def run(self):
        while True:
            self.root.update()
            self.check_alarm()

if __name__ == "__main__":
    alarm_clock = AlarmClock()
    alarm_clock.run()
