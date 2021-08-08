from selenium import webdriver
import webbrowser
from tkinter import*


root = Tk()
root.geometry("650x500")
root.configure(bg='white')
root.resizable(0,0)


def modules():
    driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\chromedriver.exe')
    e1 = entry.get()
    driver.get(f'https://pypi.org/project/{e1}/')
    x = driver.find_element_by_id("pip-command")
    pypi_result = x.text
    lblname = Label(root, text=pypi_result, font="arial 18 bold", bg='white', fg='DodgerBlue2')
    lblname.place(x=50, y=350)
    driver.close()

entry = Entry(root,font="arial 18 bold")
entry.place(x=50,y=250,width=550)

button = Button(root,text='\U0001F50E',font="arial 14 bold",bg='white',fg='DodgerBlue2',command=modules)
button.place(x=560,y=250)

intro = Label(root,text="PYPI\n(PYTHON PACKAGE INDEX)",font="arial 30 bold",bg='DodgerBlue2',fg='white')
intro.place(x=0,y=0,width=700)
lblname  = Label(root,text="Enter Module Name:-",font="arial 18 bold",bg='white',fg='DodgerBlue2')
lblname.place(x=50,y=200)

root.mainloop()

