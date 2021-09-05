from tkinter import*
import webbrowser

root = Tk()
root.geometry("500x500+300+0")
root.resizable(0,0)
root.title("SFLIX.TO MOVIE WEBSITE")


lbl = Label(root,text="WATCH FREE",font="arial 45 bold",fg="red")
lbl.place(x=40,y=0)
lbl = Label(root,text="HD MOVIES",font="arial 46 bold",fg="red")
lbl.place(x=150,y=90)
emoji = """\U0001F3A5 \t \U0001F4FD \t \U0001F39E \t \U0001F3AC \t \U0001F4FA"""
emoji2 = """\U0001F4FD \t \U0001F39E \t \U0001F3A5 \t \U0001F4FA \t \U0001F3AC"""
icon = Label(root,fg="red",text=emoji,font="arial 17 bold")
icon.place(x=10,y=180)
icon2 = Label(root,fg="red",text=emoji2,font="arial 17 bold")
icon2.place(x=50,y=280)

def clr():
    entry.delete(0,END)

def movie():
    en = entry.get()
    webbrowser.open(f"https://sflix.to/search/{en}")


entry = Entry(root,font="arial 18 bold",)
entry.place(x=30,y=380,width=450)

btn = Button(root,text="x",bg="white",fg="red",font="aral 11 bold",bd=0,command=clr)
btn.place(x=450,y=383)

search = Button(root,text="SEARCH MOVIE",bg="white",fg="red",font="aral 18 bold",bd=0,command=movie)
search.place(x=150,y=420)
root.mainloop()


