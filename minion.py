"""https://www.hackerrank.com/challenges/the-minion-game"""
def minion():

    l = ['a','e','i','o','u']
    s = input().lower()
    a,b = 0,0
    len_s = len(s)
    for i , string in enumerate(s):

        if string in l:
            a+= len_s-i
        else:
            b+= len_s-i

        
    if a > b:
        print(f'Kevin {a}')
    elif b > a:
        print(f'Stuart {b}')
    else:

        print('Draw')

minion()
