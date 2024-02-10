import random
import tkinter as tk
from tkinter import messagebox

pg=tk.Tk()
pg.title("Password Generator")
pg.geometry('250x200')
pg.resizable(0,0)

def process():
    length=int(inp.get())

    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special = ['@', '#', '$', '%', '&', '*']

    total=lower+upper+num+special
    ran=random.sample(total,length)
    psw="".join(ran)
    tk.messagebox.showinfo('Result','Your Password {} \n\nPassword copied to clipboard'.format(psw))
    



inp=tk.StringVar()
lab=tk.Label(text="Password Length").pack(pady=10)
txt=tk.Entry(textvariable=inp).pack()
btn=tk.Button(text="Generator",command=process).pack(pady=10)


pg.mainloop()