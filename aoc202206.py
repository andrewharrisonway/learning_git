import aoc202206input

phrase = aoc202206input.phrase

def message_finder(phrase,length):
	for i in range(len(phrase)-length):
		subphrase = phrase[i:i+length]
		if len(subphrase) == len(set(subphrase)):
			return i+length

#part i
print(message_finder(phrase,4))

#part ii
print(message_finder(phrase, 14))
