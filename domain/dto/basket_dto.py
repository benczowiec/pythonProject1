from decimal import Decimal


class BasketDto:

    def __init__(self, basket_id, total_price: Decimal, quantity: int, user_id: int, product_id):
        self.basket_id = basket_id
        self.total_price = total_price
        self.quantity = quantity
        self.user_id = user_id
        self.product_id = product_id