import random

def signUp():
    username = input("Enter username : ")
    number = input("Enter your number : ")
    password = input("Enter password : ")
    cPassword = input("Confirm Password : ")
    
    special = '!@|~`#$%^&*(_+=>.),/#'
    has_digit = any(ch.isdigit() for ch in username)
    pass_digit = any(d.isdigit() for d in password)

    # Username validation
    if len(username) < 6 or not has_digit:
        print("Invalid username! Please Enter a valid username !")
        return None, None   # exit if invalid
    else:
        print("Username : ", username)

    # Password validation
    if len(password) < 8 or not pass_digit or not any(ch in special for ch in password):
        print("Password is invalid you'll need to enter a valid password !")
        return None, None
    else:
        print("Password : ", password)

    # Confirm password
    if cPassword != password:
        print("Your password did not match with your original password ! Please enter valid password !")
        return None, None
    else:
        print("Confirm Password : ", cPassword)
        print("Matched with original!")

    # Number validation and OTP
    if len(number) != 10 or not number.isdigit():
        print("Enter a valid phone number !")
        return None, None
    else:
        print("Number : ", number)
        Otp = random.randint(1000,9999)
        print("OTP : ", Otp)
        try:
            with open('otp.txt', 'a') as file:
                file.write(number + " : " + str(Otp) + "\n")
                print("OTP saved successfully !")
        except Exception as e:
            print("OTP didn't save:", e)

    # OTP verification
    userOtp = input("Enter OTP: ")
    with open('otp.txt', 'r') as f:
        verified = False
        for line in f:
            if userOtp in line:
                print("OTP Verified !")
                verified = True
                break
        if not verified:
            print("OTP did not match !")
            return None, None

    print("Sign Up successful ! ")

    #  THIS IS THE IMPORTANT RETURN
    return username, password

# signUp()
