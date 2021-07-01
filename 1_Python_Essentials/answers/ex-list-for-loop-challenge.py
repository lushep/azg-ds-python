answer_list = []

for item in this_list:
    if str(item).replace('.','').isdigit():
        answer_list.append(item)
        
answer_list