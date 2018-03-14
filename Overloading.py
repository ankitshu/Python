class OverLoadExample:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __str__(self):
            return 'Vector (%d, %d)' % (self.a, self.b)
    
        def __add__(self,other):
            print(';;;;')
            return OverLoadExample(self.a + other.a, self.b + other.b)

v1 = OverLoadExample(2,10)
v2 = OverLoadExample(5,-2)
v3 = OverLoadExample(5,20)
print (v1+v2+v3)
#print(5+2)