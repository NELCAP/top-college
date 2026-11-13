import random

# задание 1
a = []
for i in range(10):
    a.append(random.randint(-10, 10))
print(a)

s1 = 0
s2 = 0
s3 = 0
p1 = 1
first = -1
last = -1

for i in range(len(a)):
    if a[i] < 0:
        s1 = s1 + a[i]
    if a[i] % 2 == 0:
        s2 = s2 + a[i]
    if a[i] % 2 != 0:
        s3 = s3 + a[i]
    if i % 3 == 0:
        p1 = p1 * a[i]
    if a[i] > 0:
        if first == -1:
            first = i
        last = i

i1 = a.index(min(a))
i2 = a.index(max(a))
if i1 > i2:
    t = i1
    i1 = i2
    i2 = t

p2 = 1
for i in range(i1 + 1, i2):
    p2 = p2 * a[i]

s4 = 0
for i in range(first + 1, last):
    s4 = s4 + a[i]

print("Сумма отрицательных:", s1)
print("Сумма четных:", s2)
print("Сумма нечетных:", s3)
print("Произведение кратных 3:", p1)
print("Произведение между min и max:", p2)
print("Сумма между положительными:", s4)

# задание 2
b = []
for i in range(10):
    b.append(random.randint(-10, 10))
print(b)

chet = []
nechet = []
otr = []
pol = []

for x in b:
    if x % 2 == 0:
        chet.append(x)
    if x % 2 != 0:
        nechet.append(x)
    if x < 0:
        otr.append(x)
    if x > 0:
        pol.append(x)

print("Четные:", chet)
print("Нечетные:", nechet)
print("Отрицательные:", otr)
print("Положительные:", pol)
