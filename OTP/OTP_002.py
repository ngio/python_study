#Alphanumeric OTP:

import random
import string

def generate_alphanumeric_otp(length=6):
    """
    Generates an alphanumeric OTP of the given length.
    """
    if length <= 0:
        raise ValueError("Length must be greater than zero")
    characters = string.ascii_letters + string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

# Example usage
otp = generate_alphanumeric_otp(8)
print(f"Your Alphanumeric OTP is: {otp}")

    