def f(x):
    return x * 2
z = f(8)
if z == 12:
    print ("z равно 12")
else:
    print ("z не равно 12")

len("Python")

str(100)

int("22")

float(235)

age = input("Укажите возраст: ")
int_age = int(age)
if int_age < 24:
    print ("Вы молоды")
else: 
    print ("Ну вы и старый")

def even_odd(x):
    if x % 2 == 0:
        print ("even")
    else:
        print ("odd")
even_odd(2)
even_odd(3)

def f(x):
    return x ** 2
result = f(22)
print(result)
 
def f(x = 58, y = 67, z = 79): 
    return x + y + z
print (f())
print (f(23,54,12))
print (f(22,8090,2312))
    
def f(x = 34):
    return x // 2
print (f())

def f(x = 43):
    return x * 4
print (f())
print (f(17))

a = input("число: ")
a = float(a)
try:
    print(float(a))
except (FloatingPointError, ValueError):
    print ("None")




