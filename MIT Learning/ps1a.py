# Python36
# -*- coding: utf-8 -*-
# @Date    : 2018-01-24 14:32:26
# @Author  : Raphael Wang


portion_down_payment = 0.25
current_saving = 0
Number_of_months = 0
r = 0.04


annual_salary = 80000 #input('Enter your annual salary: ')
portion_saved = .15 #input('Enter the percent of your salary to save, as a decimal: ')
total_cost = 500000 #input('Enter the cost of your dream home: ')

while current_saving <= total_cost*portion_down_payment:

    current_saving = current_saving + (portion_saved*annual_salary/12) + (current_saving*r/12)

    Number_of_months += 1

print ('Number of months:', Number_of_months)

# 几个改进地方可以操作:
# 1. 需要增加判断数据是否正确(比如说是否为正数的条件判断);
# 2. 可以考虑使用list来进行 current_saving的操作, 已获得每一个月增加的数额.
# 3. 不一定需要使用while, 可以使用for loop+if条件.
