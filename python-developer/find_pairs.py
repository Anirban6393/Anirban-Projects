from itertools import combinations 

# combinations() produces an iterator over tuples of all combinations of n elements in inputs. 
# We make the use of these combinations and output those having ‘k’ difference.

def findPairs(lst, k): 
    return [(x, y) for x, y in combinations(lst, r = 2) if abs(x - y) == k] 
    
# Driver code 
lst = [1, 3, 5] 
k = 2
set(findPairs(lst, k))