def read_stock_list():
    stock_list=input("Enter stock list prices: ")
    stock_list=list(map(int,stock_list.split()))
    return stock_list

def max_profit (stock_list):
    max_profit=0
    for day in range (len(stock_list)):
        for i in range(day,len(stock_list)):
            profit=stock_list[i]-stock_list[day]
            if profit>max_profit:
                max_profit=profit 
    return max_profit

stock_list=read_stock_list()
max_profit=max_profit(stock_list)
print(max_profit)

