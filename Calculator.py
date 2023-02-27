#functions 

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y    
def divide(x,y):
    return x/y
def multiply(x,y):
    return x*y   

#user options
print('welcome to the calculator')
print('please pick an operation')
print('1. add')
print('2. subtract')
print('3. multiply')
print('4. divide')

#variables 
choice = input('please enter the number of the operation youd like to preform')
num1 = float(input('enter first number: '))
num2 = float(input('enter the second number: '))

if choice == '1':
    print(num1, '+', num2, '=', add(num1,num2))
elif choice == '2':
    print(num1, '-', num2, '=', subtract(num1,num2))
elif choice == '3':
    print(num1, '*', num2, '=', multiply(num1,num2))
elif choice == '4':
    print(num1, '/', num2, '=', divide(num1,num2))
else:
    print('invaild input')