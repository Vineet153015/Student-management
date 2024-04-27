from tkinter import*
from PIL import ImageTk
import time
import ttkthemes
from tkinter import ttk, messagebox, filedialog
import pymysql
import pandas



def iexit():
    result = messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        data.destroy()
    
    else:
        pass


def export_data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = table.get_children()
    newlist=[]
    for index in indexing:
        content = table.item(index)
        datalist =content['values']
        newlist.append(datalist)

    table1 = pandas.DataFrame(newlist, columns=['ID','Name', 'Mobile','Email','Address','Gender','DOB','Date','Time'])
    table1.to_csv(url, index=False)
    messagebox.showinfo('Success',"Data Saved Successfully")




def update_student():

    def update_data():
        query = 'update student set name=%s, mobile=%s, email=%s, address =%s , gender =%s ,dob=%s, date=%s, time=%s where id=%s'
        mouse.execute(query,(nameEntry.get(), mobEntry.get(), emailEntry.get(),addEntry.get(), genderEntry.get(), dobEntry.get(), date, ctime, idEntry.get()))
        main.commit()
        messagebox.showinfo("Success", f"Id {idEntry.get()} is modified successfully", parent = update_window)
        update_window.destroy()
        show_student()




    update_window = Toplevel()
    update_window.title('Update Student')
    update_window.grab_set()
    update_window.resizable(False,False)

    # ID
    idl = Label(update_window,text='ID',font=('new times roman',20,'bold'))
    idl.grid(row=0,column=0,padx=50,pady=15)
    idEntry = Entry(update_window,font=('arial',15),bd=2)
    idEntry.grid(row=0,column=1,padx=30)

    #NAME
    namel = Label(update_window,text='Name',font=('New times roman',20,'bold'))
    namel.grid(row=1,column=0,padx=50,pady=15)
    nameEntry = Entry(update_window,font=('arial',15),bd=2)
    nameEntry.grid(row=1,column=1,padx=30)

    #mobile number
    mobl= Label(update_window,text='Mob',font=('New times roman',20,'bold'))
    mobl.grid(row=2,column=0,padx=50,pady=15)
    mobEntry = Entry(update_window,font=('arial',15),bd=2)
    mobEntry.grid(row=2,column=1,padx=30)

    #email
    email = Label(update_window,text='E-mail',font=('New times roman',20,'bold'))
    email.grid(row=3,column=0,padx=50,pady=15)
    emailEntry = Entry(update_window,font=('arial',15),bd=2)
    emailEntry.grid(row=3,column=1,padx=30)


    #address
    addl = Label(update_window,text='Address',font=('new times roman',20,'bold'))
    addl.grid(row=4, column=0,padx=50,pady=15)
    addEntry = Entry(update_window,font=('arial',15),bd=2)
    addEntry.grid(row=4,column=1,padx=30)

    #GENDER
    genderl = Label(update_window,text='Gender',font=('New times roman',20,'bold'))
    genderl.grid(row=5,column=0,padx=50,pady=15)
    genderEntry = Entry(update_window,font=('arial',15),bd=2)
    genderEntry.grid(row=5,column=1,padx=30)

    #dob
    dobl = Label(update_window,text='D.O.B', font=('new times roman',20,'bold'))
    dobl.grid(row=6,column=0,padx=50,pady=15)
    dobEntry = Entry(update_window,font=('arial',15),bd=2)
    dobEntry.grid(row=6,column=1,padx=30)

    #button
    addstub = ttk.Button(update_window,text='UPDATE',width=30, command=update_data)
    addstub.grid(row=8,column=1,pady=15)

    indexing = table.focus()
    content = table.item(indexing)
    listdata= content['values']
    idEntry.insert(0, listdata[0])
    nameEntry.insert(0, listdata[1])
    mobEntry.insert(0, listdata[2])
    emailEntry.insert(0, listdata[3])
    addEntry.insert(0, listdata[4])
    genderEntry.insert(0, listdata[5])
    dobEntry.insert(0, listdata[6])





def show_student():
    query='select * from student'
    mouse.execute(query)
    fdata = mouse.fetchall()
    table.delete(*table.get_children())
    for data in fdata:
        table.insert('',END,values=data)




def del_button():
    indexing = table.focus()
    print(indexing)
    content = table.item(indexing)
    content_id = content['values'][0]
    query = 'delete from student where id=%s'
    mouse.execute(query,content_id)
    main.commit()
    messagebox.showinfo('Deleted', f'This {content_id} is deleted Successfully')
    query='select * from student'
    mouse.execute(query)
    table.delete(table.get_children())
    fdata = mouse.fetchall()
    for data in fdata:
        table.insert('',END,values=data)
    



