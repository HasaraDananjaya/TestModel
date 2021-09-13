#Taking an input from the user
#grpNum = int(input("Enter your Group number: "))
#print ("\nHi, Our Group number is",grpNum)

#Hard code the group number to the variable grpNum
print ("Hi, Our Group number is 08")
grpNum = 8      

#Operation and Print results
quotient = grpNum/4
remainder = grpNum%4
print ("Quotient : ",int(quotient))
print ("Remainder : ",remainder)
numGrpMem = 3
if remainder==0:
    print ("Relevant Operation : Addition")
    result = numGrpMem + remainder
elif remainder==1:
    print ("Relevant Operation : Subtraction")
    result = numGrpMem - remainder
elif remainder==2:
    print ("Relevant Operation : Multiplication")
    result = numGrpMem * remainder
elif remainder==3:
    print ("Relevant Operation : Division")
    result = numGrpMem / remainder
else:
    print ("Program Calculation Error")

print ("Result According to the operation : ",result)
if (result%2)==0:
    print ("Result is an Even Number")
elif (result%2)==1:
    print ("Result is an Odd Number")
else:
    print ("Result is not an Odd or an Even Number")