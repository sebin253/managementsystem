from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
 
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='user' and passwordEntry.get()=='password':
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import sms

    else:
        messagebox.showerror('Error','Please enter correct credentials')


window =Tk()
window.geometry('1288x700+0+0')
window.title('Login system of student managment')
window.resizable(False,False)

backgroundImage=ImageTk.PhotoImage(file='C:\\Users\\sebin\\Desktop\\programming\\pyhton course\\studentmanagement\\college.jpg')
bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

loginFrame = Frame(window)
loginFrame.place(x=400,y=150)
logoImage =PhotoImage(file='C:\\Users\\sebin\\Desktop\\programming\\pyhton course\\studentmanagement\\student.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,padx=10)

usernameImage=PhotoImage(file='C:\\Users\\sebin\\Desktop\\programming\\pyhton course\\studentmanagement\\user.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='username',compound=LEFT,font=('times new roman',20,'bold' ),bg='white')
usernameLabel.grid(row=1,column=0,padx=10,pady=20)

usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5)
usernameEntry.grid(row=1,column=1,pady=20)


passwordImage=PhotoImage(file='C:\\Users\\sebin\\Desktop\\programming\\pyhton course\\studentmanagement\\password.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='passsword',compound=LEFT,font=('times new roman',20,'bold' ),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5)
passwordEntry.grid(row=2,column=1,pady=20,padx=20)

loginbutton = Button(loginFrame, text='Login', font=('times new roman', 14, 'bold'), width=15, fg='white', bg='cornflowerblue', activebackground='cornflowerblue', activeforeground='white', cursor='hand2',command=login)

loginbutton.grid(row=3,column=1,pady=10)
window.mainloop()