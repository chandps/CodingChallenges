# Apple Stock

Returns the best profit could have been made from 1 purchase and 1 sale
Algorithm: greedy approach, optimal solution so far for each iteration
Time Complexity: O(n) - Linear
Space Complexity: O(1)


''' normal stock prices '''
def stock_prices(data):
	if len(data) < 1:
		return 0
	
	buy, sell, profit = data[0], data[0], 0
	
	for price in data:
		
		if price < buy:
			buy = price
			sell = price
		
		sell = max(sell, price)
		
		profit = max(profit, sell - buy)
	
	return profit
	


''' reversed stock prices '''
def reversed_stock_prices(data):
	
	if len(data) < 1:
		return 0
	
	buy, sell, profit = data[0], data[0], 0
	
	for price in data:
		
		if price > buy:
			buy = price
			sell = price
		
		sell = min(sell, price)
		
		profit = max(profit, buy - sell)
		
	return profit
 
 
stockPrices = [10,7,5,8,11,9]
print(stock_prices(stockPrices2))
