# Create a class called Shop. Upon initialization, it should receive a name (str), type (str), and capacity (int).
# The store should also have an attribute called items (an empty dictionary that stores the name of an item and its
# quantity). The class should have 4 methods:
# •	small_shop(name: str, type: str) - a new shop with a capacity of 10 should be created
# •	add_item(item_name: str) - adds 1 to the quantity of the given item. On success, the method should return
# "{item_name} added to the shop". If the addition is not possible, the following message should be returned
# "Not enough capacity in the shop"
# •	remove_item(item_name:str, amount:int) - removes the given amount from the item. On success, it should return
# "{amount} {item_name} removed from the shop". Otherwise, the method should return "Cannot remove {amount} {item_name}"
#   o	If the item quantity reaches 0, the item should be removed from the items' dictionary.
# •	__repr__() - returns a string representation in the format "{shop_name} of type {shop_type} with capacity {shop_capacity}"
#
# Test code:
# fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
# small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
# print(fresh_shop)
# print(small_shop)
#
# print(fresh_shop.add_item("Bananas"))
# print(fresh_shop.remove_item("Tomatoes", 2))
#
# print(small_shop.add_item("Jeans"))
# print(small_shop.add_item("Jeans"))
# print(small_shop.remove_item("Jeans", 2))
# print(small_shop.items)
#
# Output:
# Fresh Shop of type Fruit and Veg with capacity 50
# Fashion Boutique of type Clothes with capacity 10
# Bananas added to the shop
# Cannot remove 2 Tomatoes
# Jeans added to the shop
# Jeans added to the shop
# 2 Jeans removed from the shop
# {}

class Shop:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, items_name:str):
        if self.capacity <= sum(self.items.values()):
            return "Not enough capacity in the shop"
        if items_name not in self.items:
            self.items[items_name] = 0
        self.items[items_name] += 1
        return f"{items_name} added to the shop"

    def remove_item(self, item_name, amount):
        if item_name not in self.items or self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"
        self.items[item_name] -= amount
        if self.items[item_name] == 0:
            del self.items[item_name]
        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)
