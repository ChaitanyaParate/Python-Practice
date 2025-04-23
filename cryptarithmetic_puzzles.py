import time 
import itertools 
def solution1(): 
    letters = ('s', 'e', 'n', 'd', 'm', 'o', 'r', 'y') 
    digits = range(10)
    for perm in itertools.permutations (digits, len (letters)): 
        sol = dict(zip(letters, perm)) 
        if sol['s'] == 0 or sol['m'] == 0: 
            continue 
        send = 1000 * sol['s'] + 100 * sol['e'] + 10* sol['n'] + sol['d'] 
        more = 1000 * sol['m'] + 100 *sol['o'] + 10 *sol['r'] + sol['e'] 
        money = 10000 * sol['m'] + 1000 *sol['o'] + 100 *sol['n'] + 10 *sol['e'] + sol['y'] 
        if send + more == money: 
            print("SEND + MORE = MONEY") 
            return send,more,money

def solution2(): 
    letters = ('s', 'c', 'r', 'o', 'a', 'd', 'n', 'g' , 'e') 
    digits = range(10)
    for perm in itertools.permutations (digits, len (letters)): 
        sol = dict(zip(letters, perm)) 
        if sol['c'] == 0 or sol['r'] == 0: 
            continue 
        cross = 10000 * sol['c'] + 1000 * sol['r'] + 100* sol['o'] + 10* sol['s'] + sol['s'] 
        roads = 10000 * sol['r'] + 1000 *sol['o'] + 100 *sol['a'] + 10*sol['d'] + sol['s'] 
        danger = 100000 * sol['d'] + 10000 *sol['a'] + 1000 *sol['n'] + 100 *sol['g'] + 10*sol['e'] + sol['r']
        if cross + roads == danger: 
            print("CROSS + ROADS = DANGER") 
            return cross,roads,danger
        
if __name__ == "__main__":
    send , more , money = solution1()
    
    print(send)
    print(more)
    print(money)

    cross , roads , danger = solution2()

    print(cross)
    print(roads)
    print(danger)

