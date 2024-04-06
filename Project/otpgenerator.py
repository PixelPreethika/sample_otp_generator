
import hashlib
import time

import pyotp

import qrcode
import tkinter as tk


def generate_otp(username):
    # Extract first two characters of username
    username_prefix = username[:2]

    # Extract last two digits of the year from DOB
    # year = dob.split('-')[0][-2:]

    # Get current time formatted as HHMM
    current_time = time.strftime("%H%M%S")

    # Concatenate components to generate OTP
    otp_data = username_prefix + current_time
    print("Generated OTP:", otp_data)
    return otp_data
    




def generate_user_otp(username):
    print("Your name is:", username)
    # Concatenate username and current time
    data = username[:2] +time.strftime("%H%M%S")
    print("Your OTP is:", data)
    return data
def generate_otp(ip_address,user_otp):
    print("generate otp using:", ip_address,user_otp)
    # Concatenate IP address, username, and current time
    data = ip_address + user_otp
    print("Your final OTP is:", user_otp)
    # Generate OTP by hashing the concatenated data
    otp = hashlib.sha256(data.encode()).hexdigest()
    print("Your hashed OTP is:", user_otp)
    return otp

def verify_user_input(ip_address, entered_data, stored_otp):
    print("Your OTP compared using :", ip_address, entered_data, stored_otp)
    # Concatenate IP address and entered data
    data = ip_address + entered_data
    print("Your entered OTP is:", data)
    # Generate OTP by hashing the concatenated data
    hashed_input = hashlib.sha256(data.encode()).hexdigest()
    print("Your entered hash OTP is:", hashed_input)
    return hashed_input == stored_otp


def generate_secret_key():
    # Generate a random secret key
    secret_key = pyotp.random_base32()
    return secret_key

def generate_qr_code(secret_key, account_name):
    # Generate the URI for the QR code
    uri = pyotp.totp.TOTP(secret_key).provisioning_uri(account_name, issuer_name="YourApp")

    # Create a QR code instance
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

    # Add data to the QR code
    qr.add_data(uri)

    # Make the QR code
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    return img, secret_key

def verify_otp(secret_key, entered_otp):
    # Create a TOTP object using the secret key
    totp = pyotp.TOTP(secret_key)
    print(secret_key ," : ", entered_otp)
    print(totp)
    # Verify the entered OTP
    return totp.verify(entered_otp)