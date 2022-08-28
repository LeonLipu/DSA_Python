def binary(arr,n,i,j):
    if i>j:
        return False
    else:
        mid=(j+i)//2
        element=arr[mid]
        
        if element == n:
            return True
        else:
            if n>arr[mid]:
                return binary(arr,n,mid+1,j)
            else:
                return binary(arr,n,i,mid-1)
