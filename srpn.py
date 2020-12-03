import random    # imports library to generate random integers
random.seed(0)      # sets seed

def equals():
    print(int(stack[top]))   # prints the value at the top of the stack when '=' inputted

def add(x, y):
    ans = x + y     # adds top 2 values on stack when '+' inputted
    return ans

def subtract(x, y):
    ans = x - y     # 2nd value subtract top value on stack when '-' inputted
    return ans

def multiply(x, y):
    ans = x * y     # multiplies top 2 values on stack when '*' inputted
    return ans

def divide(x, y):
    ans = x / y     # 2nd value divided by top value on stack when '/' inputted
    return ans

def power(x, y):
    ans = x ** y    # 2nd value to the power of top value on stack when '^' inputted
    return ans

def modulo(x, y):
    ans = x % y     # 2nd value modulo top value on stack when '%' inputted
    return ans

# Takes input as parameter if it strts with 0, converted to an decimal number and returned.
def octtodec(x):
    dec = 0     # int, stores final decimal number
    base = 1    # int, stores the multiplier so 8^n
    temp = x    # int, stores the remaining digits
    while temp != 0:
        digit = temp % 10   # int, removes furthest right digit
        temp = int(temp / 10)   # stores digits left
        dec += digit * base     # multiplies digit by 8^n where n is incremented each digit
        base = base * 8     # increments the base from 8^n to 8^(n+1)
    return dec

# takes an operator as a parameter, finds the number of instances of the operator and returns it
def find_operator(operator, expression):
    counter = 0     # int, to hold the number of times the operator is present
    for i in range (0, (len(expression))):  # loop through each element in the array
        if expression[i] == operator:
            counter += 1    # if operator present here, increment counter by 1
    return counter

''' takes the input as a parameter, if comments are present they are deleted, the expression is checked for any
unacceptable characters, generates the random numbers in place of any 'r's, combines any multiple digit integers, and
then performs all of the operations on the values to get a final integer, which is returned'''
def infix(x):
    expression = [str(z) for z in str(x)]   # array, splits each operator or value in expression into elements
    n = 0   # int, count which element of the array the loop is currently on
    found = False # boolean, to stop the loop if the comment is found or if the end of the array is reached
    while found == False:   # loops through each element
        if expression[n] == "#" and expression[n+1] == " " and len(expression)-2 > n: # if start of comment:
            expression = delete_comment(expression, n)  # calls function to delete all elements involved in comment
            found = True    # now stop the loop
        elif len(expression) <= 1 or len(expression)-2 < n:
            found = True    # if end of array is reached, stop loop, there are no comments to delete
        n += 1  # move onto next element

    if expression != []:    # as long as there is still an expression:
        accept = check_accept(expression)   #calls a function to check for unacceptable characters
        if accept == False:
            return False    # returns False, showing there were unacceptable chars
        elif accept == True:
            if len(expression) > 0:   # if all chars acceptable and the expression isn't empty
                if expression[len(expression)-1] == "=":
                    print(expression[len(expression)-2])    # if the last element is '=' then remove it and print the
                    expression.remove(expression[len(expression)-1])    # element before it
            for b in range(0, (len(expression))):
                if expression[b] == "r":    # replace any instances of 'r' witha  random integer
                    expression[b] = random.randint(0, 2147483648)
            k = 0   # int, to count which element in array is current
            end = False     # boolean, to stop loop when end of array reached
            while end == False:
                if expression[k] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and k < (len(expression)):
                    expression[k] = int(expression[k])  # if element is a number, convert it to an integer
                    stop = False    # boolean, to stop loop when end of array reached
                    m = k   #temporarily store which element was current
                    while stop == False and m < (len(expression)-1):
                        if expression[m + 1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            num = str(expression[m]) + str(expression[m+1])     # if the next element is also an
                            expression[m] = num     # integer, combine them
                            del expression[m+1]     # delete the original second integer in a row
                        else:
                            stop = True     # stop loop if end of array reached
                if k == (len(expression)-1):
                    end = True      # stop loop if end of array reached
                k += 1  # increment k to move onto next element
            index = len(expression) - 1     # int, holds highest index of expression
            if expression[index] in ['^','*','+','-','/']:
                del expression[index]   # if its an operator, delete it and print stack underflow
                print("Stack Underflow")
            counter = find_operator("^", expression)    # counts instances of operator in expression
            for j in range(0, counter):     # for each instance
                i = expression.index("^")   # get the index
                ans = power(int(expression[i - 1]), int(expression[i + 1]))     # and perform the operation
                expression[i - 1] = ans     # store the result at the smallest index involved
                expression = reformat(expression, i)    # delete void elements
            counter = find_operator("*", expression)    # repeated as above for each operator
            for j in range(0, counter):
                i = expression.index("*")
                ans = multiply(int(expression[i - 1]), int(expression[i + 1]))
                expression[i - 1] = ans
                expression = reformat(expression, i)
            counter = find_operator("/", expression)
            for j in range(0, counter):
                i = expression.index("/")
                ans = divide(int(expression[i - 1]), int(expression[i + 1]))
                expression[i - 1] = ans
                expression = reformat(expression, i)
            counter = find_operator("+", expression)
            for j in range(0, counter):
                i = expression.index("+")
                ans = add(int(expression[i - 1]), int(expression[i + 1]))
                expression[i - 1] = ans
                expression = reformat(expression, i)
            counter = find_operator("-", expression)
            for j in range(0, counter):
                i = expression.index("-")
                ans = subtract(int(expression[i - 1]), int(expression[i + 1]))
                expression[i - 1] = ans
                expression = reformat(expression, i)
            ans = expression.pop()  # gets result from expression and returns it
            return ans
    else:
        return expression   # or returns empty stack if it is empty

# takes the expression and current index of operator and deletes now void elements
def reformat(expression, index):
    del expression[index]
    del expression[index]
    return expression

# takes x as a parameter and appends it to the stack at the top
def push(x):
    stack.append(x)

# takes the highest index in stack and removes the element, returning it
def pop(top):
    if len(stack) >= 1:
        item = stack.pop(top)
        top -= 1
        return item
    else:
        pass    # ignore if stack empty

# finds the highest index in stack and returns it
def findtop():
    top = (len(stack)) - 1
    return top

# prints each element in stack, unless it's empty
def printstack():
    n = findtop()
    if n == -1:
        print(-2147483648)
    else:
        for i in range(0, n+1):
            print(int(stack[i]))

# takes expression as  a parameter and checks for unacceptable characters
# returns true if all chars acceptable, false otherwise
def check_accept(expression):
    check = 0   # int, should match length of array at the end if all chars are acceptable
    for k in range(0, (len(expression))):
        if expression[k] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '^', '*', '+', '-', '/', '=', 'r']:
            check += 1  # if current character acceptable, increment check
    if check != len(expression):
        return False    # if check doesn't equal length of array, unacceptable characters are present so return false
    else:
        return True     # return true if all chars acceptable

