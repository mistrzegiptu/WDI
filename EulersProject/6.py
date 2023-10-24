n = 100
sumN = ((1+n)*(n)//2)**2
sumP = 0

for i in range(1, n+1):
    sumP += i*i
    
print(sumP, sumN, sumN-sumP)