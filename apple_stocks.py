def my_function(arg):
    # write the body of your function here
    max_value = None
    for n in range(len(arg)): 
        for i in range(1, len(arg)-n):
            if arg[i+n]-arg[n] > max_value or max_value is None:
                max_value = arg[i+n]-arg[n]
    return max_value

# run your function through some test cases here
# remember: debugging is half the battle!
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
print my_function(stock_prices_yesterday)


#optimized solution O(n)

def get_max_profit(stock_prices_yesterday):

    max_profit = stock_prices_yesterday[1]-stock_prices_yesterday[0]
    lowest_price = stock_prices_yesterday[0]

    if len(stock_prices_yesterday) < 2:
        raise IndexError("You cant sell and buy at the same time")

    for index, current_price in enumerate(stock_prices_yesterday):
        if index == 0 :
            continue 
        if current_price - lowest_price > max_profit:
            max_profit = current_price - lowest_price

        if current_price < lowest_price:
            lowest_price = current_price

    return max_profit