first_name = "Stanley"

last_name = "Ipkiss"

candy_bars = [["mars", 5], ["snickers", 4], ["bounty", 3]]
new_candy = candy_bars.append(["Solero", 2.50])

cigarette_prices = [["Malboro", 15], ["B&H Silver", 11], ["B&H Gold", 13], ["Starling", 9]]
alcohol_prices = [["Ciroc", 30], ["Martel", 35], ["Jack Daniels", 19], ["Baileys", 15]]

for cigarette in cigarette_prices:
    if cigarette[0] == str("B&H"):
        cigarette[0] = "Rothmans"

# print(cigarette_prices[2][0])

def discounted_prices(stock, discount_amount):
    new_price=[]
    for price in stock:
        new_p = price[1]-discount_amount
        price = [price[0], new_p]
        new_price.append(price)

    return new_price

print(discounted_prices(cigarette_prices, 5.9))
print(discounted_prices(alcohol_prices, 3))
print(discounted_prices(candy_bars, 1))


