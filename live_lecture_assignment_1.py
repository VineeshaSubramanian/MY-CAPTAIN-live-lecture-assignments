x = input ("enter your name:")
print ("hello" , x)

x1 = "how are you doing today?"
x2 = x1.capitalize()
print(x2)

x2 = x1.casefold()
print(x2)

x2 = x.center(17)
print (x2)

x3 = "i love mango sceneted candles because not only do they smell great, but mango is also my favourite fruit"
x2 = x3.count ("mango")
print(x2)

x2= x.encode()
print("my name is" ,x2)

x4= "hope you're having a great day!"
x2= x4.endswith("!")
print(x2)

txt = "H\te\tl\tl\to"
x2 =  txt.expandtabs(4)
print(x2)

x2 = x3.find("love")
print(x2)

x2= "my name is {}, i'm a {}".format( x , "tutor")
print(x2)

x2= x3.index("candles")
print(x2)

n= "covid19"
x2= n.isalnum()
print(x2)

x2= n.isalpha()
print (x2)

x2= n.isascii()
print (x2)

y = "\u0030"
z = "\u0047"
print(y.isdecimal())
print(z.isdecimal())

n1= "171999"
x2= n.isdigit()
print(x2)

x2 = n.isidentifier()
print(x2)

x2= x3.islower()
print(x2)

x2= n1.isnumeric()
print(x2)

x2= x3.isprintable()
print(x2)

x2= n1.isspace()
print(x2)

x2= x3.istitle()
print(x2)

n3= "EARTH"
x2= n3.isupper()
print(x2)

n4= (" Thor", " is", " the", " strongest", " avenger")
x2= "*".join(n4)
print(x2)

x2= n3.ljust(10)
print (x2, "is a planet.")

x2= n3.lower()
print(x2)

n5= "        Thor"
x2= n5.lstrip()
print("of all the marvel characters", x2 , "is my favourite")

n6= "hahahahahahahahahaha"
x2= n6.maketrans("h","l")
print(x2)

n7= " i love all italian dishes, especially pizza and ravioli"
x2= n7.partition("dishes")
print(x2)

x2= n7.replace("ravioli", "anglio olio")
print(x2)

x2= x3.rfind("mango")
print(x2)

x2= n3.rjust(10)
print(x2, "is a planet")

x2= n7.rpartition("dishes")
print(x2)

n8 = "captain america, thor, ironman, hawkeye, coulson, fury"
x2= n8.rsplit(",")
print(x2)

x2= n7.split()
print(x2)

x2= n7.splitlines()
print(x2)

x2= n7.startswith("i")
print(x2)

n8= "HELLO my name is NICK FURY"
x2= n8.swapcase()
print(x2)

x2= n7.title()
print(x2)

x2= n7.upper()
print(x2)

x2= n8.zfill(50)
print(x2)

#following are list methods for python

a = ['norway', 'finland', 'sweden', 'italy', 'france', 'greece']
b = ['athena', 'zeus', 'thor', 'aries', 'odin', 'poseidon']
c = ['maharashtra', 'goa', 'kerala', 'delhi']

c.clear()
print(c)

l= a.copy()
print(l)

l= b.count("zeus")
print(l)

a.extend(b)
print(a)

l= a.index("finland")
print(l)

a.insert(4, "antartica")
print(a)

a.pop(4)
print(a)

b.remove("thor")
print(b)

b.reverse()
print(b)

a.sort()
print(a)

b.append("artemis")
print(b)
