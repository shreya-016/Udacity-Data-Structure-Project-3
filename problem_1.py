# square root of a number
def sqrt(number):
    if number < 0:
        return -1
    if number < 2:
        return number
    lo = 1
    high = number
    while(lo <= high):
        mid = (lo + high)//2
        if mid*mid == number:
            return mid
        if mid*mid < number:
            lo = mid+1
            ans = mid
        else:
            high = mid-1 
    return ans
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(17)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (None == sqrt(-1)) else "Fail")
            
