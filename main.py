class Cat:
    est_hvost = True

    def __init__(self, color, age):  # дантер методы
        self.color = color
        self.age = age

    def meow(self):
        print(f"meoooow я {self.color}")

cat_vaska = Cat("black", 1)
cat_petya = Cat("white", 2)

Cat.meow(cat_vaska)
cat_vaska.meow()


print("Hello")
