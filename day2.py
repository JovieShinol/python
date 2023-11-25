def shortcut():
    print(''' General
Ctrl+Shift+P,   F1 Show Command Palette
Ctrl+P Quick    Open, Go to File…
Ctrl+Shift+N     New window/instance
Ctrl+Shift+W     Close window/instance
Ctrl+,           User Settings
Ctrl+K           Ctrl+S Keyboard Shortcuts


Basic editing


Ctrl+/               Toggle line comment   " # "


Ctrl+X               Cut line (empty selection)
Ctrl+C               Copy line (empty selection)
Alt+ ↑ / ↓           Move line up/down
Shift+Alt + ↓ / ↑    Copy line up/down
Ctrl+Shift+K         Delete line
Ctrl+Enter           Insert line below
Ctrl+Shift+Enter     Insert line above
Ctrl+Shift+\         Jump to matching bracket
Ctrl+] / [           Indent/outdent line
Home /End            Go to beginning/end of line
Ctrl+Home            Go to beginning of file
Ctrl+End             Go to end of file
Ctrl+↑ / ↓           Scroll line up/down
Alt+PgUp /           PgDn Scroll page up/down
Ctrl+Shift+[         Fold (collapse) region
Ctrl+Shift+]         Unfold (uncollapse) region
Ctrl+K Ctrl+[        Fold (collapse) all subregions
Ctrl+K Ctrl+]        Unfold (uncollapse) all subregions
Ctrl+K Ctrl+0        Fold (collapse) all regions
Ctrl+K Ctrl+J        Unfold (uncollapse) all regions
Ctrl+K Ctrl+C        Add line comment
Ctrl+K Ctrl+U        Remove line comment
Ctrl+/               Toggle line comment
Shift+Alt+A          Toggle block comment
Alt+Z                Toggle word wrap



Navigation
Ctrl+T Show all Symbols
Ctrl+G Go to Line...
Ctrl+P Go to File...
Ctrl+Shift+O Go to Symbol...
Ctrl+Shift+M Show Problems panel
F8                    Go to next error or warning
Shift+F8 Go to previous error or warning
Ctrl+Shift+Tab Navigate editor group history
Alt+ ← / → Go back / forward
Ctrl+M Toggle Tab moves focus
Search and replace
Ctrl+F Find
Ctrl+H Replace
F3 / Shift+F3 Find next/previous
Alt+Enter Select all occurences of Find match
Ctrl+D Add selection to next Find match
Ctrl+K Ctrl+D Move last selection to next Find match
Alt+C / R / W Toggle case-sensitive / regex / whole word
Multi-cursor and selection
Alt+Click Insert cursor
Ctrl+Alt+ ↑ / ↓ Insert cursor above / below
Ctrl+U Undo last cursor operation
Shift+Alt+I Insert cursor at end of each line selected
Ctrl+L Select current line
Ctrl+Shift+L Select all occurrences of current selection
Ctrl+F2 Select all occurrences of current word
Shift+Alt+→ Expand selection
Shift+Alt+← Shrink selection
Shift+Alt +
(drag mouse)
Column (box) selection
Ctrl+Shift+Alt
+ (arrow key)
Column (box) selection
Ctrl+Shift+Alt
+PgUp/PgDn
Column (box) selection page up/down
Rich languages editing
Ctrl+Space, Ctrl+I Trigger suggestion
Ctrl+Shift+Space Trigger parameter hints
Shift+Alt+F Format document
Ctrl+K Ctrl+F Format selection
F12 Go to Definition
Alt+F12 Peek Definition
Ctrl+K F12 Open Definition to the side
Ctrl+. Quick Fix
Shift+F12 Show References
F2 Rename Symbol
Ctrl+K Ctrl+X Trim trailing whitespace
Ctrl+K M Change file language
Editor management
Ctrl+F4, Ctrl+W Close editor
Ctrl+K F Close folder
Ctrl+\ Split editor
Ctrl+ 1 / 2 / 3 Focus into 1
st, 2nd or 3rd editor group
Ctrl+K Ctrl+ ←/→ Focus into previous/next editor group
Ctrl+Shift+PgUp / PgDn Move editor left/right
Ctrl+K ← / → Move active editor group
File management
Ctrl+N New File
Ctrl+O Open File...
Ctrl+S Save
Ctrl+Shift+S Save As...
Ctrl+K S Save All
Ctrl+F4 Close
Ctrl+K Ctrl+W Close All
Ctrl+Shift+T Reopen closed editor
Ctrl+K Enter Keep preview mode editor open
Ctrl+Tab Open next
Ctrl+Shift+Tab Open previous
Ctrl+K P Copy path of active file
Ctrl+K R Reveal active file in Explorer
Ctrl+K O Show active file in new window/instance
Display
F11 Toggle full screen
Shift+Alt+0 Toggle editor layout (horizontal/vertical)
Ctrl+ = / - Zoom in/out
Ctrl+B Toggle Sidebar visibility
Ctrl+Shift+E Show Explorer / Toggle focus
Ctrl+Shift+F Show Search
Ctrl+Shift+G Show Source Control
Ctrl+Shift+D Show Debug
Ctrl+Shift+X Show Extensions
Ctrl+Shift+H Replace in files
Ctrl+Shift+J Toggle Search details
Ctrl+Shift+U Show Output panel
Ctrl+Shift+V Open Markdown preview
Ctrl+K V Open Markdown preview to the side
Ctrl+K Z Zen Mode (Esc Esc to exit)
Debug
F9 Toggle breakpoint
F5 Start/Continue
Shift+F5 Stop
F11 / Shift+F11 Step into/out
F10 Step over
Ctrl+K Ctrl+I Show hover
Integrated terminal
Ctrl+` Show integrated terminal
Ctrl+Shift+` Create new terminal
Ctrl+C Copy selection
Ctrl+V Paste into active terminal
Ctrl+↑ / ↓ Scroll up/down
Shift+PgUp / PgDn Scroll page up/down
Ctrl+Home / End Scroll to top/bottom
Keyboard shortcuts for Windows
Other operating systems’ keyboard shortcuts and additional 
unassigned shortcuts available at aka.ms/vscodekeybindings''')
def decimal():
    from decimal import Decimal as d
    if d(1.1+2.2)==d(3.3):
        print("i")
    
    else:
        print("a")
    print(d(1.1+2.2))
    print(d(3.3))
