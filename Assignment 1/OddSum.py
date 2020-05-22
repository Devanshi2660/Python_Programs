minimum = int(input('Enter min value:'))
maximum = int(input('Enter max value:'))

sum = 0

for i in range(minimum, maximum + 1):
    if(i % 2 != 0):
        sum = sum + i

print('Sum of odd numbers from', minimum,'to', maximum,'is:', sum)