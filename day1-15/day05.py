"""
寻找水仙花数
"""
for i in range(100, 1000):
    a = i // 100
    b = (i - a * 100) // 10
    c = i - a * 100 - b * 10
    if i == a ** 3 + b ** 3 + c ** 3:
        print(i)
        i = i + 1
    else:
        i = i + 1
