import re


def phone_numbers(text):
    return re.findall(r'\(\d{3}\)\s\d{3}-\d{4}', text)
