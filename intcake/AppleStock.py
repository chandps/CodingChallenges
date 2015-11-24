"""
returns only max profit without the corresponding time/index
Algorithm: greedy approach, optimal solution so far for each iteration
Running time: O(n) - Linear
"""


# returns 6 (buying $5 and selling for $11)
def get_max_profit(stock_prices_yesterday):
    min_price = stock_prices_yesterday[0]
    max_profit = 0
    for current_price in stock_prices_yesterday:
        min_price = min(current_price, min_price)
        current_profit = current_price - min_price
        max_profit = max(current_profit, max_profit)
    return max_profit

"""
returns a list containing corresponding min, max index and max profit
Algorithm: greedy approach, optimal solution so far for each iteration
Running time: O(n) - Linear
"""


# returns [2,4,6] (buying $5 and selling for $11)
def get_max_profit_index(stock_prices_yesterday):
    min_price = stock_prices_yesterday[0]
    max_profit = min_index = max_index = next_min_index = 0

    for index, current_price in enumerate(stock_prices_yesterday):
        if current_price < min_price:
            next_min_index, min_price = index, current_price

        current_profit = current_price - min_price
        if current_profit > max_profit:
            max_profit, max_index = current_profit, index
            min_index = next_min_index
    solution = [min_index, max_index, max_profit]
    return solution


stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
print(get_max_profit_index(stock_prices_yesterday))
