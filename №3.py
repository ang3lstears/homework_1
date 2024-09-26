import math
l = (int(input("Введите длинну в метрах: \n")))
g = 9.81
t = 2*math.pi*math.sqrt(l/g)
print(round(t, 3))