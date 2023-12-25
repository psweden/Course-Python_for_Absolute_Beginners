# Defining a funtion
# Python most have four space, or 'tab' to now that is a function se line 4 in the function.
def function_name(parameter):
    print(parameter + 2)


# Calling function "metodanrop"
# function parameters
# function_name(8)

# Variable
first_str = "The number "

# new function
def function_name2(p1, p2, p3):
    print(p1 + str(p2) + p3)

# Multiple parameters
function_name2(first_str, 5, " is an integer.")

# default parameters
def default_example(num1=7, num2=8):
    print(num1 * num2)

# Calling default functions
default_example()

# return
def default_example2(num1=7, num2=8):
    return num1 * num2

product = default_example2(2)

# Using return with expressions
print(default_example2() + 44)
