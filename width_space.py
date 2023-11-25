"""Problem Statement:
Given 2 numbers, print the first number as a 5-digit number and print the second number in the next line with 5 width space

Explanation: If numbers are 25 and 98,print the first number as 00025 and second number as 3 space and 98(   98).


Input Format:
Accept the two integer as a input

Output Format:
5 digit number format followed by number with 5 width space in new line.

Constraints:
10^-15 <= num1,num2 <= 10^15

Sample Output 1:
00745
569


Sample Input 2:          Sample Output 2:
1 23                       00001
                              23 

Sample Input 3:          Sample Output 3:
123 234                     00123
                              234

Sample Input 4:
223 678945


Sample Output 4:
00223
678945


Sample Input 5:
34 7896


Sample Output 5:
00034
7896  Sample Input 6:
-125 -36


Sample Output 6:
-0125
-36


Sample Input 7:
65432345678 456789876546


Sample Output 7:
65432345678
456789876546


Sample Input 8:              Sample Output 8:
-23890 238901                    -23890
                                  238901



   """

num1,num2 = input().split()
num1 = int(num1)
num2 = int(num2)
print(f"{num1:05}")
print(f"{num2:5}")



"""
get two integers as input  and split using split().
use formatted string (f-strings) to print numbers in desired format.
"{num1:05}" formats num1 as a 5-digit number with leading zeros if necessary.
"{num2:5}" formats num2 with a width of 5 characters, providing space if necessary.
When you run this code and provide two integer inputs, it will display the numbers in the specified format.

"""

