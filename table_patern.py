from sqlalchemy.orm import declarative_base
from sqlalchemy import BLOB, FLOAT,TEXT, INTEGER, Column, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship


BaseClass = declarative_base()

class Product(BaseClass):
    __tablename__ = 'Products'

    id = Column(INTEGER, primary_key = True, autoincrement = True)
    name = Column(TEXT)
    description = Column(TEXT)
    picture = Column(TEXT)
    price = Column(FLOAT)
    quantity = Column(INTEGER)

    orders = relationship("OrderProduct", back_populates = "product")

# class Order(BaseClass):
#     __tablename__ = 'Orders'

#     id = Column(INTEGER, primary_key = True, autoincrement = True)
#     id_user = Column(INTEGER)
#     pickupPoint = Column(TEXT)
#     dateTime = Column(INTEGER)
#     typePay = Column(TEXT)
#     status = Column(TEXT)

#     products = relationship("OrderProduct", back_populates = "order")

class OrderProduct(BaseClass):
    __tablename__ = 'Orders-Products'

    id = Column(INTEGER, primary_key = True)
    id_order = Column(ForeignKey("Products.id"))
    id_product = Column(ForeignKey("Orders.id"))
    
    quantity = Column(INTEGER)

    order = relationship("Order", back_populates="products")
    product = relationship("Product", back_populates="orders")
    

class Order(BaseClass):
    __tablename__ = 'Orders'

    id = Column(INTEGER, primary_key = True, autoincrement = True)
    id_user = Column(INTEGER, ForeignKey("Users.id_Telegram"))
    pickupPoint = Column(INTEGER, ForeignKey("Pickup_points.id"))
    dateTime = Column(INTEGER)
    typePay = Column(TEXT)
    status = Column(TEXT)
    # зв'язок з PickupPoint
    pick_up_point_order_parent = relationship("PickupPoint", back_populates="order_pick_up_point_child")
    # зв'язок з User
    user_parent = relationship("User", back_populates="order_user_child")

    products = relationship("OrderProduct", back_populates = "order")

class User(BaseClass):
    __tablename__ = 'Users'

    id_Telegram = Column(INTEGER, primary_key = True, unique=True)
    role = Column(TEXT, ForeignKey("Roles.id"))
    name = Column(TEXT)
    lastName = Column(TEXT)
    # зв'язок з Role
    role_parent = relationship("Role", back_populates="user_role_child")
    # зв'язок з Order
    order_user_child = relationship("Order", back_populates="user_parent", cascade="all, delete-orphan")


class Role(BaseClass):    
    __tablename__ = 'Roles'

    id = Column(INTEGER, primary_key = True, autoincrement = True)
    name = Column(INTEGER)
    user_role_child = relationship("User", back_populates="role_parent", cascade="all, delete-orphan")

class PickupPoint(BaseClass):
    __tablename__ = 'Pickup_points'    

    id  = Column(INTEGER, primary_key = True, autoincrement = True)
    name = Column(TEXT)
    coordinats = Column(TEXT)
    # зв'язок з Order
    order_pick_up_point_child = relationship("Order", back_populates="pick_up_point_order_parent", cascade="all, delete-orphan")
