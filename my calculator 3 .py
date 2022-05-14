import tkinter as tk 
from tkinter import *

root = tk.Tk()
root.geometry("170x230")
root.title("Calculator")
#Entry Widgets to show calculations
inp = Entry(root,width=16,borderwidth=3,relief=RIDGE)
inp.grid(pady=10,row=0,sticky="w",padx=15)
def nine():
        inp.insert("end","9")
def eight():
        inp.insert("end","8")
def seven():
        inp.insert("end","7")
def six():
        inp.insert("end","6")
def five():
        inp.insert("end","5")
def four():
        inp.insert("end","4")
def three():
        inp.insert("end","3")
def two():
        inp.insert("end","2")
def one():
        inp.insert("end","1")
def zero():
        inp.insert("end","0")
def double_zero():
        inp.insert("end","00")
def dot():
        inp.insert("end",".")
def plus():
        inp.insert("end","+")
def minus():
        inp.insert("end","-")
def mul():
        inp.insert("end","*")
def divide():
        inp.insert("end","/")
def modulus():
        inp.insert("end","%")
def result():
        if inp.get() == "":
                inp.insert("end","error")
        elif inp.get()[0] == "0":
                inp.delete(0,"end")
                inp.insert("end","error")
        else:
              #result
                res = inp.get()
                res = eval(res)
                #input
                inp.insert("end"," = ")
                inp.insert("end",res)
def clear():
        inp.delete(0,"end")
#button clear
button_clear = Button(root,text="C",width=2,command=clear,bg="red",fg="white",relief=RIDGE)
button_clear.grid(row=0,sticky="w",padx=125)
#button nine
button_nine = Button(text="9",width=2,command=nine,borderwidth=3,relief=RIDGE)
button_nine.grid(row=1,sticky="w",padx=15)
#button eight
button_eight = Button(text="8",width=2,command=eight,borderwidth=3,relief=RIDGE)
button_eight.grid(row=1,sticky="w",padx=45)
#button seven
button_seven = Button(root,text="7",width=2,command=seven,borderwidth=3,relief=RIDGE)
button_seven.grid(row=1,sticky="w",padx=75)
#button plus
button_plus = Button(root,text="+",width=2,command=plus,borderwidth=3,relief=RIDGE)
button_plus.grid(row=1,sticky="e",padx=125)
#button six
button_six = Button(text="6",width=2,command=six,borderwidth=3,relief=RIDGE)
button_six.grid(row=2,sticky="w",padx=15,pady=5) 
#button five
button_five = Button(text="5",width=2,command=five,borderwidth=3,relief=RIDGE)
button_five.grid(row=2,sticky="w",padx=45,pady=5)
#button four
button_four = Button(root,text="4",width=2,command=four,borderwidth=3,relief=RIDGE)
button_four.grid(row=2,sticky="w",padx=75,pady=5)
#underscore button
button_underscore = Button(root,text="-",width=2,command=minus,borderwidth=3,relief=RIDGE)
button_underscore.grid(row=2,sticky="e",padx=125,pady=5)
# button three
button_three = Button(text="3",width=2,command=three,borderwidth=3,relief=RIDGE)
button_three.grid(row=3,sticky="w",padx=15,pady=5)
# button two
button_two = Button(text="2",width=2,command=two,borderwidth=3,relief=RIDGE)
button_two.grid(row=3,sticky="w",padx=45,pady=5)
# button one 
button_one = Button(root,text="1",width=2,command=one,borderwidth=3,relief=RIDGE)
button_one.grid(row=3,sticky="w",padx=75,pady=5)
#multiply button *
button_multiply = Button(root,text="*",width=2,command=mul,borderwidth=3,relief=RIDGE)
button_multiply.grid(row=3,sticky="e",padx=125,pady=5)
#zero button 
button_zero = Button(text="0",width=2,command=zero,borderwidth=3,relief=RIDGE)
button_zero.grid(row=4,sticky="w",padx=15,pady=5)
# double button zero
double_zero = Button(text="00",width=2,command=double_zero,borderwidth=3,relief=RIDGE)
double_zero.grid(row=4,sticky="w",padx=45,pady=5)
#dot button
button_dot = Button(root,text=".",width=2,command=dot,borderwidth=3,relief=RIDGE)
button_dot.grid(row=4,sticky="w",padx=75,pady=5)
#divide button
button_divide = Button(root,text="/",width=2,command=divide,borderwidth=3,relief=RIDGE)
button_divide.grid(row=4,sticky="e",padx=125,pady=5)
#result button
button_result = Button(root,text="=",width=10,command=result,bg="red",fg="white",borderwidth=3,relief=RIDGE)
button_result.grid(row=5,sticky="w",padx=15,pady=5)
#modulus button
button_modulus = Button(root,text="%",width=2,command=modulus,borderwidth=3,relief=RIDGE)
button_modulus.grid(row=5,sticky="e",padx=125,pady=5)

root.mainloop()