def print_ids(a, b):
    id_a = id(a)
    id_b = id(b)
    print(f"id(a): {id_a}")
    print(f"id(b): {id_b}")
def indexing ():
    var = 'hellow'
    return var
def slicing(a):
    b = a[0:4]
    c = a[:1:-1]
    return b,c
def slicing_a(a):
    b = a.split(" ")
    return b
def myfunc():
  global x
  x = "fantastic"
def range_a(a,b,c):
    print(list(range(c)))
    print(list(range(a,c)))
    print(list(range(b,c)))
 # range_a(0,1,10)
'''
number=input()
temp = []
for i in number:
    temp.append(i)
out = ' '.join(str(i) for i in temp)
print(out)
'''


def for_loop():
    student_name ="ansal"
    marks = {'ansal' : 95 , 'suresh' : 90 ,'raj' : 99}
    for mark in marks:
        if mark == student_name:
            print(marks[mark])
 # for_loop()
def while_a():
    num = 10
    sum = 0
    i = 1
    while i <= num:
        sum = sum + 1
        i = i + 1
    print('sum of first 10 number' , sum)
 
 # while_a()
def recursion():
    import sys
    sys.setrecursionlimit("enter 'number'how many time recursion happens")
    print("hello world")
    recursion()
    
 # recursion()
# class and object
class computer:
    # class contain attributes and methord
    # attributes -> variabls
    # methord -> function

    def config(self):
        return ('proceresser : i5 \ngpu : intel \nram : 12Gb')
 # com1 = computer() 
 # # print(com1.config()) 
 # # print(computer) 
# class and self
class student:

    def __init__(self,name,age):
        self.name = name
        self.age = age


    def print_list(self):
        print('student 1:',self.name,'age : ',self.age)


std1 = student('ansal',19)
std2 = student('vignesh',20)

 # std1.print_list()
 # std2.print_list()

class home:
    # example 
    def __init__(self,name,deprt):

        self.name = name
        self.deprt = deprt


    def print_list(self):
        print(self.name,self.deprt)


ex1 = home("ansal",19)
ex2 = home("aravint",20)

#  ex1.print_list()
#  ex2.print_list()
class hi:
    pass
    # we should not keep our class empty  / to keep empty class use pass comment


a = hi()
 # print(id(a))

class constructor_self():

    def detail(self,):
        self.name = 'ansal'
        self.age = 19
        print(self.name)
        
    def update (self):
        self.age = 20
        return self.age
       
  # c1 = constructor_self()

  # c2 = constructor_self()

  # c1.detail()

class dog:

    def __init__(self,age,colour):
        self.age = age
        self.colour = colour


    def details (self):
        
        print('age :',self.age)
        print('colour : ',self.colour)
    def compare(self,others):
        if self.age == others.age:
            return True
        else:
            return False

tommy = dog(5,'gold')
piku = dog(3,'black')
# print(tommy)
# tommy.details()
# piku.details()
# if tommy.compare(piku):
    # print('they are same')
# else :
    # print('they are diffrent')

    
class hack1:
    def print_formatted(number):
        width = len(bin(number)) - 2  
    
        for i in range(1, number + 1):
            decimal_format = "{:>{width}d}".format(i, width=width)
            octal_format = "{:>{width}o}".format(i, width=width)
            hexadecimal_format = "{:>{width}X}".format(i, width=width)
            binary_format = "{:>{width}b}".format(i, width=width)
    
            print(f"{decimal_format} {octal_format} {hexadecimal_format} {binary_format}")

c1 = hack1
# c1.print_formatted(10)

x = 3.4565678
round_num = round(x,2)
print(f"{round_num}")


def dictionary():   
    student = {
    
        "bike": "2 wheel",    
        "cycle" : "2 wheel",    
        "motorcycle" : "2 wheel",
        "car": "4 wheel",    
        "van" : "6 wheel",    
    }
    
   
    for details in student:    
        print(details,student[details],sep=" : ")
# dictionary()

def hcf():
    num1,num2 = map(int,input().split())
    
    i = 1
    while ( i < num1 and i < num2 ):
    
        if ( num1%i == 0 == num2%i ):
    
            hcf = i
        i +=1
    
    print(hcf)

# hcf()