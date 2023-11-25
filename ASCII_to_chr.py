"""Problem Statement:
Accept an integer value and print the corresponding character associated with the integer value.

Input Format:
Integer value indicating the ASCII value to be evaluated

Output Format:
Given integer:Corresponding character

Constraints:
0 <= ch <=127

Sample Input 1:
65

Sample Output 1:
65:A"""

num1 = int(input("enter : "))
print(f"{num1}:{chr(num1)}")