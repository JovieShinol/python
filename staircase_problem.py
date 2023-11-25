"""Problem Description

There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time.

Count the number of ways, the person can reach the top.

Output
5
8
"""
def calc(x):
    if x<=1:
        return x
    return calc(x-1)+calc(x-2)
def count(n):
    return calc(n+1)

n = int(input())
print(count(n))