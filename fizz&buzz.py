#program on fizz and buzz
for a in range(1,50):
    if a%3==0:
        print("fizz",a);
    elif a%5==0:
        print("buzz",a);
    elif a%3==0 and a%5==0:
        print("fizz and buzz");
    else:
        print("numbers");



