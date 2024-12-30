myarr=[1,64,2,5,19,10,3,4,20]
n=len(myarr)
for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if myarr[j]<myarr[min_index]:
            min_index=j
    min_value=myarr.pop(min_index)
    # print(min_value)
    myarr.insert(i,min_value)
print('sorted array',myarr)
