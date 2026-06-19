#calculate discount amount on price
discount=0;
price=int(input("enter the total price:"));
def discount_amount(price):
    if(price<4000):
       discount=(price*2)/100;
       print("discount amount",discount);
    elif (price>4000 and price<5000):
       discount=(price*5)/100;
       print("discount amount",discount);
    elif(price>5000):
       discount=(price*10)/100;
       print("discount amount",discount);
    else:
       print("your total amount",price);
    totalprice=price-discount;
    print("total price",totalprice);
discount_amount(price)  
