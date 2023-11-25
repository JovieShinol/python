class item:
    
    all = []
    pay_rate = 0.8 # 20% Discount 
    def __init__(self,name,price,quantity = 0):
        # Run validation to the received argument
        assert price >=0 , f"price {price} is not greater than or equal to zero"
        assert quantity >=0 , f"quantity {quantity} is not greater than or equal to zero"
        
        # assign self object
        self.name = name
        self.price = price
        self.quantity = quantity
        item.all.append(name)
    
        
    def calc(self):
        return f"total {self.name} price : {self.price*self.quantity}"
    def discount(self):
        return  f"{self.name} at offer price : {self.price*self.pay_rate}"   




item1 = item("phone",10000,5)
print(item1.discount())

item2 = item("watch",2000,3)
item2.pay_rate = 0.7
print(item2.discount())
print(item.all)
