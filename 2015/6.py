import fileinput
import numpy as np
#python 1.py Input\Day1.txt
#python 2015\6.py 2015\Input\Day6.txt
X = [str(line) for line in fileinput.input()]

grid = np.zeros((1000, 1000), dtype=int)

'''
#Part one solution
for command in X:
    command = command.split(" ")
    if "on" in command:
        x1, y1 = command[2].split(',')
        x2, y2 = command[4].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        grid[x1:x2+1, y1:y2+1] = 1    
    elif "off" in command:
        x1, y1 = command[2].split(',')
        x2, y2 = command[4].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        grid[x1:x2+1, y1:y2+1] = 0
    elif "toggle" in command:
        x1, y1 = command[1].split(',')
        x2, y2 = command[3].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        grid[x1:x2 + 1, y1:y2 + 1] = 1 - grid[x1:x2 + 1, y1:y2 + 1]
'''
for command in X:
    command = command.split(" ")
    if "on" in command:
        x1, y1 = command[2].split(',')
        x2, y2 = command[4].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        grid[x1:x2+1, y1:y2+1] += 1    
    elif "off" in command:
        x1, y1 = command[2].split(',')
        x2, y2 = command[4].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        grid[x1:x2+1, y1:y2+1] += -1
        grid[grid < 0] = 0
    elif "toggle" in command:
        x1, y1 = command[1].split(',')
        x2, y2 = command[3].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        grid[x1:x2+1, y1:y2+1] += 2        
print(np.sum(grid))

