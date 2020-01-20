from typing import TextIO
from io import StringIO
import time_series

def find_largest(line: str) -> int:
    """ Return the largest value in line, which is a whitespce-delimited string of integers that each end with a '.'.
    
    >>> find_largest('1. 3. 2. 5. 2.')
    5
    """ 
    #The largest value seen so far
    lrgest = -1
    for value in line.split():
       #Remove the trailing period.
        v = int(value[:-1])
        #If we find a larger value, remember it.
        if v > largest:
            largest = v
     
     return largest
