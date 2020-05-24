def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

print('Select operation')
print('1.Add')
print('2.Substract')
print('3.Multiply')
print('4.Divide')

choice = input('Enter choice(1/2/3/4):')

n1 = int(input('Enter num1:'))
n2 = int(input('Enter num2:'))

if choice == '1':
    print(n1,'+',n2,'=',add(n1,n2))

elif choice == '2':
    print(n1,'-',n2,'=',sub(n1,n2))

elif choice == '3':
    print(n1,'*',n2,'=',mul(n1,n2))

elif choice == '4':
    print(n1,'/',n2,'=',div(n1,n2))

else:
    print('Invalid output')
    






