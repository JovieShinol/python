""" Problem Statement:
Accept an integer  and print the number along with its sign.

Input Format:
Accept an integer as a input

Output Format:
Print the number along with its sign.

Constraints:
10^-15 <= N <= 10^15

Sample Input 1:
8

Sample Output 1:
+8

Sample Input 2:
-15

Sample Output 2:
-15 """

n  = int(input())
if n>=0:
  print('+'+str(n))
else:
  print(n)