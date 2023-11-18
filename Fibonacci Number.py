while True :
    a = int(input("Enter the number of Fibonacci numbers you want: "))
    if a < 1: 
        print("Entered value should be a whole number")
        continue
    elif a == 1: 
        print("0") 
    elif a == 2: 
        print("0") 
        print("1")
    else: 
        print("0") 
        print("1") 
        y = 0 
        z = 1 
        x = y + z 
        print (x) 
        n = 3
        while n < a: 
            y = z 
            z = x 
            x = y + z 
            print (x) 
            n = n + 1     
    break
print("Done")