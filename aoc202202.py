import aoc202202input

def rps_scorer(plays):
    play_vals = {
        'A':1,
        'B':2,
        'C':3,
        'X':1,
        'Y':2,
        'Z':3
    }
    
    wins = {
        'Y':'A',
        'Z':'B',
        'X':'C'
    }
    
    player_score = 0
    opponent_score = 0
    
    for round in plays.split('\n'):
        opponent,player = round.split(' ')
        opponent_score += play_vals[opponent]
        player_score += play_vals[player]

        if wins[player] == opponent:
            player_score += 6
        #draw
        elif play_vals[player] == play_vals[opponent]:
            player_score += 3
            opponent_score += 3
        else:
            opponent_score += 6
            
    return(player_score)

print(rps_scorer(aoc202202input.input_))

def rps_scorer2(plays):
    play_vals = {
        'A':1,
        'B':2,
        'C':3,
        'X':0,
        'Y':3,
        'Z':6
    }
    
    outcomes = {
        'A X':'C',
        'A Y':'A',
        'A Z':'B',
        'B X':'A',
        'B Y':'B',
        'B Z':'C',
        'C X':'B',
        'C Y':'C',
        'C Z':'A'
    }
    
    player_score = 0
    opponent_score = 0
    
    for round in plays.split('\n'):
        opponent,win_status = round.split(' ')
        opponent_score += play_vals[opponent]
        player_move = outcomes[round]
        player_score += play_vals[player_move]
        player_score += play_vals[win_status]
        
    return(player_score)

print(rps_scorer2(aoc202202input.input_))