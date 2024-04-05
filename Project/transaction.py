import tkinter as tk
from tkinter import *
from tkinter import ttk
from database import transaction

def transaction_page(login,home,loggedin_user):
    def back():
        root.destroy()
        home(login,loggedin_user)
    def load_data():
        transactions = transaction(loggedin_user)
        # Insert data into the treeview
        for data in transactions:
            tree.insert("", tk.END, values=data)

    # Create main window
    root = tk.Tk()
    root.title("Transaction History")
    root.geometry("925x500+300+200")
    root.configure(bg="#fff")
    root.resizable(False,False)

    # Create Treeview widget
    tree = ttk.Treeview(root, columns=("Date", "Phone", "Type", "Amount"), show="headings")

    # Define column headings
    tree.heading("Date", text="Date")
    tree.heading("Phone", text="Phone")
    tree.heading("Type", text="Type")
    tree.heading("Amount", text="Amount")

    # Set column widths
    tree.column("Date", width=100)
    tree.column("Phone", width=150)
    tree.column("Type", width=100)
    tree.column("Amount", width=100)

    # Set style
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="#f0f0f0", foreground="black")
    style.map("Treeview", background=[('selected', '#0078d7')])

    # Add a vertical scrollbar
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Load data into the treeview
    load_data()

    # Pack the treeview
    tree.pack(fill="both", expand=True)
    Button(width=15,pady=7,text="Submit", bg="#57a1f8",fg="white",border=0,command=back).place(x=800,y=450)
    # Run the application
    root.mainloop()