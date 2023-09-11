from tkinter import *
import time
import ttkthemes
from tkinter import ttk ,messagebox,filedialog
import  pymysql
import pandas

def iexit():
    result=messagebox.askyesno('Confirm','Do You Want To Exit')
    if result:
        root.destroy()
    else:
        pass

def export_data():
   url= filedialog.asksaveasfilename(defaultextension='.csv')
   indexing=studentTable.get_children()
   newlist=[]
   for index in indexing:
       content =studentTable.item(index)
       datalist=content['values']
       newlist.append(datalist)
       print(newlist)
   
   table=pandas.DataFrame(newlist,columns=['Id','Name','mobile','Email','Address','Gender','Dob','Added Date','Added Time'])
   table.to_csv(url,index=False)
   messagebox.showinfo('Success','Data is saved succesfully')

def top_level_data(title,button_text,command):
    global idEntry,phoneEntry,nameEntry,emailEntry,addressEntry,dobEntry,genderEntry,screen
    screen=Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(False,False)
    idLabel=Label(screen,text='Id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,padx=10,pady=15)
    
    nameLabel=Label(screen,text='Name',font=('times new roman',20,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,padx=10,pady=15)

    phoneLabel=Label(screen,text='Phone No:',font=('times new roman',20,'bold'))
    phoneLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    phoneEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    phoneEntry.grid(row=3,column=1,padx=10,pady=15)

    emailLabel=Label(screen,text='Email ID:',font=('times new roman',20,'bold'))
    emailLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    emailEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    emailEntry.grid(row=4,column=1,padx=10,pady=15)

    addressLabel=Label(screen,text='Address',font=('times new roman',20,'bold'))
    addressLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    addressEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    addressEntry.grid(row=5,column=1,padx=10,pady=15)

    genderLabel=Label(screen,text='Gender',font=('times new roman',20,'bold'))
    genderLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    genderEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    genderEntry.grid(row=6,column=1,padx=10,pady=15)

    dobLabel=Label(screen,text='D.O.B',font=('times new roman',20,'bold'))
    dobLabel.grid(row=7,column=0,padx=30,pady=15,sticky=W)
    dobEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    dobEntry.grid(row=7,column=1,padx=10,pady=15)

    student_button=ttk.Button(screen,text=button_text,command=command)
    student_button.grid(row=8,columnspan=2,pady=15)
    if title=='Update Student':

     indexing = studentTable.focus()

     content=studentTable.item(indexing)  
     listdata=content['values']
     idEntry.insert(0,listdata[0])
     nameEntry.insert(0,listdata[1])
     phoneEntry.insert(0,listdata[2])
     emailEntry.insert(0,listdata[3])
     addressEntry.insert(0,listdata[4])
     genderEntry.insert(0,listdata[5])
     dobEntry.insert(0,listdata[6])


def update_data():
    query='update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
    mycursor.execute(query,(nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currenttime,idEntry.get()))
    con.commit()
    messagebox.showinfo('Success',f'Id {idEntry.get()} is modified successfully',parent=screen)
    screen.destroy()
    shows_student()


def shows_student(): 
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)

def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Delete',f'Id  {content_id}is deleted succesfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)


def search_data():
    query='select *from student where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob =%s'
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),phoneEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)


    



def add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
        messagebox.showerror ('Error','All Feilds are required',parent=screen)
    else:
        
        try:
            
            query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(), nameEntry.get(),phoneEntry.get() ,emailEntry.get(), addressEntry.get(), genderEntry.get(), dobEntry.get(), date, currenttime))
            con.commit()
            result=messagebox.askyesno('Confirm','Data addes successfully.Do not want to clean the form?',parent=screen)
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                phoneEntry.delete(0,END)
                emailEntry.delete(0,END)
                addressEntry.delete(0,END)
                genderEntry.delete(0,END)
                dobEntry.delete(0,END)
            else:
                pass
        except:
            messagebox.showerror('Error','Id cannot be repeated',parent=screen)
            return

        query='select *from student '
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            datalist=list(data)
            studentTable.insert('',END,values=datalist)

   


