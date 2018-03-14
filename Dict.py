f = {'name': 'Harsh', 'age': 25}
f['location'] = 'delhi'

f['location']
del f['location']

f['gender']='Male'

list(f.keys())
sorted(f.keys())

'name' in f
'age' not in f

f['xyz']
f['name']='Mayank'
f.clear()
f['another']='item'


d=dict([('name','A'),('age',20),('loc','india')])

k_list=list(d.keys())
k_values=list(d.values())
#data=zip(k_list,k_values)

list(d.items())
{x: x**2 for x in (2, 4, 6)}
dict(x=413, y=412, z=409)
str(dict)



#IMMUTABLE
dic = { [1,2,3]:"abc"}
dic = { (1,2,3):"abc", 3.14:"abc"}


w={"house":"Haus","cat":"Katze","red":"rot"}
w1 = {"red":"rouge","blau":"bleu"}
w.update(w1)




#looping
for k in d:
    print(k)
    print(d[k])
    
for v in d.values():
    print(v)

for k,v in d.items():
    print(k,'---',v)
    
len(d)



my_list = [1, 2, 3]
my_dict = dict.fromkeys(my_list,0)


my_dict = {"1": 1, "2": 2, "3": 3}
new_dict = dict.fromkeys(my_dict)
my_dict.get("1")
my_dict.get("4",'default')


d.pop('name')
d.pop('x','empty')
d.popitem()
f.setdefault("xyz",'random')


letter_counts={}
for letter in "Mississippi":
    letter_counts[letter] = letter_counts.get(letter, 0) + 1
    