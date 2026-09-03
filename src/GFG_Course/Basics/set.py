#have distinct items
#unordered
#no indexing
#union,intersection,set difference,etc are fast
# using hashing internally
si={10,20,30}
print(si)
s2=set([20,30,40])
print(s2)
s3={}
print(type(s3))
s4=set()
print(type(s4))
print(s4)

#example2
s={10,20}
s.add(30)
print(s)
s.add(30)
print(s)
s.update([40,50])#update for getting items for other collections like tuple or list
print(s)
s.update({90,80},[60,70])
print(s)
s.update((5,8))
print(s)
s.discard(5)
print(s)
s.remove(40)
print(s)
#difference between discard and remove is that if there is an item like 41 
#and not given in set discard function will not raise an error but the remove 
#function will raise a error or ticket
s.clear()# this clear the items present in the list
print(s)
del s # this deletes the whole object

# some more functions
s={10,30,20,40}
print(len(s))
print(20 in s)
print(50 in s)

#operators on two sets
s1={2,4,6,8}
s2={3,6,9}
print(s1|s2) #union
print(s1&s2)#intersection
print(s1-s2)#difference
print(s1^s2)#symmteric difference
print(si.isdisjoint(s2))#have no common elements
print(s1<=s2)#subset
print(s1<s2)#proper subset
print(s1>=s2)#superset
print(s2>s1)#proper superset
#difference between simple and proper subset or superset is that simple one can be equal but proper one cannot have equal no. of elements