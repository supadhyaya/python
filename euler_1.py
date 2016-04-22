
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""

# This problem will give an overview of the logical error while programming.

multiplier = set()  # Store the use given multipliers in a set
result = set()      # Add all the numbers which produces 0 as remainder
final_result = 0    # Holds sum of all the numbers from the set named result
mul_cnt = True      # Counter to track the inputs from the user


#  Number whose multiple we are going to add
try:
    number = int(input("please enter a number you want to divide\n"))

except ValueError:
    print("Oopsy !! Enter a valid integer")


#  Ask the user for the multipliers they want to use
while mul_cnt:
    try:
        x = int(input("Please enter the multipliers you want to use. Press 0 to end the input\n"))

        if x != 0:
            multiplier.add(x)
        else:
            mul_cnt = False

            break

    except ValueError:
        print("Oppsy !! Enter a valid integer")


#  Add all the multipliers to a single tuple called result
for mul in multiplier:
    # noinspection PyUnboundLocalVariable
    for num in range(mul, number):
        if num % mul == 0:
            result.add(num)


#  Add all the elements of the tuple to print the final result
for items in result:
    final_result = final_result + items


print("Answer: %s" % final_result)




