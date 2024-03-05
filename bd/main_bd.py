import psycopg2 as pg
from config import host, user, password, db_name
import sys
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\client_table")
import client
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\order_table")
import order
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\product_table")
import product
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\suppiler_table")
import supplier
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\warehouse_table")
import warehouse
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\select_table")
import select





    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         "create database Product_shop;"
    #         ) 
    
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """
    #         create table Product(
    #         id_product int primary key,
    #         name_product varchar(50) not null,
    #         price_product int not null,
    #         description_product text not null
    #         );

    #         create table Supplier(
    #         id_supplier int primary key,
    #         id_product SERIAL REFERENCES Product(id_product),
    #         name_supplier varchar(50) not null,
    #         adres varchar(50) not null,
    #         information text not null
    #         );

    #         create table Warehouse(
    #         id_Warehouse int primary key,
    #         id_product SERIAL REFERENCES Product(id_product),
    #         total int not null,
    #         delivery_date_number varchar(50) not null
    #         );

    #         create table Client(
    #         id_client int primary key,
    #         name varchar(50) not null,
    #         surname varchar(50) not null,
    #         adres varchar(50) not null,
    #         value_contact text not null
    #         );

    #         create table orders(
    #         id_orders int primary key,
    #         id_client SERIAL REFERENCES Client(id_client),
    #         id_product SERIAL REFERENCES Product(id_product),
    #         value int not null,
    #         date varchar(50)
    #         );
    #         """
    #         )


def add_value_request_client():
    connection = pg.connect(host=host, dbname=db_name, user=user, password=password)
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM client")
            rows = cursor.fetchall()
            
            for row in rows:
                print(f"{row}")
    except (Exception, pg.DatabaseError) as error:
        print(f"Ошибка при выполнении запроса: {error}")
    finally:
        print("Соединение закрыто")
        connection.close()