"""Problem Statement:
Round off the given floating point value with accurate to 2 decimal places.


Input Format:
Accept a floating point value


Output Format:
Print the value accurate to 2 decimal places


Constraints:
3.4E-4932 <= inp <= 1.1E+4932


Sample Input 1:
17.82448


Sample Output 1:
17.82

"""
def roundoff(num): 

    value = round(num,4)
    print(value)
roundoff(float(764874877687.784378873787))






"""Problem Statement:
Accept a floating point value and print it with 20 width space and round off to 4 decimal places.

Input Format:
Accept a floating point value

Output Format:
Print the give value with width 20 and rounded off to 4 decimal places

Constraints:
2.3E-308 to 1.7E+308

Sample Input 1:
-89.236

Sample Output 1:
-89.2360"""
# num = float(input())
def roundoff(num):    
    
    value = "{:20.4f}".format(num)
    print(value)

# roundoff(num)


num = float(input())
precis = int(input())
value = "{:.{}f}".format(num,precis)
print(value)


