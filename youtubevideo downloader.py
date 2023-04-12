#corret program
# It is designed to download any video from the youtube to your system software without any interruption
from pytube import YouTube
from tkinter import *
# window making
root=Tk()
root.geometry("400x400")
root.title("Youtube video Downloader")
root.resizable()
Label(root,text="Paste your Video link down \nand get it download in seconds",font=("Footlight MT Light",18)).pack()
link=StringVar() # making link entering variable
# making function for downloading
def download():
    url=link.get()
    g=v.get()
    video = YouTube(url)
    stream = video.streams.filter(res=v).first()
    location = 'D:\SEM 1\PYCHARM\ideos from py program'
    stream.download(output_path=location)
    print("video downloaded")
    # messagebox.showinfo("Download Successfull")
# Initializing radiobuttons
q1=Radiobutton()
q2=Radiobutton()
q3=Radiobutton()
url=Entry(root,textvariable=link,font=("Sitka Subheading Semibold",15)).place(x=70,y=80)
v = StringVar(root, "1")

# Dictionary to create multiple buttons
values = {"720p": "720p",
          "480p": "480p",
          "360p": "360p",
          "144p": "144p"}

# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
w=110
e=120
for (text, value) in values.items():
    Radiobutton(root, text=text, variable=v,value=value, indicator=0,background="light blue").place(x=w,y=e)
    w=w+40
# exit function
def des():
    root.destroy()
# last button to download and exit
Button(root, text="Download", command=download,padx=10).place(x=100,y=160)
Button(root,text="Exit",command=des).place(x=240,y=160)
root.update()
root.mainloop()



