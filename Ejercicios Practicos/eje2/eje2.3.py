# funcion fibonacci

def fibonacci(num):
    a,b = 0,1
    fibonacci_list = [0]
    for i in range(num):
        if b > num : return fibonacci_list
        else: 
            fibonacci_list.append(b)
            a,b = b,a+b

print(fibonacci(100))

#########################################################

def fibonacci2(num):
    a,b= 0,1
    for i in range(num):
        c = a+b
        a,b = b,c
    return b
        

for i in range(20):
    print(fibonacci2(i))
    
##############################################################
print('fibonacci 3')

def fib(num):
    list_fib = []
    if num < 2 : return num
    return fib(num-1) + fib(num-2)
    
for i in range(20):
    print(fib(i))
all()