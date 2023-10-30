number = input("Enter number: ").split(" ")

condition = True
first = int(number[0])
second = int(number[1])
third = int(number[2])
forth = int(number[3])

x = 3

y = 10**5
while (condition):
    
    if x == y:
        
        print("None")
        condition = False
        
    elif x%first == forth and x%second == forth and x%third == forth and x%2 != 0:
          print(x)
        
          condition = False
        
    else:
        x=x+1
