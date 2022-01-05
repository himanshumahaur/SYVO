#GUI libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

#supporting libraries for tkinter
from PIL import ImageTk, Image

#library for multithreading operation
from threading import *

#library for youtube handelings
from pytube import YouTube




#root window GUI design
root = Tk()
root.configure(bg='teal')
root.geometry('758x600')
root.minsize(758, 600)
root.maxsize(758, 600)

root.title('SYVO - DOWNLOADER')
root.iconbitmap("D:/.CODE/python/SYVO/icon.ico")

logoImage = ImageTk.PhotoImage(Image.open("D:/.CODE/python/SYVO/logo.png"))
logoLabel = Label(image=logoImage, bg='teal')
logoLabel.grid(row=1, column=1, padx=10, pady=0, columnspan=2)

frameLeft = LabelFrame(root, text='Stream', padx=50, pady=56, bg='teal', fg='white', font='Helvetica 9 bold')
frameLeft.grid(row=2, column=1, padx=10, pady=0)

frameRight = LabelFrame(root, text='Quality', padx=50, pady=50, bg='teal', fg='white', font='Helvetica 9 bold')
frameRight.grid(row=2, column=2, padx=0, pady=0)

frameRight1 = LabelFrame(root, text='Quality', padx=50, pady=50, bg='black', fg='white', font='Helvetica 9 bold')

framebutton = LabelFrame(root, bg='teal', borderwidth=0)
framebutton.grid(row=0, column=2, columnspan=1, padx=50)



#entery, GUI - URL
linkLabel = Label(frameLeft, text='Link', bg='teal', fg='#ffffff', font='Helvetica 9 bold')
linkLabel.grid(row=1, column=1, padx=5, pady=10)

urlEntry = Entry(frameLeft, width=50, borderwidth=0, highlightthickness=1)
urlEntry.grid(row=1, column=2, padx=10, pady=10)


#entery, GUI - path
savePath = StringVar()

pathLabel = Label(frameLeft, text='Path', bg='teal', fg='#ffffff', font='Helvetica 9 bold')
pathLabel.grid(row=2, column=1, padx=5, pady=10)

pathEntry = Entry(frameLeft, text=savePath, width=50, borderwidth=0, highlightthickness=1)
pathEntry.grid(row=2, column=2, padx=10, pady=10)


#stream quality function
quastm = IntVar()
quastm.set(22)
itag = 22

def func_quality(value):
    global itag
    itag = str(value)

    return 0

button720p = Radiobutton(frameRight, text='720p', variable=quastm, value=22, command=lambda: func_quality(quastm.get()), bg='teal', fg='black', font='Helvetica 9 bold').pack()
button360p = Radiobutton(frameRight, text='360p', variable=quastm, value=18, command=lambda: func_quality(quastm.get()), bg='teal', fg='black', font='Helvetica 9 bold').pack()
button1440p = Radiobutton(frameRight, text='144p', variable=quastm, value=17, command=lambda: func_quality(quastm.get()), bg='teal', fg='black', font='Helvetica 9 bold').pack()
buttonAudio = Radiobutton(frameRight, text='Audio', variable=quastm, value=251, command=lambda: func_quality(quastm.get()), bg='teal', fg='black', font='Helvetica 9 bold').pack()

button720p = Radiobutton(frameRight1, text='720p', variable=quastm, value=22, command=lambda: func_quality(quastm.get()), bg='black', fg='teal', font='Helvetica 9 bold').pack()
button360p = Radiobutton(frameRight1, text='360p', variable=quastm, value=18, command=lambda: func_quality(quastm.get()), bg='black', fg='teal', font='Helvetica 9 bold').pack()
button1440p = Radiobutton(frameRight1, text='144p', variable=quastm, value=17, command=lambda: func_quality(quastm.get()), bg='black', fg='teal', font='Helvetica 9 bold').pack()
buttonAudio = Radiobutton(frameRight1, text='Audio', variable=quastm, value=251, command=lambda: func_quality(quastm.get()), bg='black', fg='teal', font='Helvetica 9 bold').pack()


#browse directory function
def func_browse():
    global savePath
    PATH = filedialog.askdirectory()
    savePath.set(PATH)

    return 0
