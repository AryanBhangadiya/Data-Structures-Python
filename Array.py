# stock_prices =[2,3,5,6]

# stock_names = ["AAPL", "IBM", "TATA"]

# stock_data = [
#     {"ticker":"AAPL", "price": 302},
#     {"ticker":"TSLA", "price": 902},
#     {"ticker":"TATA", "price": 278}
# ]
# for i in range(len(stock_data)):
#     print(stock_data[i])

# stock_prices = [[2, 3, 5, 6], [40, 42, 38, 44], [78, 89, 71, 66]]

# print(stock_prices[1][1])


my_expense = [2200, 2350, 2600, 2130, 2190]


# 1. In Feb, how many dollars you spent extra compare to January?
print("In feb this much extra is paid as compared to jan:", my_expense[1] - my_expense[0])

# 2. Find out your total expense in first quarter (first three months) of the year.
print("Expense in the first three quarter:",my_expense[0] + my_expense[1] + my_expense[2])

# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent 2000$ in any month:", 2000 in my_expense)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
my_expense.append(1980)
print("Expenses at the end of June:", my_expense)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

my_expense[3] = my_expense[3] + 200

print("My updated expenses:", my_expense)