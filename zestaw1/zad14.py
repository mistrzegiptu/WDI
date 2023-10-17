def factorial(n): 
    if(n == 0): 
       return 1
    i = n 
    fact = 1  
    while(n / i != n): 
        fact = fact * i 
        i -= 1
          
    return fact
    
x = float(input())

eps = 1e-6
a = 0
y = 1
sign = -1
i = 2

while abs(y-a)>eps:
    a = y
    y = y + (x**i/factorial(i))*sign
    sign = sign * (-1)
    i += 2
    
print(y)