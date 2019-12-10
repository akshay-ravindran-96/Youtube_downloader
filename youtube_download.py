from __future__ import unicode_literals
import tkinter as tk


import youtube_dl
import sys

def show_entry_fields():
    
    link=e1.get()
    print("link")
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    	ydl.download([link])

    e1.delete(0, tk.END)
    print("Download Completed")

    

master = tk.Tk()
master.title('Downloader')
tk.Label(master, text="ENTER YOUTUBE URL").grid(row=0)


e1 = tk.Entry(master)
e1.insert(10, "Youtube URL")

e1.grid(row=0, column=1)


tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, text='DOWNLOAD', command=show_entry_fields).grid(row=3, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=4)

master.mainloop()

tk.mainloop()
