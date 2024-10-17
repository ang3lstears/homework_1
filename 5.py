import math
xx = int(input("введите координату x для оси абцисс \n"))
xy = int(input("введите координату x для оси ординат \n"))
yx = int(input("введите координату y для оси абцисс \n"))
yy = int(input("введите координату y для оси ординат \n"))
zx = int(input("введите координату z для оси абцисс \n"))
zy = int(input("введите координату z для оси ординат \n"))
def yg():
    x = math.atan(xy / xx)
    y = math.atan(yy / yx)
    z = math.atan(zy / zx)
    if x < y and x < z:
        print(f'наименьший угол у точки x с координатами {xx} {xy}')
    elif y < x and y < z:
        print(f'наименьший угол у точки y с координатами {yx} {yy}')
    else: print(f'наименьший угол у точки z с координатами {zx} {zy}')
yg()