class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, quantity, price):
        self.products[product_id] = {
            "name": name,
            "quantity": quantity,
            "price": price
        }

    def add_stock(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id]["quantity"] += quantity

    def remove_stock(self, product_id, quantity):
        if product_id not in self.products:
            return False

        if self.products[product_id]["quantity"] < quantity:
            return False

        self.products[product_id]["quantity"] -= quantity
        return True

    def get_stock(self, product_id):
        if product_id in self.products:
            return self.products[product_id]["quantity"]

        return 0


if __name__ == "__main__":
    inventory = Inventory()

    inventory.add_product(
        product_id=101,
        name="Notebook",
        quantity=50,
        price=80
    )

    inventory.add_stock(101, 20)
    inventory.remove_stock(101, 10)

    print("Product:", inventory.products[101]["name"])
    print("Available Stock:", inventory.get_stock(101))
