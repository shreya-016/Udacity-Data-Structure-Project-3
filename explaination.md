# Explaination of Projects
Total 7 projects covered. 

## Problem 1

### Time and Space complexity:
In this case time complexity is __O(log(n))__, as we transverse the _hypothetically ordered natural's number list_ by 
using a __binary search approach__. As for the space complexity it is O(1).

## Problem 2

### Time and Space complexity
The time complexity being an algorithm based on binary search is __O(log(n))__.  The number of iterations we perform,
i.e. recursive depth, follows the rule of _recursive_depth^2 = n_. As for the space complexity it is __O(1)__.

## Problem 3

### Time and Space complexity 
WE achieve  __O(n*log(n))__ time complexity, by using a variation of the __merge sort__ algorithm. 
The space complexity is of __O(n)__.

## Problem 4
We take three pointers and we are keeping track of first and last pointers with the middle pointer which is being used to swap the values with first and last pointer.
Subsequently we are incrementing the first pointer and mid and decrementing the last pointer. 

### Time and Space complexity
In this case the _time complexity_ is __O(n)__. The _space complexity_ is  __O(1)__ as we are not using any extra space.

## Problem 5
We use a __trie__ a data structure to solve the complex problem of autocompletion.

### Time and Space complexity
For the __trie__, time complexity of **searching and inserting** from a trie depends on the length of the word **a** 
that’s being searched for, inserted, and the number of total words, **n**, making the runtime of these operations
 __O(a*n__). Looking into the space complexity of a __trie__, the worst case, would be when we have a word (or words),
 with no common characters between them, hence having, a node for each letter. Resulting in a _space complexity_ of 
 __O(n)__.

### Time and Space complexity
In this case, we perform a __single transverse__ of the whole input, being the time complexity of __O(n)__. In respect 
to the _space complexity_, we have just a pair of pointers, hence, it is independent from _input size_; __O(1)__.

## Problem 6

This problem focuses on __finding max and min values__ from an unsorted array, we are using two placeholders minVal and maxVal that is used to find global minimum 
and maximum by traversing the complete array and swapping if required with the localMax and localMin. 

### Time and Space complexity
In this case, we perform a __single transverse__ of the whole input, being the time complexity of __O(n)__. In respect 
to the _space complexity_, we have just a pair of pointers, hence, it is independent from _input size_; __O(1)__.


## Problem 7 
It is similar to __problem 5__, except for the _edge cases_, like "root handler", and working with a __hierarchy of 
web pages__ instead of strings. This problem is focused on the development of the of a __trie__ a data structure 
derived from a _tree_, suited for a good ratio between _time and space_ complexity.

### Time and Space complexity
In __trie__, time complexity of **searching and inserting** is the length of the path **n**
that’s being searched for, inserted that is __O(n)__, _space complexity_ for __trie__ in the worst case would be when we have a paths with no common folders between them that is __O(n)__. 

The function calls the split_path(url_path) method to split the path around the '/' character and returning a list of path_parts. The time complexity of this function is O(n). The insert method has O(n) time complexity, resulting in an overall time complexity of O(n). Similarly, the Space Complexity depends on the number of nodes in the Trie and, hence, it scales proportionally to the number of parts in the url_path.