def connect_database():
    def connect():
        global mycursor,con
        try:
            con = pymysql.connect(host='localhost',user='root',password='0715')
            mycursor=con.cursor()   
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectwindow)
            return
        try:
            query='create database studentmanagementsystem' 
            mycursor.execute(query)
            query='use studentmanagementsystem'
            mycursor.execute(query)
            query='create table student(id int not null primary key,name varchar(30),mobile varchar(10),email varchar(30),address varchar(100),gender varchar(20),dob varchar(20),date varchar(50),time varchar(50))'
            mycursor.execute(query)
        except:
              query='use studentmanagementsystem'
              mycursor.execute(query)
        messagebox.showinfo('Sucess','Database Connection is successful',parent=connectwindow)
        connectwindow.destroy()
        addstudentbutton.config(state=NORMAL)
        searchstudentbutton.config(state=NORMAL)
        updatestudentbutton.config(state=NORMAL)
        showstudentbutton.config(state=NORMAL)
        exportstudentbutton.config(state=NORMAL)
        deletestudentbutton.config(state=NORMAL)


    connectwindow=Toplevel ()
    connectwindow.grab_set()
    connectwindow.geometry('470x250+730+230')
    connectwindow.title('Database connection')
    connectwindow.resizable(0,0)

    hostnameLabel=Label(connectwindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)
    hostentry=Entry(connectwindow,font=('roman',15,'bold'),bd=2)
    hostentry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel=Label(connectwindow,text='user Name',font=('arial',20,'bold'))
    usernameLabel.grid(row=1,column=0,padx=20)
    userentry=Entry(connectwindow,font=('roman',15,'bold'),bd=2)
    userentry.grid(row=1,column=1,padx=40,pady=20)

    passwordLabel=Label(connectwindow,text='Password',font=('arial',20,'bold'))
    passwordLabel.grid(row=2,column=0,padx=20)
    passwordentry=Entry(connectwindow,font=('roman',15,'bold'),bd=2)
    passwordentry.grid(row=2,column=1,padx=40,pady=20)

    connectButton=ttk.Button(connectwindow,text='connect',command=connect)
    connectButton.grid(row=3,columnspan=2)



count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderlabel.config(text=text)
    count+=1
    sliderlabel.after(300,slider)

def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'    Date:{date}\n   Time: {currenttime}')
    datetimeLabel.after(1000,clock)


root=ttkthemes.ThemedTk()

root.get_themes()
root.set_theme('radiance')


root.geometry('1174x680+50+20')
root.resizable(0,0)  
root.title('student management system')

datetimeLabel=Label(root,text='hello',font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Student Management System'  
sliderlabel=Label(root,text=s,font=('arial',28,'italic bold'),width=30)
sliderlabel.place(x=200,y=0)
slider()

connectbutton=ttk.Button(root,text='Connect Database',command=connect_database)
connectbutton.place(x=980,y=0)

leftframe=Frame(root)
leftframe.place(x=50,y=80,width=300,height=600)
logo_image=PhotoImage(file='C:\\Users\\sebin\\Desktop\\programming\\pyhton course\\studentmanagement\\studentgp.png')
logo_label=Label(leftframe,image=logo_image)
logo_label.grid(row=0,column= 0)

addstudentbutton =ttk.Button(leftframe,text='Add student',width=25,state=DISABLED,command=lambda:top_level_data('Add student','ADD',add_data))
addstudentbutton.grid(row=1,column=0,pady=20)

searchstudentbutton =ttk.Button(leftframe,text='Search student',width=25,state=DISABLED,command=lambda:top_level_data('Search Student','Search',search_data))
searchstudentbutton.grid(row=2,column=0,pady=20)

deletestudentbutton =ttk.Button(leftframe,text='Delete student',width=25,state=DISABLED,command=delete_student)
deletestudentbutton.grid(row=3,column=0,pady=20)

updatestudentbutton =ttk.Button(leftframe,text='Update Student',width=25,state=DISABLED,command=lambda:top_level_data('Update Student','Update',update_data))
updatestudentbutton.grid(row=4,column=0,pady=20)

showstudentbutton =ttk.Button(leftframe,text='show student',width=25,state=DISABLED,command=shows_student)
showstudentbutton.grid(row=5,column=0,pady=20)

exportstudentbutton =ttk.Button(leftframe,text='Export student',width=25,state=DISABLED,command=export_data)
exportstudentbutton.grid(row=6,column=0,pady=20)

exitstudentbutton =ttk.Button(leftframe,text='Exit',width=25,command=iexit)
exitstudentbutton.grid(row=7,column=0,pady=20)

rightframe=Frame(root)
rightframe.place(x=350,y=80,width=820,height=600)

ScrollbarX=Scrollbar(rightframe,orient=HORIZONTAL)
Scrollbary=Scrollbar(rightframe,orient=VERTICAL)

studentTable=ttk.Treeview(rightframe,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time')
                          ,xscrollcommand=ScrollbarX.set,yscrollcommand=Scrollbary.set)
ScrollbarX.config(command=studentTable.xview)
Scrollbary.config(command=studentTable.yview)
ScrollbarX.pack(side=BOTTOM,fill=X)
Scrollbary.pack(side=RIGHT,fill=Y)
studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile No',text='Mobile No')
studentTable.heading('Email',text='Email Address')
studentTable.heading('Address',text='Assress')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added time')

studentTable.column('Id',width=50,anchor=CENTER) 
studentTable.column('Name',width=300,anchor=CENTER) 
studentTable.column('Email',width=300,anchor=CENTER) 
studentTable.column('Mobile No',width=200,anchor=CENTER) 
studentTable.column('Address',width=300,anchor=CENTER) 
studentTable.column('Gender',width=100,anchor=CENTER) 
studentTable.column('D.O.B',width=100,anchor=CENTER) 
studentTable.column('Added Date',width=200,anchor=CENTER) 
studentTable.column('Added Time',width=200,anchor=CENTER) 
style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('arial',15,'bold'))
style.configure('Treeview.Heading',font=('arial',14,'bold'))

studentTable.config(show='headings')

root.mainloop()