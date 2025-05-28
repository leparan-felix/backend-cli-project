class Product:
    def __init__(self, id, name, quantity, price, ):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
      

    def is_low_stock(self):
        return self.quantity < 10

    def __str__(self):
        status = "LOW STOCK" if self.is_low_stock() else ""
        return f"[{self.id}] {self.name} - Qty: {self.quantity}, Price: ${self.price:.2f} {status}"
