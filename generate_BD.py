import sqlalchemy
from table_patern import BaseClass, RowTableProduct, RowTableOrder, RowTableOrderProduct,RowTableRole,  RowTablePickupPoint, RowTableUser  
from sqlalchemy.orm import Session
from random import randint
class Creature_bd:
    bdEngine = sqlalchemy.create_engine("sqlite:///bot_BD.db")
    bdConection = bdEngine.connect()

    BaseClass.metadata.drop_all(bdEngine)
    BaseClass.metadata.create_all(bdEngine)

    # заполнене таблицы Products для ПРИМЕРА    
    with Session(bdEngine) as db:
        row_1 = RowTableProduct(
            name = "Burger",
            description = '''
                            veal cutlet, 
                            wheat bun, 
                            American mustard, 
                            red onion, 
                            mayonnaise, 
                            pickles, 
                            lettuce leaf, 
                            barbecue sauce;
                            ''',
            picture = "picture/Burger.png", 
            price = 20,
            quantity = 5)    
        db.add(row_1)
        db.commit()

        row_2 = RowTableProduct(
            name = "Cheeseburger",
            description = '''
                            grilled natural beef steak,
                            seasoning for grill,
                            hamburger bun, toasted,
                            processed cheese Cheddar,
                            mustard sauce,
                            pickles,
                            reconstituted onion
                        ''',
            picture = "picture/Cheeseburger.png",
            price = 20, 
            quantity = 6)
        db.add(row_2)
        db.commit()

        row_3 = RowTableProduct(
            name = "French fries",
            description = 'potatoes',
            picture = "picture/French fries.png",
            price = 22, 
            quantity = 7)
        db.add(row_3)
        db.commit()

        row_4 = RowTableProduct(
            name = "Hamburger",
            description = '''
                        grilled natural beef steak,
                        toasted burger bun,
                        seasoning for grill,
                        mustard sauce,
                        pickles,
                        reconstituted onion,
                        ''',
            picture = "picture/Hamburger.png",
            price = 20, 
            quantity = 5)
        db.add(row_4)
        db.commit()

    # заполнене таблицы Orders для ПРИМЕРА
    with Session(bdEngine) as db:
        row_1 = RowTableOrder(
            id_user = 1,
            pickupPoint = 'avenue Dmytro Yavornytsky 100',
            dateTime = 14,
            typePay = 'cash',
            status = 'ready'
            )
        db.add(row_1)
        db.commit()

        row_2 = RowTableOrder(
            id_user = 2,
            pickupPoint = 'avenue Dmytro Yavornytsky 50',
            dateTime = 13,
            typePay = 'cash',
            status = 'wait'
            )
        db.add(row_2)
        db.commit()

    # заполнене таблицы Orders-Products для ПРИМЕРА
    with Session(bdEngine) as db:
        row_1 = RowTableOrderProduct(
            id_order = 1,
            id_product = 2,
            quantity = 10
        )
        db.add(row_1)
        db.commit()
    
        row_2 = RowTableOrderProduct(
            id_order = 2,
            id_product = 3,
            quantity = 11
        )
        db.add(row_2)
        db.commit()
    
    # заполнене таблицы RowTableRole для ПРИМЕРА
        user = RowTableRole(
            name = "User",
            role_child = []
           )    
        admin = RowTableRole(
            name = "Admin",
            role_child = []
           ) 
        meneger = RowTableRole(
            name = "Meneger",
            role_child = []
           )  
        db.add_all(user, admin, meneger)
        db.commit()
    
    # заполнене таблицы RowTableUser для ПРИМЕРА
        user1 = RowTableUser(
            id_Telegram = randint(1_000_000, 10_000_000),
            role = [],
            name = "Ivan",
            lastName = "Shelkovski"
           )  
        db.add_all(user1)
        db.commit()

    # заполнене таблицы RowTablePickupPoint для ПРИМЕРА
        place1 = RowTablePickupPoint(
            name = "Ivan",
            lastName = "Shelkovski"
           )  
        db.add_all(user1)
        db.commit()




    # функция добавления строки в таблицу Products
    # def row_add_products(productDictionary:dict)->RowTableProducts:
    #     with Session(Creature_bd.bdEngine) as db:
    #         row = RowTableProducts(
    #             picture = productDictionary['picture'], 
    #             product_name = productDictionary['product_name'], 
    #             pickUp_point = productDictionary['pickUp_point'], 
    #             price = productDictionary['price'], 
    #             quantity = productDictionary['quantity'])
    #         db.add(row)
    #         db.commit()

    # # функция добавления строки в таблицу Products
    # def row_add_users(userDictionary:dict)->RowTableUsers:
    #     with Session(Creature_bd.bdEngine) as db:
    #         row = RowTableUsers(
    #             first_name = userDictionary['first_name'], 
    #             last_name = userDictionary['last_name'], 
    #             mail = userDictionary['mail'], 
    #             card_naumber = userDictionary['card_naumber']
    #         )
    #         db.add(row)
    #         db.commit()

    # # выбор укзанной строки
    # def singleSelect(id):
    #     row = Creature_bd.db.get(RowTableProducts, id)
    #     return row

# для проверки функции row_add_products
# myDictionary = {'picture':"picture/Burger.png", 'product_name':"Sandvich", 'pickUp_point':'avenue', 'price':200, 'quantity':9}
# Creature_bd.row_add_products(myDictionary)

 # вывод значений полей БД
# for el in Creature_bd.singleSelect(2):
#     print(el.product_name, el.price)
