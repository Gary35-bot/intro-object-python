from tkinter import *

root = Tk()
root.title("Class in Tkinter")
root.geometry("500x500")


class Circle:
    myresult = StringVar()
    import math

    def __init__(self, master):
        self.lab1 = Label(master, text="please enter radius")
        self.lab1.place(x=5, y=5)
        self.myentry = Entry(master)
        self.myentry.place(x=150, y=5)
        self.lab2 = Label(master, text="", width="50", textvariable=self.myresult)
        self.lab2.place(x=20, y=50)
        self.btn_area = Button(master, text="Calculate Area", command=self.area_of_circle)
        self.btn_area.place(x=100, y=100)

    def area_of_circle(self):
        result = self.math.pi * int(self.myentry.get()) * int(self.myentry.get())
        self.myresult.set(result)

x =Circle(root)

class Rectangle:
    my_result = StringVar()

    def __init__(self, master):
        self.lab1 = Label(master, text="Please enter size")
        self.lab1.place(x=10, y=10)





root.mainloop()
