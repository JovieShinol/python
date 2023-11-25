arr = [7,0,4,0,0,5,0]
package = []
for i in range(1,len(arr)+1):
    if arr[-i]!= 0:
        package.insert(0,arr[-i])

    else:
        
        package.append(arr[-i])
print(package)
        


