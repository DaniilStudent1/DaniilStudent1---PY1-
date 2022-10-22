salary = 5000
spend = 6000
months = 10
increase = 0.03
growing = increase + 1
need_money = 0
for money in range(1, months +1):
    money = spend - salary
    spend = spend * growing
    need_money += money
print(round(need_money))