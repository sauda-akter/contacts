def validate_name(name):
    if not isinstance(name, str) or not name.strip():
        return False, "The contact's name must be a non-empty string."
    return True, ""

def validate_phone(phone):
    if not phone.isdigit():
        return False, "The phone number must be an integer."
    return True, ""
