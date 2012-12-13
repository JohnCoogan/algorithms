## Dynamic Programming

# Question: 
Alice is a kindergarden teacher. She wants to give some candies to the children in her class.
All the children sit in a line and each of them has a rating score according to his or her usual performance.  
Alice wants to give at least 1 candy for each child. 
Children get jealous of their immediate neighbors, so if two children sit next to each other
then the one with the higher rating must get more candies. 
Alice wants to save money, so she wants to minimize the total number of candies.

# Input
The first line of the input is an integer N, the number of children in Alice's class. 
Each of the following N lines contains an integer indicates the rating of each child.
 
# Sample Input
3 <- number of children
1 <- rating
2 <- rating
2 <- rating
 
# Sample Ouput
4

# Explanation
The number of candies Alice must give are 1, 2 and 1.

# Ouput
Output a single line containing the minimum number of candies Alice must give.

# Constraints:
N and the rating of each child are no larger than 100000.

# Method
    *   Give 1 candy to each child.
    *   Iterate over all children to check with the neighboring children if the condition is held.
    *   Keep iterating until the condition is never broken.
