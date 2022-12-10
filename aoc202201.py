import aoc202201input

numlist = aoc202201input.input_.split('\n')

def calorie_finder(numlist):
    base = 0
    sumlist = []
    for number in numlist:
        try:
            base += int(number)
        except ValueError:
            sumlist.append(base)
            base = 0
    return max(sumlist)

print(calorie_finder(numlist))

def calorie_finder2(numlist):
    base = 0
    sumlist = []
    for number in numlist:
        try:
            base += int(number)
        except ValueError:
            sumlist.append(base)
            base = 0
    sumlist.sort()
    return sum(sumlist[-3:])

print(calorie_finder2(numlist))