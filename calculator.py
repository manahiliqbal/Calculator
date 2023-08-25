from tkinter import *

root = Tk()
root.geometry("250x410")
root.title("Calculator")
root.wm_iconbitmap("cal_icon.ico")
root.minsize(250, 410) 
root.maxsize(250,410)
def click(event):
    global val
    text = event.widget.cget("text")
    if (text=="="):
        if (val.get().isdigit()):
           value = float(val.get())
        else:
            try:
                value = eval(screen.get())
            except Exception:
                value = "Error"
        val.set(value) 
        screen.update()    
    elif (text=="C"):
        val.set("")
        screen.update()
    elif(text=="%"):
       val.set(float(val.get())*0.100) 
       screen.update()      
    else:
        if (text=="x"):
          val.set(val.get() + "*")
          screen.update()
        else:
           val.set(val.get() + text)
           screen.update()  
val = StringVar()
val.set("")
screen = Entry (root, textvariable=val, bg="light grey", font="TimesNewRoman 30 bold")
screen.pack(ipadx=5 ,padx=10, pady=10, fill=X)

f1 = Frame(root)
row1_buttons = ["C", "="]
for row1_button in row1_buttons:
  b = Button(f1, text=row1_button, fg="purple3", bg="mediumpurple1", font="TimesNewRoman 20 bold", padx=8, pady=3, width=5, height=1)
  b.pack(side=LEFT, padx=4, pady=3)
  b.bind("<Button-1>", click)
f1.pack() 

f2 = Frame(root)
row2_buttons = ["7", "8", "9", "x"] 
for row2_button in row2_buttons:
  if row2_button=="x":
    b = Button(f2, text=row2_button, fg="purple3", bg="mediumpurple1", font="TimesNewRoman 20 bold", padx=5, pady=3, width=2, height=1)
  else:
    b = Button(f2, text=row2_button, font="TimesNewRoman 20 bold", padx=5, pady=3, width=2, height=1)   
  b.pack(side=LEFT, padx=3, pady=3)
  b.bind("<Button-1>", click)
f2.pack()  

f3 = Frame(root)
row3_buttons = ["4", "5", "6", "+"]
for row3_button in row3_buttons:
  if row3_button=="+":
    b = Button(f3, text=row3_button, fg="purple3", bg="mediumpurple1", font="TimesNewRoman 20 bold", padx=5, pady=3, width=2, height=1)
  else:
    b = Button(f3, text=row3_button, font="TimesNewRoman 20 bold", padx=5, pady=3, width=2, height=1) 
  b.pack(side=LEFT, padx=3, pady=3)
  b.bind("<Button-1>", click)
f3.pack()

f4 = Frame(root)
row4_buttons = ["1", "2", "3", "-"]
for row4_button in row4_buttons:
  if row4_button=="-":
    b = Button(f4, text=row4_button, fg="purple3", bg="mediumpurple1", font="TimesNewRoman 20 bold", padx=5, pady=3, width=2, height=1)
  else:
    b = Button(f4, text=row4_button, font="TimesNewRoman 20 bold", padx=5, pady=3, width=2, height=1) 
  b.pack(side=LEFT, padx=3, pady=3)
  b.bind("<Button-1>", click)
f4.pack()

f5 = Frame(root)
row5_buttons = [ ".","0", "%", "/"]
for row5_button in row5_buttons:
  if row5_button=="/":
    b = Button(f5, text=row5_button, fg="purple3", bg="mediumpurple1", font="TimesNewRoman 20 bold", padx=5, pady=3, width=2, height=1)
  else:
    b = Button(f5, text=row5_button, font="TimesNewRoman 20 bold", padx=5, pady=3, width=2, height=1) 
  b.pack(side=LEFT, padx=3, pady=3)
  b.bind("<Button-1>", click)
f5.pack()

root.mainloop()