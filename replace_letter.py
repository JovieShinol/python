"""Problem Statement

You are given a function,

Void *ReplaceCharacter(Char str[], int n, char ch1, char ch2);

The function accepts a string  ‘ str’ of length n and two characters ‘ch1’ and ‘ch2’ as its arguments . Implement the function to modify and return the string ‘ str’ in such a way that all occurrences of ‘ch1’ in original string are replaced by ‘ch2’ and all occurrences of ‘ch2’  in original string are replaced by ‘ch1’.

Assumption: String Contains only lower-case alphabetical letters.

Note:

Return null if string is null.
If both characters are not present in string or both of them are same , then return the string unchanged.
Example:

Input:
Str: apples
ch1:a
ch2:p
Output:
paales
Explanation:

‘A’ in original string is replaced with ‘p’ and ‘p’ in original string is replaced with ‘a’, thus output is paales."""


def replace(s,ch1,ch2):
    # s = s.replace(ch1,'*').replace(ch2,ch1).replace('*',ch2)
    # print(s)
    string = list(s)
    new_str = []
    index = -1
    for i in string:
        index+=1
        if i == ch1:
            new_str.insert(index,ch2)
        elif i == ch2:
            new_str.insert(index,ch1)
        else:
            new_str.insert(index,i)
        
       
    print(*new_str,sep='')

    
s = 'apples'
ch1 = 'a'
ch2 = 'p'

replace(s,ch1,ch2)

# paales


"""
def swap (user_input, str1, str2):
    result = ''
    if user_input != None:
        result = user_input.replace(str1, '*').replace(str2, str1).replace('*', str2)
        return result
    return 'Null'
user_input = input()
str1, str2 = map(str,input().split())
print(swap(user_input, str1,str2))


"""