from tkinter import*
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"

YELLOW1 = "#f7f5dd"
FONT_NAME = "Courier"
timer=None
WORK_MIN = 1
SHORT_BREAK_MIN =5
LONG_BREAK_MIN =20
reps=0


window=Tk()
window.title("Pomodoro")
window.config(padx=200,pady=200,bg=YELLOW1)

def reset_method():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    label_check.config(text="")
    global reps
    reps=0







def start_method(rep=None):
    global reps
    reps=reps+1
    work_sec = 1 * 60
    short_sec = 5*60

    long_sec = 20*60
    if reps%8==0:
        timer_label.config(text="Long_break",fg=PINK )
        count_red(long_sec)
    elif  reps%2==0:
        timer_label.config(text="short_break",fg=RED)
        count_red(short_sec)
    else:
        timer_label.config(text="Break",fg=GREEN)
        count_red(work_sec)




def count_red(count):

    count_minute=math.floor(count/60)
    count_sec=count%60
    if count_sec==0:
        count_sec="00"
    elif count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_minute}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(100, count_red, count - 1)
    else:
        start_method()
        #after every work section a  checkmark is created
        if reps%2==0:
            label_check.config(text="✔")





timer_label=Label(window,text="Timer",fg=GREEN,bg=YELLOW1,font=(FONT_NAME,30,"bold"))
timer_label.grid(row=0,column=1)


button_start=Button(window,text="Start",highlightthickness=0,command=start_method)
button_start.grid(row=2,column=0)

button_reset=Button(window,text="reset",highlightthickness=0,command=reset_method)
button_reset.grid(row=2,column=2)


label_check=Label(window,fg=GREEN,font=(FONT_NAME,30,"bold"))
label_check.grid(row=3,column=1)



tomato_image=PhotoImage(file="tomato.png")
canvas=Canvas(width=200,height=223,bg=YELLOW1,highlightthickness=0)
canvas.create_image(101,105,image=tomato_image)
timer_text=canvas.create_text(100,120,text="00:00",fill="white",font=(FONT_NAME,20,"bold"))
canvas.grid(row=1,column=1)

window.mainloop()