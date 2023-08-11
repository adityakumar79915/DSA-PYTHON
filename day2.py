#list is sequences of values
'''
factors = [1,2,5,10]
''' 

#list need not be uniform
'''
mixed=[3,true,"yellow"]
'''
#we can extract values by position , slice,like str
#nested list is possible
'''nested=[[2,[37]],4,['hello']]
print(nested[2])
print(nested[2][0][3])
print(nested[0][1:2])'''

#list is muttable
'''nested=[[2,[37]],4,['hello']]
nested[1]=7
print(nested)'''

#copying list
#l[:]==l[0:len(l)] full slice
#list2=list[:]
list1=[1,3,5,7]
list2=list1[:]
list1[2]=4
print(list2)

