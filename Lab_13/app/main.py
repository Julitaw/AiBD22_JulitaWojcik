from typing import List
import numpy as np

def bubblesort(list1: List[int]):    
    if isinstance(list1, List):
        list2 = list1[:]
        n: int = len(list2)
        licz: int = 0
        swap: bool = False
        while (n > 1) and not swap:
            swap = True
            for i in range(n-1):
                licz += 1
                if list2[i] > list2[i+1]:
                    list2[i], list2[i+1] = list2[i+1], list2[i]
                    swap = False
            n -= 1
        tup = (list2, licz)
        return tup
    else:
        return None

