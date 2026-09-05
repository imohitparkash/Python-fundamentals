#implicit type conversion
a=10
b=1.5
c=a+b 
print(c)
d=True
e=a+d
print(e)

#explicit type conversion
#example 1
s="135"
i=10+int(s)
print(i)
f=float(s)
print(f)

#example 2
k="banana"
print(list(k))
print(tuple(k))
print(set(k))

#example 3
l=['a','b','c']
print(l)
print(str(l))
print(type(l))
a=10
b=11
c=str(a)+str(b)
print(c)
d=12.5
print(str(d))

#example 4
t=(10,20,30)
print(list(t))
s={10,20,30}
print(list(s))

