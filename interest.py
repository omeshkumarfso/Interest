from calendar import month


monthly_paid_amount = int(input("monthly paid"))
numberOfMonths = int(input("number of months"))
interest = int(input("interest in percent"))

totalBalance = int()
calcTotalBalance = int(monthly_paid_amount)

for i in range(0, numberOfMonths):
    monthly_interest = (calcTotalBalance * (interest/100) * 1/12)
    monthlyTotalAmount = monthly_interest + calcTotalBalance
    totalBalance = monthlyTotalAmount
    calcTotalBalance = monthlyTotalAmount + monthly_paid_amount

print(totalBalance)
