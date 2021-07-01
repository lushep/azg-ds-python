

# 1. integers and floats

monthly_sales_flt = [float(x) if str(x).isdigit() else 0.0 for x in monthly_sales]



# 2. strings

months = [x.strip().capitalize() for x in first_months + second_months + third_months]



# 3. booleans

# option 1 - loop

def greater_than_10000_loop(lst):
    output_lst = []
    for x in lst:
        if x > 10000:
            output_lst.append(x > 10000)

    return output_lst

# option 2 - list comprehension

def greater_than_10000(lst):
    return [l > 10000 for l in lst]




# 4. lists and tuples

monthly_sales_tups = [(x, y) for x, y in zip(months, monthly_sales_flt)]



# 5. sets

len(set(monthly_sales_flt))



# 6. dictionaries

monthly_sales_dict = dict(monthly_sales_tups)



# 7. functions

def add_monthly_sales(mnth_dict):
    
    # check whether there are 12 months
    if len(mnth_dict)!=12:
        print("Not using full year!")
        print(f"Months used are: {' '.join(mnth_dict)}")
        
    return sum(mnth_dict.values())



# 8. directories

import os
os.mkdir('monthly sales')



# 9. files

file_path1 = os.path.join("monthly sales", "cleaned monthly sales.txt")
with open(file_path1, "w") as f: 
    for x in monthly_sales_flt:
        f.write(str(x))
        if x == monthly_sales_flt[-1]:
            break
        f.write('\n')