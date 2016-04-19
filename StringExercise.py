
x = "There are %d types of people. " %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s. " %(binary, do_not)

print(x)
print(y)

print("I said: %s " %x)
print("I also said: %s " %y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %s"

print(joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with a right side."

print(w+e)

formatter = "%r %r %r %r "

print(formatter %(formatter,formatter, formatter, formatter))

days = "Sunday, Monday, Tuesday, Wednesday, Thursday, Friday and Saturday"

Month = "\nJan \nFeb \nMarch \nApril \nMay \nJune \nJuly \netc"

print("so the days of the weeks are: %r" %days)
print("so the months of the year are: %r" %Month )


#drill for getting the input from the user and printing it with the help of the string formatter
age = input("what is your age?")

height = input("what is your height")

print("so you are %s old and %s feet tall. NICE !! just like a fucking model" %(age,height))