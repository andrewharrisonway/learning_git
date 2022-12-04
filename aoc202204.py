with open('aoc202204.txt') as f:
	data = f.read().split('\n')
	
elf1 = [numrange.split(',')[0] for numrange in data]
elf2 = [numrange.split(',')[1] for numrange in data]

#part i

def double_section_finder(range1,range2):
	double_section_count = 0
	
	for member1,member2 in zip(range1,range2):
		member_range1  = set([i for i in range(
							int(member1.split('-')[0]),
							int(member1.split('-')[1])+1)])
		member_range2  = set([i for i in range(
							int(member2.split('-')[0]),
							int(member2.split('-')[1])+1)])
		if len(member_range1.union(member_range2)) == len(member_range1) or \
			len(member_range1.union(member_range2)) == len(member_range2):
				double_section_count += 1
	return double_section_count

result = double_section_finder(elf1,elf2)
print(result)

#part ii

def any_overlap_finder(range1,range2):
	any_overlap_count = 0
	
	for member1,member2 in zip(range1,range2):
		member_range1  = set([i for i in range(
							int(member1.split('-')[0]),
							int(member1.split('-')[1])+1)])
		member_range2  = set([i for i in range(
							int(member2.split('-')[0]),
							int(member2.split('-')[1])+1)])
		if len(member_range1.union(member_range2)) < len(member_range1) + len(member_range2):
				any_overlap_count += 1
	return any_overlap_count

result = any_overlap_finder(elf1,elf2)
print(result)