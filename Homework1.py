print("number 1")
import math
r = (int(input("Введите радиус в сантиметрах: \n")))
x = r*0.01
l = 2*math.pi*x
s = math.pi*x**2
print(round(l, 3))
print(round(s, 3))
print("number 2")
x = 10
y = 55
z = 0
print(x)
print(y)
z = x
x = y
y = z
print(x)
print(y)
print("number 3")
import math
l = (int(input("Введите длинну в метрах: \n")))
g = 9.81
t = 2*math.pi*math.sqrt(l/g)
print(round(t, 3))