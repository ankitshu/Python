# class Parent:        
#     def myMethod(self):
#         print ('Calling parent method')
#       
#     def myMethod1(self):
#         print ('Calling parent method-------')
#   
# class Child(Parent): # define child class
#     def myMethod(self):
#         print ('Calling child method')
#   
# c = Child()          # instance of child
# c.myMethod()         # child calls overridden method
# c.myMethod1()
# exit(0)


# class Person:
#   
#     def __init__(self, first, last):
#         print('parent class constructer')
#         self.firstname = first
#         self.lastname = last
#   
#     def Name(self):
#         return self.firstname + " " + self.lastname
#   
# class Employee(Person):
#   
#     def __init__(self, first, last, staffnum):
#         #Person.__init__(self,first, last)
#         #super().__init__(first, last)
#         self.staffnumber = staffnum
#   
#     def GetEmployee(self):
#         return self.Name() + ", " +  self.staffnumber
#   
# #x = Person("Marge", "Simpson")
# y = Employee("Homer", "Simpson", "1007")
#   
# #print(x.Name())
# print(y.GetEmployee())
# exit(0)


# 
# 
# 
# class Person:
#   
#     def __init__(self, first, last):
#         self.firstname = first
#         self.lastname = last
#   
#     def Name(self):
#         return self.firstname + " " + self.lastname
#  
# class Employee(Person):
#   
#     def __init__(self, first, last, staffnum):
#         Person.__init__(self,first, last)
#         self.staffnumber = staffnum
#   
#     def GetEmployee(self):
#         return self.Name() + ", " +  self.staffnumber
#   
# x = Person("Marge", "Simpson")
# y = Employee("Homer", "Simpson", "1007")
#   
# print(x.Name())
# print(y.GetEmployee())
    
    
    
    
    
# class Person:
#   
#     def __init__(self, first, last):
#         self.firstname = first
#         self.lastname = last
#   
#     def __str__(self):
#         print("str method called")
#         return self.firstname + ">> " + self.lastname
# 
# class Employee(Person):
#   
#     def __init__(self, first, last, staffnum):
#         super().__init__(first, last)
#         self.staffnumber = staffnum
#     def __str__(self):
#         return self.firstname + " " + self.lastname + ", " +  self.staffnumber
#       
# #     def __str__(self):
# #         return super().__str__() + ", " +  self.staffnumber
#       
#   
# x = Person("Marge", "Simpson")
# print(x)

 
# y = Employee("Homer", "Simpson", "1007")
# print(y)
# exit(0)