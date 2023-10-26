from math import log

x = 10

for _ in range(1000):
    print(x)
    x = (x+x*log(x)-1)/(1+log(x))
    
print(x)