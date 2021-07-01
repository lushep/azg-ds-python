# sets 
list(set(list1) ^ set(list2))

# list comprehension
[x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]

# for loop
answer = []

for one in list1:
    if one not in list2:
        answer.append(one)
for two in list2:
    if two not in list1:
        answer.append(two)
            
answer