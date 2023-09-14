Number = float(input("Enter a number: " ))
Till = int(input("You Want Its Tablr Till: "))
i = Till * Number
z = 1
x = Number
print(z ,"-" , Number)
while Number < i : 
    print (z + 1 ,"-" , x + Number)
    Number = x + Number
    z = z + 1
print("Done")
