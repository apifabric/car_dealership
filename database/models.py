# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 15, 2024 16:43:39
# Database: sqlite:////tmp/tmp.I0O1PhZqfw/car_dealership/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class CarModel(SAFRSBaseX, Base):
    """
    description: The CarModel table represents different models of cars available in the dealership.
    """
    __tablename__ = 'car_model'
    _s_collection_name = 'CarModel'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    model_name = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    base_price = Column(Float, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    CarInventoryList : Mapped[List["CarInventory"]] = relationship(back_populates="model")



class Customer(SAFRSBaseX, Base):
    """
    description: The Customer table stores information about the dealership's customers.
    """
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    SaleList : Mapped[List["Sale"]] = relationship(back_populates="customer")



class Dealership(SAFRSBaseX, Base):
    """
    description: The Dealership table captures details of the dealership's locations.
    """
    __tablename__ = 'dealership'
    _s_collection_name = 'Dealership'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String)
    phone = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    DealershipEmployeeList : Mapped[List["DealershipEmployee"]] = relationship(back_populates="dealership")



class Employee(SAFRSBaseX, Base):
    """
    description: The Employee table contains information about the dealership's employees.
    """
    __tablename__ = 'employee'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    position = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    DealershipEmployeeList : Mapped[List["DealershipEmployee"]] = relationship(back_populates="employee")



class Service(SAFRSBaseX, Base):
    """
    description: The Service table logs services offered to cars, either during sale or maintenance.
    """
    __tablename__ = 'service'
    _s_collection_name = 'Service'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    cost = Column(Float, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    MaintenanceList : Mapped[List["Maintenance"]] = relationship(back_populates="service")



class Supplier(SAFRSBaseX, Base):
    """
    description: The Supplier table contains details about suppliers providing cars or parts.
    """
    __tablename__ = 'supplier'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_email = Column(String)
    contact_phone = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    PartList : Mapped[List["Part"]] = relationship(back_populates="supplier")



class CarInventory(SAFRSBaseX, Base):
    """
    description: The CarInventory table tracks individual car units available for sale or sold.
    """
    __tablename__ = 'car_inventory'
    _s_collection_name = 'CarInventory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    vin = Column(String, nullable=False, unique=True)
    model_id = Column(ForeignKey('car_model.id'), nullable=False)
    purchase_date = Column(Date, nullable=False)
    status = Column(String, nullable=False)
    sale_price = Column(Float)

    # parent relationships (access parent)
    model : Mapped["CarModel"] = relationship(back_populates=("CarInventoryList"))

    # child relationships (access children)
    InventoryPartList : Mapped[List["InventoryPart"]] = relationship(back_populates="inventory")
    MaintenanceList : Mapped[List["Maintenance"]] = relationship(back_populates="inventory")
    SaleList : Mapped[List["Sale"]] = relationship(back_populates="inventory")



class DealershipEmployee(SAFRSBaseX, Base):
    """
    description: The DealershipEmployee table links employees with specific dealership locations.
    """
    __tablename__ = 'dealership_employee'
    _s_collection_name = 'DealershipEmployee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    employee_id = Column(ForeignKey('employee.id'), nullable=False)
    dealership_id = Column(ForeignKey('dealership.id'), nullable=False)

    # parent relationships (access parent)
    dealership : Mapped["Dealership"] = relationship(back_populates=("DealershipEmployeeList"))
    employee : Mapped["Employee"] = relationship(back_populates=("DealershipEmployeeList"))

    # child relationships (access children)



class Part(SAFRSBaseX, Base):
    """
    description: The Parts table stores information about car parts available through suppliers.
    """
    __tablename__ = 'parts'
    _s_collection_name = 'Part'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    supplier_id = Column(ForeignKey('supplier.id'))

    # parent relationships (access parent)
    supplier : Mapped["Supplier"] = relationship(back_populates=("PartList"))

    # child relationships (access children)
    InventoryPartList : Mapped[List["InventoryPart"]] = relationship(back_populates="part")



class InventoryPart(SAFRSBaseX, Base):
    """
    description: The InventoryPart table links parts to specific cars in inventory, indicating part usage.
    """
    __tablename__ = 'inventory_part'
    _s_collection_name = 'InventoryPart'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    inventory_id = Column(ForeignKey('car_inventory.id'), nullable=False)
    part_id = Column(ForeignKey('parts.id'), nullable=False)
    used_in_maintenance = Column(DateTime)

    # parent relationships (access parent)
    inventory : Mapped["CarInventory"] = relationship(back_populates=("InventoryPartList"))
    part : Mapped["Part"] = relationship(back_populates=("InventoryPartList"))

    # child relationships (access children)



class Maintenance(SAFRSBaseX, Base):
    """
    description: The Maintenance table records maintenance activities for cars.
    """
    __tablename__ = 'maintenance'
    _s_collection_name = 'Maintenance'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    inventory_id = Column(ForeignKey('car_inventory.id'), nullable=False)
    service_id = Column(ForeignKey('service.id'), nullable=False)
    maintenance_date = Column(Date, nullable=False)

    # parent relationships (access parent)
    inventory : Mapped["CarInventory"] = relationship(back_populates=("MaintenanceList"))
    service : Mapped["Service"] = relationship(back_populates=("MaintenanceList"))

    # child relationships (access children)



class Sale(SAFRSBaseX, Base):
    """
    description: The Sale table records each car sale transaction.
    """
    __tablename__ = 'sale'
    _s_collection_name = 'Sale'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'), nullable=False)
    inventory_id = Column(ForeignKey('car_inventory.id'), nullable=False)
    sale_date = Column(Date, nullable=False)
    sale_amount = Column(Float, nullable=False)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("SaleList"))
    inventory : Mapped["CarInventory"] = relationship(back_populates=("SaleList"))

    # child relationships (access children)
