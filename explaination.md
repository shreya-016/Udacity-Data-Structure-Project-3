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

Individual complexities:
1. Class Trie __insert__ method: [Time complexity O(w) w is the length of the word, Space complexity O(w) as the word is inserted in trie]
2. Class Trie __find__ method: [Time complexity O(p) p is the length of the prefix, Space complexity O(1)]
3. Class Trie __init__ method: [Time complexity and space complexity both will be O(1)]
4. Class TrieNode __suffixes__ method: [Time complexity O(n) n is total number of words in worst case, Space complexity will be O(n) which is recursive stack space]
5. Class TrieNode __insert__ method: [Time complexity will be O(1). Space complexity will be O(1)]
6. Class TrieNode __init__ method: [Here also time complexity and space complexity both will be O(1)]
7. Class TrieNode __suffixRecursive__ method: [Time complexity will be O(2^n). Space complexity of recursive algorithm is proportinal to maximum depth of recursion tree generated. If each function call of recursive algorithm takes O(m) space and if the maximum depth of recursion tree is 'n' then space complexity of recursive algorithm would be O(nm).]


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

Individual complexities:
1. Class Router __add_Handler__ method: [Time complexity O(n), where n is number of path peices in url, Space complexity will be O(n) as it calls insert method.]
2. Class Router __init__ method: [Time complexity will be O(1)]
3. Class Router __lookup__ method: [ Time complexity is O(n) and the space complexity is O(1). This follows from the lookup directly calling the RouteTrie's find method)]
4. Class Router __split_path__ method: [Time and space complexity are both O(n), where n is the number path pieces in the url.]
5. Class RouterTrieNode __init__ method: [The time and space complexity will be O(1)]
6. Class RouterTrieNode __insert__ method: [The time and space complexity will be O(1)]
7. Class RouterTrie __insert__ method: [Time complexity O(n), where n is the number path pieces in the url. For example: “/a/b/c/d” has n = 4, and Space complexity will also be O(n) as we need to insert the elements as well]
8. Class RouterTrie __init__ method: [The time and space complexity will be O(1).]
9. Class RouteTrie __find__ method: [Time complexity for this method will be O(n) and space complexity will be O(1).]
