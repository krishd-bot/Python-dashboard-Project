# main.py
from auth import signUp       # signup.py se import
from dashboard import dashboard      # Login.py se import
from Login import Login  

# Step 1: Signup
username, password = signUp()  # Signup se values receive

# Step 2: Login (only if signup successful)
if username and password:
    success = Login(username, password)  # Login function call

    # Step 3: Dashboard only if login successful
    dashboard(success)

