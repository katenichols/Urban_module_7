from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = "products.txt"

    def get_products(self):
        file_ = open(self.__file_name, "r")
        file_.seek(0)
        pprint(file_.read())
        file_.close()

    def add(self, *products):
        file = open(self.__file_name, "r+")
        content = file.read()
        for el in products:
            str_ = "".join(str(el))
            if str_ in content:
                print(f"Продукт {el.name} уже есть в магазине")
            else:
                file.write(str_ + "\n")
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
