from decorators import is_Login_Required

@is_Login_Required
def dashboard():
    print("Dashboard successfully ! Verified")
    print("You can now access tasks, games, etc.")
    