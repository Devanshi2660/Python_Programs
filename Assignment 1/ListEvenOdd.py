List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

even = []
odd = []

for num in List:
    if num%2 == 0:
        even.append(num)
    else:
        odd.append(num)

print('List:',List)
print('Even List:', even)
print('Odd List:',odd)
