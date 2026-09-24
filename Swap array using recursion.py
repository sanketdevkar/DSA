def f(i,n,arr):
    if i>=n/2:
        return 
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    f(i+1,n,arr)
arr=[1,2,3,4]
f(0,4,arr)
print(arr)
