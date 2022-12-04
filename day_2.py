def choose_shape(op, outcome):
    win = {'scissors': 'rock', 'paper': 'scissors', 'rock': 'paper'}
    lose = {v: k for k, v in win.items()}

    if outcome == 'draw':
        return op
    if outcome == 'won':
        return win[op]
    return lose[op]

def play_round(opponent_choice, outcome):
    decryption = {'A': 'rock', 'B': 'paper', 'C': 'scissors',
                  'X': 'lost', 'Y': 'draw', 'Z': 'won'}
    
    opponent_choice = decryption[opponent_choice]
    outcome = decryption[outcome]

    outcome_score = {'lost': 0, 'draw': 3, 'won': 6}
    shape_score = {'rock': 1, 'paper': 2, 'scissors': 3}

    shape = choose_shape(opponent_choice, outcome)
    return outcome_score[outcome] + shape_score[shape]

def rock_paper_scissors(strategy_guide):
    total_score = 0
    for strategy in strategy_guide:
        opponent_choice, outcome = strategy.split(' ')
        total_score += play_round(opponent_choice, outcome[:-1])

    return total_score

if __name__ == '__main__':
    inputs = open('day_2_input.txt', 'r').readlines()
    print(rock_paper_scissors(inputs))