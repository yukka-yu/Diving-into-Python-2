number = int(input("Enter number: "))
print(hex(number))
symbol_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

string = ''
while number > 0:
    string = str(symbol_list[int(number % 16)]) + string
    number //= 16
print("0x" + string)