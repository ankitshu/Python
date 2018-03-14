cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")

a= 'Hello.python'
length_a = 12
b='hello_world'
length_b=11

print ("value of a is  %s." % a)
print ("length of a is  %d." % length_a)
print ("So first string is  %s and second is %s ." % (a,b))
print ("So first string is  %s and length is %d while second is %s and length is %d ." % (a,length_a,b,length_b))





print ("." * 10)

a1 = "a"
b2 = "b"
c3 = "c"
d4 = "d"
e5 = "e"
f6 = "f"
g7 = "g"
h8 = "h"
i9 = "i"
j10 = "j"
k11 = "k"
m12 = "l"


print (a1 + b2 + c3 + d4 + e5 + f6)
print(g7 + h8 + i9 + j10 + k11 + m12)

months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print ("Here are the months: ", months)


print ("""
Hi This is python class
to learn python.
After class we will be able to code in python.
""")
