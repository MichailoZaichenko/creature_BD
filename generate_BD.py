import sqlalchemy
from table_patern import BaseClass, Product, Order, OrderProduct,Role,  PickupPoint, User  
from sqlalchemy.orm import Session
from random import randint
import config
class Creature_bd:
    bdEngine = sqlalchemy.create_engine(config.nameBD)
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
            coordinats = "45.234.345"
           )  
        db.add(place1)
        db.commit()
        place2 = PickupPoint(
            name = "Minicha 56",
            coordinats = "76.234.123"
           )  
        db.add(place1)
        db.commit()

        # заполнене таблицы Role для ПРИМЕРА
        user = Role(
            name = "User",
            user_role_child = []
           )    
        admin = Role(
            name = "Admin",
            user_role_child = []
           ) 
        meneger = Role(
            name = "Meneger",
            user_role_child = []
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
            pick_up_point_order_parent=place1,
            dateTime=14,
            typePay='cash',
            status='ready'
        )

        ord2 = Order(
            id_user=user2.id_Telegram,
            pick_up_point_order_parent=place2,
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
    
    
    
    

    


# функция добавления строки в таблицу Orders
    def add_orders(orderDictionary:dict)->Order:
        with Session(Creature_bd.bdEngine) as db:
            row = Order(
                id_user = orderDictionary['id_user'],
                pick_up_point_order_parent = orderDictionary['pick_up_point_order_parent'],
                dateTime = orderDictionary['dateTime'],
                typePay = orderDictionary['typePay'],
                status = orderDictionary['status']
            )
            db.add(row)
            db.commit()

# функция добавления строки в таблицу User
    def add_users(userDictionary:dict)->User:
        with Session(Creature_bd.bdEngine) as db:
            row = User(
                id_Telegram = userDictionary['id_Telegram'], 
                role_parent = userDictionary['role_parent'], 
                name = userDictionary['name'], 
                lastName = userDictionary['lastName']
            )
            db.add(row)
            db.commit()

# функция добавления строки в таблицу Role
    def add_role(userDictionary:dict)->Role:
        with Session(Creature_bd.bdEngine) as db:
            row = Role(
                name = userDictionary['name']
            )
            db.add(row)
            db.commit()

# функция добавления строки в таблицу PickupPoint

    def add_pick_up_point(userDictionary:dict)->PickupPoint:
        with Session(Creature_bd.bdEngine) as db:
            row = PickupPoint(
                name = userDictionary['name'], 
                coordinats = userDictionary["coordinats"]
            )
            db.add(row)
            db.commit()



# функция выбора всех строк таблицы Orders, возвращает список с вложенными кортежами
    def allOrder()->list:
        with Session(Creature_bd.bdEngine) as db:
            listTable = []
            for el in db.query(Order).all():
                 listTable.append((el.id, el.id_user, el.pick_up_point_order_parent, el.dateTime, el.typePay, el.status))
        return listTable

# Чтение всех строк таблици User, возвращает список с вложенными кортежами
    def allUser()->list:
        with Session(Creature_bd.bdEngine) as db:
            listTable = []
            for el in db.query(User).all():
                listTable.append((el.id_Telegram, el.role_parent, el.name, el.lastName))
        return listTable

# Чтение всех строк таблици Role, возвращает список с вложенными кортежами
    def allRole()->list:
        with Session(Creature_bd.bdEngine) as db:
            listTable = []
            for el in db.query(Role).all():
                listTable.append((el.name))
        return listTable

# Чтение всех строк таблици Role, возвращает список с вложенными кортежами
    def allPickupPoint()->list:
        with Session(Creature_bd.bdEngine) as db:
            listTable = []
            for el in db.query(PickupPoint).all():
                listTable.append((el.name, el.coordinats))
        return listTable



# функция выбор укзанной строки таблицы Orders по primay_key
    def selectOrder(id)->dict:
        with Session(Creature_bd.bdEngine) as db:
            row = db.get(Order, id)
            rowProoduct = {'id_user':row.id_user, 'pickupPoint':row.pick_up_point_order_parent, 'dateTime':row.dateTime, 'typePay':row.typePay, 'status':row.status}
        return rowProoduct 

# функция выбор укзанной строки таблицы User по primay_key
    def selectRowUser(id_Telegram)->dict:
        with Session(Creature_bd.bdEngine) as db:
            row = db.get(User, id_Telegram)
            rowUser = {'role_parent':row.role_parent, 'name':row.name, 'lastName':row.lastName}
        return rowUser

# функция выбор укзанной строки таблицы Role по primay_key
    def selectRowRole(id)->dict:
        with Session(Creature_bd.bdEngine) as db:
            row = db.get(Role, id)
            rowRole = {'name':row.name}
        return rowRole

# функция выбор укзанной строки таблицы PickupPoint по primay_key
    def selectRowPickupPoint(id_Telegram)->dict:
        with Session(Creature_bd.bdEngine) as db:
            row = db.get(PickupPoint, id_Telegram)
            rowPickupPoint = {'name':row.name, "coordinats":row.coordinats}
        return rowPickupPoint



# фунция изменения поля таблици Orders
# id - это id строки таблицы Orders
# calumn - это имя поля для изменения
# value - новое значение поля
    def setOrder(id, calumn:str, value):
        with Session(Creature_bd.bdEngine) as db:
            singleSelect = db.get(Order, id)
            match calumn:
                case 'id':
                    singleSelect.id = value
                    db.commit()
                    db.refresh(singleSelect)
                case 'id_user':
                    singleSelect.id_user = value
                    db.commit()
                    db.refresh(singleSelect)
                case 'pickupPoint':
                    singleSelect.pick_up_point_order_parent = value
                    db.commit()
                    db.refresh(singleSelect)
                case 'dateTime':
                    singleSelect.dateTime = value
                    db.commit()
                    db.refresh(singleSelect)
                case 'typePay':
                    singleSelect.typePay = value
                    db.commit()
                    db.refresh(singleSelect)
                case 'status':
                    singleSelect.status = value
                    db.commit()
                    db.refresh(singleSelect)
                case other:
                    print ('There is no such calumn in a table')

# фунция изменения поля таблици User
    def setUser(id_telegram, calumn:str, value):
        with Session(Creature_bd.bdEngine) as db:
            singleSelect = db.get(User, id_telegram)
            match calumn:
                case 'id':
                    singleSelect.id_Telegram = value
                    db.commit()
                    db.refresh(singleSelect)
                case 'role_parent':
                    singleSelect.role_parent = value
                    db.commit()
                    db.refresh(singleSelect)
                case 'name':
                    singleSelect.name = value
                    db.commit()
                case 'lastName':
                    singleSelect.lastName = value
                    db.commit()
                    db.refresh(singleSelect)
                case other:
                    print ('There is no such calumn in a table')

# фунция изменения поля таблици Role
    def setRole(id, calumn:str, value):
        with Session(Creature_bd.bdEngine) as db:
            singleSelect = db.get(Role, id)
            match calumn:
                case 'id':
                    singleSelect.id = value
                    db.commit()
                    db.refresh(singleSelect)
                case 'name':
                    singleSelect.name = value
                    db.commit()
                    db.refresh(singleSelect)
                case other:
                    print ('There is no such calumn in a table')

# фунция изменения поля таблици PickupPoint
    def setPickupPoint(id, calumn:str, value):
        with Session(Creature_bd.bdEngine) as db:
            singleSelect = db.get(PickupPoint, id)
            match calumn:
                case 'id':
                    singleSelect.id = value
                    db.commit()
                    db.refresh(singleSelect)
                case 'name':
                    singleSelect.name = value
                    db.commit()
                    db.refresh(singleSelect)
                case "coordinats":
                    singleSelect.coordinats = value
                    db.commit()
                    db.refresh(singleSelect)
                case other:
                    print ('There is no such calumn in a table')



# удаление строки таблицы Orders по id
    def delOrder(id):
        with Session(Creature_bd.bdEngine) as db:
            singleSelect = db.get(Order, id)
            db.delete(singleSelect)
            db.commit()

# удаление строки таблицы User по id
    def delUser(id):
        with Session(Creature_bd.bdEngine) as db:
            singleSelect = db.get(User, id)
            db.delete(singleSelect)
            db.commit()

# удаление строки таблицы Role по id
    def delRole(id):
        with Session(Creature_bd.bdEngine) as db:
            singleSelect = db.get(Role, id)
            db.delete(singleSelect)
            db.commit()

# удаление строки таблицы PickupPoint по id
    def delPickupPoint(id):
        with Session(Creature_bd.bdEngine) as db:
            singleSelect = db.get(PickupPoint, id)
            db.delete(singleSelect)
            db.commit()



# ПРОВЕРКА ФУНКЦИЙ

# usertDictionary = {'id_Telegram':21345, 'id_role': 1, 'name':"Micha", "lastName":"Zaichenko"}
# Creature_bd.add_users(productDictionary)

# roleDictionary = {'name':"premium_user"}
# Creature_bd.add_role(roleDictionary)

# pickupPointDictionary = {'id_order':1, 'id_product':4, 'quantity':3}
# Creature_bd.add_pick_up_point(pickupPointDictionary)

# Возвращает словарь из таблици User по id
# print(Creature_bd.selectRowUser(1))

# Возвращает словарь из таблици User по id
# print(Creature_bd.selectRowRole(1))

# Возвращает словарь из таблици User по id
# print(Creature_bd.selectRowPickupPoint(1))

# print(Creature_bd.allPickupPoint())

# print(Creature_bd.allRole())

# print(Creature_bd.allUser())

# # изменения в таблице PickupPoint id=1 поля=name на значение 'Khatkiv, Darvin street. 51' 
# Creature_bd.setPickupPoint(1, 'name', 'Khatkiv, Darvin street. 51')

# # Удаление строки таблици User по id
# Creature_bd.delUser(1)

# # Удаление строки таблици Role по id
# Creature_bd.delRole(1)

# # Удаление строки таблици PickupPoint по id
# Creature_bd.delPickupPoint(1)