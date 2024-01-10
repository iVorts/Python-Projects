from part import *

followuser = Tk()
followuser.title("Following")
followuser.geometry("500x600")
followuser.resizable(0, 0)

user = Label(followuser, text="Khalifa Albusaeedi", fg="black", font="arial 12 bold")
user.place(x=10, y=70)
user = Label(followuser, text="Abdulaziz Buhaji", fg="black", font="arial 12 bold")
user.place(x=10, y=130)
def click():
    handel = open("Report.txt", 'a')
    handel.readlines()
    handel.close()
    return followuser.destroy()


following = Button(followuser, text="Follow", fg="Black", command=click)
following.place(x=200, y=70)

following = Button(followuser, text="Follow", fg="Black", command=click)
following.place(x=200, y=130)
followuser.mainloop()