browseButton = Button(frameLeft, text='Browse', command=func_browse, bg='#73cbab', fg='black', font='Helvetica 9 bold')
browseButton.grid(row=2, column=3, padx=10, pady=10)


#progress register function
def func_progress(chunk, fh, bytes_remaining):
    global dProgress

    streamSize = stream.filesize
    dProgress = int(((streamSize - bytes_remaining) / streamSize) * 100)

    if(int(dProgress)>50):
        progresslabel.config(background="#06b025")
        
    progressbar['value']=dProgress
    gProgress = (str(dProgress)+"%")
    progresslabel.config(text=gProgress)


#completion register function
def func_complete(self, file_path):
    messagebox.showinfo('Status', 'Download Complete!')


#pytube download function >>[itag - from func_quality(), URL, dLocation]<<
def func_download():
    global stream

    progresslabel.config(background="white")

    messagebox.showinfo('Status', 'Downloading..')
    progressbar['value']=0
    progresslabel.config(text="0%")

    URL = urlEntry.get()
    dLocation = pathEntry.get()

    yt = YouTube(str(URL), on_progress_callback=func_progress, on_complete_callback=func_complete)
    stream = yt.streams.get_by_itag(int(itag))
    stream.download(str(dLocation))

    return 0


#to make the program multi-threaded 
def threading():
    # Call work function
    t1=Thread(target=func_download)
    t1.start()


#(LIGHT THEME) changing config of different widgets depending upon theme
def light_theme():
    color = 'teal'
    color2 = 'white'

    root.config(bg=color)
    logoLabel.config(bg=color)

    frameLeft.config(bg=color, fg=color2)

    linkLabel.config(bg=color, fg=color2)
    urlEntry.config(highlightbackground=color2)

    pathLabel.config(bg=color, fg=color2)
    pathEntry.config(highlightbackground=color2)

    downloadButton.config(bg='#73cbab', fg='black')
    browseButton.config(bg='#73cbab', fg='black')

    #removing frameright of darktheme
    frameRight1.grid_forget()
    #adding frameright of lighttheme
    frameRight.grid(row=2, column=2, padx=0, pady=0)

    Def_Btns.config(bg='teal')
    Def_Btnm.config(bg='teal')

    
#(DARK THEME) changing config of different widgets depending upon theme
def dark_theme():
    color = 'black'
    color2 = 'white'

    root.config(bg=color)
    logoLabel.config(bg=color)

    frameLeft.config(bg=color, fg=color2)

    linkLabel.config(bg=color, fg=color2)
    urlEntry.config(highlightbackground=color2)

    pathLabel.config(bg=color, fg=color2)
    pathEntry.config(highlightbackground=color2)

    downloadButton.config(bg='#73cbab', fg='black')
    browseButton.config(bg='#73cbab', fg='black')

    #removing frameright of lighttheme
    frameRight.grid_forget()
    #adding frameright of darktheme
    frameRight1.grid(row=2, column=2, padx=0, pady=0)

    Def_Btns.config(bg='black')
    Def_Btnm.config(bg='black')

    
#download status (GUI) (depends upon callback of pytube)
progressbar = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=550)
progressbar.grid(column=1, row=3, columnspan=4, padx=10, pady=0)


#download status (percentage)
progresslabel = ttk.Label(root, text="")
progresslabel.grid(column=1, row=3, columnspan=4, padx=10, pady=30)

#download button (calling threading func)
downloadButton = Button(root, text='Download', command=threading, bg='#73cbab', fg='black', font='Helvetica 13 bold', height=1, width=25)
downloadButton.grid(row=5, column=1, columnspan=2, pady=0)


#GUI elements for theme selection
lightimage = PhotoImage(file='D:/.CODE/python/SYVO/sun.png')
darkimage = PhotoImage(file='D:/.CODE/python/SYVO/moon.png')


#buttons for switching betweeen light and dark theme (calling respective functions) (theme selection)
Def_Btns = Button(framebutton, bg='teal', image=lightimage, command=light_theme, borderwidth=0)
Def_Btns.grid(row=0, column=0)

Def_Btnm = Button(framebutton, bg='teal',image=darkimage, command=dark_theme, borderwidth=0)
Def_Btnm.grid(row=0, column=1)

root.mainloop()