def search_button():

    def sdata():
        query = 'select * from student where id = %s or name = %s or mobile = %s or Email = %s or address = %s or gender = %s or DOB = %s'
        mouse.execute(query,(idEntry.get(),nameEntry.get(),mobEntry.get(),emailEntry.get(), addEntry.get(), genderEntry.get(),dobEntry.get()))
        table.delete(*table.get_children())
        fdata = mouse.fetchall()
        for data in fdata:
            table.insert('',END,values=data)





    search_window = Toplevel()
    search_window.title('Search Student')
    search_window.grab_set()
    search_window.resizable(False,False)

    # ID
    idl = Label(search_window,text='ID',font=('new times roman',20,'bold'))
    idl.grid(row=0,column=0,padx=50,pady=15)
    idEntry = Entry(search_window,font=('arial',15),bd=2)
    idEntry.grid(row=0,column=1,padx=30)

    #NAME
    namel = Label(search_window,text='Name',font=('New times roman',20,'bold'))
    namel.grid(row=1,column=0,padx=50,pady=15)
    nameEntry = Entry(search_window,font=('arial',15),bd=2)
    nameEntry.grid(row=1,column=1,padx=30)

    #mobile number
    mobl= Label(search_window,text='Mob',font=('New times roman',20,'bold'))
    mobl.grid(row=2,column=0,padx=50,pady=15)
    mobEntry = Entry(search_window,font=('arial',15),bd=2)
    mobEntry.grid(row=2,column=1,padx=30)

    #email
    email = Label(search_window,text='E-mail',font=('New times roman',20,'bold'))
    email.grid(row=3,column=0,padx=50,pady=15)
    emailEntry = Entry(search_window,font=('arial',15),bd=2)
    emailEntry.grid(row=3,column=1,padx=30)


    #address
    addl = Label(search_window,text='Address',font=('new times roman',20,'bold'))
    addl.grid(row=4, column=0,padx=50,pady=15)
    addEntry = Entry(search_window,font=('arial',15),bd=2)
    addEntry.grid(row=4,column=1,padx=30)

    #GENDER
    genderl = Label(search_window,text='Gender',font=('New times roman',20,'bold'))
    genderl.grid(row=5,column=0,padx=50,pady=15)
    genderEntry = Entry(search_window,font=('arial',15),bd=2)
    genderEntry.grid(row=5,column=1,padx=30)

    #dob
    dobl = Label(search_window,text='D.O.B', font=('new times roman',20,'bold'))
    dobl.grid(row=6,column=0,padx=50,pady=15)
    dobEntry = Entry(search_window,font=('arial',15),bd=2)
    dobEntry.grid(row=6,column=1,padx=30)

    #button
    addstub = ttk.Button(search_window,text='SEARCH STUDENT',width=30,command=sdata)
    addstub.grid(row=8,column=1,pady=15)








