from tkinter import*

from tkinter.ttk import*

root = Tk()

progress = Progressbar(root,orient= HORIZONTAL,length = 400, mode = 'determinate')

def loading():
    import time
    progress['value']=0
    root.update_idletasks()
    time.sleep(0.5)
    label = Label(root,text="0")
    label.place(x=200,y=200)
    
    progress['value']=10
    root.update_idletasks()
    time.sleep(0.5)
    label = Label(root,text="10")
    label.place(x=200,y=200)
    
    
    progress["value"]=30
    root.update_idletasks()
    time.sleep(0.5)
    label = Label(root, text="30")
    label.place(x=200,y=200)
    
    progress["value"]=50
    root.update_idletasks()
    time.sleep(0.5)
    label = Label(root, text="50")
    label.place(x=200,y=200)
    
    progress["value"]=70
    root.update_idletasks()
    time.sleep(0.5)
    label = Label(root, text="70")
    label.place(x=200,y=200)
    
    progress["value"]=90
    root.update_idletasks()
    time.sleep(0.5)
    label = Label(root, text="90")
    label.place(x=200,y=200)
    
    progress["value"]=99
    root.update_idletasks()
    time.sleep(0.5)
    label = Label(root, text="99")
    label.place(x=200,y=200)
    
    progress["value"]=100
    root.update_idletasks()
    time.sleep(0.5)
    label = Label(root,text="100")
    label.place(x=200,y=200)
    

progress.place(x=100,y=100)
button = Button(root,text="LOADING...",
command=loading)
button.place(x=300,y=300)



root.mainloop()