import pandas as pd

import pymysql

from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:General@1234@127.0.0.1/QUIZ_QUESTIONS")

df = pd.read_sql_query("SELECT * FROM QUIZ_1", engine)

df.head(10)
 
from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("QUIZ program for 2021")
window.geometry("800x800")
#window.size(width=100,height=100)
window.resizable(0,0)
window.configure(bg='white')
nhans=0
global totalmarks
totalmarks=0
global var


def hint():
    global var
   
    l2 = tk.Label(text="                1."+df.at[var,'OP1']+"                       ",fg="blue",bg="white").grid(row=7,column=0)
    l3 = tk.Label(text="                2."+df.at[var,'OP2']+"                       ",fg="blue",bg="white").grid(row=8,column=0)
    l4 = tk.Label(text="                3."+df.at[var,'OP3']+"                       ",fg="blue",bg="white").grid(row=9,column=0)
    l5 = tk.Label(text="                4."+df.at[var,'OP4']+"                       ",fg="blue",bg="white").grid(row=10,column=0)
   
    button1 = tk.Button(text="Option 1", command=optionone)
    button1.grid(row=7,column=1)
    button2 = tk.Button(text="Option 2", command=optiontwo)
    button2.grid(row=8,column=1)
    button3 = tk.Button(text="Option 3", command=optionthree)
    button3.grid(row=9,column=1)
    button4 = tk.Button(text="Option 4", command=optionfour)
    button4.grid(row=10,column=1)
    if(int(df.at[var,'HINT1'])==0):
        l2 = tk.Label(text="                            XXX                          ",fg="blue",bg="white").grid(row=7,column=0)
        button1.config(state="disabled")
    if(int(df.at[var,'HINT2'])==0):
        l3 = tk.Label(text="                            XXX                          ",fg="blue",bg="white").grid(row=8,column=0)
        button2.config(state="disabled")
    if(int(df.at[var,'HINT3'])==0):
        l4 = tk.Label(text="                            XXX                          ",fg="blue",bg="white").grid(row=9,column=0)
        button3.config(state="disabled")
    if(int(df.at[var,'HINT4'])==0):
        l2 = tk.Label(text="                            XXX                          ",fg="blue",bg="white").grid(row=10,column=0)
        button4.config(state="disabled")

       
       
             
   
def optionone():
    global var,totalmarks
   
    nhans=int(df.at[var,'ANSWER'])
    if(nhans==1):
        label14 = tk.Label(text="    Thats correct!   ",fg="blue",bg="white").grid(row=15,column=0)
        totalmarks=totalmarks+4
    else:
        label15 = tk.Label(text="Thats wrong sorry!",fg="blue",bg="white").grid(row=15,column=0)
   

def optiontwo():
    global var,totalmarks
   
    nhans=int(df.at[var,'ANSWER'])
    if(nhans==2):
        label14 = tk.Label(text="   Thats correct!   ",fg="blue",bg="white").grid(row=15,column=0)
        totalmarks=totalmarks+4
    else:
        label15 = tk.Label(text="Thats wrong sorry!",fg="blue",bg="white").grid(row=15,column=0)

def optionthree():
    global var,totalmarks
   
    nhans=int(df.at[var,'ANSWER'])
    if(nhans==3):
        label14 = tk.Label(text="    Thats correct!    ",fg="blue",bg="white").grid(row=15,column=0)
        totalmarks=totalmarks+4
    else:
        label15 = tk.Label(text="Thats wrong sorry!",fg="blue",bg="white").grid(row=15,column=0)
       
def optionfour():
    global var,totalmarks
   
    nhans=int(df.at[var,'ANSWER'])
    if(nhans==4):
        label14 = tk.Label(text="    Thats correct!    ",fg="blue",bg="white").grid(row=15,column=0)
        totalmarks=totalmarks+4
    else:
        label15 = tk.Label(text="Thats wrong sorry!",fg="blue",bg="white").grid(row=15,column=0)

