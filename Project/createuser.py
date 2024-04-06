from tkinter import *
from tkinter import messagebox
from database import insert_user
import pyotp
import qrcode
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
from otp_verify import generate_secret_key, generate_qr_code
from securekey import generate_encryption_key,encrypt_secret_key

def create_page(login):
    def signin():
        user_name = username.get()
        user_pwd = userpwd.get()
        user_cfmpwd = usercfmpwd.get()

        print("username : ", user_name,"pwd : ", user_pwd, " : confirm : ", user_cfmpwd)
        if user_name != 'Username' and user_pwd != 'Password' and user_cfmpwd != 'Confirm Password' :
            print("Required data is entred")
            try:
                def create():
                    user_key = generate_encryption_key(user_pwd)
                    print("user_key : ",user_key)
                    iv, data = encrypt_secret_key(secret_key,user_key)
                    insert_user(user_name, user_pwd, data,iv, user_key)
                    messagebox.showinfo("Success", "User created successfully") 
                    qr_window.destroy()
                    window.destroy()
                    login()
                secret_key = generate_secret_key()
                print("in qr : ",secret_key)
                account_name = "YourApp"  # Specify the account name
                img, secret_key = generate_qr_code(secret_key, account_name)

                # Convert PIL image to Tkinter PhotoImage
                img_tk = ImageTk.PhotoImage(img)

                # Create a Tkinter window
                qr_window = tk.Toplevel()
                qr_window.title("QR Code")

                # Display the QR code image
                qr_label = tk.Label(qr_window, image=img_tk)
                qr_label.pack()
                

                # Function to copy the secret key to clipboard
                def show_secret_key():
                    print("in key : ",secret_key)
                    def create_key():
                        user_key = generate_encryption_key(user_pwd)
                        print("user_key : ",user_key)
                        iv, data = encrypt_secret_key(secret_key,user_key)
                        insert_user(user_name, user_pwd, data,iv, user_key)
                        messagebox.showinfo("Success", "User created successfully") 
                        root.destroy()
                        window.destroy()
                        login()

                    def copy_to_clipboard():
                        root.clipboard_clear()
                        root.clipboard_append(secret_key)
                        messagebox.showinfo("Copied", "Secret key copied to clipboard")
                    qr_window.destroy()
                    root = tk.Toplevel()
                    root.title("Secret Key")
                    root.geometry("350x100")
                    root.resizable(0, 0)
                    key = tk.Entry(root,width=30, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
                    key.place(x=10, y=10)  
                    key.insert(0, secret_key)
                    key.configure(state='readonly')
                    key.pack()
                    # key = tk.Entry(root, width=25, fg="black", state="disabled", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
                    # key.insert(tk.END, secret_key)
                    # key.pack()
                    Button = tk.Button(root, text="OK", command=create_key)
                    Button.pack()
                    Button = tk.Button(root, text="Copy", command=copy_to_clipboard)
                    Button.pack()
                    
                    root.mainloop()

                # Button to display the secret key and allow copying
                secret_key_button = tk.Button(qr_window, text="Show Secret Key", command=show_secret_key)
                secret_key_button.pack()
                Button = tk.Button(qr_window, text="OK", command=create)
                Button.pack()

                # Run the Tkinter event loop
                qr_window.mainloop()
            except Exception as e:
                messagebox.showerror("Error", str(e))
            
            
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

    frame = Frame(window, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(x=100, y=5)

    username = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light", 11))
    username.place(x=30, y=80)  
    username.insert(0,"Username")

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
