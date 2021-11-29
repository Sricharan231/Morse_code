from tkinter import *
import tkinter
from PIL import Image, ImageTk
ms = Tk()
bg = PhotoImage(file = "i2.png")
label = Label( ms, image = bg)
label.place(x = 0,y = 0)
ms.geometry("900x500")
ms.iconbitmap('logo.ico')
ms.title('Instructions')
img = PhotoImage(file="instructions.png")

Label(ms, image=img).place(x=50, y=70)
img1 = PhotoImage(file="ab.png")
Label(ms, image=img1).place(x=650, y=1)

if __name__ == "__main__":
    tkinter.Label(ms, text='Instructions',
                              font=("Times New Roman Bold Italic", 22),
                              fg='black', bg="red").place(relx=0.63, rely=0.1)

    label1 = tkinter.Label(ms, text='* Just type letters, numbers and punctuation into the left box (From Language).', font=("Times New Roman", 18))
    label1.place(relx=0.48, rely=0.20)
    label2 = tkinter.Label(ms, text='* Click on Lang code to select the entered language as English.', font=("Times New Roman", 18))
    label2.place(relx=0.48, rely=0.30)
    label3 = tkinter.Label(ms, text='* Click on Lang code to select the converting language to morse.',
                           font=("Times New Roman", 18))
    label3.place(relx=0.48, rely=0.40)
    label4 = tkinter.Label(ms, text='* Click on convert button to convert english to morse code.',
                           font=("Times New Roman", 18))
    label4.place(relx=0.48, rely=0.50)
    label5 = tkinter.Label(ms, text='* Click on Play sound button to play the sound.',
                           font=("Times New Roman", 18))
    label5.place(relx=0.48, rely=0.60)
    label6 = tkinter.Label(ms, text='* After the conversion is completed click on clear button \nto clear the entered details.',
                           font=("Times New Roman", 18))
    label6.place(relx=0.48, rely=0.70)

    # T = Text(ms, height=5, width=40, font=("Times New Roman", 18))
    # Fact = """Just type letters, numbers and punctuation into \nthe left box (From Language) and the Morse code will appear in the right box (Converted Language) with a "#" if the character cannot be translated. This is not a great tool for learning Morse code as looking at the dots and dashes does not help."""
    # T.pack()
    # T.insert(tkinter.END, Fact)
    # T.place(relx=0.55, rely=0.20)
ms.mainloop()