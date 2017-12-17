import cs50

a = 0;
print ("Number: ", end = "")
a = cs50.get_int();
digit = 0;
total = 0;
credit = a;
while(credit>0):
    num = credit % 10;
    credit /= 10;
    if(digit == 0):
        total += num;
        digit = 1;
    else:
        productDigitTotal = 0;
        doubled = num*2;
        while(doubled > 0):
            productDigitTotal += doubled % 10;
            doubled /= 10;
        total += productDigitTotal;
        digit = 0;
if(total%10 != 0):
    print ("INVALID");
else:
    while(a>10):
        a /= 10;
    if(a == 3):
        print ("AMEX");
    elif (a == 4):
        print ("VISA");
    elif (a == 5):
        print ("MASTERCARD");