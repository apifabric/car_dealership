# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Customer(Base):
    """
    description: The Customer table stores information about the dealership's customers.
    """
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)

class CarModel(Base):
    """
    description: The CarModel table represents different models of cars available in the dealership.
    """
    __tablename__ = 'car_model'
    id = Column(Integer, primary_key=True, autoincrement=True)
    model_name = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    base_price = Column(Float, nullable=False)

class CarInventory(Base):
    """
    description: The CarInventory table tracks individual car units available for sale or sold.
    """
    __tablename__ = 'car_inventory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vin = Column(String, unique=True, nullable=False)
    model_id = Column(Integer, ForeignKey('car_model.id'), nullable=False)
    purchase_date = Column(Date, nullable=False)
    status = Column(String, nullable=False)
    sale_price = Column(Float, nullable=True)

class Sale(Base):
    """
    description: The Sale table records each car sale transaction.
    """
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    inventory_id = Column(Integer, ForeignKey('car_inventory.id'), nullable=False)
    sale_date = Column(Date, default=datetime.date.today(), nullable=False)
    sale_amount = Column(Float, nullable=False)

class Employee(Base):
    """
    description: The Employee table contains information about the dealership's employees.
    """
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    position = Column(String, nullable=False)

class Service(Base):
    """
    description: The Service table logs services offered to cars, either during sale or maintenance.
    """
    __tablename__ = 'service'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    cost = Column(Float, nullable=False)

class Maintenance(Base):
    """
    description: The Maintenance table records maintenance activities for cars.
    """
    __tablename__ = 'maintenance'
    id = Column(Integer, primary_key=True, autoincrement=True)
    inventory_id = Column(Integer, ForeignKey('car_inventory.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('service.id'), nullable=False)
    maintenance_date = Column(Date, nullable=False)

class Supplier(Base):
    """
    description: The Supplier table contains details about suppliers providing cars or parts.
    """
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_email = Column(String, nullable=True)
    contact_phone = Column(String, nullable=True)

class Parts(Base):
    """
    description: The Parts table stores information about car parts available through suppliers.
    """
    __tablename__ = 'parts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    supplier_id = Column(Integer, ForeignKey('supplier.id'))

class InventoryPart(Base):
    """
    description: The InventoryPart table links parts to specific cars in inventory, indicating part usage.
    """
    __tablename__ = 'inventory_part'
    id = Column(Integer, primary_key=True, autoincrement=True)
    inventory_id = Column(Integer, ForeignKey('car_inventory.id'), nullable=False)
    part_id = Column(Integer, ForeignKey('parts.id'), nullable=False)
    used_in_maintenance = Column(DateTime, nullable=True)

class Dealership(Base):
    """
    description: The Dealership table captures details of the dealership's locations.
    """
    __tablename__ = 'dealership'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=True)
    phone = Column(String, nullable=True)

class DealershipEmployee(Base):
    """
    description: The DealershipEmployee table links employees with specific dealership locations.
    """
    __tablename__ = 'dealership_employee'
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    dealership_id = Column(Integer, ForeignKey('dealership.id'), nullable=False)

# Create an engine
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')

# Create all tables
Base.metadata.create_all(engine)

# Create a configured session class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Sample data insertions
# Customers
customer1 = Customer(name='John Doe', email='john@example.com', phone='123-456-7890')
customer2 = Customer(name='Jane Smith', email='jane@example.com', phone='987-654-3210')
session.add_all([customer1, customer2])

# CarModels
model1 = CarModel(model_name='Model S', manufacturer='Tesla', year=2020, base_price=79999.99)
model2 = CarModel(model_name='Civic', manufacturer='Honda', year=2019, base_price=21999.99)
session.add_all([model1, model2])

# CarInventory
inventory1 = CarInventory(vin='5YJSA1E26JF123456', model_id=1, purchase_date=datetime.date(2021, 1, 1), status='Available', sale_price=None)
inventory2 = CarInventory(vin='2HGFC2F59KH528736', model_id=2, purchase_date=datetime.date(2020, 5, 20), status='Sold', sale_price=22999.99)
session.add_all([inventory1, inventory2])

# Sale
sale1 = Sale(customer_id=2, inventory_id=2, sale_date=datetime.date(2020, 6, 15), sale_amount=22999.99)
session.add(sale1)

# Employees
employee1 = Employee(name='Alice Johnson', email='alice@example.com', phone='321-654-0987', position='Sales Manager')
employee2 = Employee(name='Bob Brown', email='bob@example.com', phone='654-321-0987', position='Technician')
session.add_all([employee1, employee2])

# Services
service1 = Service(description='Oil Change', cost=39.99)
service2 = Service(description='Tire Rotation', cost=29.99)
session.add_all([service1, service2])

# Maintenance
maintenance1 = Maintenance(inventory_id=2, service_id=1, maintenance_date=datetime.date(2021, 8, 1))
maintenance2 = Maintenance(inventory_id=2, service_id=2, maintenance_date=datetime.date(2021, 8, 2))
session.add_all([maintenance1, maintenance2])

# Suppliers
supplier1 = Supplier(name='Auto Parts Co.', contact_email='contact@autopartsco.com', contact_phone='555-123-4567')
supplier2 = Supplier(name='Parts Plus', contact_email='info@partsplus.com', contact_phone='555-765-4321')
session.add_all([supplier1, supplier2])

# Parts
part1 = Parts(name='Brake Pad', price=19.99, supplier_id=1)
part2 = Parts(name='Air Filter', price=15.99, supplier_id=2)
session.add_all([part1, part2])

# InventoryPart
inventory_part1 = InventoryPart(inventory_id=2, part_id=1, used_in_maintenance=datetime.datetime(2021, 8, 1))
inventory_part2 = InventoryPart(inventory_id=2, part_id=2, used_in_maintenance=datetime.datetime(2021, 8, 2))
session.add_all([inventory_part1, inventory_part2])

# Dealerships
dealership1 = Dealership(name='Central Motors', address='123 Main St, Anytown, USA', phone='555-998-7654')
dealership2 = Dealership(name='Eastside Auto', address='456 Elm St, Othertown, USA', phone='555-887-2345')
session.add_all([dealership1, dealership2])

# DealershipEmployees
dealership_employee1 = DealershipEmployee(employee_id=1, dealership_id=1)
dealership_employee2 = DealershipEmployee(employee_id=2, dealership_id=2)
session.add_all([dealership_employee1, dealership_employee2])

# Commit the data
session.commit()

# Close the session
session.close()
