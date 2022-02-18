from tkinter import*
from translate import Translator
def convert():
  translator = Translator(to_lang = "hindi")
  text = entry.get()
  translation = translator.translate(text)
  lbl = Label(root,text=translation, font=("arial 30 bold"))
  lbl.place(x = 150, y =350)

root = Tk()
root.title("tkinter – projects")
root.geometry("1200x600")
root.resizable(0,0)
entry = Entry(root, font =("arial 28 bold"))
entry.place(x=100, y=70,width=1300)
btn = Button(root, text = "TRANSLATE NOW",command = convert)
btn.place(x=600, y=200)
root.mainloop()