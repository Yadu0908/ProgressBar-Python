from tkinter import StringVar, Tk,ttk
from tkinter.ttk import *
import time

def download_function():
    task= 100
    x= 0
    speed= 1

    while(x<=task):                                 # loop will be works till x is not equals to task var...
        time.sleep(0.06)
        pb['value']+=(speed/task)*100               # this will increase the progressbar by 10 unit...
       
        percent.set(str(int((x/task)*100))+"%")   # This will set the value of percent into the lable...
        
        tasks.set(str(x)+" /"+ str(task)+" files downloded.") #This will prompt the compleated out of total task...
        x+=1
        
        root.update_idletasks()                     # This will update the display of windows after each second...


root= Tk()
root.geometry("500x250")

percent= StringVar()
tasks= StringVar()

s = ttk.Style()
s.theme_use('alt')
s.configure("Horizontal.TProgressbar", troughcolor ='white', background='#007ccc', thickness= 25)


percentLabel= Label(root, text="Progress Bar with Tkinter and Python", font=("Comic Sans MS",18)).pack(pady=30)

pb= Progressbar(root, orient="horizontal", style="yellow.Horizontal.TProgressbar", length=300)    
pb.pack(pady=10)

percentLabel= Label(root, textvariable=percent, font=("Comic Sans MS",12)).pack()
percentLabel= Label(root, textvariable=tasks, font=("Comic Sans MS",12)).pack()

button= Button(root, text="Download", command=download_function).pack(pady=10) 

root.mainloop()