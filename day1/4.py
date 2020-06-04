#day1
#program 4

cost_price = int(input("enter cost price"))
selling_price = int(input("Enter selling price"))

profit = selling_price - cost_price
#Calculating 5% increase in profit
new_profit = ((5/100 * profit)+profit)
selling_price = cost_price + new_profit

print("profit from sell is : ",profit)
print("Selling price for increased profit of 5%  will be: ",selling_price)