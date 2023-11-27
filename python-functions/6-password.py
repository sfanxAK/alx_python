def validate_password(password):
    if ' ' in password:
        return False
    if len(password) < 8:
        return False
    
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)

    return has_lower and has_upper and has_digit