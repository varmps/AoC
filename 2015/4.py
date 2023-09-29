import sys
import fileinput
import hashlib

#python 4.py Input\Day4.txt
#python 2015\4.py 2015\Input\Day4.txt
X = [str(line) for line in fileinput.input()]
#n = len(X)
i=0
result = hashlib.md5()
result.update(("iwrupvqb"+ str(i)).encode())
while not result.hexdigest().startswith("000000"):
    result = hashlib.md5()
    result.update(("iwrupvqb"+ str(i)).encode())
    i+=1
print(result.hexdigest())
print(i-1)
