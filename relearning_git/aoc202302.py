#!/usr/bin/env python3

#Part I

with open('aoc202302.txt') as f:
    lines=f.readlines()
lines = [line.strip('\n') for line in lines]

games = []
for round in lines:
    game_num_str,game_seq = round.split(': ')
    game = {
        'id':int(game_num_str.replace('Game ','')),
        'red':0,
        'green':0,
        'blue':0
    }
    for step in game_seq.split('; '):
        for selection in step.split(', '):
            quantity,color = selection.split(' ')
            game[color] = max(game[color],int(quantity))
    games.append(game)
    
sum = 0
for game in games:
    if game['red']<=12 and game['green']<=13 and game['blue']<=14:
        sum += game['id']
print(f'Part I: {sum}')

# Part II

games = []
total_power = 0
for round in lines:
    game_num_str,game_seq = round.split(': ')
    game = {
        'id':int(game_num_str.replace('Game ','')),
        'red':0,
        'green':0,
        'blue':0,
        'power':0
    }
    for step in game_seq.split('; '):
        for selection in step.split(', '):
            quantity,color = selection.split(' ')
            game[color] = max(game[color],int(quantity))
    game['power'] = game['red']*game['green']*game['blue']
    games.append(game)
    total_power += game['power']
    
print(f'Part II: {total_power}')