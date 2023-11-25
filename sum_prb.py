"Find the sum of all numbers in range from 1 to m(both inclusive) that are not divisible by n. Return difference between sum of integers not divisible by n with sum of numbers divisible by n."

def sum_problem(m,n):
    sum1,sum2=0,0
    

    for i in range(1,m+1):
        if i%n==0:
            sum1+=i
        else:
            sum2+=i

    diff = sum1-sum2
    return abs(diff)
        
        







n = sum_problem(10,2)
print(n)