# exercise 33-34 'function with no parameters'
def hello_world_printer():
    print("hello world")

# functions-calling
# hello_world_printer()

# exercise 35-36 'function with 1 parameter'
def name_printer(text):
    print(text)

# myVariableTextInput = input("Please enter something: ")
# functions-calling
# name_printer(myVariableTextInput)


# exercise 37-38 'function with 1 parameter'

length = int(input("Enter an integer that represents length: "))
width = int(input("Enter an integer that represents width : "))
height = int(input("Enter an integer that represents height : "))

def prism_vol(l, w, h):
    return l * w * h

print("The volume of the rectangular prism is " + str(prism_vol(length, width, height)) + " cubic feet.")
