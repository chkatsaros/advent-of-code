def calculate_points(x):
    if (x == 'A'):
        return 1
    elif (x == 'B'):
        return 2
    else:
        return 3
    
def convert_to_abc(x):
    return (chr(ord(x)-23))

def is_the_winner(opponent_bets, my_bets):
    if ((opponent_bets == 'A' and my_bets == 'C') or (opponent_bets == 'B' and my_bets == 'A') or (opponent_bets == 'C' and my_bets == 'B')):
        return True
    return False

def calculate_score_1(bets):
    my_bets = convert_to_abc(bets[1])
    # Draw
    if (bets[0] == my_bets):
        return 3 + calculate_points(my_bets)
    # Defeat
    elif (is_the_winner(bets[0], my_bets)):
        return calculate_points(my_bets)
    # Victory 
    else:
        return 6 + calculate_points(my_bets)
    
def select_bet(opponent_bet, win):
    if (win):
        if (opponent_bet == 'A'): 
            return calculate_points('B')
        elif (opponent_bet == 'B'):
            return calculate_points('C')
        else:
            return calculate_points('A')
    else: 
        if (opponent_bet == 'A'): 
            return calculate_points('C')
        elif (opponent_bet == 'B'):
            return calculate_points('A')
        else:
            return calculate_points('B')

def calculate_score_2(symbols):
    opponent_bet = symbols[0]
    plan = symbols[1] 
    # Draw
    if (plan == 'Y'):
        return 3 + calculate_points(opponent_bet)
    # Defeat
    elif (plan == 'X'): 
        return select_bet(opponent_bet, False)
    # Victory
    else:
        return 6 + select_bet(opponent_bet, True)
    

input = open('input.txt', 'r')
lines = input.readlines()

case_1 = 0
case_2 = 0

for line in lines:
    symbols = line.strip().split(" ")
    case_1 += calculate_score_1(symbols)
    case_2 += calculate_score_2(symbols)
    
print(case_1)
print(case_2)

input.close()