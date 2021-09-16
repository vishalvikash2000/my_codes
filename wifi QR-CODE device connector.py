from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.filedialog import  asksaveasfilename,askopenfilename
import wifi_qrcode_generator
from wifi_qrcode_generator import*

root = Tk()
root.geometry("1300x650+0+0")
root.configure(bg="grey")
root.title("WIFI QR-CODE GENERATOR {TKINTER PROJECTS INDIA}")


#SAVE YOUR WIFI NAME AND PASSWORD IN QR CODE
def qr():
    entry = ent.get()
    password = pswd.get()
    wifi = wifi_qrcode_generator.wifi_qrcode(entry,False,'WPA',password)
    files = [('All Files','*.*'),('Image Files','*png'),('Image Files','*jpg')]
    file = asksaveasfilename(filetypes = files,defaultextension= files)
    wifi.save(file)

# SHOW QR CODE IMAGE IN TKINTER "TOPLEVEL FRAME (pil module used)"
def showmyqr():
    messagebox.showinfo('message from tkinter projects india',"how to connect your wifi through qr code \n\n"
                                                              "1) open your wifi option  in mobile \n "
                                                              "2) open qrcode option \n "
                                                              "3) scan your qr code and connect your network with mobile device \n boom Done \U0001F604")
    open = askopenfilename(filetypes=[("Image File",'.png')])
    image = Image.open(open)
    imgshow = ImageTk.PhotoImage(image)
    frame = Toplevel()
    frame.geometry("410x410")
    frame.title("WIFI QR-CODE GENERATOR {TKINTER PROJECTS INDIA}")
    myvar = Label(frame, image=imgshow)
    myvar.image = imgshow
    myvar.pack()


wifititle = Label(root,text="SCAN-WIFI-CONNECTOR",font="arial 37 bold",bg="grey")
wifititle.place(x=0,y=10)

wifiname = Label(root,text="SSD (NETWORK NAME)",font="arial 17 bold",bg="grey")
wifiname.place(x=50,y=140)

wifipass= Label(root,text="PASSWORD (NETWORK PASSWORD)",font="arial 17 bold",bg="grey")
wifipass.place(x=50,y=270)

ent = Entry(root,font="arial 20 bold",)
ent.place(x=50,y=180,width="500")

pswd = Entry(root,font="arial 20 bold",)
pswd.place(x=50,y=310,width="500")

btn = Button(root,text="GENERATE QR-CODE",font="arial 17 bold",bg="grey",command=qr)
btn.place(x=50,y=450,width="500")

btn_show = Button(root,text="CLICK HERE TO  \n SHOW QR-CODE",font="arial 37 bold",bg="grey",command=showmyqr)
btn_show.place(x=700,y=10,width=600,height=635)
root.mainloop()
