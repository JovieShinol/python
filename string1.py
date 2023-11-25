"""
99946
if even even (or) odd odd comes next next print '-' in between
9-9-94-6 
"""

def str_fromat(string):
    empty = []
    l = list(string)
    empty.append(int(l[0]))
    for i in range(len(l)-1):
        
        if int(l[i])%2==0 and int(l[i+1])%2==0:
            
            empty.append('-')
            empty.append(int(l[i+1]))

        elif int(l[i])%2!=0 and int(l[i+1])%2!=0:
            
            empty.append('-')
            empty.append(int(l[i+1]))

        else:
            
            empty.append(int(l[i+1]))

    
    for i in empty:
        print(i,end='')
    


n = "99964"
output = str_fromat(n)
