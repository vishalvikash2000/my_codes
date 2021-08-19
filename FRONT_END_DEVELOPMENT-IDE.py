#This code is not complete yet.
#final result will be released on December.

from tkinter import*
from tkinter.filedialog import asksaveasfilename
import os
import webbrowser
root = Tk()
root.title('WEBDEVELOPMENT IDE {TKINTER PROJECTS INDIA}')
root.geometry('900x650+100+0')
root.resizable(0,0)

def exit():
  root.destroy()

def save():
    #--------------------save as xyz.html file----------------------------------------
    IDE = txt.get('0.1','end-1c')
    files = asksaveasfilename(title='save',filetypes=[('html files','*.html')])
    with open(files,'w') as data:
        data.write(IDE)
    #-----------------------------------------------------------------------------
    
    #------------------os.path.join will show you the files path which you've saved.for example:- c://file//user//xyz.html------------------
        x = os.path.join(files) 
    #-----------------------------------------------------------------------------
    
    #-------------------------#stored file path in filenames variable----------------------------------------
        filenames = str(x) 
    #-----------------------------------------------------------------------------
     
    #-------------------------#opened xyz.html file in webbrowser----------------------------------------
        webbrowser.open_new_tab(filenames)
    #-----------------------------------------------------------------------------
     

scroll = Scrollbar(root)
scroll.pack(side= RIGHT ,fill = Y)

Label(root,text="FRONT-END-DEVELOPER",font="arial 37 bold").place(x=0,y=10)
webdv = Label(root,text="HTML . CSS . JS . JQUERY . BOOTSTRAP",font="arial 12 bold")
webdv.place(x=300,y=70)

txt = Text(root,font='arial 18 bold',yscrollcommand = scroll.set)
txt.place(x=0,y=90,width=880,height=650)
scroll.config(command=txt.yview)

my_menu = Menu(root)
root.config(menu=my_menu,)
file_menu= Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...",command=save)
file_menu.add_command(label="Exit",command=exit)


root.mainloop()
