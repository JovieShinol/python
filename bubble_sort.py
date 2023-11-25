l = [3,9,6,8,7,5]

for j in range(len(l)-1):
        
    for i in range(len(l)-1):
            
        if l[i] > l[i+1]:
            temp = l[i]
            l[i] = l[i+1]
            l[i+1] = temp
print(l)