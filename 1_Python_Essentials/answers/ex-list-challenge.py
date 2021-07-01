# step one: A string all lower case & no punctuation:
eg_string3 == eg_string3[::-1]

# step two: remove punctuation (' ' & '.') and make lower case
new_string = eg_string3.replace(' ', '').replace('.','').lower()
new_string == new_string[::-1]