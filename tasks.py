#1
num = input('Введите число: ')
sum = 0
for a in num:
    if a.isdigit():
        sum += int(a)

print(f"Сумма {num} равна: ", sum)


#2
from msilib import sequence

n = int(input('Введите число: '))

def get_squerence(n):
    return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

nums = get_squerence(n)
print(nums)
print(round(sum(nums), 5))

#3
import random
list = [0,1,2,3,4,5,6,7,8,9]
print ("Начальный список: " + str(list))

for i in range(len(list)-1, 0, -1):
    j = random.randint(0, i + 1)
    list[i], list[j] = list[j], list[i]
print ("Перемешанный список: " + str(list))