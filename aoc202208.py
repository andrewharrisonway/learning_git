import aoc202208input

def finding_visible_trees(data):
	
	visible_trees = set()
	forest = data.split('\n')
	
	# horizontal
	for y, row in enumerate(forest):
		#from the left
		tallest_tree_height = -1
		for x, tree in enumerate(row):
			if int(tree) > tallest_tree_height:
				visible_trees.update([(x,y)])
				tallest_tree_height = int(tree)
		#from the right
		tallest_tree_height = -1
		for x, tree in enumerate(row[::-1]):
			if int(tree) > tallest_tree_height:
				visible_trees.update([(len(row)-x-1,y)])
				tallest_tree_height = int(tree)
				
	# vertical
	
	for x in range(len(forest[0])):
		
		#from the top
		tallest_tree_height = -1
		for y, row in enumerate(forest):
			if int(row[x]) > tallest_tree_height:
				visible_trees.update([(x,y)])
				tallest_tree_height = int(row[x])
		
		#from the bottom
		tallest_tree_height = -1
		for y, row in enumerate(forest[::-1]):
			if int(row[x]) > tallest_tree_height:
				visible_trees.update([(x,len(forest)-y-1)])
				tallest_tree_height = int(row[x])
	
	return visible_trees

visible_trees = finding_visible_trees(aoc202208input.input_)

print(len(visible_trees))

def look_east(treehouse,graph):
	viewable_trees = 0
	home_x,home_y = int(treehouse[0]),int(treehouse[-1])
	treehouse_height = int(graph[home_y][home_x])
	eastern_trees = graph[home_y][home_x+1:]
	for tree in eastern_trees:
		viewable_trees +=1
		if int(tree) >= treehouse_height:
			break
	return viewable_trees

def look_west(treehouse,graph):
	viewable_trees = 0
	home_x,home_y = int(treehouse[0]),int(treehouse[-1])
	treehouse_height = int(graph[home_y][home_x])
	western_trees = graph[home_y][home_x-1::-1]
	for tree in western_trees:
		viewable_trees +=1
		if int(tree) >= treehouse_height:
			break
	return viewable_trees

def look_south(treehouse,graph):
	viewable_trees = 0
	home_x,home_y = int(treehouse[0]),int(treehouse[-1])
	treehouse_height = int(graph[home_y][home_x])
	for y in range(home_y+1,len(graph)):

		viewable_trees +=1
		if int(graph[y][home_x]) >= treehouse_height:
			break
	return viewable_trees

def look_north(treehouse,graph):
	viewable_trees = 0
	home_x,home_y = int(treehouse[0]),int(treehouse[-1])
	treehouse_height = int(graph[home_y][home_x])
	for y in range(home_y-1,-1,-1):
		viewable_trees +=1

		if int(graph[y][home_x]) >= treehouse_height:
			break
	return viewable_trees


def visibility_maxscore(data,sites):
	forest = data.split('\n')
	max_visibility = 0
	
	for potential_th in sites:
		vis_score = 1
		vis_score *= look_east(potential_th,forest)
		vis_score *= look_west(potential_th,forest)
		vis_score *= look_north(potential_th, forest)
		vis_score *= look_south(potential_th, forest)
		if vis_score > max_visibility:
			max_visibility = vis_score
	return max_visibility

print(visibility_maxscore(aoc202208input.input_, visible_trees))