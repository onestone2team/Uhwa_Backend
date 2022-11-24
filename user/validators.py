import re

def emailvalidator(email):
    is_email = re.compile(r'^[a-zA-Z0-9+-_.]+@([a-zA-Z0-9-]{4,})+\.[a-zA-Z0-9-.]+$')
    if not is_email.fullmatch(email):
        return False
    return True

def passwordvalidator(password, password_check):
    print(password, password_check)
    if password == '':
        return False
    else:
        if password != password_check:
            return False
        else:
            return True

def phonevalidator(phone):
    is_phone = re.compile(r'\d{3}-\d{3,4}-\d{4}')
    if not is_phone.fullmatch(phone):
        return False
    return True