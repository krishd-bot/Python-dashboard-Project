# Login.py
def Login(username, password):
    u = input("Enter username: ")
    p = input("Enter password: ")

    if u == username and p == password:
        print("Login Successfully dude! ")
        return True
        
    else:
        print("Invalid Login dude! ")
        return False
