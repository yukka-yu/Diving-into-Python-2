import math

f1 = input("Enter first fraction: ")
f2 = input("Enter second fraction: ")

l1 = f1.split('/')
l2 = f2.split('/')

numerator = int(l1[0]) * int(l2[0])
denominator = int(l1[1]) * int(l2[1])

if numerator % denominator == 0:
    print(f'Product of {f1} and {f2} is {numerator // denominator}')

else:
    gcd = math.gcd(numerator, denominator)
    numerator  //= gcd
    denominator //= gcd
    mult = str(numerator)+ '/' + str(denominator) 
    print(f'Product of {f1} and {f2} is {mult}')



denominator = math.lcm(int(l1[1]), int(l2[1]))
numerator1 = int(l1[0]) * denominator // (int(l1[1]))
numerator2 = int(l2[0]) * denominator // (int(l2[1]))
numerator = (numerator1 + numerator2)

gcd = math.gcd(numerator, denominator)
numerator //= gcd
denominator //= gcd

if numerator % denominator == 0:
    print(f'Sum of {f1} and {f2} is {numerator // denominator}')

else:
    sum_ = str(numerator)+ '/' + str(denominator)
    print(f'Sum of {f1} and {f2} is {sum_}')
