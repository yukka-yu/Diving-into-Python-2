TAKE_OFF_TAX = 0.015
EVERY_THIRD_OPERATION_TAX = 0.03

WEALTH_TAX = 0.1
WEALTH = 5_000_000

START = 0

MIN_TAKE_OFF_TAX = 30
MAX_TAKE_OFF_TAX = 600

MULTIPLICITY = 50

sum_ = START
operation_count = 0

while True:
    
    choice = int(input('Choose an action: '
                       '\n1 - Put money'
                       '\n2 - Take off money'
                       '\n3 - Exit\n'))
    match choice:

        case 1:
            if sum_ > WEALTH:
                sum_ -= (sum_ - WEALTH) * WEALTH_TAX
                print(f'Since you have more than {WEALTH} on your account, we take off wealth tax {WEALTH_TAX}')
            while True:
                number = int(input('Enter sum you want to PUT: '))
                if number % 50 == 0 and number > 0:
                    sum_ += number
                    print(f'Operation completed successfully, you have {sum_} on your account')
                    operation_count += 1
                    if operation_count % 3 == 0:
                        sum_ += number * EVERY_THIRD_OPERATION_TAX
                        print(f'And since it was the third operation, we add you {EVERY_THIRD_OPERATION_TAX} and now there is {sum_} on your account')
                    break
                else:
                    print(f'Enter a summ multiples in {MULTIPLICITY} and not null')

        case 2:
            if sum_ == 0:
                print('You have no money at all')

            elif sum_ > 0:
                if sum_ > WEALTH:
                    sum_ -= (sum_ - WEALTH) * WEALTH_TAX
                    print(f'Since you have more than {WEALTH} on your account, we take off wealth tax {WEALTH_TAX}')

            while True:
                number = int(input('Enter sum you want to TAKE OFF: '))

                if number <= 0 or number % MULTIPLICITY != 0:
                    print(f'Enter a summ multiples in {MULTIPLICITY} and not null')
                else:
                    if number < MIN_TAKE_OFF_TAX / TAKE_OFF_TAX:
                        tax_sum = MIN_TAKE_OFF_TAX
                    elif number > MAX_TAKE_OFF_TAX / TAKE_OFF_TAX:
                        tax_sum = MAX_TAKE_OFF_TAX
                    else:
                        tax_sum = number * TAKE_OFF_TAX

                    if sum_< number + tax_sum:
                        print(f'You have not enough money on your account for this operation')
                    else:
                        sum_ -= number + tax_sum
                        print(f'Operation completed successfully. Summ on your account now is {sum_}')
                        operation_count += 1
                        if operation_count % 3 == 0:
                            sum_ += number * EVERY_THIRD_OPERATION_TAX
                            print(f'And since it was the third operation, we add you {EVERY_THIRD_OPERATION_TAX} and now there is {sum_} on your account')
                        break
                
        case 3:
            break
