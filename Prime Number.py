number = input("Enter number: ").split(" ")

cond = True
a = int(number[0])
b = int(number[1])
c = int(number[2])
q = int(number[3])

if q == a or q == b or q == c:
     print("None")
     cond = False

numbers = [a , b , c , q]

greatest_number = max(numbers)

p = greatest_number + 1
while (cond):
    
    if p == 10**10:
        
        print("None")
        cond = False
        
    elif p % a == q and p % b == q and p % c == q and p % 2 != 0:
          print(p)
        
          cond = False

    elif p % a == q and p % b == q and p % c == q and p % 2 == 0:
          print("None")
        
          cond = False
        
    else:
        p=p+1
