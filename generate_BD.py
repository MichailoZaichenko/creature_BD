import sqlalchemy
from table_patern import BaseClass, Product, Order, OrderProduct,Role,  PickupPoint, User  
from sqlalchemy.orm import Session
from random import randint
class Creature_bd:
    bdEngine = sqlalchemy.create_engine("sqlite:///bot_BD.db")
    bdConection = bdEngine.connect()

    BaseClass.metadata.drop_all(bdEngine)
    BaseClass.metadata.create_all(bdEngine)

    # заполнене таблицы Products для ПРИМЕРА    
    with Session(bdEngine) as db:
        row_1 = Product( name = "Burger",
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

        row_2 = Product(
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

        # row_3 = Product(
        #     name = "French fries",
        #     description = 'potatoes',
        #     picture = "picture/French fries.png",
        #     price = 22, 
        #     quantity = 7)
        # db.add(row_3)
        # db.commit()

        # row_4 = Product(
        #     name = "Hamburger",
        #     description = '''
        #                 grilled natural beef steak,
        #                 toasted burger bun,
        #                 seasoning for grill,
        #                 mustard sauce,
        #                 pickles,
        #                 reconstituted onion,
        #                 ''',
        #     picture = "picture/Hamburger.png",
        #     price = 20, 
        #     quantity = 5)
        # db.add(row_4)
        # db.commit()

    # заполнене таблицы Orders для ПРИМЕРА
    # with Session(bdEngine) as db:
    #     row_1 = Order(
    #         id_user = 1,
    #         pickupPoint = 'avenue Dmytro Yavornytsky 100',
    #         dateTime = 14,
    #         typePay = 'cash',
    #         status = 'ready'
    #         )
    #     db.add(row_1)
    #     db.commit()

    #     row_2 = Order(
    #         id_user = 2,
    #         pickupPoint = 'avenue Dmytro Yavornytsky 50',
    #         dateTime = 13,
    #         typePay = 'cash',
    #         status = 'wait'
    #         )
    #     db.add(row_2)
    #     db.commit()
        
    # заполнене таблицы Orders-Products для ПРИМЕРА
    with Session(bdEngine) as db:
        pr = Product( name = "Burger2",
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

        # заполнене таблицы PickupPoint для ПРИМЕРА
        place1 = PickupPoint(
            name = "Sholochova 56",
            coordinats = 45.234
           )  
        db.add(place1)
        db.commit()
        place2 = PickupPoint(
            name = "Minicha 56",
            coordinats = 76.234
           )  
        db.add(place1)
        db.commit()

        # заполнене таблицы Role для ПРИМЕРА
        user = Role(
            name = "User",
            role_child = []
           )    
        admin = Role(
            name = "Admin",
            role_child = []
           ) 
        meneger = Role(
            name = "Meneger",
            role_child = []
           )  
        db.add_all((user, admin, meneger))
        db.commit()

        # заполнене таблицы User для ПРИМЕРА
        user1 = User(
            id_Telegram = 123,
            role_parent = admin,
            name = "Ivan",
            lastName = "Shelkovski"
           )  

        user2 = User(
            id_Telegram = 435,
            role_parent = user,
            name = "Boris",
            lastName = "Shelk"
           )
        user3 = User(
            id_Telegram = 678,
            role_parent = meneger,
            name = "Gianni",
            lastName = "White"
           )    
        db.add_all((user1, user2, user3))
        db.commit()
        
        # заполнене таблицы Order для ПРИМЕРА
        ord1 = Order(
            id_user=user1.id_Telegram,
            order_parent=place1,
            dateTime=14,
            typePay='cash',
            status='ready'
        )

        ord2 = Order(
            id_user=user2.id_Telegram,
            order_parent=place2,
            dateTime=14,
            typePay='cash',
            status='ready'
        )
        db.add_all((ord1, ord2))
        db.commit()


        # row_1 = OrderProduct(
        #     order=ord1,
        #     product=pr,
        #     # id_order = 1,
        #     # id_product = 2, 
        #     quantity = 10
        # )
        # db.add(row_1)
        # db.commit()
    
        # row_2 = OrderProduct(
        #     # id_order = 2,
        #     # id_product = 3,
        #     quantity = 11
        # )
        # db.add(row_2)
        # db.commit()
    
    
    
    

    





# функция добавления строки в таблицу User
    def row_add_users(userDictionary:dict)->User:
        with Session(Creature_bd.bdEngine) as db:
            row = User(
                id_Telegram = userDictionary['id_Telegram'], 
                role = userDictionary['role'], 
                name = userDictionary['name'], 
                lastName = userDictionary['lastName']
            )
            db.add(row)
            db.commit()

# функция добавления строки в таблицу Role
    def row_add_role(userDictionary:dict)->Role:
        with Session(Creature_bd.bdEngine) as db:
            row = Role(
                name = userDictionary['name']
            )
            db.add(row)
            db.commit()

# функция добавления строки в таблицу PickupPoint

    def row_add_pick_up_point(userDictionary:dict)->PickupPoint:
        with Session(Creature_bd.bdEngine) as db:
            row = PickupPoint(
                name = userDictionary['name'], 
                coordinats = userDictionary["coordinats"]
            )
            db.add(row)
            db.commit()

# CRUD(Create, Read, Update, Delete) для таблици User
    
    def ReadUser(id)->dict:
        with Session(Creature_bd.bdEngine) as db:
            user = db.get(Product, id)
            userObj = {'id_Telegram':user.id_Telegram,
            'role':user.role, 
            'name':user.name, 
            'lastName':user.lastName}
        return userObj 
    
    def UpdateUser(id, Role, Name, lastName):
        with Session(Creature_bd.bdEngine) as db:
            user = db.get(Product, id)
            user.id_Telegram = user.id_Telegram
            user.role = Role
            user.Product.name = Name
            user.lastName = lastName
        return user