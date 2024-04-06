from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from otpgenerator import generate_otp
from plyer import notification
from database import card_details
import os


def addcard_page(login,home,loggedin_user):
    window = Tk()
    window.title("Cards")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False,False)
            
    def enter_cardno(event):
        if cardno.get() == 'Card Number':
            cardno.delete(0, "end")
    def leave_cardno(event):
        print(cardno.get())
        if cardno.get() == '':
            cardno.insert(0,"Card Number") 
            
    def enter_expdt(event):
        if expdt.get() == 'Expiry Date':
            expdt.delete(0, "end")

    def leave_expdt(event):
        if expdt.get() == '':
            expdt.insert(0, "Expiry Date") 

    def enter_cvv(event):
        if cvv.get() == 'CVV':
            cvv.delete(0, "end")

    def leave_cvv(event):
        if cvv.get() == '':
            cvv.insert(0, "CVV") 

            
    def addcard():
        card = cardtype.get()
        num = cardno.get()
        dt = expdt.get()
        cv = cvv.get()
        if (card != "Select Card Type") and (num != "Card Number") and (dt != "Expiry Date") and (cv != "CVV"):
            card_details(card,num,dt, cv,loggedin_user)
            messagebox.showinfo("Success", "Card Added Successfully!")
            window.destroy()
            home(login,loggedin_user)
        else:
            messagebox.showerror("Invalid", "Please fill up all the fields")

    frame = Frame(window, height=410,width=830, bg="white")
    frame.place(x=50, y=40)

    heading = Label(frame, text="Add Card", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(relx=0.5, rely=0.05, anchor=CENTER)

    cardtype = Combobox(frame, width=35, state="readonly", font=("Microsoft YaHei UI Light", 11))
    cardtype['values'] = ("Select Card Type", "Debit Card", "Credit Card")
    cardtype.current(0)  # Select the default option
    cardtype.place(x=25, y=100)

    cardno = Entry(frame, width=35, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    cardno.place(x=30, y=170)
    cardno.insert(0, "Card Number")

    cardno.bind("<FocusIn>", enter_cardno)
    cardno.bind("<FocusOut>", leave_cardno)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=198)


    expdt = Entry(frame, width=35, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light", 11))
    expdt.place(x=495, y=100)  
    expdt.insert(0,"Expiry Date")

    # Bind the function to clear the entry when the user starts typing
    expdt.bind("<FocusIn>", enter_expdt)
    expdt.bind("<FocusOut>", leave_expdt)

    Frame(frame,width=295,height=2,bg="black").place(x=490,y=127)


    cvv = Entry(frame, width=35, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light", 11))
    cvv.place(x=495, y=170)  
    cvv.insert(0,"CVV")

    cvv.bind("<FocusIn>", enter_cvv)
    cvv.bind("<FocusOut>", leave_cvv)
    Frame(frame,width=295,height=2,bg="black").place(x=490,y=198)


    Button(frame,width=39,pady=7,text="Submit", bg="#57a1f8",fg="white",border=0, command=addcard).place(x=280,y=280)
    window.mainloop()