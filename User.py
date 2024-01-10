from Login import *
from NewsFeed import *
from CreatePost import *
from FollowUser import *
from Ads import *
from tkinter import *
from tkinter import messagebox


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __str__(self):
        return self.name + "-" + self.password


class IndividualUser(User):
    def __init__(self, name, password):
        User.__init__(self, name, password)
        self.followers = []


def setUsers():
    handel = open("Register.txt", 'a')
    u1 = IndividualUser("Khalifa", "1234\n")
    u2 = IndividualUser("Abdulaziz", "3215\n")
    list = [u1.__str__(), u2.__str__()]
    handel.writelines(list)
    handel.close()


def getUsers():
    handel = open("Register.txt", 'a')
    lst = (handel.readlines())
    users = []
    for l in lst:
        line = l.split("-")
        name = line[0]
        password = line[1]
        i = IndividualUser(name, password)
        print(i)
        users.append(i)
    handel.close()


getUsers()


class Business(User):
    '''class to represent Business user'''

    def __init__(self, name, password):
        User.__init__(self, name, password)
        self.link = ""
        self.ads = ""

    def setUser(self):
        handel = open("Report.txt", 'a')
        u1 = Business("Khalifa", "1234\n")
        u2 = Business("Abdulaziz", "3215\n")
        list = [u1.__str__(), u2.__str__()]
        handel.writelines(list)
        handel.close()

    def getUser(self):
        handel = open("Register.txt", 'a')
        list = (handel.readlines())
        users = []
        for l in list:
            line = l.split("-")
            name = line[0]
            password = line[1]
            i = Business(name, password)
            print(i)
            users.append(i)
        handel.close()

    getUser()


# creating the GUI
window = Tk()
# this is the title for the GUI
window.title("Social App")
# this is the geometry of the GUI
window.geometry("700x400+10+20")


# this is a class that represent an system administrator
class SystemAdministrator:
    '''class to represent an System Administrator'''

    # constructor
    def __init__(self):
        self.monitor = ""

    def setmonitor(self, mon=""):
        self.monitor = mon

    def getmonitor(self):
        return self.monitor


class SocialNetworkApp:
    '''class to represent a Social Network App'''

    # Constructor
    def __init__(self):
        self.name = ""

    def setname(self, name=""):
        self.name = name

    def getname(self):
        return self.name

    def Admin(self, monitor):
        admins = SystemAdministrator()
        admins.__setattr__("monitor", monitor)

    def __str__(self):
        return "Name: {}".format(
            self.getname()
        )


class SystemUser(SystemAdministrator):

    '''class to represent a system user'''

    # constructor

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        SystemAdministrator.__init__(self)
        self.username = ""
        self.password = ""
        self.rName = ""
        self.bio = ""
        self.location = ""
        self.dob = ""

        self.realName = Label(text="Real Name: ", fg="Black", font="bold")
        self.realNameBox = Entry()
        self.realName.place(x=60, y=50)
        self.realNameBox.place(x=180, y=50)

        self.bio1 = Label(text="Bio: ", fg="black", font="bold")
        self.bioBox1 = Entry()
        self.bio1.place(x=60, y=80)
        self.bioBox1.place(x=180, y=80)

        self.location1 = Label(text="Location: ", fg='black', font="bold")
        self.location1Box = Entry()
        self.location1.place(x=60, y=110)
        self.location1Box.place(x=180, y=110)

        self.dob1 = Label(text="Date Of Birth: ", fg='black', font="bold")
        self.dob1Box = Entry()
        self.dob1.place(x=60, y=140)
        self.dob1Box.place(x=180, y=140)

        self.print = Button(text="Save", fg='black', bg="white", command=self.save)
        self.print.place(x=120, y=350)

    # this is the function to save the input from the user
    def save(self):
        try:
            # here is to check if the entry box is full or not
            if self.realNameBox.get() == "" or self.bioBox1.get() == "" or self.location1Box.get() == "" or self.dob1Box.get() == "":
                # this is for the pop-up error message box
                messagebox.showinfo(title="Error", message="You need to Fill the blank ")

        except:
            pass
        # this is to create the file  and to appaend into the file.
        line = self.realNameBox.get() + " : " + self.bioBox1.get() + " : " + self.location1Box.get() + " : " + self.dob1Box.get()
        manager = open("Report.txt", 'a')
        manager.write(str(line) + '\n')
        manager.close()

        self.realNameBox.delete(0, END)
        self.bioBox1.delete(0, END)
        self.location1Box.delete(0, END)
        self.dob1Box.delete(0, END)
        return window.destroy()


user = SystemUser(window)
window.mainloop()
