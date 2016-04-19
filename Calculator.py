

#ask the user for the first operand
var1 = int(input("enter the number"))

#ask the user for the operator
operator = input("enter the operator. Only + and - are supported now.")

#ask the user for the second operand
var2 = int(input("enter the number"))

result = 0

if(operator == "+"):
    result = var1 + var2

elif(operator == "-"):
    result = var1 - var2

else:
    print("other operations are not supported yet")

print("result: %s" %result)







