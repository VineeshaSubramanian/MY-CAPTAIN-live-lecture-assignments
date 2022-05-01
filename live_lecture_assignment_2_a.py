mydict = {
    "country" : "Norway",
    "capital" : "Oslo",
    "coastline" : "25.148 km",
    "continent" : "Europe",
    "neighbouring countries" : "Sweden and Finland",
    "national animal" : "Lion"
    }
print(mydict)

x = mydict.copy()
print(x)

x = mydict.get("continent")
print(x)

x = mydict.items()
print (x)

x = mydict.keys()
print (x)

x = mydict.pop("continent")
print (x)

x = mydict.popitem()
print (x)

x = mydict.setdefault("country")
print (x)

x = mydict.update({"national sport" : "cross country skiing"})
print (x)

x = mydict.values()
print (x)

mydict.clear()
print(mydict)

a = ('key1', 'key2', 'key3')
b = 18

mydict = dict.fromkeys(a,b)
print(mydict)

