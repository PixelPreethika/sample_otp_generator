from tkinter import *
from tkinter import messagebox
from otpgenerator import generate_otp
from plyer import notification
from tkinter.ttk import Combobox
from database import wallet, check_cvv,cards
from flask import  session
import os


def wallet_page(login,home,loggedin_user):
    window = Tk()
    window.title("Wallet")
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
    def enter_amt(event):
        if amt.get() == 'Amount':
            amt.delete(0, "end")

    def leave_amt(event):
        if amt.get() == '':
            amt.insert(0, "Amount") 

    def enter_cvv(event):
        if cvv.get() == 'CVV':
            cvv.delete(0, "end")

    def leave_cvv(event):
        if cvv.get() == '':
            cvv.insert(0, "CVV") 
    def addamt():
        card_type = cardtype.get()
        card_no = cardno.get()
        cv = cvv.get()
        amount = amt.get()
        if (card_type != "Select Card Type") and (card_no != "Card Number") and (cv != "CVV"):
            card_cvv = check_cvv(card_type, card_no,cv,loggedin_user)
            # session_cvv = card_cvv
            if(card_cvv != None):
                wallet(amount,loggedin_user)
                messagebox.showinfo("Success", "Amount Added Successfully!")
                window.destroy()
                home(login,loggedin_user)
            else:
                messagebox.showerror("Invalid", "Something went wrong. Please try again later")
        else:
            messagebox.showerror("Invalid", "Please fill up all the fields")

    frame = Frame(window, height=410,width=830, bg="white")
    frame.place(x=50, y=40)

    heading = Label(frame, text="Add Amount", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(relx=0.5, rely=0.05, anchor=CENTER)

    amt = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light", 11))
    amt.place(x=30, y=100)  
    amt.insert(0,"Amount")
    # amt.config(state='readonly')

    # Bind the function to clear the entry when the user starts typing
    amt.bind("<FocusIn>", enter_amt)
    amt.bind("<FocusOut>", leave_amt)

    Frame(frame,width=295,height=2,bg="black").place(x=25,y=127)


    # cardtype = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light", 11))
    # cardtype.place(x=30, y=170)  
    # cardtype.insert(0,"Card Type")

    # cardtype.bind("<FocusIn>", enter_cardtype)
    # cardtype.bind("<FocusOut>", leave_cardtype)
    # Frame(frame,width=295,height=2,bg="black").place(x=25,y=198)

    cardtype = Combobox(frame, width=35, state="readonly", font=("Microsoft YaHei UI Light", 11))
    cardtype['values'] = ("Select Card Type", "Debit Card", "Credit Card")
    cardtype.current(0)  # Select the default option
    cardtype.place(x=22, y=170)

    cardno = Combobox(frame, width=35, state="readonly", font=("Microsoft YaHei UI Light", 11))
    cardno['values'] = ("Select Card Number", "Card Number 1", "Card Number 2", "Card Number 3")
    cardno.current(0)
    cardno.config(state='disabled')
    cardno.place(x=490, y=100)  

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


    cvv = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light", 11))
    cvv.place(x=495, y=170)  
    cvv.insert(0,"CVV")

    cvv.bind("<FocusIn>", enter_cvv)
    cvv.bind("<FocusOut>", leave_cvv)
    Frame(frame,width=295,height=2,bg="black").place(x=490,y=198)


    Button(frame,width=39,pady=7,text="Submit", bg="#57a1f8",fg="white",border=0, command=addamt).place(x=280,y=280)
    window.mainloop()

# wallet_page()