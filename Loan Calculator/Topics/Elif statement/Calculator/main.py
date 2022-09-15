# put your python code here
a = float(input())
b = float(input())
ar = input()
if (ar == '+'):
    print(a + b)
elif (ar == '-'):
    print(a - b)
elif (ar == '/' and b != 0):
    print(a / b)
elif (ar == '/' and b == 0):
    print('Division by 0!')
elif (ar == '*'):
    print(a * b)
elif (ar == 'mod' and b != 0):
    print(a % b)
elif (ar == 'mod' and b == 0):
    print('Division by 0!')
elif (ar == 'pow'):
    print(a ** b)
elif (ar == 'div' and b != 0):
    print(a // b)
elif (ar == 'div' and b == 0):
    print('Division by 0!')

