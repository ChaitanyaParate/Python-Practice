import random
import sys
def get_card():
    cards = ["Ace" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10" , "Jack" , "Queen" , "King"]
    card = random.choice(cards)
    value = {
        "Ace" : "choice" ,
        "2" : 2,
        "3" : 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9,
        "10" : 10,
        "Jack" : 10,
        "Queen" : 10,
        "King" : 10
    }
    if value[card] == "choice":
        while True:
            a = input("You got an Ace chose 1 or 11: ")
            if a == "1" or a == "11":
                break
            else:
                continue
        return a
    else:
        return value[card]

def player_card():
    try:
        if len(p_cards) == 0:
            p_cards = []
    except (UnboundLocalError , NameError):
        p_cards = []
        
    c_card = int(get_card())
    p_cards.append(c_card)
    return c_card

def dealer():
    global d_cards
    try:
        if len(d_cards) == 0:
            d_cards = []
    except (UnboundLocalError, NameError):
        d_cards = []
    d_card = int(get_card())
    d_cards.append(d_card)
    return d_card

def limit(total):
    if total > 21:
        return True
    else:
        return False
        

def find_largest_number(lst):
    if not lst:
        return None 

    max_number = lst[0] 

    for number in lst:
        if number > max_number:
            max_number = number 

    return max_number

def list_length(my_list):
    if len(my_list) == 0:
        print("Every one lost!")
        sys.exit()

def player_changing(change_player):
    while True:
        if change_player == "yes":
            return True
        elif change_player == "no":
            change_player = input("Now: ")
            continue

def main():
    while True:
        try:
            number_of_player = int(input("Enter the number of players: "))
            break
        except ValueError:
            print("Enter a valid input!")
    while True:
        players = input(f"Input the name of all {number_of_player} players: ")
        individual_players = players.split(" ")
        if len(individual_players) == number_of_player:
            break
        else:
            print(f"Enter names of {number_of_player} players")
    

    individual_players_name = players.split(" ")
    for i in range(len(individual_players_name)):
        while True:
            try:
                individual_players[i] = int(input(f"{individual_players[i]} what is your beat: "))
                break
            except ValueError:
                print("Enter a valid input!")

    for i in range(len(individual_players_name)):
        print(f"Beats are {individual_players_name[i]}: {individual_players[i]}")
    print("Best of luck for the game!")

    player_lists = {}

    d_first_card = dealer()
    print(f"Dealer's first card has a value of {d_first_card}")
    change_player = "yes"
    for i in range(len(individual_players_name)):
        player_changing(change_player)
        print(f"{individual_players_name[i]}'s turn!")
        
        player_lists[f"{individual_players_name[i]}_list"] = []
        
        player_lists[f"{individual_players_name[i]}_list"].append(player_card())
        
        player_lists[f"{individual_players_name[i]}_list"].append(player_card())
        
        cards = player_lists[f"{individual_players_name[i]}_list"]
        
        print(f"{individual_players_name[i]}'s cards are {cards}")
        if i < (len(individual_players_name)-1):
            change_player = input("Want to change player: ")
    out = []
    
    for i in range(len(individual_players_name)):
        if player_changing(change_player):
            print(f"{individual_players_name[i]}'s turn!")
        
        x = input("Do you want to see all of your cards?(yes/no) ")
        if x == "yes":
            print(player_lists[individual_players_name[i]+'_list'])
            
            cont = input("Do you want to hit, stay or beat? ")
        elif x == "no":
            cont = input("Do you want to hit, stay or beat? ")

        if cont == "beat":
            
            print(f"You wone Rs.{individual_players[i]}")
            out.append(individual_players_name[i])

            
        if cont == "hit":
            player = player_card()
            player_lists[f"{individual_players_name[i]}_list"].append(player)
            
            print(f"Card received has a value of {player}")
            x = f"{individual_players_name[i]} Lost!"
            cards = player_lists[f"{individual_players_name[i]}_list"]
            print(f"Your card total is {sum(cards)}")
            if limit(sum(cards)):
                print(f"{individual_players_name[i]} lost")
                out.append(individual_players_name[i])
            
                
        elif cont == "stay":
            cards = player_lists[f"{individual_players_name[i]}_list"]
            print(f"Your card total is {sum(cards)}")
        if i > (len(individual_players_name) - 1):
            change_player = input("Want to change player: ")
            
    list_length(player_lists)
    d_second_card = dealer()
    print(f"Dealer's second card has a value of {d_second_card}")
    d = 3
    while sum(d_cards) < 17:
        print("Sum of dealer's all cards is less than 17 so dealer picks another card")
        if d == 3:
            num = f"{d}rd"
        else:
            num = f"{d}th"
        
        d_third_card = dealer()
        print(f"Dealer's {num} card has a value of {d_third_card}")
        x = "Player Win Their Bet!"
        print(f"Sum of dealer's card is {sum(d_cards)}")
        if limit(sum(d_cards)):
            print("Dealer is busted!")
            print("All players that are not busted win their beat")
            sys.exit()
            
    print(f"Sum of dealer's card is {sum(d_cards)}")

    for i in range(len(individual_players_name)):

        if sum(d_cards) > sum(player_lists[f"{individual_players_name[i]}_list"]):
            print(f"{individual_players_name[i]} Lost!")
            out.append(individual_players_name[i])

        elif sum(d_cards) < sum(player_lists[f"{individual_players_name[i]}_list"]):
            continue

    for i in range(len(out)):
        individual_players_name.remove(out[i])
        player_lists.pop(out[i] + '_list')

    if len(individual_players_name) == 0:
        print("Every one lost!")
        sys.exit()

    list_length(player_lists)
    sums_dict = {}

    for i in range(len(individual_players_name)):
        player_name = individual_players_name[i]
        player_list = player_lists[f"{individual_players_name[i]}_list"]
        sums_dict[f"{player_name}_sum"] = sum(player_list)

    sum_list = []

    for i in range(len(individual_players_name)):
        sum_list.append(sums_dict[f"{individual_players_name[i]}_sum"])

    result = find_largest_number(sum_list)
    winners = []
    for i in range(len(individual_players_name)):
        if sum(player_lists[f"{individual_players_name[i]}_list"]) == result:
            winners.append(individual_players_name[i])
    result_string = ' '.join(map(str, winners))
    if len(winners) > 1:
        print(f"Winners are{result_string}")

    else:
        print(f"Winner is {result_string}")

if __name__ == "__main__":
    main()
