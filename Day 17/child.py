import parent as p

class Female(p.person):
    def greeting(self):
        print("Hello, everyone^^")

class male(p.person):
    def greeting(self):
        print("Hi, guys ㅠㅠ")

class pencil(p.상품):
    def how_much_dozen(self):
        print(f"{self.name}한 다스의 가격은 {self.price*12}원 입니다")

class eraser(p.상품):
    def how_much_pack(self):
        print(f"{self.name}한 팩의 가격은 {self.price*10}원 입니다")