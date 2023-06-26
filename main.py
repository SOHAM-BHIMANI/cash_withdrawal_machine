import time
while True :
s_name = "soham"
k_name = "kalap"
r_name = "rujhuta"
s_pin = 1234
k_pin = 1245
r_pin = 7845
a = input("enter your name :- ")
b = int(input("enter your pin :- "))
if a == s_name and b == s_pin :
    print("loading . . . ")
    time.sleep(3)
    print("Account holder name :- ", a)
    c = int(input("enter the amount to be withdrawn :- "))
    d = c//2000
    e = c%2000
    print("2000 X ",d)
    print("500  X ",e)
    print(c)
elif a == k_name and b == k_pin:
    print("loading . . . ")
    time.sleep(3)
    print("Account holder name :- ", a)
    c = int(input("enter the amount to be withdrawn :- "))
    d = c//2000
    e = c%2000
    print("2000 X ",d)
    print("500  X ",e)
    print(c)
elif a == r_name and b == r_pin:
    print("loading . . . ")
    time.sleep(3)
    print("Account holder name :- ", a)
    c = int(input("enter the amount to be withdrawn :- "))
    d = c//2000
    e = c%2000
    print("2000 X ",d)
    print("500  X ",e)
    print(c)
else :
    print("invalid")