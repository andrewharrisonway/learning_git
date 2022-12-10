import aoc202209input

long_instructions = ''
for instruction in aoc202209input.input_.split('\n'):
    direction,distance = instruction.split(' ')
    long_instructions += direction*int(distance)

def head_mover(head_position,direction):
    head_x, head_y = head_position
    if direction == 'U':
        head_y += 1
    elif direction == 'D':
        head_y -= 1
    elif direction == 'R':
        head_x += 1
    elif direction == 'L':
        head_x -= 1
    return [head_x,head_y]

def tail_mover(head_position, tail_position):
    head_x,head_y = head_position
    tail_x,tail_y = tail_position
    x_diff = head_x - tail_x
    y_diff = head_y - tail_y
    
    #if head and tail are not touching
    if max([abs(x_diff),abs(y_diff)]) > 1:
        if x_diff > 0:
            tail_x += 1
        if x_diff < 0:
            tail_x -= 1
        if y_diff > 0:
            tail_y += 1
        if y_diff < 0:
            tail_y -= 1
    return [tail_x,tail_y]

def tail_tracker(instructions):

    head_position = [0,0]
    tail_position = [0,0]
    
    tail_locations = set()
    
    for step in instructions:
        head_position = head_mover(head_position, step)
        tail_position = tail_mover(head_position, tail_position)
        tail_locations.update([tuple(tail_position)])
    return(len(tail_locations))

print(tail_tracker(long_instructions))

def tail_tracker2(instructions, snake_length):

    snake = [[0,0] for _ in range(snake_length)]
    
    tail_locations = set()
        
    for step in instructions:
        snake[0] = head_mover(snake[0], step)
        for i in range(1,len(snake)):
            snake[i] = tail_mover(snake[i-1], snake[i])
            tail_locations.update([tuple(snake[-1])])
    return(len(tail_locations))

print(tail_tracker2(long_instructions,10))