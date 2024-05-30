import re
def password_checker(user):
    min_len = 12
    count = 0
    has_digit = True
    has_uppercase = True
    has_lowercase = True
    has_special_char = True

    if len(user) < min_len:
        return False, (f"The password must contain {min_len} characters")

    if has_digit and not any(char.isdigit() for char in user):
        return False, (f"The password must contain a digit")

    if has_uppercase and not any(char.isupper() for char in user):
        return False, (f"The password must contain an uppercase letter")

    if has_lowercase and not any(char.islower() for char in user):
        return False, (f"The password must contain a lowercase letter")

    if has_special_char and not re.search(r"[!@#$%^&*(),.?\":{}|<>]", user):
        return False, (f"The password must contain a special character")

    return True, ("The password is valid")

def user_input():
    user_run = input("Enter a password: ")
    is_valid, error_message = password_checker(user_run)

    if is_valid:
        print("The password is valid")
    else:
        print(f"Invalid Password: {error_message}")

if __name__ == "__main__":
    user_input()