# takes expression and index of '#' as parameters, returns expression without comment
def delete_comment(expression, n):
    comment = True  # boolean, current element is within comment
    p = n   # int, holds index of '#' temporarily
    if expression[p-1] == " ":
        del expression[p]   # if there's a space before the '#', delete it
        p -= 1  # decrement current index as an element has been removed
    while comment == True:  # while between '#'s
        if p < len(expression)-1:
            if expression[p] == " " and expression[p + 1] == "#":   # if end of comment
                del expression[p]   # delete the space and the '#'
                del expression[p]
                if p < len(expression):
                    if expression[p] == ' ':
                        del expression[p]   # if space after '#' at end, delete it
                comment = False     # end loop as comment ended

            else:
                del expression[p]   # otherwise delete the current element as it is in the comment
            if len(expression) == 0:
                comment = False    # ignore if array empty
        else:
            del expression[p]
            comment = False
    return expression

# takes y as parameter, returns true if number is negative, false if not
def is_negative(y):
    if y[0] == "-" and y[1] == "0":
        del y[0]    # deletes '-' if present
        return True
    else:
        return False

# takes y as parameter if it is an octal number, returns decimal number
def is_octal(y):
    del y[0]    # delete 0 at front
    maxi = len(y)   # int, length of array
    x = 0   # int,  holds octal number as integer
    for j in range((maxi - 1), -1, -1):
        x = x + (int(y[j]) * (10 ** ((maxi - 1) - j)))  # for each element, convert it to int and add it and its base
    if len(y) == 1 and int(y[0]) >= 8:  # of 10 to the integer x
        if negative == True:
            x = x - 2 * x   # if it was negative, convert it to its negative
    else:
        valid = True    # boolean, true if octal value valid
        for i in range(0, maxi - 1):
            if int(y[i]) >= 8:  # if any char is >7, not a valid octal, unless it was only one digit then it is decimal
                valid = False
        if valid == True:
            x = octtodec(int(x))    # calls function to convert octal to decimal
            if negative == True:
                x = x - 2 * x   # if octal was negative, convert it to its negative
    return x

