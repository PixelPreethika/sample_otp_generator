
from tkinter import *
from tkinter import messagebox
from database import register_user
from plyer import notification
from createuser import create_page
from otpgenerator import generate_user_otp, generate_otp, verify_user_input
import socket

hashed = None
def register_page(login):
    window =Tk()
    window.title("Register") 
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False,False)  
    
     
            
    def enter_fn(event):
        if first_name_entry.get() == 'First Name':
            first_name_entry.delete(0, "end")
    def leave_fn(event):
        if first_name_entry.get() == '':
            first_name_entry.insert(0, "First Name") 
    
    def enter_ln(event):
        if last_name_entry.get() == 'Last Name' :
            last_name_entry.delete(0, "end")
    def leave_ln(event):
        if last_name_entry.get() == '':
            last_name_entry.insert(0, "Last Name")
            
    def enter_email(event):
        if useremail.get() == 'Email':
            useremail.delete(0, "end")
    def leave_email(event):
        if useremail.get() == '':
            useremail.insert(0, "Email")        
            
    def enter_country(event):
        if usercountry.get() == 'Country':
            usercountry.delete(0, "end")
    def leave_country(event):
        if usercountry.get() == '':
            usercountry.insert(0, "Country") 
    
    def enter_phn(event):
        if userphone.get() == 'Phone Number':
            userphone.delete(0, "end")
    def leave_phn(event):
        if userphone.get() == '':
            userphone.insert(0, "Phone Number")   
            
    def enter_dob(event):
        if userdob.get() == 'Date of Birth':
            userdob.delete(0, "end")
    def leave_dob(event):
        if userdob.get() == '':
            userdob.insert(0, "Date of Birth")                                  
    def log_in():
        window.destroy()
        login()
    def signup():
        
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        country = usercountry.get()
        phone_number = userphone.get()
        date_of_birth = userdob.get()
        
        email = useremail.get()
        print("user : ", first_name,"user : ", last_name, " : email : ", email ,"user : ", country ,"user : ", phone_number ,"user : ", date_of_birth)
        if first_name != 'First Name' and last_name != 'Last Name' and email != 'Email' and country != 'Country' and phone_number != 'Phone Number' and date_of_birth != 'Date of Birth' :
            print("Required data is entred")
            try:
                register_user(first_name, email,last_name,country,phone_number,date_of_birth)
                try:
                    def otpgen():
                        global hashed
                        otp = generate_user_otp(first_name)
                        ip = socket.gethostbyname(socket.gethostname())
                        hashed = generate_otp(ip,otp)
                        full_title="Hello "+first_name+"!"
                        full_message ="Your OTP is " + otp
                        notification.notify(
                            title=full_title,
                            message=full_message,
                            app_icon = None,
                            timeout=60,
                            toast=False
                        )
                    def verify_otp(entry):
                        ip_address = socket.gethostbyname(socket.gethostname())
                        entered_otp = entry.get()
                        

                        if verify_user_input(ip_address, entered_otp, hashed):
                            messagebox.showinfo("Verification Result", "OTP Verified Successfully!")
                            otp_window.destroy()  
                            window.destroy()
                            create_page(login)
                        else:
                            messagebox.showerror("Verification Result", "Invalid OTP!")
                    def resend_otp():
                        otpgen()

                    otpgen()
                    otp_window = Tk()
                    otp_window.title("OTP Verification")
                    otp_window.geometry("200x100")
                    otp_window.attributes('-topmost', True) # sets this as topmost window
                    
                    label = Label(otp_window, text="Enter OTP:")
                    label.pack()
                    
                    otp_entry = Entry(otp_window)
                    otp_entry.pack()
                    
                    verify_button = Button(otp_window, text="Verify OTP", command=lambda: verify_otp(otp_entry))
                    verify_button.pack()
                    
                    resend_button = Button(otp_window, text="Resend OTP", command=resend_otp)
                    resend_button.pack()
                    otp_window.mainloop()
                except Exception as e:
                    print("Error:", e)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Invalid", "Please fill up all the fields")  
        
    frame= Frame(window,height=410,width=830,bg='white')

    frame.place(x=50, y=40)

    heading = Label(frame, text="Register", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(relx=0.5, rely=0.05, anchor=CENTER)
    
    first_name_entry = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    first_name_entry.place(x=30, y=80) 
    first_name_entry.insert(0, "First Name")
    
    first_name_entry.bind("<FocusIn>", enter_fn)
    first_name_entry.bind("<FocusOut>", leave_fn)
    Frame(frame, width=295, height=2, bg="black").place(x=25,y=107)
    
    last_name_entry = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    last_name_entry.place(x=30, y=150)
    last_name_entry.insert(0, "Last Name")

    last_name_entry.bind("<FocusIn>", enter_ln)
    last_name_entry.bind("<FocusOut>", leave_ln)
    Frame(frame, width=295, height=2, bg="black").place(x=25,y=178)

    useremail = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light", 11))
    useremail.place(x=30, y=220)  
    useremail.insert(0,"Email")
    
    useremail.bind("<FocusIn>", enter_email)
    useremail.bind("<FocusOut>", leave_email)
    Frame(frame,width=295,height=2,bg="black").place(x=25,y=247)

    userdob = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    userdob.place(x=495, y=80)  
    userdob.insert(0, "Date of Birth")
    
    userdob.bind("<FocusIn>", enter_dob)
    userdob.bind("<FocusOut>", leave_dob)
    Frame(frame, width=295, height=2, bg="black").place(x=490,y=107)
   
    usercountry = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    usercountry.place(x=495, y=150)  
    usercountry.insert(0, "Country")
    
    usercountry.bind("<FocusIn>", enter_country)
    usercountry.bind("<FocusOut>", leave_country)
    Frame(frame, width=295, height=2, bg="black").place(x=490,y=178)
    

    userphone = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    userphone.place(x=495, y=220)  
    userphone.insert(0, "Phone Number")
    
    userphone.bind("<FocusIn>", enter_phn)
    userphone.bind("<FocusOut>", leave_phn)
    Frame(frame,width=295,height=2,bg="black").place(x=490,y=247)


    Button(frame,width=39,pady=7,text="Sign up", bg="#57a1f8",fg="white",border=0,command=signup).place(x=280,y=280)
    label = Label(frame, text="I have an account", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
    label.place(x=350, y=340)
    

    signin = Button(frame,width=6,text="Sign in",border=0,bg="white",cursor="hand2",fg="#57a1f8",command=log_in).place(x=460, y=340)
    window.mainloop()

