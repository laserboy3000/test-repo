# simplecalculator
print('Введите первое число:')
x = float(input())
print('Введите операцию:')
oper = input()
print('Введите второе число:')
y = float(input())
if y == 0:
    print('На ноль делать нельзя')
elif oper == '+':
    print(x+y)
elif oper == '-':
    print(x-y)
elif oper == '*':
    print(x*y)
elif oper == '/':
    print(x/y)
elif oper == '**':
    print(x**y)
elif oper == '//':
    print(x//y)
elif oper == '%':
    print(x%y)
else:
    print('Что-то явно пошло не так')
