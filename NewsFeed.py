from tkinter import *
from tkinter import messagebox

News = Tk()
News.title("NewsFeed")
News.geometry("700x790")


def Sport():
    sports = Tk()
    sports.title("Sport News")
    sports.geometry("700x790")
    Label(sports, text="Sport News", font='arial 30 bold ', bg="black", fg="white", width=500).pack()

    def volleyball():
        Label1 = Label(sports, text="VolleyBall ZU News", font="arial 13 bold", fg="white", bg="green", width=60)
        Label1.place(x=40, y=230)

        print("https://www.adisl.ae/mens-volleyball")

    def Basketball():
        Label1 = Label(sports, text="Basketball ZU News", font="arial 13 bold", fg="white", bg="green", width=60)
        Label1.place(x=40, y=230)

        print("https://www.adisl.ae/mens-basketball-first-division")

    def FootBall():
        Label1 = Label(sports, text="FootBall ZU News", font="arial 13 bold", fg="white", bg="green", width=60)
        Label1.place(x=40, y=230)

        print("https://www.adisl.ae/mens-football")

    bvolleyball = Button(sports, text="VolleyBall", font="arial 9 bold ", fg="black", bg="orange", width=20,
                         command=volleyball)
    bvolleyball.place(x=61, y=150)

    bBasketball = Button(sports, text="BasketBall", font="arial 9 bold ", fg="black", bg="orange", width=20,
                         command=Basketball)
    bBasketball.place(x=203, y=150)

    bfootball = Button(sports, text="FootBall", font="arial 9 bold ", fg="black", bg="orange", width=20,
                       command=FootBall)
    bfootball.place(x=345, y=150)


def news():
    print("https://www.khaleejtimes.com/uae")


def close():
    return News.destroy()


Button(News, text="Next", font="arial 15 bold", fg="white", bg="black", command=close).place(x=330, y=700)

Label(News, text="News", font="arial 30 bold", bg="Black", fg='white', width=500).pack()
Button(News, text="General News", font="arial 10 bold", fg="white", bg="orange", padx=2, command=news).place(x=70, y=70)
Button(News, text="Sport News", font="arial 10 bold", fg="white", bg="orange", padx=2, command=Sport).place(x=500, y=70)

News.mainloop()