def one():
    global var
    var=0
    l1 = tk.Label(text=df.at[0,'QUESTION'],fg="blue",bg="white").grid(row=6,column=0)
    l2 = tk.Label(text="1."+df.at[0,'OP1']+"                       ",fg="blue",bg="white").grid(row=7,column=0)
    l3 = tk.Label(text="2."+df.at[0,'OP2']+"                       ",fg="blue",bg="white").grid(row=8,column=0)
    l4 = tk.Label(text="3."+df.at[0,'OP3']+"                       ",fg="blue",bg="white").grid(row=9,column=0)
    l5 = tk.Label(text="4."+df.at[0,'OP4']+"                       ",fg="blue",bg="white").grid(row=10,column=0)
    button1 = tk.Button(text="Option 1", command=optionone)
    button1.grid(row=7,column=1)
    button2 = tk.Button(text="Option 2", command=optiontwo)
    button2.grid(row=8,column=1)
    button3 = tk.Button(text="Option 3", command=optionthree)
    button3.grid(row=9,column=1)
    button4 = tk.Button(text="Option 4", command=optionfour)
    button4.grid(row=10,column=1)
    hintbutton = tk.Button(text="50/50 chance", command=hint)
    hintbutton.grid(row=11,column=0)
   
def two():
    global var
    var=1
    l1 = tk.Label(text="      "+df.at[1,'QUESTION']+"                       ",fg="blue",bg="white").grid(row=6,column=0)
    l2 = tk.Label(text="            1."+df.at[1,'OP1']+"                       ",fg="blue",bg="white").grid(row=7,column=0)
    l3 = tk.Label(text="            2."+df.at[1,'OP2']+"                       ",fg="blue",bg="white").grid(row=8,column=0)
    l4 = tk.Label(text="            3."+df.at[1,'OP3']+"                       ",fg="blue",bg="white").grid(row=9,column=0)
    l5 = tk.Label(text="            4."+df.at[1,'OP4']+"                       ",fg="blue",bg="white").grid(row=10,column=0)
    button1 = tk.Button(text="Option 1", command=optionone)
    button1.grid(row=7,column=1)
    button2 = tk.Button(text="Option 2", command=optiontwo)
    button2.grid(row=8,column=1)
    button3 = tk.Button(text="Option 3", command=optionthree)
    button3.grid(row=9,column=1)
    button4 = tk.Button(text="Option 4", command=optionfour)
    button4.grid(row=10,column=1)
    hintbutton = tk.Button(text="50/50 chance", command=hint)
    hintbutton.grid(row=11,column=0)
   
def three():
    global var
    var=2  
    l1 = tk.Label(text="      "+df.at[2,'QUESTION']+"                       ",fg="blue",bg="white").grid(row=6,column=0)
    l2 = tk.Label(text="            1."+df.at[2,'OP1']+"                       ",fg="blue",bg="white").grid(row=7,column=0)
    l3 = tk.Label(text="            2."+df.at[2,'OP2']+"                       ",fg="blue",bg="white").grid(row=8,column=0)
    l4 = tk.Label(text="            3."+df.at[2,'OP3']+"                       ",fg="blue",bg="white").grid(row=9,column=0)
    l5 = tk.Label(text="            4."+df.at[2,'OP4']+"                       ",fg="blue",bg="white").grid(row=10,column=0)
    button1 = tk.Button(text="Option 1", command=optionone)
    button1.grid(row=7,column=1)
    button2 = tk.Button(text="Option 2", command=optiontwo)
    button2.grid(row=8,column=1)
    button3 = tk.Button(text="Option 3", command=optionthree)
    button3.grid(row=9,column=1)
    button4 = tk.Button(text="Option 4", command=optionfour)
    button4.grid(row=10,column=1)
    hintbutton = tk.Button(text="50/50 chance", command=hint)
    hintbutton.grid(row=11,column=0)
   
def four():
    global var
    var=3
    l1 = tk.Label(text="               "+df.at[3,'QUESTION']+"                       ",fg="blue",bg="white").grid(row=6,column=0)
    l2 = tk.Label(text="             1."+df.at[3,'OP1']+"                       ",fg="blue",bg="white").grid(row=7,column=0)
    l3 = tk.Label(text="             2."+df.at[3,'OP2']+"                       ",fg="blue",bg="white").grid(row=8,column=0)
    l4 = tk.Label(text="             3."+df.at[3,'OP3']+"                       ",fg="blue",bg="white").grid(row=9,column=0)
    l5 = tk.Label(text="             4."+df.at[3,'OP4']+"                       ",fg="blue",bg="white").grid(row=10,column=0)
    button1 = tk.Button(text="Option 1", command=optionone)
    button1.grid(row=7,column=1)
    button2 = tk.Button(text="Option 2", command=optiontwo)
    button2.grid(row=8,column=1)
    button3 = tk.Button(text="Option 3", command=optionthree)
    button3.grid(row=9,column=1)
    button4 = tk.Button(text="Option 4", command=optionfour)
    button4.grid(row=10,column=1)
    hintbutton = tk.Button(text="50/50 chance", command=hint)
    hintbutton.grid(row=11,column=0)
   
