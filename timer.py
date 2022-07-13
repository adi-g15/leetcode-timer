#!/bin/env python
from tkinter import DISABLED, Tk, Canvas, Frame, Label, Button

"""
Editing defaults:
    - Edit self.t for default time (in seconds, default 300s)
"""

class App(Tk):

    def __init__(self):
        super().__init__()

        self.after_id = None

        self.t = 300
        self.counter = 0

        # Window will not be resizable
        self.resizable(width=False, height=False)
        self.title("Timer")

        self.main_canvas = Canvas(self, height=220, width=400, bg="#2e2e2f")
        self.main_canvas.pack()

        self.main_frame = Frame(self, bg="#2e2e2f")
        self.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.counter_lbl= Label(self.main_frame,text="5:00",bg="#2e2e2f",fg="#b7b7b7",font="SourceCodePro 68")
        self.counter_lbl.grid(row=1,column=0,columnspan=2,rowspan=4,padx=23,pady=20)

        self.lbl_questions= Label(text=f"Total Questions: {self.counter}",fg="#b7b7b7",bg="#2e2e2f",font="Times 10 italic")
        #self.lbl_questions.grid(row=0,column=0,columnspan=2)
        self.lbl_questions.place(x=10,y=10)

        self.btn_study=Button(self.main_frame,text="Reset",activebackground="#242424", bg="#3f3f3f",width=23, fg="#b7b7b7", border=0, command=self.reset)
        self.btn_study.grid(row=5, column=0,columnspan=1)

        self.btn_break=Button(self.main_frame,text="Stop",activebackground="#242424", bg="#3f3f3f", fg="#b7b7b7",width=25,border=0,command=self.stop)
        self.btn_break.grid(row=5, column=1, columnspan=1)

    def countdown(self):
        print(self.t)
        if self.t>0:
            mins,secs=divmod(self.t,60)
            timer="{:01d}:{:02d}".format(mins,secs)
            self.counter_lbl.config(text=timer)
            self.t=self.t-1
            self.after_id = self.counter_lbl.after(1000,self.countdown)

        elif self.t==0:
            self.counter_lbl.config(text="00:00")
            self.counter+=1
            self.lbl_questions.config(text=f"Total Questions: {self.counter}")

    def reset(self):
        # Reset to 5 minutes
        self.t = 300-1
        if self.after_id:
            self.counter_lbl.after_cancel(self.after_id)
        self.countdown()
        print(self.after_id)

    def stop(self):
        if self.after_id:
            self.counter_lbl.after_cancel(self.after_id)
        self.counter_lbl.config(text="00:00")
        self.btn_break.config(state=DISABLED)
        self.btn_study.config(text="Start")

def run():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    run()
