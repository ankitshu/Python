def foo():
    print ("begin")
    for i in range(3):
        print ("before yield", i)
        yield i
        print ("after yield", i)
        print ("end")
f = foo()
print(next(f))
print("-------")
print(next(f))
print(next(f))

def city_generator():
    yield("Konstanz")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")
  
x = city_generator()
print(next(x))

def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    #print(n)
    yield n
 
    n += 1
    print('This is printed second')
    #print(n)
    yield n
 
    n += 1
    print('This is printed at last')
    #print(n)
    yield n
 
a=my_gen()
print(next(a))
print(next(a))
print(next(a))
# 
for items in a:
    print(items)
# 
# 
a = (x*x for x in range(5))
for it in a:
    print(it)
print(sum(a))
