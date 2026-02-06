class Cars:
    def __init__(self, brand, price):
        self.brand = brand
        self.price =price
      # this is a methods that is created by the user for objects
    def Thanks(self):
        print("thaks for taking", self.brand)
    
    def speed(self):
        print("10,000cc to 20,000cc")
    
    def what_price(self):
        return self.price
    
c1 = Cars("ferrari",20,000)
print(c1.brand,c1.price)
    