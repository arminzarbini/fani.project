class MavadeGhazaei :
    def __init__(
            self, food_code, name, company, nature, product_date, 
            expiration_date, purchase_order, stock, price
            ):
        self.code = food_code
        self.name = name
        self.company = company
        self.nature = nature
        self.product_date = product_date
        self.expiration_date = expiration_date
        self.purchase_order = purchase_order
        self.stock = stock
        self.price = price


class Kharbar(MavadeGhazaei):
    def __init__(self, food_code, name, company, nature, product_date, expiration_date, purchase_order, stock, price):
        super().__init__(food_code, name, company, nature, product_date, expiration_date, purchase_order, stock, price)


class Labaniat(MavadeGhazaei):
    def __init__(self, food_code, name, company, nature, product_date, expiration_date, purchase_order, stock, price, fat):
        super().__init__(food_code, name, company, nature, product_date, expiration_date, purchase_order, stock, price)
        self.fat = fat


class MavadeProteini(MavadeGhazaei):
    def __init__(self, food_code, name, company, nature, product_date, expiration_date, purchase_order, stock, price, meat_color):
        super().__init__(food_code, name, company, nature, product_date, expiration_date, purchase_order, stock, price)
        self.meat_color = meat_color


class Noshidani(MavadeGhazaei):
    def __init__(self, food_code, name, company, nature, product_date, expiration_date, purchase_order, stock, price, hot_cold, carbonated):
        super().__init__(food_code, name, company, nature, product_date, expiration_date, purchase_order, stock, price)
        self.hot_cold = hot_cold
        self.carbonated = carbonated


class Tanagholat(MavadeGhazaei):
    def __init__(self, food_code, name, company, nature, product_date, expiration_date, purchase_order, stock, price):
        super().__init__(food_code, name, company, nature, product_date, expiration_date, purchase_order, stock, price)
        

class BehdashtiArayeshi(MavadeGhazaei):
    def __init__(self, food_code, name, company, nature, product_date, expiration_date, purchase_order, stock, price):
        super().__init__(food_code, name, company, nature, product_date, expiration_date, purchase_order, stock, price)


class GhazayeAmade(MavadeGhazaei):
    def __init__(self, food_code, name, company, nature, product_date, expiration_date, purchase_order, stock, price):
        super().__init__(food_code, name, company, nature, product_date, expiration_date, purchase_order, stock, price)


class ChashniAdvieh(MavadeGhazaei):
    def __init__(self, food_code, name, company, nature, product_date, expiration_date, purchase_order, stock, price):
        super().__init__(food_code, name, company, nature, product_date, expiration_date, purchase_order, stock, price)


class User():
    def __init__(self, username, name_family, national_code, tel, purchase_ammount, discount, debit):
        self.username = username
        self.name_family = name_family
        self.national_code = national_code
        self.tel = tel
        self.purchase_ammount = purchase_ammount
        self.discount = discount
        self.debit = debit


class Store():
    def __init__(self, store_code, store_name, delivered_orders, sell_price):
        self.store_code = store_code
        self.store_name = store_name
        self.delivered_orders = delivered_orders
        self.sell_price = sell_price


class Order():
    def __init__(self, order_code, food_code, order_number, order_date, delivery_date):
        self.order_code = order_code
        self.food_code = food_code
        self.order_number = order_number
        self.order_date = order_date
        self.delivery_date = delivery_date


class StoreOrder(Order):
    def __init__(self, order_code, food_code, order_number, order_date, delivery_date, store_code):
        super().__init__(order_code, food_code, order_number, order_date, delivery_date)
        self.store_code = store_code


class UserOrder(Order):
    def __init__(self, order_code, food_code, order_number, order_date, delivery_date, username):
        super().__init__(order_code, food_code, order_number, order_date, delivery_date)
        self.username = username





    