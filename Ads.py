from tkinter import *
from tkinter import messagebox

ads = Tk()
ads.title("Advertisement")
ads.geometry("200x300")


class Plan:
    '''class to represent a plan'''

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.name = Label(text="Plans", width=14, font="arial 10 bold").pack()

        self.basic = Button(master, text="Basic", fg="Black", width=8, font="arial 10 bold", command=self.basic)
        self.basic.place(x=65, y=100)

        self.silver = Button(master, text="Silver", fg="black", width=8, font="arial 10 bold", command=self.silver)
        self.silver.place(x=65, y=150)

        self.gold = Button(master, text="Gold", fg="Yellow", bg="black", width=8, font="arial 10 bold",
                           command=self.gold)
        self.gold.place(x=65, y=200)

    def basic(self):
        self.b = Tk()
        self.b.geometry("400x400")
        self.b.title("Basic Plan ")
        Label(self.b, text="The Basic plan for advertisement", font="arial 13 bold ", fg="Black").pack()
        Label(self.b, text="This advertisement's benefit:  ", font="arial 10 bold").place(x=50, y=89)
        Label(self.b, text="This plan cost of 10 AED and it will be sent to 5 Users only", fg="black",
              font="arial 10 bold").place(x=50, y=110)

        def buy():
            messagebox.showinfo("Done", "Your purchase is successful")
            self.b.destroy()

        Button(self.b, text="Buy", fg="black", command=buy).place(x=350, y=350)
        self.b.mainloop()

    def silver(self):
        self.s = Tk()
        self.s.geometry("400x400")
        self.s.title("Silver Plan ")
        Label(self.s, text="The Basic plan for advertisement", font="arial 13 bold ", fg="Black").pack()
        Label(self.s, text="This advertisement's benefit:  ", font="arial 10 bold").place(x=50, y=89)
        Label(self.s, text="This plan cost of 30 AED and it will be sent to 10 Users only", fg="black",
              font="arial 10 bold").place(x=50, y=110)

        def buy():
            messagebox.showinfo("Done", "Your purchase is successful")
            self.s.destroy()

        Button(self.s, text="Buy", fg="black", command=buy).place(x=350, y=350)

        self.s.mainloop()

    def gold(self):
        self.g = Tk()
        self.g.geometry("400x400")
        self.g.title("Gold Plan ")
        Label(self.g, text="The Basic plan for advertisement", font="arial 13 bold ", fg="Black").pack()
        Label(self.g, text="This advertisement's benefit:  ", font="arial 10 bold").place(x=50, y=89)
        Label(self.g, text="This plan cost of 30 AED and it will be sent to 10 Users only", fg="black",
              font="arial 10 bold").place(x=50, y=110)

        def buy():
            messagebox.showinfo("Done", "Your purchase is successful")
            self.g.destroy()

        Button(self.g, text="Buy", fg="black", command=buy).place(x=350, y=350)

        self.g.mainloop()


p = Plan(ads)

ads.mainloop()
