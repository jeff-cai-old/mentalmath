#! /usr/bin/python
"""Mental math trainer

Choose operations, output question, compare answer
"""

import random
import numpy as np


def user_ops():
    """User chosen operations, return a list for random.choice()."""

    user_ops = input("choose operations: \n (example: '124')\
        \n 1 = + \n 2 = - \n 3 = * \n 4 = // \n" )
    L=[]
    for i in range(1,5):
        if str(i) in user_ops:
            L.append(i-1)
    return(L)

class Question:
    def __init__(self, n1=random.randint(1, 100), n2=random.randint(1, 100),
                ops_list=["+", "-", "*", "//"]):
        self.n1 = n1
        self.n2 = n2
        self.ops_list = ops_list

    def choose_ops(self, L):
        """Randomly choose operation from L, returns op as int"""

        if len(L) ==1:
            return L[0]
        else:
            op = random.choice(L)
        return op
    
    def get_equation(self, pick):
        """Randomize two numbers, return an equation tuple based on operation.

        """

        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        answer = [n1+n2, n1-n2, n1*n2, n1//n2]
        # Difficulty/facilitation
        # Make multiplication easier
        if n1 > 10 and n2 > 10 and pick == 2:
            n2 //= 10 # Make multiplication 2 by 1
            n2 /= 10 # Percentages
            answer[2] = n1*n2
        # Make floored quotient slightly harder
        if n1 > 10 and n2 > 10 and pick == 3:
            n2 //= 10
            answer[3] = n1//n2
        # Make floored quotient non-zero
        if n2 > n1 and pick == 3:
            n1,n2 = n2,n1
            if n2 > 10:
                n2 //= 10
            answer[3] = n1//n2
        return (n1, n2, answer[pick])


counter = 0
loop = True
q = Question()

#let user choose operations
ops = user_ops()

while loop:
    op_int = q.choose_ops(ops)
    eq = q.get_equation(op_int)
    user = float(input("{} {} {} = ".format\
            (eq[0], q.ops_list[op_int], eq[1])))
    if np.isclose(user, eq[2]):
        print("correct, the answer is ", eq[2])
        counter += 1
    else:
        print("incorrect, the answer is ", eq[2])
        print("number correct: ", counter)
        counter = 0
        loop = input("try again? y/n ") == "y"

