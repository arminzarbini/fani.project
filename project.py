import csv
from datetime import date

class Food:
    def __init__(
            self, food_code, food_name, company, manufacture_date, 
            expire_date, purchase_order, stock, price
            ):
        self.food_code = food_code
        self.food_name = food_name
        self.company = company
        self.manufacture_date = manufacture_date
        self.expire_date = expire_date
        self.purchase_order = purchase_order
        self.stock = stock
        self.price = price

    def get_food_code(self):
        return self.food_code
    
    def edit_food_name(self,new_food_name):
        self.food_name = new_food_name

    def edit_company(self,new_company):
        self.company = new_company

    def edit_manufacture_date(self,new_manufacture_date):
        self.manufacture_date = new_manufacture_date

    def edit_expire_date(self,new_expire_date):
        self.expire_date = new_expire_date

    def edit_price(self,new_price):
        self.price = new_price


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
    def __init__(self, store_code, store_name, not_delivered_orders, sell_price):
        self.store_code = store_code
        self.store_name = store_name
        self.not_delivered_orders = not_delivered_orders
        self.sell_price = sell_price

    def get_store_code(self):
        return self.store_code
    
    def edit_store_name(self,new_store_name):
        self.store_name = new_store_name


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
    add_user(new_user_list)

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
    update_user()
        
