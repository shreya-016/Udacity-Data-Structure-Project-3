# Search in a rotaed sorted array
def binarySearch(arr, target):

    lo = 0
    hi = len(arr)-1
    
    while lo <= hi:
        mid = lo + (hi-lo)//2
        if arr[mid] == target:
            return mid
        if arr[lo] <= arr[mid]:
            if target < arr[mid] and target >= arr[lo]:
                hi = mid-1
            else:
                lo = mid+1
        else:
            if target <= arr[hi] and target > arr[mid]:
                lo = mid+1
            else:
                hi = mid-1
    
        
def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

def test_function(test_case):
    arr = test_case[0]
    target = test_case[1]
    if linear_search(arr, target) == binarySearch(arr, target):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], 5])
