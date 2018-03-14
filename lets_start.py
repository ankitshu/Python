# Commenting
a=1 #comment
#comment is just use for code readability
name="#isko comment mat samagh lena"
print(name)
 
#basic operators
a=2+2
print(a)
print(2+3)
print(40-4*2)
#grouping
a=(40-4)/5
print(a)
print(type(a))

#floor division
print(17/3)
print(17//3)
print(17%3)
print(5*3+2)
print(4**2)

w=5*4
y=10
x=w+y
print(x)


tax = 12.5 / 100
price = 100.50
print(price * tax)
x=round(price * tax, 2)
print(x)


#relationalops
print(10>20)
print(2<1)
print(20<=20)
print(20>=20)
print(20<=19)
print(20<=21)
print(20==20)
print(20==19)
print(20!=19)
print(20!=20)

#assignment operators
a=10
print(a)
a+=10
print(a)
a-=5
print(a)
a*=5
print(a)
a**=2
print(a)
a//=7
print(a)
a%=5
print(a)
a/=10
print(a)

a=10
b=5
a+=b
print(a)

#logical-ops
a=5>4 and 3>2  
print (a)  
b=5>4 or 3<2  
print (b)  
c=not(5>4)  
print (c)  


#Strings
print('Hello')
print("Hello Python")
print('doesn\'t')
print("doesn't")
print('Oh . "My God"')
print("Oh . \"My God\"")
print('I couldn\'t do that, can you?')
#concatination
word='hello' 'python'
print(word)
#word 'again'
a=word+'again'
print(a)

#repeat
a='Hello'
b=a*2
print(b)
c=b+"world"
print(c)
print('hello'*2+"python")

#indexing
word="Hello Python"
print(word[0])
print(word[1])
print(word[6])
#print(word[12])
print(word[-1])
print(word[-2])
print(word[-6])
print(word[-12])
#print(word[-13])

#slicing
 

#error-slicing
#print(word[30])
print(word[2:30])
print("---"+word[30:])

#IMMUTABLE
#word[3]="H"
a="Hi"+word[5:]
print(a)