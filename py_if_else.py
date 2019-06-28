# Task 
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints

# Output Format

# Print Weird if the number is weird; otherwise, print Not Weird.

# Sample Input 0

# 3
# Sample Output 0

# Weird
# Explanation 0

 
#  is odd and odd numbers are weird, so we print Weird.

# Sample Input 1

# 24
# Sample Output 1

# Not Weird
# Explanation 1

 
#  and  is even, so it isn't weird. Thus, we print Not Weird.



n = int(input())
while 1 <= n <= 100:
    while 2 <= n <= 5:
        if n % 2 == 0:
            print("Not Weird")
            break
        else:
            print("Weird")
            break
        break
    while 6 <= n <= 20:
        if n % 2 == 0:
            print("Weird")
            break
        else:
            print("Weird")
            break
        break
    while n > 20:
        if n % 2 == 0:
            print("Not Weird")
            break
        else:
            print("Weird")
            break
        break
    break