#function syntax
#def functionNameHere(parameters):
#your code here

#docstring
def functionNameHere(parameters):
    """place your doc string here"""
    #rest of the code.
    
    
def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b
    
fib(4)
print(fib)
func1=fib
func1(4)
print(func1)
 

#return
def return_func():
    return "this is returned from function"   

print(return_func())


def return_fib(n): 
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a) 
        a, b = b, a+b
    return result

var=return_fib(2)
var

#default param
def default_param_func(a=2,b=4,c=2,d=4):
    return a+b+c+d

print(default_param_func())
print(default_param_func(1,2))
print(default_param_func(1,2,3,4))

i = 50
def default_func1(arg=i):
    print(i)
    print(arg)
   
default_func1()
i = 60
default_func1()

#caution
def default_arg_f(a, List=[]):
    List.append(a)
    return List

print(default_arg_f(1))
print(default_arg_f(2))
print(default_arg_f(3))

L=[1,2,3]
def fnList(arg=L):
    print(arg)
    print(L)


#suggestion
def default_arg_f1(a, List=None):
    if List is None:
        List = []
    List.append(a)
    return List

#keyword arguments
def keyword_arg_func(var,a=2,b="Hello",c=4):
    print(var,a,b,c)

keyword_arg_func(100)
keyword_arg_func(var=200)
keyword_arg_func(var=200,c=5)
keyword_arg_func(b="Python",var=200)
keyword_arg_func(1,2,3,4)
keyword_arg_func(100,b="Python")
#incorrect ones
keyword_arg_func()
keyword_arg_func(var=200,2)
keyword_arg_func(100,var=200)
keyword_arg_func(d=1000)
        
#arbitrary args
def fn(*a):
    print(type(a))
    print(a)
    
def concat(delim='-',*args):
    print(delim)
    print(type(args))
    print("args ",args)
    return delim.join(args)
concat("--","earth", "mars", "venus","moon")

def concat(*args,delim="-"):
    return delim.join(args)
concat("earth", "mars", "venus","moon")
concat("earth", "mars", "venus","moon",delim="/")


def f(): 
    print(s) 
s = "123"
f()

def f11(): 
    s = "1234"
    print(s) 

s = "12345" 
f()
f11()
print(s)


def final_f():
    print(s)
    s1="4321"
    print(s1)
s="7896"
f()
f11()
final_f()


def final_update_f():
    global s
    print(s)
    s="41321"
    print(s)
    
    
def final_update_f11():
    s="41321"
    print(s)
    global s
    print(s)

s="78961"
f()
f11()
final_update_f()
print(s)

s="10"
def final_update_f1():
    global s
    t="11"
    print(s)

f()
f11()
final_update_f()
print(s)





#example
def example_fun(x, y):
    global a
    a = 42
    x,y = y,x
    b = 33
    b = 17
    c = 100
    print(a,b,x,y)
a,b,x,y = 1,15,3,4
example_fun(17,4)
print(a,b,x,y)





ads=2
def fun1():
    ads=3
    print(ads)
    def fun2():
        #global ads
        print(ads)
        #ads=100
        print(ads)
    fun2()    
fun1()
ads

#console input
a = input("give the value of a ")
b = input("give the value of b ? ")
c = input("give the value of c ? ")

print ("So, a=  %r  ,b= %r and c = %r." % (a, b, c))


#



def print_two(arg1,arg2):
    print ("arg1: %r, arg2: %r" % (arg1, arg2))

print_two(1,20)
