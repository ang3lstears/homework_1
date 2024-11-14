# номер 1
''' sum = 1
x = 1
n = int(input("введите верхний предел \n"))
if n <= 100:
    while x <= n:
        x += 1
        print(x)
        a = x*x*x
        print(a)
        sum += a
else: print("введите число меньше 100:")
print(sum)
'''
# номер 2
print("    ", end="")
for i in range(1, 10):
    print(f"{i:3}", end=" ")
print()
print("    " + "----" * 9)
for i in range(1, 10):
    print(f"{i:2} |", end=" ")
    for j in range(1, 10):
        print(f"{i * j:3}", end=" ")
    print()