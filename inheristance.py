class pearson(object):
   
    def __init__(self,name,idnum):
        self.name = name
        self.idnum = idnum
       
    def display(self):
        print(self.idnum)
        print(self.name)
       
    def details(self): 
        print(f"id number : {self.idnum}")
        print(f"name : {self.name}")
       
class employee(pearson):
    def __init__(self,name,idnum,salary,post):
        self.salary = salary
        self.post = post
       
        pearson.__init__(self,name,idnum)
       
    def details(self):
        print(f"name : {self.name}")
        print(f"id number : {self.idnum}")
        print(f"salary : {self.salary}")
        print(f"post :{self.post}")
       
a = employee("ansal",14423,200000, "Intern")
a.details()
