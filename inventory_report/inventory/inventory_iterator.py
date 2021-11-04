from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, stock):
        self.stock = stock
        self.current_item = 0

    def __next__(self):
        try:
            stock1 = self.stock[self.current_item]
        except IndexError:
            raise StopIteration()
        self.current_item += 1
        return stock1
