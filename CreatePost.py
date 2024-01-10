from fileinput import filename
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog

post = Tk()
post.title("Post")
post.geometry("700x700")


def open():
    global img
    global image
    post.filename = filedialog.askopenfilename(title="Select a file", filetypes=(
    ("png files", "*.png"), ("all files", "*.*"), ("jpg Files", "*.jpg")))
    image = Image.open(post.filename)
    pixels_x, pixels_y = 500, 500
    # size of the image
    img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y)))
    holder = Label(post, image=img)
    holder.image = img
    holder.place(x=10, y=50)


browse = Button(post, text="Browse", fg="black", command=open).pack()


def close():
    return post.destroy()


exit = Button(text="Close", fg="black", command=close)
exit.place(x=600, y=660)
post.mainloop()
