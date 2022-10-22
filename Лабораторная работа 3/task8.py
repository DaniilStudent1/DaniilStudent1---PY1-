money_capital = 10000
salary = 5000
spend: int = 6000
increase = 1.05
month = 0
R = salary - spend
spend *= increase
while money_capital + R >= spend:
    money_capital += R
    month += 1
print(month)