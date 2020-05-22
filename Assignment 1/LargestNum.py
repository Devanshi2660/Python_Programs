a = float(input('Enter num1:'))
b = float(input('Enter num2:'))
c = float(input('Enter num3:'))

if (a > b) and (a > c):
    largest = a
elif (b > a) and (b > c):
    largest = b
else:
    largest = c

print('Largest number:', largest)
