import tkinter
from tkinter import *
from tkinter import messagebox
from playsound import playsound
import about
from about import *
morse = Tk()

bg = PhotoImage(file = "bg image.png")

morse.title("Translator")
morse.iconbitmap('logo.ico')

menu = Menu(morse)
morse.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=morse.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=open("about.py"))
label1 = Label(morse, image=bg)
label1.place(x=0, y=0)
variable1 = StringVar(morse)
variable2 = StringVar(morse)
variable1.set("lang-code")
variable2.set("lang-code")

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                   'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-',
                   'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
                   '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                   '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', '\n': '|'}



def clearAll():
    language1_field.delete(1.0, END)
    language2_field.delete(1.0, END)
    # if language1_field.delete() == language2_field.delete():
    #     messagebox.showinfo("CLEARED!", "Successfully Cleared😑.")
    #     return

def convert():
    message = language1_field.get("1.0", "end")[:-1]
    if variable1.get() == variable2.get():
        messagebox.showerror("ERROR!", "Can't Be same Language😑.")
        return

    elif variable1.get() == "Eng" and variable2.get() == "Morse":
        rslt = encrypt(message)

    elif variable1.get() == "Morse" and variable2.get() == "Eng":
        rslt = decrypt(message)

    else:
        messagebox.showwarning("ERROR😑", "please choose valid language😒")
        return

    language2_field.insert('end -1 chars', rslt)

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
    return cipher
def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i+= 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[
                    list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''

    return decipher

def play():
    global playsound
    playsound('cw10.wav')

if __name__ == "__main__":
    morse.geometry("900x500")
    headlabel = tkinter.Label(morse, text='😀WELCOME TO MORSE CODE TRANSLATOR😄', font=("Times New Roman Bold Italic", 22),
                      fg='black', bg="red")
    headlabel.place(relx=0.3,rely=0.05)
    label1 = tkinter.Label(morse, text="Enter Language", font=("Times New Roman Bold Italic", 14),fg='Black', bg='yellow')
    label1.place(relx=0.10,rely=0.25)
    label2 =tkinter.Label(morse, text="From Language",font=("Times New Roman Bold Italic", 14),
                   fg='blue', bg='pink')
    label2.place(relx=0.40,rely=0.35)
    label3 = tkinter.Label(morse, text="To Language ",font=("Times New Roman Bold Italic", 14),
                   fg='black', bg='orange')
    label3.place(relx=0.40, rely=0.50)
    label4 = tkinter.Label(morse, text="Converted Language ",font=("Times New Roman Bold Italic", 14),
                   fg='black', bg='yellow')
    label4.place(relx=0.71,rely=0.25)
    language1_field = Text(morse, height=10, width=35,
                           font="lucida 16")
    language1_field.place(relx=0.04,rely=0.35)
    language2_field = Text(morse, height=10, width=35,
                           font="lucida 16")
    language2_field.place(relx=0.65, rely=0.35)

    languageCode_list = ["Eng", "Morse"]
    FromLanguage_option = OptionMenu(morse, variable1, *languageCode_list )
    FromLanguage_option.place(relx=0.5,rely=0.40)
    FromLanguage_option.config(bg="lightgrey", fg="black")
    ToLanguage_option = OptionMenu(morse, variable2, *languageCode_list)
    ToLanguage_option.place(relx=0.5, rely=0.55)
    ToLanguage_option.config(bg="lightgrey", fg="black")

    button1 = Button(morse, text="Convert🔄", font=("Times New Roman Bold Italic", 20), bg="lightblue", fg="black",
                     command=convert)
    button1.place(relx=0.40,rely=0.75)

    button2 = Button(morse, text="Clear😑", font=("Times New Roman Bold Italic", 20),bg="palegreen",
                     fg="black", command=clearAll)
    button2.place(relx=0.25, rely=0.75)

    play_button = Button(morse, text="▶Play Sound", font=("Times New Roman Bold", 20),bg="green",fg="lightblue",command=play)
    play_button.place(relx=0.56,rely=0.75)

    morse.mainloop()