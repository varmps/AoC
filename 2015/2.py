import sys
import fileinput
#python 2.py Input\Day2.txt
#python 2015\2.py 2015\Input\Day2.txt
list = [line.removesuffix("\n").split("x") for line in fileinput.input()]
total = 0
ribbon = 0
for present in list:
    sorted = [int(present[0]),int(present[1]),int(present[2])]
    sorted.sort()
    dim = [sorted[0]*sorted[1],sorted[0]*sorted[2],sorted[2]*sorted[1]]
    summa = sum(dim)*2 + min(dim)
    wrap = 2*(sorted[0]+sorted[1])
    bow = sorted[0]*sorted[1]*sorted[2]
    total += summa
    ribbon = ribbon + wrap + bow
    
print ("total is ", total)
print ("total ribbon: ", ribbon)       