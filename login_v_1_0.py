from tkinter import *
import sys

def command1(event):
    if entry1.get() == 'admin' and entry2.get() == 'password' or entry1.get() == 'test' and entry2.get() == 'pass':
        root.deiconify()
        top.destroy()

def command2():
    top.destroy()
    root.destroy()
    sys.exit()


root = Tk()
top = Toplevel()

top.geometry('300x270')
top.title('LOGOWANIE')
top.configure(background = "white")

lbl1 = Label(top, text = 'Użytkownik:', font = {'Arial', 10})
entry1 = Entry(top)
lbl2 = Label(top, text = 'Hasło:', font = {'Arial', 10})
entry2 = Entry(top, show = '*')
button2 = Button(top, text = "Anuluj", command = lambda:command2())

entry2.bind('<Return>', command1)

lbl = Label(top, text = "Logowanie 2019")

lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
button2.pack()
lbl.pack()





root.title('Okno Główne')
root.configure(background = 'white')
root.geometry('855x650')

root.withdraw()
root.mainloop()