class Order:
    def __init__(self, order_id: int, user: User, items: List[Item]):
        self.order_id = order_id
        self.order_name = order_name
        self.items = items

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, item: Item):
        self.items.remove(item)

    def clear_basket(self):
        self.items.clear()

    def basket(self):
        return self.items

    def total_price(self):
        return sum(item.price for item in self.items)
