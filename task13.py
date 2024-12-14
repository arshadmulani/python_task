def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=left+(right-left)//2

        if arr[mid]==target:
           return f"Found at index {mid}"
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return "Not Found"
arr=[1,3,5,7,9]
target=7
print(binary_search(arr,target))
