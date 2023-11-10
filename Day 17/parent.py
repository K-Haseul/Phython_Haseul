class person:
    def __init__(self,name):
        self.name=name
    def greeting(self):
        print(f"Hello, {self.name}")

class 상품:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def how_much(self):
        print(f"{self.name}의 가격은 {self.price}원입니다")