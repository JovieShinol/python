import string
value = string.ascii_lowercase
print(value)
t = []
n = 5
for i in range(n):
    s = '-'.join(value[i:n])
    
    t.append((s[::-1]+s[1:]).center(4*n-3,'-'))
print('\n'.join(t[::-1]+t[1:]))