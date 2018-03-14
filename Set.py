a = set('abracadabra')
print("---",a)
b=set('alacazam')
print("---",b)
print(a-b)
print(a | b)
print(a & b)
#print(a ^ b)
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
x=set("A pyhton tutorial")
print(x)
x = set(["Perl", "Python", "Java"])
cities = set(("Paris", "Lyon", "London","Berlin","Paris","Birmingham"))
print(cities)

colours = {"red","green"}
colours.add("yellow")
colours.clear();

set1={1,2,3,4}
set2=set1.copy()
set1.clear();
set2

x = {"a","b","c","d","e"}
y = {"b","c"}
z = {"c","d"}
x.difference(y)
x.difference(y).difference(z) 

#x=x-y
x = {"a","b","c","d","e"}
y = {"b","c"}
x.difference_update(y)

x = {"a","b","c","d","e"}
x.discard("a")
x.discard("z")

x = {"a","b","c","d","e"}
x.remove("a")
x.remove("z")

x = {"a","b","c","d","e"}
y = {"c","d","e","f","g"}
x.intersection(y)
x&y


x = {"a","b","c"}
y = {"c","d","e"}
x.isdisjoint(y)

x = {"a","b","c"}
y = {"d","e","f"}
x.isdisjoint(y)
 
x = {"a","b","c","d","e"}
y = {"c","d"}
x.issubset(y)
y.issubset(x)
x < y
y < x
x < x
x<=x

x.issuperset(y)
x > y
x >= y
x >= x
x > x
x.issuperset(x)