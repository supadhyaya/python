

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""

#This problem will give an overview of the logical error while programming.

#Number whose multiple we are going to add
number = int(input("please enter a number\n"))



#Number which the user's multiple
multiplier1 = int(input("what is the first multiplier\n"))
multiplier2 = int(input("what is the second multiplier\n"))


result1 = 0
result2 = 0

for i_1 in range(multiplier1, number):
    if(i_1 % multiplier1 == 0):
        result1 = result1 + i_1

for i_2 in range(multiplier2, number):
    if(i_2 % multiplier2 == 0):
        result2 = result2 + i_2

print("Result: %s" %(result1+result2))

print(result1)
print(result2)


