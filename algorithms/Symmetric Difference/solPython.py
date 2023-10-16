#Solution 1
def sym(*args):
    a = list(set(args[0]))
    for i in range(1,len(args)):
        b = list(set(args[i]))
        a = list(filter(lambda x : b.count(x) ==0, a)) +  list(filter(lambda x : a.count(x) ==0, b))
    
    return a
print(sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]))

#Solution 2
def sym2(*args):
    a = list(set(args[0]))
    for i in range(1,len(args)):
        b = list(set(args[i]))
        a = list(filter(lambda x : x not in b, a)) +  list(filter(lambda x : x not in a, b))
    
    return a

print(sym2([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]))

#Solution 3
def sym3(*args):
    a = list(set(args[0]))
    for i in range(1,len(args)):
        b = list(set(args[i]))
        a = list(set(a) ^ set(b))
    
    return a
print(sym3([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]))

