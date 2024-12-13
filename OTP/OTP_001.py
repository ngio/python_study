import random

def generate_otp(length=6):
    """
    Generates a numeric OTP of the given length.
    Default length is 6.
    """
    if length <= 0:
        raise ValueError("Length must be greater than zero")
    otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return otp

# Example usage
otp = generate_otp(6)
print(f"Your OTP is: {otp}")
