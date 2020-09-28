from pytube import *
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *
from threading import *

#total size container
file_size = 0

#to update percentage downloaded
def percentage(stream=None,chunk=None,remaining=None):
    #to get percentage of file downloaded
    file_downloaded=(file_size-remaining)
    percent=(file_downloaded/file_size)*100
    b.config(text="{:00.0f} % downloaded".format(percent))

def startdownload():
    global file_size
    try:
        url = urlField.get()
        # changing button text
        b.config(text='Please Wait...')
        b.config(state=DISABLED)
        path_to_save_video = askdirectory()
        if path_to_save_video is None:
            return

        # creating youtube object with url
        ob = YouTube(url,on_progress_callback=percentage)
        strm = ob.streams.first()
        file_size=strm.filesize

        # show title
        vtitle.config(text=strm.title)
        vtitle.pack(side=TOP)

        # to download the video
        strm.download(path_to_save_video)
        print("Video Downloaded")
        b.config(text='Downloaded')
        b.config(text='Start Download')
        b.config(state=NORMAL)
        showinfo("Download Finished", "Downloaded successfully")
        urlField.delete(0,END)
        vtitle.pack_forget()
    except Exception as e:
        print(e)
        print("Error!")
#creating new thread
def startdownloadThread():
    thread = Thread(target=startdownload)
    thread.start()

# building GUI
main = Tk()
# title
main.title("Youtube Downloader")
# set icon
main.iconbitmap('icon.ico')
# set size
main.geometry("500x600")
# content icon
file = PhotoImage(file='youtube.png')
headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP)
# url textfield
urlField = Entry(main, font=("verdana", 18), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10)

# download button
b = Button(main, text="Start Download", font=("verdana", 18), relief='ridge', command=startdownloadThread)
b.pack(side=TOP, pady=10)

#title of video
vtitle=Label(main,text="Video Title")

# make window visible
main.mainloop()