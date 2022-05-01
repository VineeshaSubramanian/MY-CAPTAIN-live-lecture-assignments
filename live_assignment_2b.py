a = {"Norway" , "Sweden" , "Finland" , "Italy" , "Egypt" , "India" }
b = {"France" , "Norway" , "Finland" , "Italy" , "Sweden" }
print(a)

a.add("Canada")
print(a)

x = a.copy()
print(x)

x = a.difference(b)
print (x)

a.difference_update(b)
print (a)

a.discard("Egypt")
print (a)

x = a.intersection(b)
print (x)

a.intersection_update(b)
print (a)

x = a.isdisjoint(b)
print (x)

x = a.issubset(b)
print (x)

x = a.issuperset(b)
print (x)

b.pop()
print (b)

x = a.symmetric_difference(b)
print(x)

a.symmetric_difference_update(b)
print(a)

c = a.union(b)
print(c)

a.update(b)
print(a)

c.clear()
print(c)
