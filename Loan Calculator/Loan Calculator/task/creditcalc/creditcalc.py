import argparse
import math
parser = argparse.ArgumentParser(description="Differentiate payment")
parser.add_argument("--type", help="annuity or diff")
parser.add_argument("--principal", help="principal (diff or annuity)", type=float)
parser.add_argument("--periods", help="periods (diff or annuity)", type=int)
parser.add_argument("--interest", help="interest (diff or annuity)", type=float)
parser.add_argument("--payment", help="interest (diff or annuity)", type=float)
args = parser.parse_args()
if args.type == 'diff':
    if args.principal is not None and args.interest is not None and args.periods is not None:
        if args.principal >= 0 and args.interest >= 0 and args.periods >= 0:
            norm_interest = (args.interest / 12) * 0.01
            j = 1
            suma_a = 0
            for j in range(1, args.periods + 1):
                d = (args.principal / args.periods) + norm_interest * (args.principal - ( (args.principal * (j - 1))/ args.periods))
                print(f'Month {j}: periods is {math.ceil(d)}')
                suma_a += math.ceil(d)
                j = j + 1
            print(f'\nOverpayment = {int(suma_a - args.principal)}')
        else:
            print('Incorrect parameters')
    else:
        print('Incorrect parameters')
elif args.type == 'annuity':
    if args.principal is not None and args.interest is not None and args.periods is not None:
        if args.principal >= 0 and args.interest >= 0 and args.periods >= 0:
            norm_interest = (args.interest / 12) * 0.01
            k = norm_interest * (1 + norm_interest) ** args.periods / ((1 + norm_interest) ** args.periods - 1)
            pay_a = k * args.principal
            print(f'Your annuity payment = {math.ceil(pay_a)}!')
            j = 1
            suma_b = 0
            for j in range(1, args.periods + 1):
                suma_b += math.ceil(pay_a)
                j += 1
            print(f'Overpayment = {int(suma_b - args.principal)}')
        else:
            print('Incorrect parameters')
    elif args.payment is not None and args.interest is not None and args.periods is not None:
        if args.payment >= 0 and args.interest >= 0 and args.periods >= 0:
            norm_interest = (args.interest / 12) * 0.01
            k = norm_interest * (1 + norm_interest) ** args.periods / ((1 + norm_interest) ** args.periods - 1)
            princep = args.payment / k
            print(f'Your loan principal = {int(princep)}!')
            j = 1
            suma_b = 0
            for j in range(1, args.periods + 1):
                suma_b += math.ceil(args.payment)
                j += 1
            print(f'Overpayment = {math.ceil(suma_b - princep)}')
    elif args.principal is not None and args.payment is not None and args.interest is not None:
        if args.principal >= 0 and args.payment >= 0 and args.interest >= 0:
            norm_interest = (args.interest / 12) * 0.01
            k = args.payment / args.principal
            ks = 0
            n = 1
            while k >= ks:
                ks = norm_interest * (1+norm_interest) ** n / ((1 + norm_interest) ** n - 1)
                n += 1
            if n > 1:
                print(f'It will take {n} years to repay this loan!')
            else:
                print(f'It will take {n} year to repay this loan!')
            suma_b = 0
            for j in range(1, (n * 12) + 1):
                suma_b += math.ceil(args.payment)
                j += 1
            print(f'Overpayment = {suma_b - math.ceil(args.principal)}')
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
