print("...calculator...")
op = input('''
please select operation:
add(+)
subtract(-)
multiply(*)
divide(/)
-> ''')
fnum = int(input('enter first operand: '))
snum = int(input('enter second operand: '))
if op == '+':
	ans = fnum + snum
elif op == '-':
	ans = fnum - snum
elif op == '*':
	ans = fnum * snum
else:
	ans = fnum/snum
print(f'{fnum} {op} {snum} = {ans}')