def five():
    global var
    var=4
    l1 = tk.Label(text="               "+df.at[4,'QUESTION']+"                       ",fg="blue",bg="white").grid(row=6,column=0)
    l2 = tk.Label(text="              1."+df.at[4,'OP1']+"                       ",fg="blue",bg="white").grid(row=7,column=0)
    l3 = tk.Label(text="              2."+df.at[4,'OP2']+"                       ",fg="blue",bg="white").grid(row=8,column=0)
    l4 = tk.Label(text="              3."+df.at[4,'OP3']+"                       ",fg="blue",bg="white").grid(row=9,column=0)
    l5 = tk.Label(text="              4."+df.at[4,'OP4']+"                       ",fg="blue",bg="white").grid(row=10,column=0)
    button1 = tk.Button(text="Option 1", command=optionone)
    button1.grid(row=7,column=1)
    button2 = tk.Button(text="Option 2", command=optiontwo)
    button2.grid(row=8,column=1)
    button3 = tk.Button(text="Option 3", command=optionthree)
    button3.grid(row=9,column=1)
    button4 = tk.Button(text="Option 4", command=optionfour)
    button4.grid(row=10,column=1)
    hintbutton = tk.Button(text="50/50 chance", command=hint)
    hintbutton.grid(row=11,column=0)
   
def six():
    global var
    var=5
    l1 = tk.Label(text="              "+df.at[5,'QUESTION']+"                       ",fg="blue",bg="white").grid(row=6,column=0)
    l2 = tk.Label(text="               1."+df.at[5,'OP1']+"                       ",fg="blue",bg="white").grid(row=7,column=0)
    l3 = tk.Label(text="               2."+df.at[5,'OP2']+"                       ",fg="blue",bg="white").grid(row=8,column=0)
    l4 = tk.Label(text="               3."+df.at[5,'OP3']+"                       ",fg="blue",bg="white").grid(row=9,column=0)
    l5 = tk.Label(text="               4."+df.at[5,'OP4']+"                       ",fg="blue",bg="white").grid(row=10,column=0)
    button1 = tk.Button(text="Option 1", command=optionone)
    button1.grid(row=7,column=1)
    button2 = tk.Button(text="Option 2", command=optiontwo)
    button2.grid(row=8,column=1)
    button3 = tk.Button(text="Option 3", command=optionthree)
    button3.grid(row=9,column=1)
    button4 = tk.Button(text="Option 4", command=optionfour)
    button4.grid(row=10,column=1)
    hintbutton = tk.Button(text="50/50 chance", command=hint)
    hintbutton.grid(row=11,column=0)  
   
def seven():
    global var
    var=6
    l1 = tk.Label(text="                   "+df.at[6,'QUESTION']+"                       ",fg="blue",bg="white").grid(row=6,column=0)
    l2 = tk.Label(text="                  1."+df.at[6,'OP1']+"                       ",fg="blue",bg="white").grid(row=7,column=0)
    l3 = tk.Label(text="                  2."+df.at[6,'OP2']+"                       ",fg="blue",bg="white").grid(row=8,column=0)
    l4 = tk.Label(text="                  3."+df.at[6,'OP3']+"                       ",fg="blue",bg="white").grid(row=9,column=0)
    l5 = tk.Label(text="                  4."+df.at[6,'OP4']+"                       ",fg="blue",bg="white").grid(row=10,column=0)
    button1 = tk.Button(text="Option 1", command=optionone)
    button1.grid(row=7,column=1)
    button2 = tk.Button(text="Option 2", command=optiontwo)
    button2.grid(row=8,column=1)
    button3 = tk.Button(text="Option 3", command=optionthree)
    button3.grid(row=9,column=1)
    button4 = tk.Button(text="Option 4", command=optionfour)
    button4.grid(row=10,column=1)
    hintbutton = tk.Button(text="50/50 chance", command=hint)
    hintbutton.grid(row=11,column=0)
   
