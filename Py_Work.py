# 按照日期分割保存写过的所有代码

# @Date    : 2018-01-23 13:50:44
# @Author  : Raphael Wang

import os
a = 6 + 4 * 10
b = (6 + 4) * 10

print(a)
print(b)

import math
c = math.cos(3.4)**2 + math.sin(3.4)**2
print(c)
print(math.log2(2))
x = 2
print("log(x) = ", math.log2(x))

# ------------------------------------------

# @Date    : 2018-02-11
# @Author  : Raphael Wang
# 打印list当中的元素
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])

print('-----------------------------')

count = 0
while count <= 2:
    print(L[count][count])
    count += 1
    pass
