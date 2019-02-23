def format_price(price):
    price=int(price)
    price=str(price)
    price=price.upper()
    price1='Цена '+price+ ' руб.'
    return price1

price2=format_price(56.24)
print(price2)
