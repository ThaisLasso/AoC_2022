def outcome(op, me):
    winning = {('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')}

    if (me, op) in winning: return 'won'
    if me == op: return 'draw'
    return 'lost'

def play_round(opponent_choice, my_choice):
    decryption = {'A': 'rock', 'B': 'paper', 'C': 'scissors',
                  'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
    
    opponent_choice = decryption[opponent_choice]
    my_choice = decryption[my_choice]

    outcome_scores = {'lost': 0, 'draw': 3, 'won': 6}
    shape_scores = {'rock': 1, 'paper': 2, 'scissors': 3}

    outcome_score = outcome_scores[outcome(opponent_choice, my_choice)]
    shape_score = shape_scores[my_choice]
    return outcome_score + shape_score

def rock_paper_scissors(strategy_guide):
    total_score = 0
    for strategy in strategy_guide:
        opponent_choice, my_choice = strategy.split(' ')
        total_score += play_round(opponent_choice, my_choice[:-1])

    return total_score

if __name__ == '__main__':
    inputs = open('day_2_input.txt', 'r').readlines()
    print(rock_paper_scissors(inputs))