from cgitb import text 
from textwrap import wrap
from tkinter import*
from tkinter import ttk
from turtle import bgcolor
from googletrans import Translator, LANGUAGES
from numpy import RAISE


def change(text="type", src="English", dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text


def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0, END)
    textget = change(text=msg, src=s , dest=d)
    Dest_txt.delete(1.0, END)
    Dest_txt.insert(END,textget)


root = Tk()
root.title("Translator")
root.geometry("400x600")
root.config(bg='grey')

lab_txt = Label(root, text="Translater", font=(
    "Comic Sans MS", 20, "bold"), bg="grey")  
lab_txt.place(x=50, y=5, height=50, width=300)  

Frame = Frame(root).pack(side=BOTTOM)


lab_txt = Label(root, text="Input Text:", font=(
    "Comic Sans MS", 10, "bold"), bg="grey") 
lab_txt.place(x=25, y=45, height=20, width=80)

Sor_txt = Text(Frame, font=("Comic Sans MS", 20), wrap=WORD)  
Sor_txt.place(x=25, y=70, height=100, width=350)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(Frame, values=list_text)
comb_sor.place(x=25, y=180, height=25, width=100)
comb_sor.set("english")

PhotoImage= PhotoImage(file= "tt.png")

Button_change = Button(Frame,image=PhotoImage, bg="grey",
                         relief=RAISED, command=data) 
Button_change.place(x=160, y=180, height=25, width=90)


comb_dest = ttk.Combobox(Frame, values=list_text)
comb_dest.place(x=280, y=180, height=25, width=100)  
comb_dest.set("english")

lab_txt = Label(root, text="Output Text:", font=(
    "Comic Sans MS", 10, "bold"), bg="grey")  
lab_txt.place(x=25, y=250, height=20, width=90)

Dest_txt = Text(Frame, font=("Comic Sans MS", 20),
                )  
Dest_txt.place(x=25, y=280, height=100, width=350)

root.mainloop()
