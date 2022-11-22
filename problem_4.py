def sort_012(arr):
    n = len(arr)
    p1, p2 = 0, 0
    p3 = n-1
    while p2<=p3:
        if arr[p2] == 0:
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p1 += 1
            p2 += 1
        elif arr[p2] == 1:
            p2 += 1
        else:
            arr[p2], arr[p3] = arr[p3], arr[p2]
            p3 -= 1
    return arr

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
