def greet(name, question):
    
    return f"Hello, " + name + "! How's is " + question + "?"
a = greet("ansal","health")
print(a)

name = 'Hi ansal'
print("1,2,3")
print(len(name))
print(name.find('a'))
print(name.capitalize())
print(name.title())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("a"))
print(name.replace('o','a'))
print(name*3)


print("{} how are you".format(name))
print("{:>10} how are you".format(name))
print("{:<10} how are you".format(name))
print("{:^10} how are you".format(name))

number = 3.145

print("the value of pi is {:.2f}".format(number))

num = 10
print("decimal to binary {:b}".format(num))
print("decimal to oxtal {:o}".format(num))
print("decimal to lowercase hexa {:x}".format(num))
print("decimal to uppercase hexa {:X}".format(num))
print("decimal to lowercase sifinotation {:e}".format(num))
print("decimal to uppercase sifinotation {:E}".format(num))


