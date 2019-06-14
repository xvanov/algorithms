def getKey(item):
    return item[0][0]

l = [[(2,1), (1,1)], [(2,4), (0,5)], [(1,3), (4,0)], [(1,1), (7,2)], [(3,1), (2,2)]]

q = sorted(l, key=getKey)

z = [i[0] for i in sorted(enumerate(l), key=lambda x:x[1])]

lnew = []
for i in range(len(l)):
    lnew.append(l[z[i]])
    
print(lnew)
print(q)