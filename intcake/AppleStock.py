"""
returns only max profit without the corresponding time/index
Algorithm: greedy approach, optimal solution so far for each iteration
Running time: O(n) - Linear
"""
def get_max_profit(stock_prices_yesterday): # returns 6 (buying $5 and selling for $11)
	min_price = stock_prices_yesterday[0]
	max_profit = 0
	for current_price in stock_prices_yesterday:
		min_price = min(current_price, min_price)
		#max_price = max(current_price, max_price)
		current_profit = current_price - min_price
		max_profit = max(current_profit, max_profit)
	return max_profit


stock_prices_yesterday = [10, 7, 5 , 8, 11, 9]
print(get_max_profit(stock_prices_yesterday))