myarr=[5,8,12,2,6,4,17]
n=len(myarr)

for i in range(n-1):
 
    for j in range(n-1-i):
        if myarr[j]>myarr[j+1]:
            myarr[j],myarr[j+1]=myarr[j+1],myarr[j]
print('my sorted array is',myarr)
      






