def ArrayChallenge(strArr):
    cache = []
    for char in strArr:
        if char not in cache:
            if len(cache) == 5:
                cache.pop(0)
            cache.append(char)
        else:
            cache.remove(char)
            cache.append(char)
    return '-'.join(cache)


input_array = ["A", "B", "C", "D", "A", "E", "D", "Z"]
result = ArrayChallenge(input_array)
print(result)
"""def revers(string):
    revers_str =''
    index = len(string)
    while index:
        index-=1
        revers_str +=string[index]
    return revers_str

 
answer = revers(result)
print(answer)"""


# Output: "C-A-E-D-Z"
""" Array Challenge
Have the function

ArrayChallenge (strArr) take the array of characters stored in strarr, which will contain characters ranging from A to Z in some arbitrary order, 
and determine what elements still remain in a virtual cache that can hold up to 5 elements with an LRU cache algorithm implemented.
For example: if strArr is ["A", "B", "C", "D", "A", "E", "D", "Z"], then the following steps are taken:

(1) A does not exist in the cache, so access it and store it in the cache.
(2) B does not exist in the cache, so access it and store it in the cache as well. So far the cache contains: ["A", "B"].
(3) Same goes for C, so the cache is now: ["A","B", "C"].
(4) Same goes for D, so the cache is now: ["A","B", "C", "D"].
(5) Now A is accessed again, but it exists in the cache already so it is brought to the front: ["B", "C", "D", "A"].
(6) E does not exist in the cache, so access it and store it in the cache: ["B", "C", "D", "A", "E"]. 
(7) D is accessed again so it is brought to the front: ["B", "C", "A", "E", "D"].
(8) Z does not exist in the cache so add it to the front and remove the least recently used element: ["C", "A", "E", "D", "Z"].

Now the caching steps have been completed and your program should return the order of the cache with the elements joined into a string, separated by a hyphen. Therefore, for the example above your program should return C- A-E-D-Z.

Once your function is working, take the final output string and replace all characters that appear in your ChallengeToken with - [CHAR]-
Your ChallengeToken: vxd9gzc1586 1
Examples
Input: 3  new String[] {"A", "B", "A","C", "A", "B"} 
Output: C-A-B
Find Output: C-A-B
Input: 5  new String[] {"A", "B", "C", "D", "E", "D", "Q", "Z", "C"} 
Output: E-D-Q-Z-C Final 
Output: E-D-Q-Z-C """