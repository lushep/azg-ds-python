import string

def get_alphabet_values(*args):
    alphabet = string.ascii_lowercase
    # or without import string: alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    return {a: alphabet[a%26-1] for a in args}

get_alphabet_values(1, 4, 5, 6, 26)