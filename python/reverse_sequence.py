"""
Build a function that returns an array of integers from n to 1 where n>0.
Example : n=5 --> [5,4,3,2,1]
"""

# use lambda function and range to loop over the positive integer
#  converte the result into a list
reverse_seq = lambda n : [x for x in range(n,0,-1)]
# pass in any argument
reverse_seq(5)

