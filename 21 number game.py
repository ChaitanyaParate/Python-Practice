import random
def select():
    integer = random.randint(1, 3)
    return integer
usednum = [0]
last_num = usednum[-1]
print("If you want to play first enter 1")
print("If you want to be second enter 2")

a = int(input("Enter your choise: "))
if a == 1 :
       while True:
           comp_choise = select()
           player_choice = input("How many Values do you Want to enter: ")
           if player_choice == str(1): 
               last_num += 1
               usednum.append(last_num)
               
           elif player_choice == str(2):
               last_num += 2
               usednum.extend([last_num - 1, last_num])
               
           elif player_choice == str(3):
               last_num += 3
               usednum.extend([last_num - 2, last_num - 1, last_num])
           else:
               print("Enter a valid input")
               continue
           if len(usednum) >= 22:
               print(usednum)
               print("Number exceeded 20")
               print("You Loose")
               break
           if comp_choise == 1: 
             last_num += 1
             usednum.append(last_num)
               
           elif comp_choise == 2:
               last_num += 2
               usednum.extend([last_num - 1, last_num])
               
           elif comp_choise == 3:
               last_num += 3
               usednum.extend([last_num - 2, last_num - 1, last_num])
               
           if len(usednum) >= 22:
               print("Order of inputs after computer's turn is:")
               print(usednum)
               print("Number exceeded 20")
               print("you Won!") 
               break
           print("Order of inputs after computer's turn is:")
           print(usednum)
           print("Your Turn")
elif a ==2:
    while True:
        if len(usednum) >= 22:
            break
        comp_choise = select()
        if comp_choise == 1: 
          last_num += 1
          usednum.append(last_num)
            
        elif comp_choise == 2:
            last_num += 2
            usednum.extend([last_num - 1, last_num])
            
        elif comp_choise == 3:
            last_num += 3
            usednum.extend([last_num - 2, last_num - 1, last_num])
            
        if len(usednum) >= 22:
            print("Order of inputs after computer's turn is:")
            print(usednum)
            print("Number exceeded 20")
            print("you Won!") 
            break
        print("Order of inputs after computer's turn is:")
        print(usednum)
        print("Your Turn")
        
        while True: 
            player_choice = input("How many Values do you Want to enter: ")
            if player_choice == str(1): 
                last_num += 1
                usednum.append(last_num)
                if len(usednum) >= 22:
                    print(usednum)
                    print("Number exceeded 20")
                    print("You Loose")
                    break
                break
                
            elif player_choice == str(2):
                last_num += 2
                usednum.extend([last_num - 1, last_num])
                if len(usednum) >= 22:
                    print(usednum)
                    print("Number exceeded 20")
                    print("You Loose")
                    break
                break
                
            elif player_choice == str(3):
                last_num += 3
                usednum.extend([last_num - 2, last_num - 1, last_num])
                if len(usednum) >= 22:
                    print(usednum)
                    print("Number exceeded 20")
                    print("You Loose")
                    break
                break
            
            else:
                print("Enter a valid input")
                continue
            break
         