import aoc202210input

def signal_measure(data):
    
    X_register = 1
    strength_record = []
    
    expanded_steps = []
    for step in data.split('\n'):
        if step == 'noop':
            expanded_steps.append('noop')
        else:
            expanded_steps.append('noop')
            expanded_steps.append(step)

    for i,step in enumerate(expanded_steps):
        strength_record.append(X_register*(i+1))
        if step != 'noop':
            X_register += int(step.split(' ')[-1])

    return (sum(strength_record[19::40]))
        
print(signal_measure(aoc202210input.input_))

def CRT(data):
    
    expanded_steps = []
    for step in data.split('\n'):
        if step == 'noop':
            expanded_steps.append('noop')
        else:
            expanded_steps.append('noop')
            expanded_steps.append(step)
            
    X_register = 1
    display = ''
    
    for i,step in enumerate(expanded_steps):
        if ((i%40 <= X_register+1) and (i%40>=X_register-1)):
            display += '@'
        else:
            display += ' '
            
        if step != 'noop':
            X_register += int(step.split(' ')[-1])
    
    for i in range(6):
        print(display[i*40:(i*40)+40])

CRT(aoc202210input.input_)