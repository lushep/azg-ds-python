#
#
# 1) Write code to print the number 72 from of the list

my_new_list[-1][1]



# 2) Write code to get a new list that contains only numbers

# option 1: for loops

new_list = []

for x in my_new_list:
    if type(x) in [float, int] or str(x).isdigit():
        new_list.append(x)

print(new_list)

# option 2: list comprehension
[x for x in my_new_list if type(x) in [float, int] or str(x).isdigit()]



# 3) Write a function that takes a list, extracts all the numbers, then returns them in order (bonus: include an option to specify whether the order is ascending or descending)

def take_list(l):
    only_numbers = [float(x) for x in l if type(x) in [float, int] or str(x).isdigit()]
    return sorted(only_numbers)

take_list(my_new_list)
