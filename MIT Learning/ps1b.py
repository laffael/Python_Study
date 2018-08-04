# Python36
# -*- coding: utf-8 -*-
# @Date    : 2018-01-24 14:32:26
# @Author  : Raphael Wang


portion_down_payment = 0.25
current_saving = 0
Number_of_months = 0
r = 0.04


annual_salary = 120000 #input('Enter your annual salary: ')
portion_saved = .05 #input('Enter the percent of your salary to save, as a decimal: ')
total_cost = 500000 #input('Enter the cost of your dream home: ')
semi_anunual_raise = 0.03 #input('Enter the semiannual raise, as a decimal: ')

while current_saving <= total_cost*portion_down_payment:

    current_saving = current_saving + (portion_saved*annual_salary/12) + (current_saving*r/12)

    if Number_of_months%6 == 0:
        annual_salary = annual_salary * (1+semi_anunual_raise)


        Number_of_months += 1

        print ('Number of months:', Number_of_months)
