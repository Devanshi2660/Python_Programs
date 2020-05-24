
def div(n1,n2):
    try:
        print(n1/n2)
    except ZeroDivisionError:
        print('Denominator is zero.')

n1 = int(input("Numerator:"))
n2 = int(input('Denominator'))
div(n1,n2)

def file(file_name):
    try:
        f = open(file_name)
        f.close()
    except FileNotFoundError:
        print('File does not exist.')
    
file_name = input('Enter file name:')
file(file_name)

