# Unsorted Integer Array
class Solution():
    def get_min_max(self, arr):
        minVal = arr[0]
        maxVal = arr[0]
        for i in range(1, len(arr)):
            if maxVal < arr[i]:
                maxVal = arr[i]
            if minVal > arr[i]:
                minVal = arr[i]
            
        return minVal, maxVal
    
Solution().get_min_max([5, 8, 34, 9, 12, 59, 3, 49, 12, 44, 7, 33])
## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == Solution().get_min_max(l)) else "Fail")
