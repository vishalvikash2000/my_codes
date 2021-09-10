from tkinter import*
from tkinter import messagebox
import sys
import os
import re
import requests as r
import wget

root = Tk()
root.geometry("600x400")
root.configure(bg="blue")
root.title("tkinter projects india {FB VIDEO DOWNLOADER}")
root.resizable(0,0)


def download():
    #file where your video will be saved
    filedir = os.path.join('C:\\Users\\vishalvikash\\PycharmProjects\\pythonProject')

    # Download Low Resolution Video
    try:
        e1 = ent.get()
        html = r.get(e1)
        sdvideo_url = re.search('sd_src:"(.+?)"', html.text)[1]
    except r.ConnectionError as e:
        messagebox.showinfo("tkinter projects india","OOPS!! Connection Error.")
    except r.Timeout as e:
        messagebox.showinfo("tkinter projects india","OOPS!! Timeout Error")
    except r.RequestException as e:
        messagebox.showinfo("tkinter projects india","OOPS!! General Error or Invalid URL")
    except (KeyboardInterrupt, SystemExit):
        messagebox.showinfo("tkinter projects india","Ok ok, quitting" )
        sys.exit(1)
    except TypeError:
        messagebox.showinfo("tkinter projects india","Video May Private or Invalid URL")
    else:
        sd_url = sdvideo_url.replace('sd_src:"', '')
        messagebox.showinfo("tkinter projects india","Normal Quality: " + sd_url)
        messagebox.showinfo("tkinter projects india","[+] Video Started Downloading")
        wget.download(sd_url, filedir)
        # sys.stdout.write(ERASE_LINE)
        messagebox.showinfo("tkinter projects india","video downloaded")
        messagebox.showinfo("messages from tkinter projects india","this video will take you 2-3 minutes to download\n so please wait...")



title = Label(root,text="FACEBOOK \n DOWNLOADER\n \U0001F5F3",font="arial 56 bold",bg="blue",fg="white")
title.place(x=10,y=10)

ent = Entry(root,font="arial 18 bold",)
ent.place(x=10,y=300,width=580)

btn =  Button(root,text="DOWNLOAD NOW \U0001F5F3",font="arial 14 bold",fg="blue",bg="white",command=download)
btn.place(x=250,y=340)


root.mainloop()
