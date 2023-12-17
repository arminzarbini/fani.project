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
        self.user_name = user_name
        self.name_family = name_family
        self.national_code = national_code
        self.phone_number = phone_number
        self.purchase_ammount = purchase_ammount
        self.discount = discount
        self.debit = debit

    def edit_user_name(self,new_user_name):
        self.user_name = new_user_name


    def edit_user_name_family(self,new_name_family):
        self.name_family = new_name_family


    def edit_national_code(self,new_national_code):
        self.national_code = new_national_code


    def edit_phone_number(self,new_phone_numnber):
        self.phone_number = new_phone_numnber

    

    
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
    while True :
        user_name_input = input("username : ")
        if user_name_input.isalnum() == False :
            print("enter username only with alphabet letter (a-z) and numbers (0-9)")
        else:
            for object in all_user :
                if object.user_name == user_name_input :
                    print("username already exists")
                    break
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
            for object in all_user :
                if object.national_code == national_code_input :
                    print("national code already exists")
                    break
            else :
                break 
    while True :
        phone_number_input = input("phone number : ")   
        if phone_number_input.startswith("0") == True :
            print("start without 0")
        elif len(phone_number_input) != 10 or phone_number_input.isalnum == False :
            print("enter 10 numbers.example : 9352993173")
        else :
            for object in all_user :
                if object.phone_number == phone_number_input :
                    print("phone number already exists")
                    break
            else :
                break         
    new_user = User(user_name_input, name_family_input, national_code_input, phone_number_input, 0, 0, 0)
    all_user.append(new_user)
    new_user_list = [new_user.user_name,new_user.name_family,new_user.national_code,new_user.phone_number,new_user.purchase_ammount,new_user.discount,new_user.debit]
    with open("user.csv","a",newline="\n") as user_file:
            user_writer = csv.writer(user_file)
            user_writer.writerow(new_user_list)


def edit_user():
    user_name_show = []
    national_code_show = []
    phone_number_show = []
    with open("user.csv","r") as user_file:
        user_reader = csv.DictReader(user_file)
        for row in user_reader :
            user_name_show.append(row["UserName"])
            national_code_show.append(row["NationalCode"])
            phone_number_show.append(row["PhoneNumber"])
    for item in user_name_show :
            print(item,end="|")
    print()
    while True :
        user_edit_input = input("choose username from the top usernames : ")
        if user_edit_input in user_name_show :
            break
        else :
            print("this username does not exist!")
    for object in all_user :
        if object.user_name == user_edit_input :
            print(f"UserName : {object.user_name}")
            print(f"Name and Family : {object.name_family}")
            print(f"National Code : {object.national_code}")
            print(f"Phone Number : {object.phone_number}")
            print(f"Purchase Amount : {object.purchase_ammount}")
            print(f"Discount : {object.discount}")
            print(f"Debit : {object.debit}")
            while True :
                print("""1.edit username
2.edit name and family
3.edit national code
4.edit phone number
5.exit""")
                edit_input = input("")
                if edit_input == "1":
                    while True :
                        user_name_edit_input = input("new username : ")
                        if user_name_edit_input.isalnum() == False :
                            print("enter username only with alphabet letter (a-z) and numbers (0-9)")
                        else :
                            if user_name_edit_input in user_name_show :
                                print('username already exist')
                            else :
                                object.edit_user_name(user_name_edit_input)
                                break
                elif edit_input == "2" :
                    while True :
                        try : 
                            name,family = input("name and family : ").split(" ")
                        except :
                            print("enter one space between name and family")
                        else :
                            if name.isalpha() == False or family.isalpha == False :
                                print("enter name and family only with alphabet letter (a-z)")
                            else :
                                name_family_edit_input = f"{name} {family}"
                                object.edit_user_name_family(name_family_edit_input)
                            break
                elif edit_input == "3" :
                    while True :
                        national_code_edit_input = input("national code : ")
                        if national_code_edit_input.isnumeric == False or len(national_code_edit_input) != 10 :
                            print("enter national code with ten numbers (0-9)")
                        else : 
                            if national_code_edit_input in national_code_show :
                                print("national code already exists")
                            else :
                                object.edit_national_code(national_code_edit_input)
                                break
                elif edit_input == "4" :
                    while True :
                        phone_number_edit_input = input("phone number : ")   
                        if phone_number_edit_input.startswith("0") == True :
                            print("start without 0")
                        elif len(phone_number_edit_input) != 10 or phone_number_edit_input.isalnum == False :
                            print("enter 10 numbers.example : 9352993173")
                        else :
                            if phone_number_edit_input in phone_number_show :
                                print("phone number already exists")
                            else :
                                object.edit_phone_number(phone_number_edit_input)
                                break
                elif edit_input == "5" :                    
                    break
                else : 
                    print("\nwrite the correct command!\n")

    default_header = ["UserName", "NameFamily", "NationalCode", "PhoneNumber", "PurchaseAmmount", "Discount", "Debit"]  
    user = []              
    with open("user.csv","w",newline="\n") as user_file:
        user_writer = csv.writer(user_file)
        user_writer.writerow(default_header)
        for object in all_user :
            user = [object.user_name,object.name_family,object.national_code,object.phone_number,object.purchase_ammount,object.discount,object.debit]
            user_writer.writerow(user)

        
        

def create_all_user():
    default_header = ["UserName", "NameFamily", "NationalCode", "PhoneNumber", "PurchaseAmmount", "Discount", "Debit"]
    with open("user.csv","r") as user_file:
        user_reader = csv.reader(user_file)
        header = next(user_reader)
        for row in user_reader :
            user = User(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            all_user.append(user)
            
all_user = []
create_all_user()
edit_user()





  










    