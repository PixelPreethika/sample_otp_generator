import hashlib
import time

def generate_dob_otp(username, dob):
    # Extract first two characters of username
    username_prefix = username[:2]

    # Extract last two digits of the year from DOB
    year = dob.split('-')[0][-2:]

    # Get current time formatted as HHMM
    current_time = time.strftime("%H%M")

    # Concatenate components to generate OTP
    otp_data = username_prefix + year + current_time
    print("Generated OTP:", otp_data)
    return otp_data

# # Example usage
username = "john_doe"
# dob = "1990-01-01"  # Date of birth format: YYYY-MM-DD


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

# otp = generate_otp(username)