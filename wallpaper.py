from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
app = Tk()
app.title("Image")
app.config(background="white")
app.geometry("500x500")
app.iconbitmap("C:\\Users\\umair\\Downloads\\calculator_jNH_icon.ico")
image2 = Image.open("C:\\Users\\umair\\Downloads\\image.png")
image1 = ImageTk.PhotoImage(image2)
w = image1.width()
h = image1.height()
app.geometry('%dx%d+0+0' % (w, h))

label1 = Label(app, image=image1, justify=CENTER)
label1.pack()

app.mainloop()