def add_stu():
    def data():
        if idEntry.get()=='' or nameEntry.get()=='' or mobEntry.get()=='' or emailEntry.get()=='' or addEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
            messagebox.showerror('Error','Data cannot be empty', parent=window)

        else:
            
            try:
                query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mouse.execute(query,(idEntry.get(),nameEntry.get(),mobEntry.get(),emailEntry.get(),addEntry.get(),genderEntry.get(),dobEntry.get(),date,ctime))
                main.commit()
                result = messagebox.askyesno('Success','Do you want to clean the Form!!',parent = window)
                if result:
                    idEntry.delete(0,END)
                    nameEntry.delete(0,END)
                    mobEntry.delete(0,END)
                    addEntry.delete(0,END)
                    genderEntry.delete(0,END)
                    dobEntry.delete(0,END)
                    emailEntry.delete(0,END)
                    
                else:
                    pass 
            except:
                messagebox.showerror('Error','Id cannot be Repeated',parent = window)
                return

        query = 'select * from student'
        mouse.execute(query)
        fect_data = mouse.fetchall()
        #print(fect_data)
        table.delete(*table.get_children())
        for data in fect_data:
            table.insert('',END,values=data)




    window= Toplevel()
    window.resizable(False,False)
    window.grab_set()
    # ID
    idl = Label(window,text='ID',font=('new times roman',20,'bold'))
    idl.grid(row=0,column=0,padx=50,pady=15)
    idEntry = Entry(window,font=('arial',15),bd=2)
    idEntry.grid(row=0,column=1,padx=30)

    #NAME
    namel = Label(window,text='Name',font=('New times roman',20,'bold'))
    namel.grid(row=1,column=0,padx=50,pady=15)
    nameEntry = Entry(window,font=('arial',15),bd=2)
    nameEntry.grid(row=1,column=1,padx=30)

    #mobile number
    mobl= Label(window,text='Mob',font=('New times roman',20,'bold'))
    mobl.grid(row=2,column=0,padx=50,pady=15)
    mobEntry = Entry(window,font=('arial',15),bd=2)
    mobEntry.grid(row=2,column=1,padx=30)

    #email
    email = Label(window,text='E-mail',font=('New times roman',20,'bold'))
    email.grid(row=3,column=0,padx=50,pady=15)
    emailEntry = Entry(window,font=('arial',15),bd=2)
    emailEntry.grid(row=3,column=1,padx=30)


    #address
    addl = Label(window,text='Address',font=('new times roman',20,'bold'))
    addl.grid(row=4, column=0,padx=50,pady=15)
    addEntry = Entry(window,font=('arial',15),bd=2)
    addEntry.grid(row=4,column=1,padx=30)

    #GENDER
    genderl = Label(window,text='Gender',font=('New times roman',20,'bold'))
    genderl.grid(row=5,column=0,padx=50,pady=15)
    genderEntry = Entry(window,font=('arial',15),bd=2)
    genderEntry.grid(row=5,column=1,padx=30)

    #dob
    dobl = Label(window,text='D.O.B', font=('new times roman',20,'bold'))
    dobl.grid(row=6,column=0,padx=50,pady=15)
    dobEntry = Entry(window,font=('arial',15),bd=2)
    dobEntry.grid(row=6,column=1,padx=30)


    #joining date
    #joinl = Label(window,text = 'Joining Date', font=('new times roman',20,'bold'))
    #joinl.grid(row=7,column=0,padx=50,pady=15)
    #joinEntry = Entry(window,font=('arial',15),bd=2)
    #joinEntry.grid(row=7,column=1,padx=30)

    #joining time
    #joint = Label(window,text = 'Joining time', font=('new times roman',20,'bold'))
    #joint.grid(row=7,column=0,padx=50,pady=15)
    #jointEntry = Entry(window,font=('arial',15),bd=2)
    #jointEntry.grid(row=7,column=1,padx=30)

    #button
    addstub = ttk.Button(window,text='ADD STUDENT',width=30,command=data)
    addstub.grid(row=8,column=1,pady=15)


def connectdb():
    
    def connectM():
        global mouse,main
        try:    
            #main= pymysql.connect(host=hostEntry.get(), user=usernameEntry.get(), passwd=passwordEntry.get())
            main= pymysql.connect(host='localhost', user='root', passwd='Vineet@1530')
            mouse = main.cursor()
            messagebox.showinfo("Success","Connected to Database", parent=connect)
        except:
            messagebox.showerror("Invalid Details", parent=connect)
        try:

            query ='create database studentmanagementsystem'
            mouse.execute(query)
            query = 'use studentmanagementsystem'
            mouse.execute(query)
            query = 'create table student(id int not null primary key, name varchar(50), mobile varchar(15), email varchar(50), address varchar(150), gender varchar(10), dob varchar(50), date varchar(20), time varchar(15))'
            mouse.execute(query)
        except:
            query = 'use studentmanagementsystem'
            mouse.execute(query)
            #enabling buttons
            addstu.config(state=NORMAL)
            Searchstu.config(state=NORMAL)
            Deletestu.config(state=NORMAL)
            Updatestu.config(state=NORMAL)
            Showstu.config(state=NORMAL)
            Exportdata.config(state=NORMAL)
            connect.destroy()





    connect=Toplevel()
    connect.grab_set()
    connect.title('Connect to database')
    connect.resizable(False,False)
    connect.geometry('500x300+500+200')

    hostitle = Label(connect,text='Enter Details',font=('arial',18,'bold'),fg='red')
    #hostitle.place(x=170,y=0)
    hostitle.grid(row=0,column=3)

    hostname = Label(connect,text='Host Name',font=('arial',22,'bold'),fg='gray')
    hostname.grid(row=3,column=2,padx=20)
    hostentry = Entry(connect,font=('roman',15,'bold'),bd=2)
    hostentry.grid(row=3,column=3, padx=40, pady=20)

    username = Label(connect,text='User Name',font=('arial',22,'bold'),fg='gray')
    username.grid(row=8,column=2,padx=20)
    usernameentry = Entry(connect,font=('roman',15,'bold'),bd=2)
    usernameentry.grid(row=8,column=3,padx=40,pady=20)

    passwordl = Label(connect,text='Password',font=('arial',22,'bold'),fg='gray')
    passwordl.grid(row=13,column=2,padx=20)
    passwordentry = Entry(connect,font=('roman',15,'bold'),bd=2)
    passwordentry.grid(row=13,column=3,padx=40,pady=20)

    connectb = ttk.Button(connect, text="Connect", width='28',command=connectM)
    connectb.grid(row= 18,column=3)


