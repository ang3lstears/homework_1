print("номер 1")
sum = 0
x = 1
n = int(input("введите верхний предел \n"))
if n <= 100:
    while x <= n:
        a = x*x*x
        sum += a
        x += 1
else: print("введите число меньше 100:")
print(sum)

print("nomer 2")
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