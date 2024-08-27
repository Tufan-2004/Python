cost_price=int(input("Enter cost price:"))
selling_price= int(input("Enter selling price:"))

if cost_price == selling_price:
    print("No profit no loss")

elif cost_price < selling_price:
    profit=selling_price-cost_price
    print("The profit is=",profit)
else:
    loss=cost_price-selling_price
    print("The loss is=",loss)