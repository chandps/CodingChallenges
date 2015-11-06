"""
returns a list containing products of all int except at index
Algorithm: greedy approach
Running time: O(n) - Linear
"""
def get_products_of_all_ints_except_at_index(l):
    leftProduct = []
    before = 1
    
    for current in l: # go forwards
        leftProduct.append(before)
        before = before * current
    before = 1

    for i,current in reversed(list(enumerate(l))): # go backwards
        leftProduct[i] = leftProduct[i] * before
        before = before * current
    
    return leftProduct

j = [1, 2, 3, 0]
k = [0]
m = [1,0]
print(list(get_products_of_all_ints_except_at_index(j)))
print(list(get_products_of_all_ints_except_at_index(k)))
print(list(get_products_of_all_ints_except_at_index(m)))