from sqlalchemy.orm import declarative_base
from sqlalchemy import BLOB, FLOAT,TEXT, INTEGER, Column, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship


BaseClass = declarative_base()

class RowTableProduct(BaseClass):
    __tablename__ = 'Products'

    id = Column(INTEGER, primary_key = True, autoincrement = True)
    name = Column(TEXT)
    description = Column(TEXT)
    picture = Column(TEXT)
    price = Column(FLOAT)
    quantity = Column(INTEGER)

    orders = relationship("RowTableOrderProduct", back_populates = "product")

class RowTableOrder(BaseClass):
    __tablename__ = 'Orders'

    id = Column(INTEGER, primary_key = True, autoincrement = True)
    id_user = Column(INTEGER)
    pickupPoint = Column(TEXT)
    dateTime = Column(INTEGER)
    typePay = Column(TEXT)
    status = Column(TEXT)

    products = relationship("RowTableOrderProduct", back_populates = "order")

class RowTableOrderProduct(BaseClass):
    __tablename__ = 'Orders-Products'

    id = Column(INTEGER, primary_key = True)
    id_order = Column(ForeignKey("Products.id"))
    id_product = Column(ForeignKey("Orders.id"))
    
    quantity = Column(INTEGER)

    order = relationship("RowTableOrder", back_populates="products")
    product = relationship("RowTableProduct", back_populates="orders")
    

class RowTableOrder(BaseClass):
    __tablename__ = 'Orders'

    id = Column(INTEGER, primary_key = True, autoincrement = True)
    id_user = Column(INTEGER, ForeignKey("Users.id_Telegram"))
    pickupPoint = Column(TEXT, ForeignKey("Pickup_points.id"))
    dateTime = Column(INTEGER)
    typePay = Column(TEXT)
    status = Column(TEXT)
    # зв'язок з RowTablePickupPoint
    order_parent = relationship("RowTablePickupPoint", back_populates="order_child")
    # зв'язок з RowTableUser
    order_user_parent = relationship("RowTableUser", back_populates="order_user_child")


class RowTableUser(BaseClass):
    __tablename__ = 'Users'

    id_Telegram = Column(INTEGER, primary_key = True)
    role = Column(TEXT, ForeignKey("Roles.id"))
    name = Column(TEXT)
    lastName = Column(TEXT)
    # зв'язок з RowTableRole
    role_parent = relationship("RowTableRole", back_populates="role_child")
    # зв'язок з RowTableOrder
    order_user_child = relationship("RowTableOrder", back_populates="order_user_parent", cascade="all, delete-orphan")


class RowTableRole(BaseClass):    
    __tablename__ = 'Roles'

    id = Column(INTEGER, primary_key = True, autoincrement = True)
    name = Column(INTEGER)
    role_child = relationship("RowTableUser", back_populates="role_parent", cascade="all, delete-orphan")

class RowTablePickupPoint(BaseClass):
    __tablename__ = 'Pickup_points'    

    id  = Column(INTEGER, primary_key = True, autoincrement = True)
    name = Column(TEXT)
    coordinats = Column(FLOAT)
    # зв'язок з RowTableOrder
    order_child = relationship("RowTableOrder", back_populates="order_parent", cascade="all, delete-orphan")
