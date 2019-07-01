"""
test
"""
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

"""
华氏度温度转摄氏度
"""
f = float(input('请输入华氏度 F = '))
print('%d 华氏度转为摄氏度为：%d' % (f, ((f - 32) / 1.8)))

"""
输入园的半径计算圆的周长和面积
"""
import math

r = int(input('请输入圆的半径 r = '))
print('半径为%d的周长为%d' % (r, 2 * r * math.pi))
print('半径为%d的面积为%d' % (r, (r ** 2 * math.pi) / 2))

"""
判读输入的年份是否为闰年
"""
year = int(input("请输入年份："))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print("%d年是否为闰年：%d" % (year, is_leap))
