num = int(input('Введите целое число \t'))
hexa1 = hex(num)

hexa = '0x'
while num >= 16:
    hexa += str(num // 16)
    num = num % 16
hexa += str(num)

print(f'{hexa=}, {hexa1=}')

if hexa1 == hexa:
    print('All right')
else:
    print('Something wrong')

