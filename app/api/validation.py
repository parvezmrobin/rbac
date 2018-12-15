from typing import Union


def required(fields: Union[list, dict], data: dict) -> dict:
    """
    Performs a 'required' validation
    :param fields: fields that are required.
    :param data: containing the field values
    :return: fields that are not in data
    """
    errors = {}
    for field in fields:
        if not (field in data and data[field]):
            if type(fields) == list:
                errors[field] = f"{field} is required"
            elif type(fields) == dict:
                errors[field] = f"{fields[field].capitalize()} is required"
    return errors
