from project.product import Product


class Drink(Product):
    def __init__(self, name: str):
        self.quantity = 10
        super().__init__(name, self.quantity)