def eight():
    global var
    var=7
    l1 = tk.Label(text="                      "+df.at[7,'QUESTION']+"                       ",fg="blue",bg="white").grid(row=6,column=0)
    l2 = tk.Label(text="                   1."+df.at[7,'OP1']+"                       ",fg="blue",bg="white").grid(row=7,column=0)
    l3 = tk.Label(text="                   2."+df.at[7,'OP2']+"                       ",fg="blue",bg="white").grid(row=8,column=0)
    l4 = tk.Label(text="                   3."+df.at[7,'OP3']+"                       ",fg="blue",bg="white").grid(row=9,column=0)
    l5 = tk.Label(text="                   4."+df.at[7,'OP4']+"                       ",fg="blue",bg="white").grid(row=10,column=0)
    button1 = tk.Button(text="Option 1", command=optionone)
    button1.grid(row=7,column=1)
    button2 = tk.Button(text="Option 2", command=optiontwo)
    button2.grid(row=8,column=1)
    button3 = tk.Button(text="Option 3", command=optionthree)
    button3.grid(row=9,column=1)
    button4 = tk.Button(text="Option 4", command=optionfour)
    button4.grid(row=10,column=1)
    hintbutton = tk.Button(text="50/50 chance", command=hint)
    hintbutton.grid(row=11,column=0)
   
def nine():
    global var
    var=8
   
    l1 = tk.Label(text="                    "+df.at[8,'QUESTION']+"                       ",fg="blue",bg="white").grid(row=6,column=0)
    l2 = tk.Label(text="                   1."+df.at[8,'OP1']+"                       ",fg="blue",bg="white").grid(row=7,column=0)
    l3 = tk.Label(text="                   2."+df.at[8,'OP2']+"                       ",fg="blue",bg="white").grid(row=8,column=0)
    l4 = tk.Label(text="                   3."+df.at[8,'OP3']+"                       ",fg="blue",bg="white").grid(row=9,column=0)
    l5 = tk.Label(text="                   4."+df.at[8,'OP4']+"                       ",fg="blue",bg="white").grid(row=10,column=0)
    button1 = tk.Button(text="Option 1", command=optionone)
    button1.grid(row=7,column=1)
    button2 = tk.Button(text="Option 2", command=optiontwo)
    button2.grid(row=8,column=1)
    button3 = tk.Button(text="Option 3", command=optionthree)
    button3.grid(row=9,column=1)
    button4 = tk.Button(text="Option 4", command=optionfour)
    button4.grid(row=10,column=1)
    hintbutton = tk.Button(text="50/50 chance", command=hint)
    hintbutton.grid(row=11,column=0)
   
def ten():
    global var
    var=9
    l1 = tk.Label(text="                      "+df.at[9,'QUESTION']+"                       ",fg="blue",bg="white").grid(row=6,column=0)
    l2 = tk.Label(text="                      1."+df.at[9,'OP1']+"                       ",fg="blue",bg="white").grid(row=7,column=0)
    l3 = tk.Label(text="                      2."+df.at[9,'OP2']+"                       ",fg="blue",bg="white").grid(row=8,column=0)
    l4 = tk.Label(text="                      3."+df.at[9,'OP3']+"                       ",fg="blue",bg="white").grid(row=9,column=0)
    l5 = tk.Label(text="                      4."+df.at[9,'OP4']+"                       ",fg="blue",bg="white").grid(row=10,column=0)
    button1 = tk.Button(text="Option 1", command=optionone)
    button1.grid(row=7,column=1)
    button2 = tk.Button(text="Option 2", command=optiontwo)
    button2.grid(row=8,column=1)
    button3 = tk.Button(text="Option 3", command=optionthree)
    button3.grid(row=9,column=1)
    button4 = tk.Button(text="Option 4", command=optionfour)
    button4.grid(row=10,column=1)
    hintbutton = tk.Button(text="50/50 chance", command=hint)
    hintbutton.grid(row=11,column=0)
   


label1 = tk.Label(text="It contains 10 multiple choice questions(along with the choice of getting a 50/50 chance",fg="blue",bg="white").grid(row=0,column=0)
label2 = tk.Label(text="You will be given a series of 10 questions to answer.Each question costs 4 marks...", fg="blue",bg="white").grid(row=1,column=0)
label3 = tk.Label(text="Try to answer as many as you can!",fg="blue",bg="white").grid(row=2,column=0)
label4 = tk.Label(text="For every answer you mark correctly you will get 4 marks",fg="blue",bg="white").grid(row=3,column=0)
label6 = tk.Label(text="For every answer you get wrong you get no marks and move onto the next question...",fg="blue",bg="white").grid(row=4,column=0)



window.after(10000,one)
window.after(20000,two)
window.after(30000,three)
window.after(40000,four)
window.after(50000,five)
window.after(60000,six)
window.after(70000,seven)
window.after(80000,eight)
window.after(90000,nine)
window.after(100000,ten)
      
window.mainloop()
