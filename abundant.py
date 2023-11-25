"""
Example
Input : Number = 12
Output : Yes, It's an Abundant Number
Explanation : The Factors for the number 12 are, 1, 2, 3, 4 and 6. We don't want to include the number itself.
Now the sum of the factors except the number itself is :
1 + 2 + 3 + 4 + 6 = 16
as the number 16>12 , the number itself.
It's an abundant number.

"""

def fact(n):
    sum1 = 0
    for i in range(1,(n//2)+1):
        if n%i==0:
            sum1+=i
    return sum1
        

def main():
    num1 = int(input())
    a = fact(num1)
    if a > num1:

        print(f"{num1} is an Abundant Number\nNum: {num1}\nSum: {a}\nAbundance: {a-num1}")
    else:
        print(f"{num1} is not a Abundant Number")  

main()