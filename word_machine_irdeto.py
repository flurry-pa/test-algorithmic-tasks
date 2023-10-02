"""
Codility
Irdeto invites you to take a programming test
https://app.codility.com/

A 'word machine' is a system that performs a sequence of simple operations on a stack of integers.
Initially the stack is empty. The sequence of operation is given as a string.
Operation is separated by single spaces. The following operations may be specified:
- an integer X (from 0 to (2 to the power 20)): the machine pushed X into stack;
- "POP": the machine removes the topmost number from the stack;
- "DUP": the machine pushes a duplicate of the topmost number onto a stack;
- "+": the machine pops the two topmost elements from the stack, adds them together and pushes the sum into the stack;
- "-"  the machine pops the two topmost elements from the stack, subtracts the second from the first (topmost) one and
        pushes the difference into the stack.

After processing all the operations, the machine returns the topmost value from the stack.
The machine processes 20-bit unsigned integers (number from 0 to  (2 to the power 20 -1)).
An overflow in addition or underflow in subtraction causes an error.
The machine also reports an error when it tries to perform an operation that expects more numbers on the stack
than the stack actually contains.
Also, if after performing all the operations, the stack is empty, the machine reports an error
"""
from collections import deque


def solution(string):
    # Define the maximum and minimum values for 20-bit unsigned integers
    lower = 0               # lower bound of the array
    upper = 2 ** 20 - 1     # upper bound of the array
    stack = deque()         # initialize an empty stack
    ops = string.split()    # list of operations

    # Loop through the operations
    for op in ops:
        # If the operation is an integer, push it to the stack
        if op.isdigit():
            stack.append(int(op))

        # If the operation is POP, pop the topmost element from the stack
        elif op == "POP":
            # Check if the stack is not empty
            if stack:
                stack.pop()
            else:
                return -1  # err: stack underflow

        # If the operation is DUP, duplicate the topmost element on the stack
        elif op == "DUP":
            # Check if the stack is not empty
            if stack:
                stack.append(stack[-1])
            else:
                return -1  # err: stack underflow

        # If the operation is +, pop the two topmost elements and push their sum
        elif op == "+":
            # Check if the stack has at least two elements
            if len(stack) >= 2:
                x = stack.pop()
                y = stack.pop()
                z = x + y
                # Check if the sum is within the range
                if lower <= z <= upper:
                    stack.append(z)
                else:
                    return -1  # err: overflow or underflow

            else:
                return -1  # err: stack underflow

        # If the operation is -, pop the two topmost elements and push their difference
        elif op == "-":
            # Check if the stack has at least two elements
            if len(stack) >= 2:
                x = stack.pop()
                y = stack.pop()
                z = x - y
                # Check if the difference is within the range
                if lower <= z <= upper:
                    stack.append(z)
                else:
                    return -1       # err: overflow or underflow
            else:
                return -1           # err: stack underflow

        else:
            return -1               # err: invalid operation

    # after processing all the operations, check if the stack is not empty and return the topmost element
    if stack:
        return stack[-1]
    else:
        return -1                   # err: empty stack


assert solution(string="4 5 6 - 7 +") == 8
assert solution(string="13 DUP 4 POP 5 DUP + DUP + -") == 7
assert solution(string="5 6 + -") == -1
assert solution(string="3 DUP 5 - -") == -1
assert solution(string="1048575 DUP +") == -1
print("Done!")

"""
To improve "word machine" we can replace "error return value = -1" with next error codes:
Error codes:
-1  stack underflow
-2  stack overflow
-3  invalid operation
-4  empty stack
"""
