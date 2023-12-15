import pandas as pd
import csv

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
    def __init__(self, user_name, name_family, national_code, phone_number, purchase_ammount, discount, debit):
        self.username = user_name
        self.name_family = name_family
        self.national_code = national_code
        self.tel_number = phone_number
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
    def __init__(self, order_code, food_code, order_number, order_date, delivery_date, user_name):
        super().__init__(order_code, food_code, order_number, order_date, delivery_date)
        self.username = user_name


def register_user():
    user_name_check = []
    national_code_check = []
    phone_number_check = []
    with open("user.csv","r") as user_file:
        user_reader = csv.reader(user_file)
        header = next(user_reader)
        for row in user_reader:
            user_name_check.append(row[0])
            national_code_check.append(row[2])
            phone_number_check.append(row[3])
    while True :
        user_name_input = input("username : ")
        if user_name_input.isalnum() == False :
            print("enter username only with alphabet letter (a-z) and numbers (0-9)")
        else:
            if user_name_input in user_name_check :
                print("username already exists")
            else :
                break
    while True :
        try : 
            name,family = input("name and family : ").split(" ")
        except :
            print("enter one space between name and family")
        else :
            if name.isalpha() == False or family.isalpha == False :
                print("enter name and family only with alphabet letter (a-z)")
            else :
                break
    name_family_input = f"{name} {family}"
    while True :
        national_code_input = input("national code : ")
        if national_code_input.isnumeric == False or len(national_code_input) != 10 :
            print("enter national code with ten numbers (0-9)")
        else : 
            if national_code_input in national_code_check :
                print("national code already exists")
            else :
                break  
    while True :
        phone_number_input = input("phone number : ")   
        if phone_number_input.startswith("0") == False :
            print("start with 0")
        elif len(phone_number_input) != 11 or phone_number_input.isalnum == False :
            print("enter 12 numbers.example : 09352993173")
        else :
            if phone_number_input in phone_number_check :
                print("phone number already exists")
            else :
                break
                
    new_user = User(user_name_input, name_family_input, national_code_input, phone_number_input, 0, 0, 0)
    new_user_list = [new_user.username,new_user.name_family,new_user.national_code,new_user.tel_number,new_user.purchase_ammount,new_user.discount,new_user.debit]
    with open("user.csv","a",newline="\n") as user_file:
            user_writer = csv.writer(user_file)
            user_writer.writerow(new_user_list)



    
register_user()

  










    