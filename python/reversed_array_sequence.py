from typing import List


def reverse_array_seq(arr: List[int]) -> List[int]:
    """
    Given an array of integers, return a sorted array 
    containing positive integers.
    returns an array of integers from n to 1 where n>0
    """
    arr.sort(reverse=True)
    positive_int_arr = [int for int in arr if int > 0]
    return positive_int_arr

sample_array = [-1, 3, 8, 4, 2,1]

reverse_array_seq(sample_array)