def create_all_user():
    default_header = ["UserName", "NameFamily", "NationalCode", "PhoneNumber", "PurchaseAmmount", "Discount", "Debit"]
    with open("user.csv","r") as user_file:
        user_reader = csv.reader(user_file)
        header = next(user_reader)
        for row in user_reader :
            user = User(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            all_user.append(user)

def add_user(new_user_list):
    with open("user.csv","a",newline="\n") as user_file:
        user_writer = csv.writer(user_file)
        user_writer.writerow(new_user_list)

def update_user():
    default_header = ["UserName", "NameFamily", "NationalCode", "PhoneNumber", "PurchaseAmmount", "Discount", "Debit"]  
    user = []              
    with open("user.csv","w",newline="\n") as user_file:
        user_writer = csv.writer(user_file)
        user_writer.writerow(default_header)
        for object in all_user :
            user = [object.user_name,object.name_family,object.national_code,object.phone_number,object.purchase_ammount,object.discount,object.debit]
            user_writer.writerow(user) 

def register_store():
    try :            
        store_code_new = object.get_store_code()
    except:
        store_code_new = 100000
    else :
        store_code_new  = int(object.get_store_code()) + 1
    while True :
        store_name_input = input("store name : ")
        if store_name_input.isalnum() == False :
            print("enter storename only with alphabet letter (a-z) and numbers (0-9)")
        else :
            for object in all_store :
                if object.store_name == store_name_input :
                    print("storename already exists")
                    break
            else :
                break
    new_store = Store(store_code_new,store_name_input,0,0)
    all_store.append(new_store)
    new_store_list = [new_store.store_code,new_store.store_name,new_store.not_delivered_orders,new_store.sell_price]
    add_store(new_store_list)
    
def edit_store():
    store_name_show = []
    with open("store.csv","r") as store_file:
        store_reader = csv.DictReader(store_file)
        for row in store_reader :
            store_name_show.append(row["StoreName"])
    for item in store_name_show :
            print(item,end="|")
    print()
    while True :
        store_edit_input = input("choose store name from the top stores : ")
        if store_edit_input in store_name_show :
            break
        else :
            print("this store does not exist!")
    for object in all_store:
        if object.store_name == store_edit_input:
            print(f"Store Code : {object.store_code}")
            print(f"Store Name : {object.store_name}")
            print(f"Not Delivered Orders : {object.not_delivered_orders}")
            print(f"Sell Price : {object.sell_price}")
            while True :
                print("""1.edit store name
2.exit""")
                edit_input = input("")
                if edit_input == "1":
                    while True :
                        store_name_edit_input = input("store name : ")
                        if store_name_edit_input.isalnum() == False :
                             print("enter storename only with alphabet letter (a-z) and numbers (0-9)")
                        else :
                            if store_name_edit_input in store_name_show :
                                print("store name already exist")
                            else :
                                object.edit_store_name(store_name_edit_input)
                            break
                elif edit_input == "2":
                    break
                else :
                    print("\nwrite the correct command!\n")
    update_store()

def create_all_store():
    default_header = ["StoreCode", "StoreName", "NotDeliveredOrders", "SellPrice"]
    with open("store.csv","r") as store_file:
        store_reader = csv.reader(store_file)
        header = next(store_reader)
        for row in store_reader :
            store = Store(row[0],row[1],row[2],row[3])
            all_store.append(store)

def add_store(new_store_list):
    with open("store.csv","a",newline="\n") as store_file:
        store_wiriter = csv.writer(store_file)
        store_wiriter.writerow(new_store_list)

def update_store():
    default_store_header = ["StoreCode", "StoreName", "NotDeliveredOrders", "SellPrice"]  
    store = []              
    with open("store.csv","w",newline="\n") as store_file:
        store_writer = csv.writer(store_file)
        store_writer.writerow(default_store_header)
        for object in all_store :
            store = [object.store_code,object.store_name,object.not_delivered_orders,object.sell_price]
            store_writer.writerow(store)

def register_food():
    try :            
        food_code_new = object.get_food_code()
    except:
        food_code_new = 100000
    else :
        food_code_new  = int(object.get_store_code()) + 1
    while True :   
        food_name_input = input("food name : ")
        for object in all_food:
            if object.food_name == food_name_input:
                print("food name already exist")
                break
        else :
            break  
    company_input = input("company : ")
    while True :
        manufacture_date_input = input("enter manufacture date.example : 1990,9,30 : ").split(",")
        try :
            manufacture_date = date(int(manufacture_date_input[0]),int(manufacture_date_input[1]),int(manufacture_date_input[2]))
        except IndexError :
            print("enter correct fomrat.example : 1990,9,30")
        except TypeError:
            print("enter numbers")
        except ValueError:
            print("enter year between 1 to 9999-enter month between 1 to 12-enter day between 1 to 30")
        else :
            today = date.today()
            if today < manufacture_date :
                print("manufacture date must be today or before today")
            else :
                manufacture_date_str = manufacture_date.strftime("%Y-%m-%d")
                break
    while True:
        expire_date_input = input("enter expire date.example : 2024,12,17 : ").split(",")
        try :
            expire_date = date(int(expire_date_input[0]),int(expire_date_input[1]),int(expire_date_input[2]))
        except IndexError :
            print("enter correct fomrat.example : 2024,12,17")
        except TypeError:
            print("enter numbers")
        except ValueError:
            print("enter year between 1 to 9999-enter month between 1 to 12-enter day between 1 to 30")    
        else :
            if expire_date < manufacture_date :
                print("expire date must be after manufacture date")     
            elif expire_date < today :
                print("this product has expired")
                continue_for_expire = input("do you want to continue : Yes or No")
                if continue_for_expire == "Yes" :
                    expire_date_str = expire_date.strftime("%Y-%m-%d")
                    break
                elif continue_for_expire == "No" :
                    return(False)
                else :
                    print("write the correct command.Yes Or No: ")
            else :
                expire_date_str = expire_date.strftime("%Y-%m-%d")
                break
    while True :
        try : 
            purchase_order_input = int(input("purchase order : "))
        except :
            print("write number")
        else :
            break
    stock = purchase_order_input
    while True :
        price_flag = True
        price_input = input("price(example : 100.000.000) : ").split(".")
        for item in price_input :
            if len(item) != 3 :
                print("enter correct format")
            elif item.isnumeric() == False :
                price_flag = False
                print("write numbers")
                break
        if price_flag == True :
            price = ""
            for item in range(len(price_input)):
                price = price + price_input[item]
            break
    new_food = Food(food_code_new,food_name_input,company_input,manufacture_date_str,expire_date_str,purchase_order_input,stock,price)
    all_food.append(new_food)
    new_food_list = [new_food.food_code,new_food.food_name,new_food.company,new_food.manufacture_date,new_food.expire_date,new_food.purchase_order,new_food.stock,new_food.price]
    add_food(new_food_list)

def edit_food():
    food_name_show = []
    with open("food.csv","r") as food_file:
        food_reader = csv.DictReader(food_file)
        for row in food_reader :
            food_name_show.append(row["FoodName"])
    for item in food_name_show :
            print(item,end="|")
    print()
    while True :
        food_edit_input = input("choose food name from the top foods : ")
        if food_edit_input in food_name_show :
            break
        else :
            print("this food does not exist!")
    for object in all_food:
        if object.food_name == food_edit_input:
            print(f"Food Code : {object.food_code}")
            print(f"Food Name : {object.food_name}")
            print(f"Company : {object.company}")
            print(f"Manufacture Date : {object.manufacture_date}")
            print(f"Expire Date : {object.expire_date}")
            print(f"Purchese Order : {object.purchase_order}")
            print(f"Stock : {object.stock}")
            print(f"Price : {object.price}")
            while True :
                print("""1.edit food name
2.edit company
3.edit manufacture date
4.edit expire date
5.edit price
6.exit""")
                edit_input = input("")
                if edit_input == "1":
                    while True :   
                        food_name_edit_input = input("new food name : ")
                        if food_name_edit_input in food_name_show :
                            print("food name already exist")
                        else :
                            object.edit_food_name(food_name_edit_input)
                            break
                elif edit_input == "2":
                    company_input = input("new company : ")
                    object.edit_company(company_input)
                elif edit_input == "3":
                    while True :
                        manufacture_date_input = input("enter manufacture date.example : 1990,9,30 : ").split(",")
                        try :
                            manufacture_date = date(int(manufacture_date_input[0]),int(manufacture_date_input[1]),int(manufacture_date_input[2]))
                        except IndexError :
                            print("enter correct fomrat.example : 1990,9,30")
                        except TypeError:
                            print("enter numbers")
                        except ValueError:
                            print("enter year between 1 to 9999-enter month between 1 to 12-enter day between 1 to 30")
                        else :
                            today = date.today()
                            if today < manufacture_date :
                                print("manufacture date must be today or before today")
                            else :
                                manufacture_date_str = manufacture_date.strftime("%Y-%m-%d")
                                object.edit_manufacture_date(manufacture_date_str)
                                break
                elif edit_input == "4":
                    while True:
                        expire_date_input = input("enter expire date.example : 2024,12,17 : ").split(",")
                        try :
                            expire_date = date(int(expire_date_input[0]),int(expire_date_input[1]),int(expire_date_input[2]))
                        except IndexError :
                            print("enter correct fomrat.example : 2024,12,17")
                        except TypeError:
                            print("enter numbers")
                        except ValueError:
                            print("enter year between 1 to 9999-enter month between 1 to 12-enter day between 1 to 30")    
                        else :
                            if expire_date < manufacture_date :
                                print("expire date must be after manufacture date")     
                            elif expire_date < today :
                                print("this product has expired")
                                continue_for_expire = input("do you want to continue : Yes or No")
                                if continue_for_expire == "Yes" :
                                    expire_date_str = expire_date.strftime("%Y-%m-%d")
                                    object.edit_expire_date(expire_date_str)
                                    break
                                elif continue_for_expire == "No" :
                                    break
                                else :
                                    print("write the correct command.Yes Or No: ")
                            else :
                                expire_date_str = expire_date.strftime("%Y-%m-%d")
                                object.edit_expire_date(expire_date_str)
                            break
                elif edit_input == "5":
                    while True :
                        price_flag = True
                        price_input = input("price(example : 100.000.000) : ").split(".")
                        for item in price_input :
                            if len(item) != 3 :
                                print("enter correct format")
                            elif item.isnumeric() == False :
                                price_flag = False
                                print("write numbers")
                                break
                        if price_flag == True :
                            price = ""
                            for item in range(len(price_input)):
                                price = price + price_input[item]
                                object.edit_price(price)
                            break
                elif edit_input == "6":
                    break
                else :
                    print("wire the correct command")
    update_food()          

def create_all_food():
    default_header = ["FoodCode", "FoodName", "Company", "ManufactureDate","ExpireDate","PurchaseOrder","Stock","Price"]
    with open("food.csv","r") as food_file:
        food_reader = csv.reader(food_file)
        header = next(food_reader)
        for row in food_reader :
            food = Food(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
            all_food.append(food)

def add_food(new_food_list):
    with open("food.csv","a",newline="\n") as food_file:
        food_wiriter = csv.writer(food_file)
        food_wiriter.writerow(new_food_list)

def update_food():
    default_header = ["FoodCode", "FoodName", "Company", "ManufactureDate","ExpireDate","PurchaseOrder","Stock","Price"]  
    food = []              
    with open("food.csv","w",newline="\n") as food_file:
        food_writer = csv.writer(food_file)
        food_writer.writerow(default_header)
        for object in all_food :
            food = [object.food_code,object.food_name,object.company,object.manufacture_date,object.expire_date,object.purchase_order,object.stock,object.price]
            food_writer.writerow(food) 


all_user = []
all_store = []
all_food = []
create_all_user()
create_all_store()
create_all_food()






  










    