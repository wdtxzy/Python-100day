username = input("请输入用户名")
password = input("请输入密码")
if username == 'admin' and password == '123456':
    print("身份验证成功")
else:
    print('身份验证失败')

"""
英制单位英寸和公制单位厘米互换
"""

value = float(input("请输入长度： "))
unit = input("请输入单位： ")
if unit == 'in' or unit == '英尺':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('请输入正确的单位')
