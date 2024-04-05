from tkinter import Tk, Label, Entry, Button, messagebox, Toplevel
from otpgenerator import generate_otp
from plyer import notification
from homepage import home_page

otp = None  # Initialize OTP variable
def otp_verify(user_name):
    def otpgen():
        global otp
        otp = generate_otp(user_name)
        full_title = "Hello " + user_name + "!"
        full_message = "Your OTP is " + otp
        notification.notify(
            title=full_title,
            message=full_message,
            app_icon=None,
            timeout=60,
            toast=False
        )

    def verify_otp(entry, otp_window):
        entered_otp = entry.get()
        global otp
        if entered_otp == otp:
            messagebox.showinfo("Verification Result", "OTP Verified Successfully!")
            otp_window.destroy()  # Close the OTP verification window
            # home_page()  # Redirect to the home page or perform other actions after successful verification
        else:
            messagebox.showerror("Verification Result", "Invalid OTP!")

    def resend_otp():
        otp = otpgen()

    otp = otpgen()
    otp_window = Toplevel()
    otp_window.title("OTP Verification")
    otp_window.geometry("200x200+300+200")
    
    label = Label(otp_window, text="Enter OTP:")
    label.pack()
    
    otp_entry = Entry(otp_window)
    otp_entry.pack()
    
    verify_button = Button(otp_window, text="Verify OTP", command=lambda: verify_otp(otp_entry, otp_window))
    verify_button.pack()
    
    resend_button = Button(otp_window, text="Resend OTP", command=resend_otp)
    resend_button.pack()
    otp_window.mainloop()

    # Your GUI creation code goes here...
