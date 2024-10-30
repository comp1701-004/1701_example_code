def compute_num_purchased(spend: float, price: float) -> float:
    num_purchased = spend / price1
    return num_purchased

# inputs
price1 = float(input('enter purchase price'))
spend = float(input('enter money'))
price2 = float(input('enter new price'))

# processing
num_purchased = compute_num_purchased(spend, price1)
current_value = num_purchased * price2
change = current_value - spend
percent_change = change/spend

# outputs
print(f'you spent {spend:.2f} CAD to purchase {num_purchased:.6f} BTC')
print(f'now your BTC are worth ${current_value:.2f} CAD')
print(f'a change of ${change:.2f} or a percent change of {percent_change:.2%}')