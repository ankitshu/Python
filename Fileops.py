#open(filename,mode)
#w(write),r(read),a(append),'r+'(for r and w both)
f=open('/home/harsh/Entertainment/python_training/files/demo2.txt')
print(f.name)
print(f.mode)
print(f.closed)


s=f.read(4)
print(s,'-')
print('---->',f.read())
#s=f.readline()

#loop
for line in f:
    print(line)
    print('===============')
print(list(f))
print('-->',f.readlines())

f=open('/home/harsh/Entertainment/python_training/files/demo.txt','r+')
f.write("->>>>>>>")
f.write("----------")
print(f.read())

f=open('/home/harsh/Entertainment/python_training/files/demo2.txt','w')
value = ('Hi this is a tuple', 24)
s = str(value)  
print(f.write(s))

#f.close()
with open('/home/harsh/Entertainment/python_training/files/demo_r.txt') as f:
    data=f.read()
    print(data)
# print(f.closed)



#serializing and de-serializing
import json
l=[12,'Hello',[1,2,3]]
s=json.dumps(l)
print(s)

f=open('/home/harsh/Entertainment/python_training/files/demo_jsonl','w')
#l=[12,'Hello',[1,2,3]]
json.dump(l,f)
s=json.load(f)
print(s)
print(type(s))
f.close()

m = {'age': 6, 'name': 'harsh'}  
n = json.dumps(m)
print(n)
print(type(n))
 
o = json.loads(n) 
print(type(o)) 
print (o['age'], o['name'])