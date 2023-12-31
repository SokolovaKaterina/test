class Cat:
    est_hvost = True

    def __init__(self, color, age):  # дантер методы
        self.color = color
        self.age = age

    # self - ссылка на сам экземпляр
    def meow(self):
        print(f"meoooow я {self.color}")


# экземпляр класса, без параметров цвет и возраст не сможет вызваться
cat_vaska = Cat("black", 1)
cat_petya = Cat("white", 2)

Cat.meow(cat_vaska)
cat_vaska.meow()


print("Hello")
