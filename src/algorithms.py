from collections import Counter
from itertools import combinations
import time
def apriori(dataset, min_support):

    # Set of all numbers seen together frequently. Also known as L_k
    frequent_set = set()

    # Dictionary containing every item and how many times that item appears. Also known as C_k
    frequent_items = Counter()

    # Find the length of the largest basket
    n = len(max(dataset, key=len))

    # First pass to generate C_1
    for basket in dataset:
        for item in basket:
            frequent_items[frozenset([item])] += 1

    # Prune items that don't meet the min_support threshold to generate L_1
    frequent_items = Counter({item: count for item, count in frequent_items.items() if count >= min_support})

    # Add frequent items to a new array
    for item in frequent_items:
        frequent_set.add(item)  # item is always frozenset now


    # Passes 2 to n

    for k in range(2, 4):
        # In this case, 'k' acts as the length of sets generated in each pass

        # Generate C2: List of all combinations
        L = sorted({next(iter(fs)) for fs in frequent_set if len(fs) == (k - 1)})
        C = [frozenset(comb) for comb in combinations(L, k)]

        # Generate L2: Check frequency
        for basket in dataset:
            for candidate in C:
                if(candidate.issubset(basket)):
                    frequent_items[candidate] += 1
        
        # Prune items that don't meet min_support
        frequent_items = Counter({item: count for item, count in frequent_items.items() if count >= min_support})

        # Log all frequent items
        for item in frequent_items:
            frequent_set.add(item)

    return frequent_items