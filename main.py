from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
GRAY = "#79888c"
RED = "#f95335"
GREEN = "#2e8b57"
YELLOW = "#f7f5dd"
COFFEE = "#2b0800"
LIGHT_COFFEE = "#aca099"
COFFEE_TITLE = "#674a40"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 # rounds
timer = "None"
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    #reseting all the variables
    global reps
    reps = 0
    window.after_cancel(timer)
    Start_BTN['state'] = NORMAL
    Status_LBL.config(text="Timer", foreground=COFFEE)
    canvas.itemconfig(Timer_LBL, text="00:00")
    Check_LBL.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    Start_BTN['state'] = DISABLED #disable the start button
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0:#when to take a break and when to start work
        count_down(short_break_sec)
        Status_LBL.config(text="Break", foreground=GRAY)
    elif reps % 8 == 0 :
        count_down(long_break_sec)
        Status_LBL.config(text="Break",foreground=RED)
    else:
        count_down(work_sec)
        Status_LBL.config(text="Work",foreground=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    mins = math.floor(count/60)#rounding the number
    secs = count % 60
    if secs < 10:
        secs = f"0{secs}"#adding zeros to display as two digits 00:00
    if mins < 10:
        mins = f"0{mins}"
    canvas.itemconfig(Timer_LBL, text=f"{mins}:{secs}")
    if count > 0:#if the time still runnung or not
       timer = window.after(1000,count_down,count - 1)
    else:
        start_timer()#calling the function again for a break or work
        marks = ""
        work_sessions = math.floor(reps/2) # every 2 reps represents 1 round of work and break
        for i in range(work_sessions):
            marks+= "✔"
        Check_LBL.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

#-------window setup--------

window = Tk()
window.title("Coffee Timer")
window.config(padx=20,pady=10,bg=YELLOW)
canvas = Canvas(width=221,height=300,bg=YELLOW,highlightthickness=0)
Photo = PhotoImage(file="Coffee1.png")#background photo
canvas.create_image(100,150,image=Photo)

canvas.grid(column=1,row=1)

#--------buttons setup--------

Start_BTN = Button(text="Start",width=5,background=YELLOW,activebackground=LIGHT_COFFEE,highlightthickness=0,borderwidth=0,command=start_timer)
Start_BTN.grid(column=0,row=4)

Reset_BTN = Button(text="Reset",width=5,background=YELLOW,activebackground=LIGHT_COFFEE,highlightthickness=0,borderwidth=0,command=reset_timer)
Reset_BTN.grid(column=2,row=4)


#--------Labels setup--------

Status_LBL = Label(text="Timer", background=YELLOW, foreground=COFFEE_TITLE, font=(FONT_NAME, 35, "bold"))
Status_LBL.grid(column=1, row=0)

Check_LBL = Label(background=YELLOW,foreground=GREEN,font=(FONT_NAME,15,"normal"))
Check_LBL.grid(column=1,row=3)

Timer_LBL= canvas.create_text(100,200,text="00:00",fill=COFFEE,font=(FONT_NAME,25,"bold"))

window.mainloop()