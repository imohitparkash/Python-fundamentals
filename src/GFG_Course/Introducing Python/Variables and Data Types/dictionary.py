###Collection of key value pairs
#unordered
#All keys must be different
#Values may ne repeated
#All key must be distinct
#Uses hashing internally 
####
d={110:"xyz",101:"abc",501:"abc",104:"gfk"}
print(d)
m={ }
m["laptop"]=40000
m["moble"]=15000
m["earphone"]=1000
print(m)
print(m["moble"])
print(d[101])
#get function
print(d.get(110))
print(d.get(125,"Not available"))
print(d.get(104))
if 125 in d:
    print(d[125])
else:
    print("NA")
#program 3
d[101]="lmn"
print(len(d))
print(d)
print(d.pop(101))
print(d)
del d[501]
print(d)
d[108]="dsa"
print(d.popitem())