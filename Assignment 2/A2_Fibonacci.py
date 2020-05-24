def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1) + fibo(n-2))

terms = int(input('Number of terms:'))

if terms <= 0:
    print('Enter positive integer')
else:
    print('Fibonacci sequence:')
    for i in range(terms):
        print(fibo(i))
        