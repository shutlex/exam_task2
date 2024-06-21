class Product:
    total_products = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.total_products += 1

    def display_info(self):
        print(f"Товар: {self.name}")
        print(f"Ціна: ${self.price}")
        print(f"Всього продуктів створено: {Product.total_products}")
        print()


class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self.warranty_period = warranty_period

    def display_info(self):
        super().display_info()
        print(f"Термін гарантії: {self.warranty_period} місяців")
        print()


class ClothingProduct(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Розмір: {self.size}")
        print()


def main():
    p1 = Product("Телефон", 599)
    p2 = ElectronicProduct("Ноутбук", 1299, 12)
    p3 = ClothingProduct("Футболка", 29.99, "M")

    p1.display_info()
    p2.display_info()
    p3.display_info()


if __name__ == "__main__":
    main()

