#! /usr/bin/python
"""
mental math trainer
"""

"""
future: let user choose which operations
input 12345 for +-*/
"""

import random
import numpy as np

#chooseops
#user_ops = input("choose operations:\n 1 = +\n 2 = -\n 3 = * \n 4 = // \n" )
#right now comes back as a string, should be an int
#pick = random.choice(user_ops)

counter = 0
loop = True
while loop:
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)

#    ops = ["*", "+", "-", "//"]
    ops = ["*", "-", "*", "//"]
    answer = [n1+n2, n1-n2, n1*n2, n1//n2]
#    pick = random.randint(0,3)
    pick = random.randint(2,3)

#make multiplication easier
    if n1 > 10 and n2 > 10 and pick == 2:
#        n2 //= 10
        n2 //= 10
        n2 /= 10 #percentages
        answer[2] = n1*n2
#make floored quotient harder
    if n1 > 10 and n2 > 10 and pick == 3:
        n2 //= 10
        answer[3] = n1//n2
#make floored quotient non-zero
    if n2 > n1 and pick == 3:
        n1,n2 = n2,n1
        if n2 > 10:
            n2 //= 10
        answer[3] = n1//n2
    

#    user = int(input("{} {} {} = ".format(n1, ops[pick], n2)))

    if pick == 2:
        user = float(input("{} {} {} = ".format(n1, ops[pick], n2))) #make input into a float 
    else: 
        user = int(input("{} {} {} = ".format(n1, ops[pick], n2))) 

#    if user == answer[pick]:
    if np.isclose(user, answer[pick]):
        print("correct, the answer is " + str(answer[pick]))
        counter = counter + 1
    else:
        print("incorrect, the answer is " + str(answer[pick]))
        print("number correct: ", counter)
        counter = 0
        loop = input("try again? y/n ") == "y"

