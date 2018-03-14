#list data type
squares = [1, 4, 9, 16, 25]
print(squares)

#indexing
print(squares[0])
print(squares[-1])

#slicing
print(squares[2:])
print(squares[-2:])

list_copy=squares[:]
print(type(list_copy))
#concatination
new_list=squares + [36, 49, 64, 81, 100]
print(type(new_list),new_list)

#mutablity
cubes = [1, 8, 27, 65, 125]
print(id(cubes))
cubes[3]=64
print(id(cubes),cubes)
cubes.append(6**3)
print(cubes)
cubes[2:5]=[12,13,14]
print(cubes)
cubes[2:5]=[]
print(cubes)
cubes[:]=[]
print(cubes)
print(len(cubes))


#nested List
alpha=['a','b','c','d']
num=[5,30,10,5]
new_list=[alpha,num]
print(new_list)
print(new_list[0])
print(new_list[1])
print(new_list[0][2],(new_list[1][3]))
alpha.append('e')
print(new_list)


#in and not in
if('c' in alpha):
    print("it gives true")

if('e' in alpha):
    print("it gives true")
    
if('c' not in num):
    print("it gives true")

if(10 not in  num):
    print("it gives true")
