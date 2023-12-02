#!/usr/bin/env python3

# Part I

import re

with open('aoc202301.txt') as f:
    lines = f.readlines()
    
clean_lines = [line.strip('\n') for line in lines]
number_lines = [re.sub(r'[a-zA-Z]','',line) for line in clean_lines]
number_pairs = [int(line[0]+line[-1]) for line in number_lines]
print(f'Part I: {sum(number_pairs)}')

# Part II

num_replace = {
    'one':'o1e',
    'two':'t2o',
    'three':'t3e',
    'four':'f4r',
    'five':'f5e',
    'six':'s6x',
    'seven':'s7n',
    'eight':'e8t',
    'nine':'n9e',
    'zero':'z0o'
}

with open('aoc202301.txt') as f:
    lines = f.readlines()

clean_lines = [line.strip('\n') for line in lines]
cleaner_lines = []
for line in clean_lines:
    for key,val in num_replace.items():
        line = line.replace(key,val)
    cleaner_lines.append(line)
number_lines = [re.sub(r'[a-zA-Z]','',line) for line in cleaner_lines]
number_pairs = [int(line[0]+line[-1]) for line in number_lines]
print(f'Part II: {sum(number_pairs)}')