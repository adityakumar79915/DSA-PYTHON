#when a function is calling itself is called recursion
'''def factorial(n):
    if n<=0:
        return(1)
    else:
        return(n*factorial(n-1))
print(factorial(5))    
        '''
        
def factors(n):
    factorslist=[]
    for i in  range(1,n+1):
        if n%i==0:
            factorslist=factorslist+[i]
    return(factorslist)
print(factors(8))   

'''def primeupto(n):
    primelist=[]
    for i in range(1,n+1):
        if isprime(i):
            primelist=primelist+[i]
    return(primelist)
print(primeupto(8))

'''