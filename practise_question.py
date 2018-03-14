# f=open('filename')
# print(f.name)
# counter = 1;
# dict2 = {};
# for sLine in f:
#     sLine = sLine.split()    
#     for sWord in sLine:        
#         dict2[sWord]= dict2.get(sWord, 0) + 1
# print(dict2)
# F1=open('filename.txt', 'r+')
# 
# import json
# dict1=json.load(F1)
# print(dict1)
# new_dict = dict.fromkeys(dict1)
# print(new_dict)

#from collections import Counter
#A = Counter(dict2)
#B = Counter(dict1)
#print(A + B)

class employee():
    location = "New Delhi"

    def __init__(self,salary,name,employeeID):
        self.emloyee=[]
        self.dict = {}
        self.emloyee.append(salary)
        self.emloyee.append(name)
        self.emloyee.append(employeeID)
        
    #def name(self,name):
    #    self.emloyee.append(name)
        
    #def employeeID(self,empId):
    #    self.emloyee.append(empId)
    

h = employee('100000','Absi','23')
print(h.emloyee)
h = employee('100001','Absihfhffh','24')
print(h.emloyee)
h.dict['salary'] = '10000'
print(h.dict)



# h.name('abhishek')
# print(h.emloyee)
# h.employeeID('64')


 #h.addFav_food("Pizza")
        
