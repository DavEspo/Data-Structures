# Importing the deque data structure
from collections import deque
# Function that calculates an expression using deques
def Calculator(Input):
    # Sets up a deque, a number, and a boolean value
    Stack = deque()
    Num = 0
    NumVal = False
    # Test case where the input is empty
    if len(Input) == 0:
        print("Nothing in Input")
        return
    # Test case where the input is too short
    if len(Input) <= 4:
        print("Input is too short")
        return
    # Loop that goes through each element in the input expression and does the steps accordingly
    for Element in Input:
        # Step done when the number in the element is a 0 so that a bunch of 0's don't get put into the deque
        if Element == 0:
            NumVal = True
        # Step done when the element in the expression is a space
        if Element == " ":
            # Places the number on the stack if the boolean value is True
            if NumVal:
                Stack.append(Num)
            # Resets the boolean value back to False and the number to 0
            NumVal = False
            Num = 0
            continue
        # Step done when the element is a number
        # Useful to process 2 or more digit numbers
        elif Element.isdigit():
            Num = (Num * 10) + int(Element)
            NumVal = True
        # Step done when the element is an operator that is not '+'
        elif Element == '-' or Element == '*' or Element == '/':
            # Puts the value in the deque as a negative number
            if Element == '-':
                Stack.append(-Stack.pop())
                continue
            # Stores the top 2 numbers on the deque to op1 and op2
            op1, op2 = Stack.pop(), Stack.pop()
            # Puts the resulting value of op2 * op1 in the deque
            if Element == '*':
                Stack.append(op2 * op1)
            # Puts the resulting value of op2 / op1 in the deque
            elif Element == '/':
                Stack.append(op2 / op1)
    # Returns the sum of the numbers in the stack
    return sum(Stack)
# String that contains a math expression in post-fix notation
expression = "3 5 + 1 - 4 * 3 - 4 +"
# Calls the Calculator function with the expression as the input
print(Calculator(expression))

# The time complexity is O(n) because the loop goes through every element in the input expression
# The space complexity is O(n) because the deque could at worst be the same length as the input expression