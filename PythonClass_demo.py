# class ClassExmaple:
#     """A simple example class"""
#     
#     def __init__(self):
#         print('INIT called')
#         self.i=10
#      
#     def f(self):
#         self.i=11
#         return 'hello world'
#     
# obj=ClassExmaple()
# # print(obj.i)
# s=obj.f()
# # print(s)
# # print(obj.i)
# #obj.f()
# # 
# #print('obj value',obj.i)
# obj1=ClassExmaple()
# #print(obj1.i)
# obj1.i=20
# print(obj1.i)
# print(obj.i)
# print(obj.f())
# print(obj.i)
# print(obj1.f())
# print(obj1.i)
# 
#  
#print(obj.__doc__)


# class Example2():
#     def __init__(self,arg1,arg2):
#         self.r1=arg1
#         self.r2=arg2
#         print('--------')
#         pass    
#     
#     def fn(self):
#         print(self.r2)
#          
# x=Example2(23,24)
# #print(x.r1)
# #print(x.r2)
# #  
# x.r1=20
# x.r3=200
# print(x.r1)
# print(x.r2)
# print(x.r3)
# del x.r1
# del x.r2
# del x.r3
# print(x.r1)
# print(x.r2)
# print(x.r3)

# x.r1=30
# print(x.r1)







# class human():
#     gender='Male' #class variable
#     def __init__(self,name):
#         self.name=name #instance variable
#   
# a=human("Harsh")
# b=human("Jatin")
#   
# print(a.name)
# print(a.gender)
# b.gender='female'
# print(b.name)
# print(b.gender)
# print(a.gender)
# print(human.gender)
#print(human.name)



# class human_example():
#     fav_food=[]
#     def __init__(self,name):
#         self.name=name
#       
#     def addFav_food(self,food):
#         #print(self.name)
#         self.fav_food.append(food)
#   
# h=human_example('ABC')
# h.addFav_food("Pizza")
# #print(h.name)
# #print(h.fav_food)
# i=human_example('DEF')
# i.addFav_food("Curd")
# print(h.name)
# print(h.fav_food)
# print(i.name)
# print(i.fav_food)
# print(human_example.fav_food)

# class human_example():
#     ii=100
#     def __init__(self,name):
#         self.name=name
#         self.fav_food=[]
#       
#     def addFav_food(self,food):
#         #print(self.name)
#         self.fav_food.append(food)
#       
#     @staticmethod
#     def getCategory(value):
#         #print(self.name)
#         human_example.ii=value
#         print("Human",human_example.ii) 
#         print("---")   
#  
# h=human_example('ABC')
# h.addFav_food("Pizza")
# i=human_example('DEF')
# i.addFav_food("Curd")
# print(h.name)
# print(i.name)
# print(h.fav_food)
# print(i.fav_food)
# print(h.ii)
# print(h.getCategory(10))
# print("---->",h.ii)
# print(i.ii)
# print(human_example.ii)
#  
# print(i.getCategory(20))
# print("---->",i.ii)
# print(human_example.getCategory(30))
# print("---->",human_example.ii)
# print("---->h",h.ii)
# #print("---->i",i.ii)





class methodCall:
    def __init__(self):
        self.data = []
  
    def add(self, x):
        self.data.append(x)
  
    def addtwice(self, x):
        self.add(x)
        self.add(x)
          
obj=methodCall()
obj.addtwice(10)
print(obj.data)        