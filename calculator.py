# A practice calculator in python

# Create functions to perform operation
def mult(num1, num2):
    print "We will now multiple %i times %i" % (num1, num2)
    product = num1 * num2
    return product

def div(num1, num2):
    quotient = num1 / num2
    return quotient

def add(num1, num2):
    numsum = num1 + num2
    return numsum

def sub(num1, num2):
    diff = num1 - num2
    return diff

def numselect(operation):
    print "Which two numbers do you wish to %s?" % operation
    num1 = int(raw_input("Number 1: \n>"))
    num2 = int(raw_input("Number 2: \n>"))
    return (num1, num2)

def redo():
    redoans = raw_input("Would you like to peform another operation? Y/N \n>")
    if redoans == "Y":
        i = 1
    else:
        i = 2
    return i

print "Welcome to my Python Calculator!"

i = 1

while i == 1:

    operation = raw_input("What operation would you like to perform? \n>")

    if operation == "Multiply" or operation == "multiply":
        (num1, num2) = numselect(operation)
        answernum = mult(num1, num2)
        print "The product of %i and %i is %i" % (num1, num2, answernum)
        i = redo()
