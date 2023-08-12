#function is a block of code that perform a particular task
#argument value is substituted for name
def power(x,n):
     ans=1
     for i in range(x,n):
        ans=ans*x
     return(ans)    
y=power(3,5)
print(y) 



# def stupid(x):
#     n=17
#     return(x)
# n=7
# v=stupid(28)
# print(v)
# print(n)