def clock():
    global date, ctime
    date = time.strftime('%d/%m/%Y')
    ctime = time.strftime('%H:%M:%S')
    datetime.config(text=f'   Date: {date}\nTime: {ctime}')
    datetime.after(1000,clock)

count = 0
text = '' 
def slider():
    global text
    global count
    if count == len(Sname):
        count = 0
        text=''
    text = text+Sname[count]
    slidert.config(text=text)
    slidert.after(300,slider)
    count=count+1

data = ttkthemes.ThemedTk()
data.get_themes()
data.set_theme('arc')

data.title("Student management System")
data.geometry("1620x900+0+0")
data.resizable(False,False)

BgImg = ImageTk.PhotoImage(file='white.jpg')
bglabel = Label(data,bg='gray89')
bglabel.place(x=-5 , y=-3 )



#LEFT frame
butt =  Frame(data)
butt.place(x=190,y=150)
buttImg = PhotoImage(file='students.png') #student image
butl = Label(butt, image= buttImg)
butl.grid(row=1,column=0, pady=10, padx=20)

#RIGHT FRAME
leftf = Frame(data)
leftf.place(x=500,y=150,width=1083,height=678)

#SCROOLBAR
scrollx =Scrollbar(leftf,orient=HORIZONTAL)
scrolly = Scrollbar(leftf,orient=VERTICAL)

table = ttk.Treeview(leftf, columns=('ID','Name','Mobile No','Email','Address','Gender','DOB','Joining','Joining Time'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.config(command=table.xview)
scrolly.config(command=table.yview)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
table.pack(fill=BOTH,expand=1)

#adding name in coloums
table.heading('ID',text='ID')
table.heading('Name',text='Name')
table.heading('Mobile No',text='Mob No')
table.heading('Address',text='Address')
table.heading('Email',text='Email ID')
table.heading('Gender',text='Gender')
table.heading('DOB',text='D.O.B')
table.heading('Joining',text='Joining Date')
table.heading('Joining Time',text='Joining Time')

table.column('ID',width=50,anchor=CENTER)
table.column('Name',width=250,anchor=CENTER)
table.column('Mobile No',width=250,anchor=CENTER)
table.column('Email',width=400,anchor=CENTER)
table.column('Address',width=250,anchor=CENTER)
table.column('Gender',width=250,anchor=CENTER)
table.column('DOB',width=250,anchor=CENTER)
table.column('Joining',width=250,anchor=CENTER)
table.column('Joining Time',width=250,anchor=CENTER)

style = ttk.Style()
style.configure('Treeview',rowheight = 35, font = (15))

table.config(show='headings')

#Date and time
datetime= Label(data, font=('New Times Roman',14,'bold'))
datetime.place(x=5,y=5)
clock()



# slider text
Sname = "Student Management System"
slidert = Label(data,font=('New times roman',35,'bold'))
slidert.place(x=520,y=0)
slider()


#connect to dbms
connectDBMS = ttk.Button(data,text="Connect to Database",width=25,command=connectdb,cursor='hand2')
connectDBMS.place(x=1399,y=3)

#button
addstu=ttk.Button(butt, text="Add Students", width="35",state=DISABLED,command=add_stu)
addstu.grid(row=6,column=0,padx=10,pady=20)

Searchstu = ttk.Button(butt, text="Search Student", width="35",state=DISABLED,command=search_button)
Searchstu.grid(row=8,column=0,padx=10,pady=20)

Deletestu = ttk.Button(butt, text="Delete Student", width="35",state=DISABLED,command=del_button)
Deletestu.grid(row=10,column=0,padx=10,pady=20)

Updatestu = ttk.Button(butt, text="Update Student", width="35",state=DISABLED,command=update_student)
Updatestu.grid(row=12,column=0,padx=10,pady=20)

Showstu = ttk.Button(butt, text="Show Student", width="35",state=DISABLED, command=show_student)
Showstu.grid(row=14,column=0,padx=10,pady=20)

Exportdata = ttk.Button(butt, text="Export Data", width="35",state=DISABLED, command=export_data)
Exportdata.grid(row=16,column=0,padx=10,pady=20)

Exitd = ttk.Button(butt, text="Exit", width="35", command=iexit)
Exitd.grid(row=18,column=0,padx=10,pady=20)
data.mainloop()

