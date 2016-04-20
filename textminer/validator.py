import re


def binary(nums):
    return re.match(r'[01]', nums)


def binary_even(nums):
    return re.match(r'[01]*[0]$', nums)


def hex(text):
    return re.match(r'^[0-9A-F]+$', text)


def word(text):
    return re.match(r'^\w*[-]*[a-z]+$', text)


def words(text, **kwargs):
    results = re.findall(r'\w*[-]*[a-zA-Z]+', text)
    if kwargs:
        return kwargs.get('count') == len(results)
    else:
        return results != []


def phone_number(nums):
    return re.match(r'\(*\d{3}\)*[-\s\.]*\d{3}[-\s\.]*\d{4}', nums)
