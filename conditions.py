# a=10
# b=20
# if a > b:
#     print ("Inside IF")
#     print('----')    
# print ("---outside IF")
# exit(0)






# x=1
# if x >= 0:
#     print ('Negative changed to zero')
#     print ('1')
# if x==1:
#     print('Hello')
# exit(0)

#   
#   
# a=10  
# if a>=20:  
#     print ("Condition is True")  
# else:
#     print('I am in else block')  
#     if a>=15:  
#         print ("Checking second value")  
#     else:  
#         print ("All Conditions are false")
# exit(0)
        
        

#  
x=0
if x == 0:
    print("First If")
elif x > 0 and x < 20:
    print( 'Zero')
elif x != 1:
    print( 'Single')
else:
    print( 'More')
   
#exit(0)      
    
# 
x=1     
if(type(x)==str):
    print('true')
else:
    print('false') 
exit(0)   

#  
#  #looping

# s='hello python'
# for alpha in s:
#     print(alpha,end="--")
# exit(0)
#count_list = [1, 2, 3, 4, 5]
 
# fruits = ['apples', 'oranges', 'pears', 'apricots']
# change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# exit(0)
#  
#  for number in count_list:
#      print  ("This is count", number)  
#      
#  for i in change:
#      print ("got ", i)
#  
#  
# range
# seq=range(-1,-10,-2)
# for a in seq: 
#     print(a)
# exit(0)
#      
#  print("-----------------")
#      
# num=2  
# for a in range (6):
#     print  (num*a)
# 
# exit(0)  
#   
#  words = ['cat', 'dog', 'bird']
#  for w in words:
#      print( w, len(w))
#      
# seq_d=range(5, 10)
# for r in seq_d:
#     print(r)
#   
# print("-----------------")
#   
# seq_d1=range(0, 10, 3)
# for s in seq_d1:
#     print(s)   
#   
#   
# for r1 in range(-10, -100, -30):
#     print(r1)
#      
#  a = ['hello', 'the', 'beautiful', 'world']
#  for i in range(len(a)):
#      print(i, a[i])
#  
#  range_list=list(range(10))
#  print(range_list)
#  range_list=list(range(2,10))
#  print(range_list)
#  range_list=list(range(0,10,3))
#  print(range_list)
#  range_list=list(range(0, -10, -1))
#  print(range_list)
#  range_list=list(range(0))
#  print(range_list)
#  range_list=list(range(1,0))
#  print(range_list)
#  
#  i=0
#  num_list=[]
#  while i < 6:
#      print ("At the top i is ",i)
#      num_list.append(i)    
#      i+=1
 
 #for num in num_list:
 # print(num, end= " ")
 
# print("---------")
# a, b = 0, 1
# while b < 10:
#     print("a ",a)
#     print("b",b)
#     a, b = b, a+b 
# exit(0)
 
 
 # break prime number
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
          #loop fell through without finding a factor
        print(n, 'is a prime number')
exit(0)

 #Continue
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
        print("Found a number", num)