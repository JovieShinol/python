def rev_string(string):

    # return string[::-1]
    revers = ""
    index = len(string)
    value = list(string)

    while index:
        index -=1
        revers += value[index]
        

    
    return revers


print(rev_string("ansal"))


