import re


def binary(nums):
    return re.match(r'[01]', nums)


def binary_even(nums):
    return re.match(r'[01]*[0]$', nums)


def hex(text):
    return re.match(r'^[0-9A-F]+$', text)


def word(text, *args):
    return re.match(r'^\w*[-]*[a-z]+$', text)
