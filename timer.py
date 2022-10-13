#!/bin/env python
from tkinter import NORMAL, DISABLED, Tk, Canvas, Frame, Label, Button
from sys import argv

"""
Editing defaults:
    - Edit self.t for default time (in seconds, default 300s)
"""

class App(Tk):

    def __init__(self):
        super().__init__()

        self.after_id = None

        # Use argv[1] if present, else set 6 minutes (360 seconds) as default
        if len(argv) > 1:
            self.max_t = int(argv[1])*60
        else:
            self.max_t = 6*60
        self.t = self.max_t

        self.counter = 0

        # Window will not be resizable
        self.resizable(width=False, height=False)
        self.title("Timer")

        self.main_canvas = Canvas(self, height=220, width=400, bg="#2e2e2f")
        self.main_canvas.pack()

        self.main_frame = Frame(self, bg="#2e2e2f")
        self.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # t//60 represents number of minutes
        # t%60 is number of seconds
        self.counter_lbl = Label(self.main_frame,text="{:01d}:{:02d}".format(self.t//60, self.t%60),bg="#2e2e2f",fg="#b7b7b7",font="SourceCodePro 68")
        self.counter_lbl.grid(row=1,column=0,columnspan=2,rowspan=4,padx=23,pady=20)

        self.lbl_resets= Label(text=f"Total Resets: {self.counter}",fg="#b7b7b7",bg="#2e2e2f",font="Times 10 italic")
        #self.lbl_resets.grid(row=0,column=0,columnspan=2)
        self.lbl_resets.place(x=10,y=10)

        self.btn_reset=Button(self.main_frame,text="Start",activebackground="#242424", bg="#3f3f3f",width=23, fg="#b7b7b7", border=0, command=self.reset)
        self.btn_reset.grid(row=5, column=0,columnspan=1)

        self.btn_stop=Button(self.main_frame,text="Stop",activebackground="#242424", bg="#3f3f3f", fg="#b7b7b7",width=25,border=0,command=self.stop)
        self.btn_stop.config(state=DISABLED)
        self.btn_stop.grid(row=5, column=1, columnspan=1)

    def countdown(self):
        if self.t>0:
            mins,secs=divmod(self.t,60)
            timer="{:01d}:{:02d}".format(mins,secs)
            self.counter_lbl.config(text=timer)
            self.t=self.t-1
            self.after_id = self.counter_lbl.after(1000,self.countdown)

        elif self.t==0:
            self.counter_lbl.config(text="00:00")
            self.counter+=1
            self.lbl_resets.config(text=f"Total Resets: {self.counter}")

    def reset(self):
        # If the Stop button was disabled, re-enable it
        if self.btn_stop.config('state')[-1]==DISABLED:
            self.btn_stop.config(text="Stop")
            self.btn_stop.config(state=NORMAL)
            self.btn_reset.config(text="Reset")

        # Reset to max_t - 1 minutes,seconds
        self.t = self.max_t - 1

        # Increase reset counter
        self.counter+=1
        self.lbl_resets.config(text=f"Total Resets: {self.counter}")

        # Start the countdown
        if self.after_id:
            self.counter_lbl.after_cancel(self.after_id)
        self.countdown()

    def stop(self):
        if self.after_id:
            self.counter_lbl.after_cancel(self.after_id)
        self.counter_lbl.config(text="----")
        self.btn_stop.config(state=DISABLED)
        self.btn_reset.config(text="Start")

def run():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    run()
