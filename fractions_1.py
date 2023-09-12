from fractions import Fraction

str1 = input('Введите первую дробь в формате a/b \t')
str2 = input('Введите вторую дробь в том же формате \t')

a = int(str1.split('/')[0])
b = int(str1.split('/')[1])

c = int(str2.split('/')[0])
d = int(str2.split('/')[1])

# Ищем произведение дробей

mult_numerator = int(a * c)
mult_denomenator = b * d

for i in range(1, max(mult_numerator, mult_denomenator) + 1):
    if mult_denomenator % i == 0 and mult_numerator % i == 0:
        mult_numerator //= i
        mult_denomenator //= i

mult = Fraction(mult_numerator, mult_denomenator)
mult_ex = Fraction(a, b) * Fraction(c, d)

# Ищем сумму дробей

sum_numerator = a * d + c * b
sum_denomenator = b * d

for i in range(1, max(sum_numerator, sum_denomenator) + 1):
    if sum_denomenator % i == 0 and sum_numerator % i == 0:
        sum_numerator //= i
        sum_denomenator //= i

sum = Fraction(sum_numerator, sum_denomenator)
sum_ex = Fraction(a, b) + Fraction(c, d)

if sum == sum_ex and mult == mult_ex:
    print("Ok")
    print(f'{sum=}')
    print(f'{mult=}')
else:
    print("Not Ok")
    