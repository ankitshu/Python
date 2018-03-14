#10 * (1/0)
#4 + s*3
#'4' + 3

# while True:
#     try:
#         x = int(input("give a number: "))
#         print("Fine")
#         break
#     except :
#         print("invalid number...")
        

  
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
#        
# except ValueError:
#     print("Value error is found")
# # except OSError:
# #     print("OS error: ")    
# except:
#     print("Unknown error")
      
# exit(0)

# try:
#     '3' + 3
# except:
#     print('Exception occured')
# else:
#     print('execution because No error is there ')        
# exit(0)  

# try:
#     '3' + 3
# except TypeError as yogesh :
#     print(type(yogesh))
#     print('Exception occured',yogesh.args)
# else:
#     print('execution because No error is there ')      
# exit(1)
 
 
#exception in function
# def this_fails():
#     try:
#         x = 1/0
#     except:
#         print('------')   
#   
# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)
   
 
 
 
#raise exception
#raise Exception('harsh', 'sharma')
# try:
#     print('------')
#     raise Exception('harsh', 'sharma')
#     print('||||||||')
# except Exception as ex:
#     print(type(ex))    
#     print(ex.args)     
#     print(ex)          
#     x, y = ex.args     
#     print('x =', x)
#     print('y =', y)
#  
# exit(0)
 
    
    
#FUNCTION
# def validation( age ):
#     if age <18:
#         raise Exception(age,'Not a valid voter')  
#     return age
#   
# try:
#     age = validation(10)
#     print ("age = ",age)
# except Exception as e:
#    print ("error in validation fn ",e.args[1])  
      
# exit(0)

#custom exception
# 
# class MyError (Exception):
#     def __init__(self,value,message):
#         self.value=value
#         self.message=message
#   
# try:
#     x=int(input("take a number"))
#     if x < 18:
#         raise MyError(x,'small then 18')
#     else:
#         print('valid input ',x)
# except MyError as e:
#     print(type(e))
#     print(e.args)
#      
#      
# exit(0)

#finally
def divide(x, y):
    try:
        result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
    except ValueError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
# 
try:
  divide(2, 0)
except:
   print("-------")
# exit(0)            