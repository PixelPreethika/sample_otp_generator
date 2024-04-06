from tkinter import *
from tkinter import messagebox
from plyer import notification
from homepage import home_page
from database import login_user
from otpverify import otp_verify
from createuser import create_page
from register import register_page
from flask import session, request
import os
import socket
from securekey import generate_encryption_key, decrypt_secret_key
from otpgenerator import verify_otp


loggedin_user = None
hashed = None
def login_page():
    window = Tk()
    window.title("Login")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False,False)
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
      
    def register():
        window.destroy()
        register_page(login_page)    
    def signin():
        user_name = username.get()
        user_pwd = userpwd.get()
        
        if(user_name!= "Username" and user_pwd != "Password"):
            val = login_user(user_name, user_pwd)
        else:
            val = None
            messagebox.showerror("nvalid", "Please enter Username and Password")
        # val = "1"
        if (val != None):
            try:
                def verify(otp_entry):
                    entry =otp_entry.get()
                    print("otp : ",entry, otp_entry)
                    print(val[0][0], " : ",val[0][1] ," : ",val[0][2], entry)
                    encrpted_data= val[0][0]
                    iv = val[0][1]
                    encryption_key = val[0][2]
                    print("login encryption_key : ",encryption_key)
                    key = decrypt_secret_key(encrpted_data,iv,encryption_key)
                    result = verify_otp(key,entry)
                    if verify_otp(key, entry):
                        print("Verification Successful! Proceed with user authentication.")
                        otp_window.destroy()
                        window.destroy()
                        home_page(login_page, loggedin_user)
                    else:
                        print("Verification Failed! Handle failed authentication.")
                    # if result:
                    #     window.destroy()
                    #     home_page(login_page, loggedin_user)
                    # else:
                    #     messagebox.showerror("Verification Result", "Invalid OTP!")
                otp_window = Tk()
                otp_window.title("OTP Verification")
                otp_window.geometry("200x100")
                otp_window.attributes('-topmost', True) # sets this as topmost window
                
                label = Label(otp_window, text="Enter OTP:")
                label.pack()
                
                otp_entry = Entry(otp_window)
                otp_entry.pack()
                
                verify_button = Button(otp_window, text="Verify OTP", command=lambda: verify(otp_entry))
                verify_button.pack()
                otp_window.mainloop()
            except Exception as e:
                print("Error:", e)
        else:
            messagebox.showerror("Failure", "Unable to login")
        
    # Load the image
    # img = PhotoImage(file='register.png')
    current_directory = os.path.dirname(os.path.realpath(__file__))
    image_file = os.path.join(current_directory, "login.png")
    img = PhotoImage(file=image_file)

    # Create a label to display the image
    image_label = Label(window, image=img, bg="white")
    image_label.place(x=50, y=50)

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


    Button(frame,width=39,pady=7,text="Sign in", bg="#57a1f8",fg="white",border=0, command=signin).place(x=35,y=204)
    label = Label(frame, text="I do not have an account", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
    label.place(x=70, y=250)
    signin = Button(frame,width=6,text="Sign up",border=0,bg="white",cursor="hand2",fg="#57a1f8",command=register).place(x=215, y=250)
    window.mainloop()