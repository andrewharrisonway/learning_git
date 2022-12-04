# Part I

def scoring(character):
    unicode = ord(character)
    if unicode >=97:
        return unicode - ord('a') + 1
    elif unicode <=90:
        return unicode - ord('A') + 27

def split_and_search(data):
    dupes_list = []
    for bag in data:
        bag1 = bag[:int(len(bag)/2)]
        bag2 = bag[int(len(bag)/2):]
        dupes_list.extend(list(set(bag1).intersection(bag2)))
    return dupes_list

with open('aoc2022.03') as f:
    data = f.read()

data = data.split('\n')[:-1]

dupes_cost = 0
for character in split_and_search(data):
    dupes_cost += scoring(character)
print(dupes_cost)

# Part II

badge = []
for bag1,bag2,bag3 in zip(data[::3],data[1::3],data[2::3]):
    badge.extend(list(set(bag1).intersection(bag2).intersection(bag3)))

badge_cost = 0
for character in badge:
    badge_cost += scoring(character)
print(badge_cost)