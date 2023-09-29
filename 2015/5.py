import fileinput

def has_wovels(name):
    if name.count("a") + name.count("e") + name.count("i") + name.count("o")+ name.count("u") > 2:
        return True
    return False

def has_doubles(name):
    for le in name:
        if le*2 in name:
            return True        
    return False

def has_pairs(name):
    if "ab" in name or "cd" in name or "pq" in name or "xy" in name:
        return True
    return False

def has_pairs2(name):
    for x in name[:-1]:
        for y in name[1:]:
            if name.count(x+y) > 1:
                #print(name)
                return True
    return False

def has_triple(name):
    i=0
    for h in name[:-2]:
        if name[i]==name[i+2]:
            return True
        i+=1
    return False

#python 1.py Input\Day1.txt
#python 2015\5.py 2015\Input\Day5.txt
X = [str(line) for line in fileinput.input()]
counter = 0
counter1 = 0
for name in X:
    if has_triple(name) and has_pairs2(name):
        counter1+=1
print("Counter1 is ",counter1)
for name in X:
    if has_wovels(name) and has_doubles(name) and not has_pairs(name):
        counter+=1
        
print("Nr of good names ", counter)