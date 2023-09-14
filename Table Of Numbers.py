Number = float(input("Enter a number: " ))
i = 10 * Number
z = 1
x = Number
print(z ,"-" , Number)
while Number < i : 
    print (z + 1 ,"-" , x + Number)
    Number = x + Number
    z = z + 1
print("Done")