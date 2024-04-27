from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if userEntry.get()=="" or PassEntry.get()=="":
        messagebox.showerror("ERROR","Input cannot be empty!!")

    elif userEntry.get()=="Vineet" and PassEntry.get()=='1234':
        messagebox.showinfo("Success","Welcome to the Student managemnet")
        screen.destroy()
        import data

    elif userEntry.get()!="Vineet" or PassEntry.get()!='1234':
        messagebox.showwarning('Error','Invalid username/Password!')
    

#Creating object screen
screen = Tk()
screen.title("Welcome to Student management System")

screen.geometry("1620x900+0+0")

screen.resizable(False,False)

BgImage= ImageTk.PhotoImage(file='white.jpg')

bglabel= Label(screen,image=BgImage)

bglabel.place(x=-1,y=0)

#login image
loginf=Frame(screen)
loginf.place(x=600,y=250)

loginImg = PhotoImage(file="man1.png")
loginlabel = Label(loginf,image=loginImg, bg="grey94")
loginlabel.grid(row=0,column=0,columnspan=2,pady=10)

#username
userImg = PhotoImage(file="user.png")
userlabel = Label(loginf,image=userImg,text="UserName",compound=LEFT,font=('TIMES NEW ROMAN',20,'bold'),bg="grey94")
userlabel.grid(row=3, column=0, pady=10, padx=20)

userEntry = Entry(loginf ,font=('times new roman',20,'bold'),bd=5,fg="grey67")
userEntry.grid(row=3,column=1,pady=10, padx=20)

#password
PassImg = PhotoImage(file="padlock.png")
Passlabel = Label(loginf,image=PassImg,text="Password ",compound=LEFT,font=('TIMES NEW ROMAN',20,'bold'),bg="grey94")
Passlabel.grid(row=5, column=0, pady=10, padx=20)

PassEntry = Entry(loginf ,font=('times new roman',20,'bold'),bd=5,fg="grey67")
PassEntry.grid(row=5,column=1,pady=10, padx=20)

#submit button
loginb = Button(loginf, text="Log in", font=('TIMES NEW ROMAN',14,'bold'), width=15,bg='cornflowerblue',fg='white',cursor='hand2',command=login)
loginb.grid(row=7,column=0, columnspan= 4)

screen.mainloop() 