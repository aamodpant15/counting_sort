"""
Counting Sort algorithm based on the CLRS Pg. 195

where,
    a -> list to sort
    k -> number of characters in the language of the word.
"""
# (list, int) -> list
def counting_sort(a, k):
    c = [0] * (k) #k
    b = [0] * (len(a)) #n

    for j in range (0, len(a)): #n
        c[ord(a[j])-97] += 1
    # C[i] now contains the number of elements equal to i    
    
    for i in range(1, k): # k - 1
        c[i] += c[i-1]
    # C[i] now contains the number of elements less than or equal to i

    for j in range(len(a)-1, -1, -1): # n - 1
        b[c[ord(a[j])-97]-1] = a[j]
        c[ord(a[j])-97] -= 1
    return b
