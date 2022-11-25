# Rearrange Array Digits
def rearrange_digits(arr):
    
    # O(nlog(n) complexity of implementing merge sort)
    arr = mergesort(arr)
    
    first = 0
    for i in range(0, len(arr), 2):
        first = first * 10 + arr[i]
    second = 0
    for i in range(1, len(arr), 2):
        second = second * 10 + arr[i]
        
    return [first, second]

def mergesort(arr):
    n = len(arr)-1
    split(arr, 0, n)
    return arr

def split(arr, lo, hi):
    if(lo < hi):
        mid = (lo + hi) // 2
        split(arr, lo, mid)
        split(arr, mid+1, hi)

        merge(arr, lo, mid, hi)


def merge(arr, lo, mid, hi):
    p = lo
    q = mid + 1
    arr2 = [None for _ in range(hi+1 - lo)]
    k = 0

    for i in range(lo, hi+1):
        if (p > mid):
            arr2[k] = arr[q]
            k += 1
            q += 1

        elif (q > hi):
            arr2[k] = arr[p]
            k += 1
            p += 1

        # Adding the larger value
        elif (arr[p] > arr[q]):
            arr2[k] = arr[p]
            k += 1
            p += 1
        else:
            arr2[k] = arr[q]
            k += 1
            q += 1

    k = 0
    while(k < len(arr2)):
        arr[lo] = arr2[k]
        lo += 1
        k += 1
        
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print(output)
    print(solution)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_case1 = [[1, 2, 3, 4, 5], [542, 31]]
test_case2 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case3 = [[], []]
test_function(test_case)
test_function(test_case1)
test_function(test_case2)
