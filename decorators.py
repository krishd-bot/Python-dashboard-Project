def is_Login_Required(func):

    def wrapper(is_Login , *args , **kwargs):
        if is_Login :
            return func(*args , **kwargs)
        else :
            print("Access denied ! Please login first ")

    return wrapper