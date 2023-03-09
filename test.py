import re

def is_valid_email(email):
    """
    Returns True if the email is a valid format, False otherwise.
    """
    if not email:
        return False

    # Regular expression pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Validate email using regular expression
    if re.match(pattern, email):
        return True
    else:
        return False

email = input("enter email: ")

print(is_valid_email(email))

