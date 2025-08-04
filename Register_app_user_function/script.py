from python_functions import validate_name, validate_email, validate_password

def validate_user(name, email, password):
    """Validate the user name, email and password.

    Args:
        name (string): Name that we're attempting to validate.
        email (string): Email address that we're attempting to validate.
        password (string): Password that we're attempting to validate.

    Returns:
        bool: Returns True if all validation checks pass.

    Raises:
        ValueError: If any validation check fails.
    """
    if validate_name(name) == False:
        raise ValueError("Please make sure your name is greater than 2 characters!")

    if validate_email(email) == False:
        raise ValueError("Your email address is in the incorrect format, please enter a valid email.")

    if validate_password(password) == False:
        raise ValueError("Your password is too weak, ensure that your password is greater than 8 characters, "
                         "contains a capital letter and a number.")

    return True

def register_user(name, email, password):
    """Attempt to register the user if they pass validation.

    Args:
        name (string): Name of the user.
        email (string): Email address of the user.
        password (string): Password of the user.

    Returns:
        dict or bool: Returns a dictionary with the user details if validation is successful,
        or False if the validation fails.
    """
    try:
        validate_user(name, email, password)
        print("Script started computting...")
    except:
        return False

    user = {
        "name": name,
        "email": email,
        "password": password
    }

    return user

print(register_user("Shashank","suryaneupane0427@gmail.com","Shashank0427@"))


