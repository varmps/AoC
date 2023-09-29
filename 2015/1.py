import sys
import fileinput
#python 1.py Input\Day1.txt
#python 2015\1.py 2015\Input\Day1.txt
X = [str(line) for line in fileinput.input()]
#n = len(X)
i = 0
count = 0
lvl = 0
for s in X[0]:
    count+=1
    if s == "(":
        i+=1
    else:
        i-=1
    if i == -1 and lvl is 0:
        lvl = count
    

print("nr of lines: ", i)
print("level is lines: ", lvl)