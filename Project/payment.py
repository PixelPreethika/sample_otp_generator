from tkinter import *
from tkinter import messagebox
from otpgenerator import generate_otp
from plyer import notification
from tkinter.ttk import Combobox
from database import payment, check_cvv, cards
from flask import  session
import os


def payment_page(login,home,loggedin_user):
    window = Tk()
    window.title("Payment")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False,False)
    def enable_cardno(event):
        selected_card_type = cardtype.get()
        if selected_card_type == "Debit Card" :
            result = cards(selected_card_type,loggedin_user)
            if(result != None):
                cardno['values'] = (result)
                cardno.config(state='normal')
            else:
                cardno.config(state='disabled')
        if selected_card_type == "Credit Card":
            result = cards(selected_card_type,loggedin_user)
            if(result != None):
                cardno['values'] = (result)
                cardno.config(state='normal')
            else:
                cardno.config(state='disabled')
        if selected_card_type == "Select Card Type":
            cardno.config(state='disabled')
    def enter_phone(event):
        if phone.get() == 'To Phone Number':       
            phone.delete(0, "end")

    def leave_phone(event):
        if phone.get() == '':
            phone.insert(0, "To Phone Number") 

    def enter_amt(event):
        if amt.get() == 'Amount':
            amt.delete(0, "end")

    def leave_amt(event):
        if amt.get() == '':
            amt.insert(0, "Amount") 
    def pay():
        card_no = cardno.get()
        phn = phone.get()
        amount = amt.get()
        card_type=cardtype.get()
        if (card_type != "Select Card Type") and (card_no != "Card Number") and (amount != "Amount") and (phn != "To Phone Number"):
            def verify_cvv():
                cvv = cvv_entry.get()
                card_cvv = check_cvv(card_type, card_no,cvv,loggedin_user)
                # session_cvv = card_cvv
                if(card_cvv != None):
                    root.destroy()
                    payment(phn,card_no,amount,loggedin_user)
                    messagebox.showinfo("Success", "Amount Sent Successfully!")
                    window.destroy()
                    home(login,loggedin_user)
                else:
                    messagebox.showerror("Invalid", "Please enter the correct CVV")
            root = Toplevel(window)

            root.title("CVV Verification")
            root.geometry("200x100")
            
            label = Label(root, text="Enter CVV:")
            label.pack()
            
            cvv_entry = Entry(root)
            cvv_entry.pack()
            
            verify_button = Button(root, text="Submit", command=verify_cvv)
            verify_button.pack()
            root.mainloop()
        else:
            messagebox.showerror("Invalid", "Please fill up all the fields")

    frame = Frame(window, height=410,width=830, bg="white")
    frame.place(x=50, y=40)

    heading = Label(frame, text="Payment", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(relx=0.5, rely=0.05, anchor=CENTER)

    phone = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light", 11))
    phone.place(x=30, y=100)  
    phone.insert(0,"To Phone Number")
    # phone.config(state='readonly')

    # Bind the function to clear the entry when the user starts typing
    phone.bind("<FocusIn>", enter_phone)
    phone.bind("<FocusOut>", leave_phone)

    Frame(frame,width=295,height=2,bg="black").place(x=25,y=127)


    # cardtype = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light", 11))
    # cardtype.place(x=30, y=170)  
    # cardtype.insert(0,"Card Type")

    # cardtype.bind("<FocusIn>", enter_cardtype)
    # cardtype.bind("<FocusOut>", leave_cardtype)
    # Frame(frame,width=295,height=2,bg="black").place(x=25,y=198)
    cardno = Combobox(frame, width=35, state="readonly", font=("Microsoft YaHei UI Light", 11))
    cardno['values'] = ("Select Card Number", "Card Number 1", "Card Number 2", "Card Number 3")
    cardno.current(0)
    cardno.config(state='disabled')
    cardno.place(x=490, y=170)  

    

    amt = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light", 11))
    amt.place(x=22, y=170)
    amt.insert(0,"Amount")

    amt.bind("<FocusIn>", enter_amt)
    amt.bind("<FocusOut>", leave_amt)
    Frame(frame,width=295,height=2,bg="black").place(x=25, y=198)

    cardtype = Combobox(frame, width=35, state="readonly", font=("Microsoft YaHei UI Light", 11))
    cardtype['values'] = ("Select Card Type", "Debit Card", "Credit Card")
    cardtype.current(0)  # Select the default option
    cardtype.place(x=490, y=100)  


    # Frame(frame, width=295, height=2, bg="black").place(x=25, y=198)

    cardtype.bind("<<ComboboxSelected>>", enable_cardno)

    # cardno = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light", 11))
    # cardno.place(x=495, y=100)  
    # cardno.insert(0,"Card Number")
    # # cardno.config(state='readonly')

    # # Bind the function to clear the entry when the user starts typing
    # cardno.bind("<FocusIn>", enter_cardno)
    # cardno.bind("<FocusOut>", leave_cardno)

    # Frame(frame,width=295,height=2,bg="black").place(x=490,y=127)

    Button(frame,width=39,pady=7,text="Submit", bg="#57a1f8",fg="white",border=0, command=pay).place(x=280,y=280)
    window.mainloop()

# payment_page()