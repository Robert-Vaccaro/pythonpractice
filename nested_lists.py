# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format

# The first line contains an integer, , the number of students. 
# The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

# Constraints

# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry
# Explanation 0

# There are  students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.


lowest=[]
secondLowest=[]
for _ in range(int(input())):
    name=input()
    score=float(input())
    if len(lowest)==0:
        #initialize lowest list
        lowest=[ [name,score] ]
    elif score < lowest[0][1]:
        secondLowest=lowest
        lowest=[ [name,score] ]
    elif score == lowest[0][1]:
        lowest.append( [name,score] )
    elif len(secondLowest)==0:
        secondLowest=[ [name,score] ]
    elif score < secondLowest[0][1]:
        secondLowest=[ [name,score] ]
    elif score == secondLowest[0][1]:
        secondLowest.append( [name,score] )
names=[item[0] for item in secondLowest]
for name in sorted(names):
    print (name)
    