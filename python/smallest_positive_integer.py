
"""Write a function:
def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
* N is an integer within the range [1..100,000];
* each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

def solution_a(A):

  # If max value in A is negative, just return 1. 
  if max(A) <= 0 :
    return 1

  # Make the sorted list with positive integer numbers only. 
  A.sort() 
  sorted_positive_list = [ x for x in A if x>0 ]
  print(sorted_positive_list, 'here')
  
  # Find the list of pair of integer with the difference between two numbers are bigger than 2.
  for i in range(len(sorted_positive_list)-1):
    diff = sorted_positive_list[i+1] - sorted_positive_list[i]
    if diff >= 2:
      # Assume the pair is (A, B) and there is the gap, then return A+1
      return sorted_positive_list[i]+1
  # If no element of this list of pair, just return max(sorted numbers) + 1
  return max(sorted_positive_list)+1
