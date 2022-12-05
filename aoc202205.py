with open('aoc202205.txt') as f:
    data = f.read()

piles, moves = data.split('\n\n')

#sorry for hardcoding
piles = {
    1:['G','F','V','H','P','S'],
    2:['G','J','F','B','V','D','Z','M'],
    3:['G','M','L','J','N'],
    4:['N','G','Z','V','D','W','P'],
    5:['V','R','C','B'],
    6:['V','R','S','M','P','W','L','Z'],
    7:['T','H','P'],
    8:['Q','R','S','N','C','H','Z','V'],
    9:['F','L','G','P','V','Q','J']
}
piles2 = {
    1:['G','F','V','H','P','S'],
    2:['G','J','F','B','V','D','Z','M'],
    3:['G','M','L','J','N'],
    4:['N','G','Z','V','D','W','P'],
    5:['V','R','C','B'],
    6:['V','R','S','M','P','W','L','Z'],
    7:['T','H','P'],
    8:['Q','R','S','N','C','H','Z','V'],
    9:['F','L','G','P','V','Q','J']
}


moves = moves.split('\n')

# part i

for move in moves:
    iterations, location, destination = \
        move.replace('move ','').replace('from ','').replace('to ','').split(' ')
    iterations,location,destination = int(iterations),int(location),int(destination)
    for i in range(iterations):
        piles[destination].append(piles[location].pop(-1))

result_letters = [piles[i][-1] for i in range(1,10)]
print(''.join(result_letters))

# part ii

for move in moves:
    iterations, location, destination = \
        move.replace('move ','').replace('from ','').replace('to ','').split(' ')
    iterations,location,destination = int(iterations),int(location),int(destination)
    box_location = len(piles2[location]) - iterations
    for i in range(iterations):
        piles2[destination].append(piles2[location].pop(box_location))
        
result_letters = [piles2[i][-1] for i in range(1,10)]
print(''.join(result_letters))
    