# counting_sort
Counting Sort O(n) implementation based on CLRS

## How to use

Call `counting_sort(a, k)`, where `a` is the list to sort, `k` is the size of the language.   
For example, if we are using a list of decimal numbers, `k = 10`. Since decimal numbers have 10 digits. If it was a list of characters, `k = 26`, et cetera.

Returns another sorted list. Runs in O(n) time, where n is the length of the list.
