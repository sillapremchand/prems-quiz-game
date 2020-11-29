from tkinter import *

root = Tk()
label = Label(root, text="What is the answer of 99-47")
label.config(font =("Italic",22))

def click():
    label_2 = Label(root, text="Wrong")
    label_2.config(font =("Calibri",18))
    label_2.pack()

btn = Button(root, text="1000", width=5,height=2,bg = "Lime",fg = "black",command=click)
btn.config(font =("Italic",22))

def click_2():
    label_3 = Label(root, text="Wrong")
    label_3.config(font =("Calibri",18))
    label_3.pack()

btn_2 = Button(root, text="199", width=5,height=2,bg = "Lime",fg = "black",command=click_2)
btn_2.config(font =("Italic",22))

def click_3():
    label_4 = Label(root, text="Wrong")
    label_4.config(font =("Calibri",18))
    label_4.pack()
    
btn_3 = Button(root, text="50", width=5,height=2,bg = "Lime",fg = "black",command=click_3)
btn_3.config(font =("Italic",22))
 
def click_4():
    label_5 = Label(root, text="Correct")
    label_5.config(font =("Calibri",18))
    label_5.pack()
    
btn_4 = Button(root, text="52", width=5,height=2,bg = "Lime",fg = "black",command=click_4)
btn_4.config(font =("Italic",22))

def click_5():
    label_6 = Label(root, text="wrong")
    label_6.config(font =("Calibri",18))
    label_6.pack()
    
btn_5 = Button(root, text="2000", width=5,height=2,bg = "Lime",fg = "black",command=click_5)
btn_5.config(font =("Italic",22))

def click_6():
    label_7 = Label(root, text="Wrong")
    label_7.config(font =("Calibri",18))
    label_7.pack()
    
btn_6 = Button(root, text="33", width=5,height=2,bg = "lime",fg = "black",command=click_6) 
btn_6.config(font =("Italic",22))

label.pack()
btn.pack()
btn_2.pack()
btn_3.pack()
btn_4.pack()
btn_5.pack()
btn_6.pack()

root.mainloop()
