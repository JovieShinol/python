"""
Example
Input : 6 28
Output : Yes, they are a friendly pair
Explanation : The factors of 6 and 28 except the numbers themselves are 1, 2, 3 and 1, 2, 4, 7, 14 respectively.
Now the sum of factors of both the numbers are 6 and 28 respectively. 
When we divide the sums with the numbers we get 1 and 1 respectively. 
As the ratio of both the number match, they are considered as a friendly pair.

"""
def fact(n):
    sum1 = 0
    for i in range(1,(n//2)+1):
        if n%i==0:
            sum1+=i  
    return sum1-n
    
        
def main():
    num1,num2 = map(int,input().split())

    if fact(num1)==fact(num2):

        print("Friendly pair")
    else:
        print("Not a Friendly Pair")  

main()