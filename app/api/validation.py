def required(fields, data):
    errors = {}
    for field in fields:
        if not (field in data and data[field]):
            errors[field] = f"{field.capitalize()} is required"
    return errors
