from tkinter import *
from tkinter import messagebox
# from login import login_page
from database import insert_user

def create_page(login):
    def signin():
        user_name = username.get()
        user_pwd = userpwd.get()
        user_cfmpwd = usercfmpwd.get()

        print("username : ", user_name,"pwd : ", user_pwd, " : confirm : ", user_cfmpwd)
        if user_name != 'Username' and user_pwd != 'Password' and user_cfmpwd != 'Confirm Password' :
            print("Required data is entred")
            try:
                insert_user(user_name, user_pwd)
                messagebox.showinfo("Success", "User created successfully") 
            except Exception as e:
                messagebox.showerror("Error", str(e))
            window.destroy()
            login()
        else:
            messagebox.showerror("Invalid", "Please fill up all the fields")  
    def enter_username(event):
        if username.get() == 'Username':
            username.delete(0, "end")

    def leave_username(event):
        if username.get() == '':
            username.insert(0, "Username") 
            
    def enter_pwd(event):
        if userpwd.get() == 'Password':
            userpwd.delete(0, "end")
    def leave_pwd(event):
        print(userpwd.get())
        if userpwd.get() == '':
            userpwd.insert(0,"Password") 

    def enter_cfmpwd(event):
        if usercfmpwd.get() == 'Confirm Password':    
            usercfmpwd.delete(0, "end")
    def leave_cfmpwd(event):
        print(usercfmpwd.get())
        if usercfmpwd.get() == '':
            usercfmpwd.insert(0,"Confirm Password") 
    window = Tk()
    window.title("Create User")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False,False)
    # frame = Frame(window, width=350, height=350, bg="white")
    # frame.place(x=480, y=70)
    # heading = Label(frame, text="Create a User", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    # heading.place(x=100, y=5)
    # Button(frame,width=39,pady=7,text="Exit", bg="#57a1f8",fg="white",border=0, command = clicked).place(x=35,y=204)
    # window.mainloop()
        
    # Load the image
    # img = PhotoImage(file='register.png')
    # current_directory = os.path.dirname(os.path.realpath(__file__))
    # image_file = os.path.join(current_directory, "login.png")
    # img = PhotoImage(file=image_file)

    # Create a label to display the image
    # image_label = Label(window, image=img, bg="white")
    # image_label.place(x=50, y=50)

    frame = Frame(window, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(x=100, y=5)

    username = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light", 11))
    username.place(x=30, y=80)  
    username.insert(0,"Username")
    # username.config(state='readonly')

    # Bind the function to clear the entry when the user starts typing
    username.bind("<FocusIn>", enter_username)
    username.bind("<FocusOut>", leave_username)

    Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)


    userpwd = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light", 11))
    userpwd.place(x=30, y=150)  
    userpwd.insert(0,"Password")

    userpwd.bind("<FocusIn>", enter_pwd)
    userpwd.bind("<FocusOut>", leave_pwd)
    Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

    usercfmpwd = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light", 11))
    usercfmpwd.place(x=30, y=220)  
    usercfmpwd.insert(0,"Confirm Password")

    usercfmpwd.bind("<FocusIn>", enter_cfmpwd)
    usercfmpwd.bind("<FocusOut>", leave_cfmpwd)
    Frame(frame,width=295,height=2,bg="black").place(x=25,y=247)


    Button(frame,width=39,pady=7,text="Sign in", bg="#57a1f8",fg="white",border=0, command=signin).place(x=35,y=274)
    window.mainloop()
