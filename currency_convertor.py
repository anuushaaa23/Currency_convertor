from tkinter import *

#creating an instance of tkinter
window = Tk()

#function to convert rupees to dollars pounds euro yen
def from_rupees():
    american_dollar = float(e2_value.get())*0.0125  #in american dollars
    british_pound = float(e2_value.get())*0.0104    #in british pounds
    euro = float(e2_value.get())*0.0122             #in euros
    yen = float(e2_value.get())*1.7                 #in yen
    
    #inserting converted values to variables t1 t2 t3 t4
    t1.insert(END, american_dollar)
    t2.insert(END, british_pound)
    t3.insert(END, euro)
    t4.insert(END, yen)

#shows the instruction
e1 = Label(window, text="Input the amount in rupees")
e1.grid(row=0, column=0)

#to enter the value in rupees
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=0, column=1)

space = Label(window, text="")
space.grid(row=1)

e3 = Label(window, text="American dollars")
e3.grid(row=2, column=0)

e4 = Label(window, text="British pounds")
e4.grid(row=2, column=1)

e5 = Label(window, text="euro")
e5.grid(row=2, column=2)

e6 = Label(window, text="Yen")
e6.grid(row=2, column=3)

#displays amount in dollars
t1 = Text(window, height=5, width=30)
t1.grid(row=3, column=0)

#displays amount in pounds
t2 = Text(window, height=5, width=30)
t2.grid(row=3, column=1)

#displays amount in euros
t3 = Text(window, height=5, width=30)
t3.grid(row=3, column=2)

#displays amount in yen
t4 = Text(window, height=5, width=30)
t4.grid(row=3, column=3)

b1 = Button(window, text="Convert", command=from_rupees) #button with command to convert and display
b1.grid(row=0, column=2)

window.mainloop()