import math
r = (int(input("Введите радиус в сантиметрах: \n")))
x = r*0.01
l = 2*math.pi*x
s = math.pi*x**2
print(round(l, 3))
print(round(s, 3))