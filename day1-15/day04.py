"""
用for循环实现1~100求和
"""
sum = 0
for x in range(101):
    sum += x
print(sum)

import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print("大一点")
    elif number > answer:
        print('小一点')
    else:
        print("恭喜你答对了")
        break
print('你一共猜了%d次' % counter)

"""
判断一个数是否为素数
"""
from math import sqrt

num = int(input('请输入一个正整数： '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
