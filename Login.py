from tkinter import messagebox
from tkinter import *

login = Tk()
login.title("Login")
login.geometry("400x400")
login.resizable(0, 0)


class Login():
    def __init__(self, login):
        frame = Frame(login)
        frame.pack()

        # Here we are designing the GUI, with labels, entry boxes, fonts and buttons
        self.username1 = Label(login, text="Username: ", fg="black", font="bold")
        self.username1Box = Entry(login)
        self.username1.place(x=60, y=50)
        self.username1Box.place(x=180, y=50)

        self.password1 = Label(login, text="Password: ", fg='black', font="bold")
        # the show is to censored the password
        self.password1Box = Entry(login, show='*')
        self.password1.place(x=60, y=80)
        self.password1Box.place(x=180, y=80)

        # this is the function to save the input from the user
        self.print = Button(login, text="Login", fg='black', bg="white", command=self.save)
        self.print.place(x=120, y=350)

    def save(self):
        try:
            # here is to check if the entry box is full or not
            if self.username1Box.get() == "" or self.password1Box.get() == "":
                messagebox.showinfo(title="Error", message="You need to Fill the blank ")
            elif self.Authentication():
                pass
            else:
                messagebox.showwarning("Incorrect UserName/Password please Try Again")
        except:
            pass

        # this is to create the file  and to appaend into the file.
        line = self.username1Box.get() + " : " + self.password1Box.get()
        manager = open("Report.txt", 'a')
        manager.write(str(line) + '\n')
        manager.close()

        self.username1Box.delete(0, END)
        self.password1Box.delete(0, END)
        login.destroy()

    def Authentication(self):
        self.username1 = self.username1Box.get()
        self.password1 = self.password1Box.get()
        handel = open("Report.txt", 'r')
        list = handel.readlines()
        for line in list:
            value = line.split("-")
            u = value[0]
            p = value[1]
            if u == self.username1:
                return True
            return False


l = Login(login)
login.mainloop()
