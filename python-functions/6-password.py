def validate_password(password):
    if len(password) < 8:
        False
    elif ' ' in password and not any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) :
        False
    else:
        True 