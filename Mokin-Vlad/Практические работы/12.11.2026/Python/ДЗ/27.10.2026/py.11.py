# Задание 1
a = int(input())
b = int(input())
s1 = 0
s2 = 0
s3 = 0
k1 = 0
k2 = 0
k3 = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        s1 = s1 + i
        k1 = k1 + 1
    else:
        s2 = s2 + i
        k2 = k2 + 1
    if i % 9 == 0:
        s3 = s3 + i
        k3 = k3 + 1

print("Четные:", s1, s1 / k1)
print("Нечетные:", s2, s2 / k2)
print("Кратные 9:", s3, s3 / k3)


# Задание 2
n = int(input())
s = input()

for i in range(n):
    print(s)


# Задание 3
while True:
    n = int(input())
    if n == 7:
        print("Good bye!")
        break
    elif n > 0:
        print("Number is positive")
    elif n < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")


# Задание 4
n = int(input())
summa = n
max_num = n
min_num = n

while n != 7:
    n = int(input())
    if n == 7:
        print("Good bye!")
        break
    summa = summa + n
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n

print("Сумма:", summa)
print("Максимум:", max_num)
print("Минимум:", min_num)
