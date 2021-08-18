from tkinter import*
from tkinter.filedialog import asksaveasfilename
import os
import webbrowser
root = Tk()
root.geometry('900x650+100+0')
root.resizable(0,0)

def exit():
  root.destroy()

def save():
    IDE = txt.get('0.1','end-1c')
    files = asksaveasfilename(title='save',filetypes=[('html files','*.html')])
    with open(files,'w') as data:
        data.write(IDE)
        x = os.path.join(files)
        filenames = str(x)
        webbrowser.open_new_tab(filenames)

scroll = Scrollbar(root)
scroll.pack(side= RIGHT ,fill = Y)

Label(root,text="FRONT-END-DEVELOPER",font="arial 37 bold").place(x=0,y=10)
webdv = Label(root,text="HTML . CSS . JS . JQUERY . BOOTSTRAP",font="arial 12 bold")
webdv.place(x=300,y=70)

txt = Text(root,font='arial 18 bold',yscrollcommand = scroll.set)
txt.place(x=0,y=90,width=880,height=1300)
scroll.config(command=txt.yview)

my_menu = Menu(root)
root.config(menu=my_menu,)
file_menu= Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...",command=save)
file_menu.add_command(label="Exit",command=exit)


root.mainloop()
