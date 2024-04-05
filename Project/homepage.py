import tkinter as tk
from tkinter import *
import requests
from tkinter import PhotoImage
from io import BytesIO
from addcard import addcard_page
from payment import payment_page
from wallet import wallet_page
from transaction import transaction_page
from flask import session 
# from login import loggedin_user
def home_page(login,loggedin_user):
    window = tk.Tk()
    window.title("Home")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False,False)
    print("user :",loggedin_user)
    def add_card():
        window.destroy()
        addcard_page(login,home_page,loggedin_user)
    def wallet():
        window.destroy()
        wallet_page(login,home_page,loggedin_user)

    def payment():
        window.destroy()
        payment_page(login,home_page,loggedin_user)

    def transaction():
        window.destroy()
        transaction_page(login,home_page,loggedin_user)
    
    def logout():
        loggedin_user = None
        print("user is : ", loggedin_user)
        window.destroy()
        login()
    # image = Image.open("add-card.png")  # Replace "add_card.png" with your image file path
    # photo = ImageTk.PhotoImage(image)
    addCard = PhotoImage(file="add-card.png")
    walletimg = PhotoImage(file="wallet-icon.png")
    paymentimg = PhotoImage(file="payment.png")
    history = PhotoImage(file="transaction-history.png")
    logoutimg = PhotoImage(file="log-out.png")

    Button(window,padx=25,pady=25, text="Add Card", compound="left", image=addCard, bg="#57a1f8", fg="white", border=0, height=50, width=120, command=add_card).place(x=110,y=100)
    Button(window,padx=25,pady=25, text="Wallet", compound="left", image=walletimg, bg="#57a1f8", fg="white", border=0, height=50, width=120,command=wallet).place(x=380,y=100)
    Button(window,padx=25,pady=25, text="Payment", compound="left", image=paymentimg, bg="#57a1f8", fg="white", border=0, height=50, width=120, command=payment).place(x=650,y=100)
    Button(window,padx=25,pady=25, text="History", compound="left", image=history, bg="#57a1f8", fg="white", border=0, height=50, width=120,command=transaction).place(x=225,y=280)
    Button(window,padx=25,pady=25, text="Logout", compound="left", image=logoutimg, bg="#57a1f8", fg="white", border=0, height=50, width=120, command=logout).place(x=530,y=280)

    window.mainloop()