running = True  # boolean, to keep program loop on
stack = []  # array, intiialise stack to store all answers and values
top = -1    # int, to keep track of top element in stack, -1 if empty
infinite = False    # boolean, true if infinite loop should be entered
while running:
    if infinite == True:    # enter infinite loop for non ascii chars
        loop = -1
        while loop < 0:
            loop -= 1
    result = True   # boolean, true if there si a result to push onto the stack
    fail = 0    # int, 1 if failed an if, 0 if it didn't fail it
    x = input()     # user input, can be int, str
    original = x    # same type as x, to hold original
    ans = False
    ''' loops through each accepted operator, if the stack has enough elements, it perform the operation'''
    if x == "+":
        if findtop() <= 0:
            print("Stack underflow")
        else:
            y = float(stack.pop())
            x = float(stack.pop())
            x = add(x, y)
    elif x == "-":
        if findtop() <= 0:
            print("Stack underflow")
        else:
            y = float(stack.pop())
            x = float(stack.pop())
            x = subtract(x, y)
    elif x == "*":
        if findtop() <= 0:
            print("Stack underflow")
        else:
            y = float(stack.pop())
            x = float(stack.pop())
            x = multiply(x, y)
    elif x == "/":
        if findtop() <= 0:
            print("Stack underflow")
        else:
            y = float(stack.pop())
            x = float(stack.pop())
            if y == 0:
                print("Divide by 0.")
                push(x)
                push(y)
            else:
                x = divide(x, y)
    elif x == "^":
        if findtop() <= 0:
            print("Stack underflow")
        else:
            y = float(stack.pop())
            x = float(stack.pop())
            x = power(x, y)
    elif x == "%":
        if findtop() <= 0:
            print("Stack underflow")
        else:
            y = float(stack.pop())
            x = float(stack.pop())
            x = modulo(x, y)
    elif x == "d":  # input d calls a funtion to print all elements in stack
        printstack()
        result = False  # no result to push
    elif x == "r":  # input r generates random number
        x = random.randint(0, 2147483648)
    elif x == "":   # ignore blank inputs
        result = False  # no result to push
    else:
        fail = 1    # failed all previous tests
        try:    # covers octals and integers, but would throw an error if not integers so in try
            negative = False
            y = [str(z) for z in str(x)]
            negative = is_negative(y)   # is it negative?
            if y[0] == "0":
                x = is_octal(y)     # if starts with 0 it's an octal
            else:
                x = int(x)  # if not octal then integer?
            fail = 0    # didn't fail, skip all other tests

        except ValueError:
            fail = 1    # failed all previous tests

        if fail == 1:
            if x != "=":    # if input isn't '='
                original = x    # set original to equal x
                x = infix(x)  # calls function to process it as infix, but covers comments as well
                fail = 0    # didn't fail so skip all other tests
                result = True
                if x != False:
                    if x == []:
                        result = False  # if the expression is now empty, no result to push and didn't fail
                        fail = 0
                else:
                    fail = 1
    if x == [] or result == False:
        pass    # if expression is now empty
    elif fail == 0 and result == True:
        push(x)     # if a test was passed and there is a result to push, push it
    if fail == 1 and x != "=":  # if all tests failed and x isn't '='
        for i in range(0, (len(original))):     # checks for unacceptabe chars
            if original[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '^', '*', '+', '-', '/', '=']:
                if original[i] in ['£']:    # non ascii chars enter infinite loop
                    infinite = True
                else:   # if unacceptable char found, print it with this message
                    print("Unrecognised operator or operand ", original[i])

    top = findtop()     # calls function to find index of top element on stack
    if top != -1:
        if stack[top] in ['^','*','+','-','/']:
            stack.pop()     # if the last element is an operator but there aren't enough operands, remove it
        top = findtop()
    if top != -1:
        if stack[top] >= 2147483647:
            stack[top] = 2147483647    # if top element is greater than the highest possible value, make it equal to it
        elif stack[top] <= -2147483648:
            stack[top] = -2147483648    # if top element is lower than the lowest possible value, make it equal to it
    if x == "=":
        equals()    # if input was '=', calls function to print top element on stack
