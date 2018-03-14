List=['a',1,"Hello",234]
#append
List.append(2)
print(List)
List2=["b","Pyhton",10]
List.append(List2)
print(List)

#extend
List.extend(List2)
print(List)

#Insert
List.insert(1,"new")
List.insert(0,"first")

# remove
colours = ["red", "green", "blue", "green", "yellow","green","blue"]
colours.remove("green")

#pop
cities = ['delhi','gurgaon','mumbai','pune','nagpur','lucknow']
item=cities.pop(2)
print(item)
print(cities)
item=cities.pop()
print(item)
print(cities)

cities.clear()

#index
i=colours.index("green")
j=colours.index("green",2)
k=colours.index("green",4,6)
colours.index("brown")

#count
c=colours.count("green")
c=colours.count("yellow")
c=colours.count("brown")

#reverse
cities.reverse()


#list comprehensions
cubes = []
for c in range(5):
    cubes.append(c**3)
cubes = [i**3 for i in range(6)]

vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]
[x for x in vec if x >= 0]
[abs(x) for x in vec]
List=[' Hello ',"Python "]
[str1.strip() for str1 in List]
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]



#del
l = ['a','b','c','d','e','f','g']
del l[0]
print(l)

del l[2:4]
print(l)

del l[:]
print(l)
