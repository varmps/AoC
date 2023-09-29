import sys
import fileinput
#python 3.py Input\Day3.txt
#python 2015\3.py 2015\Input\Day3.txt
X = [str(line) for line in fileinput.input()]
#n = len(X)
x = 0
y = 0
k = 0
l = 0
homes = set()
homes.add((x,y))
i=0
for direction in X[0]:
    if i%2 == 0:
        if direction == "<":
            x-=1
        if direction == ">":
            x+=1
        if direction == "^":
            y+=1
        if direction == "v":
            y-=1
    else:
        if direction == "<":
            k-=1
        if direction == ">":
            k+=1
        if direction == "^":
            l+=1
        if direction == "v":
            l-=1
    i+=1 
    homes.add((k,l)) 
    homes.add((x,y))
print("nr of uniq homes ", len(homes))