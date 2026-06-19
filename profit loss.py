#check profit loss using cost price and selling price
cost=int(input("enter cost price:"));
sell=int(input("enter selling price:"));
def profit_loss(cost,sell):
    if cost>sell:
        print("loss");
    else:
        print("profit:");
profit_loss(cost,sell)