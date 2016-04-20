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
    count = kwargs.get('count')
    results = re.findall(r'\w*[-]*[a-zA-Z]+', text)
    if kwargs:
        return count == len(results)
    else:
        return results != []
