class Store:
    dicount=0.8
    def __init__(self,name,price,quantity):
        assert price>=0,"Error occur because O or less is not acceptable"
        assert quantity>=0,"Error occur because O or less is not acceptable"

        self.product_name=name
        self.product_price=price
        self.product_quantity=quantity

    def t_calculate(self):
        return self.product_price*self.product_quantity
    def d_allowed(self):
        return self.dicount*self.product_price*self.product_quantity
    
p1=Store("phone",450,17)
p2=Store("laptop",760,13)

# print(p1.__dict__)
# print(Store.__dict__)


print(f"Total Amount:{p1.t_calculate()}")
print(f"After Discount Amount:{p1.d_allowed()}")
# print(p2.t_calculate())