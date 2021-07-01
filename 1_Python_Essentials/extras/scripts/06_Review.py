# ---
# jupyter:
#   jupytext:
#     formats: ipynb,scripts//py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Python Essentials Review
#
# Using the knowledge from the Python Essentials notebooks, answer the following questions.
#
# If there is a variable for you to use make sure you run that cell first!

# # Review A

my_new_list = [3,41, 'ee', 2.43, 3.41, "55", [51, 72, 39]]

# ### 1) Write code to print the number 72 from of the list








# ### 2) Write code to get a new list that contains only numbers







# ### 3) Write a function that takes a list, extracts all the numbers, then returns them in order (bonus: include an option to specify whether the order is ascending or descending)




# # Review B
#
# ## Data types
#
# ### 1. integers and floats
#
# Clean the list of yearly sales data so that it contains only floats

monthly_sales = [12000, 13400, '17000', 'no_sales', 12000, 17000, 14555,444, 15456, 17238, 17238, 12638 ]






# ### 2. strings
#
# Create one list of months called "months of the year", ensure they all have capital letters, are in order, and no months are missing.

first_months = ['january', ' february', 'march', 'april', 'may']
second_months = ['May', 'June', 'August', 'July', ' September']
third_months = ['October', 'November', 'December']




# ### 3. booleans
#
# Build a function that takes a list as input, loops through the list
# and then prints out a bool (true or false) if the values in list are greater than 10000.
#
# Run the function on the CLEANED monthly sales list



# ## Containers
#
# ### 4. lists and tuples 
#
# Create a new list that contains tuples of the month and monthly sales, e.g. [(January, 12000.0), (February, 13400.0)]



# ### 5. sets
# How many months have a monthly sales value that has not been seen before?



# ### 6. dictionaries
#
# create a monthly sales dictionary, e.g. can look up monthly sales for January like so
# ```python
# sales_dict['January']
# ```



# ## Functions
# ### 7. functions 
#
# - Create a function that adds up monthly sales
# - bonus: it should be able to work for any number of months: e.g. first 6 months of the year
# - bonus: if it is not giving the total for the whole year, it should print and explain what months it is being used for



# ## Files
#
# ### 8. directories
# Create a directory called monthly sales.



# ### 9. files
# Save the cleaned monthly sales as a `.txt` file in the monthly sales directory.
# Ensure that each month's sales is on a new line.


