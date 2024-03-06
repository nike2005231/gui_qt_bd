import psycopg2 as pg
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from config import host, user, password, db_name
import sys
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\Error")
import error
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\order_table")
import order
# sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\product_table")
# import product
# sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\suppiler_table")
# import supplier
# sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\warehouse_table")
# import warehouse
# sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\select_table")
# import select





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

def show_error(self, text, element_class, mode) -> str:
    if mode == "set":
        element_class.textBrowser.setText(f"{text}")
    elif mode == "add":
        element_class.textBrowser.append(f"{text}")


#Warehouse
def add_value_request_supplier(self, line_edit, line_edit_2, line_edit_3, line_edit_4, line_edit_5):
    self.send_window = error.QtWidgets.QMainWindow()
    ui = error.Ui_ErrorWindow()
    ui.setupUi(self.send_window)
    connection = pg.connect(host=host, dbname=db_name, user=user, password=password)
    
    connection.autocommit = True

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"insert into supplier(id_supplier, id_product, name_supplier, adres, information) values({line_edit.text()}, {line_edit_2.text()}, \'{line_edit_3.text()}\', \'{line_edit_4.text()}\', \'{line_edit_5.text()}\')"
            )
            rows = cursor.fetchall()
            
            for row in rows:
                print(f"{row}")
    except (Exception, pg.DatabaseError) as errors:
        if str(errors) == "no results to fetch":
            show_error(self, "Запрос выполнен", ui, "set")
        else:
            show_error(self, f"{errors}", ui, "set")
    finally:
        self.send_window.show()
        show_error(self, "\n***Соединение успешно закрыто***", ui, "add")
        connection.close()



#Warehouse
def add_value_request_warehouse(self, line_edit, line_edit_2, line_edit_3, line_edit_4):
    self.send_window = error.QtWidgets.QMainWindow()
    ui = error.Ui_ErrorWindow()
    ui.setupUi(self.send_window)
    connection = pg.connect(host=host, dbname=db_name, user=user, password=password)
    
    connection.autocommit = True

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"insert into warehouse(id_Warehouse, id_product, total, delivery_date_number) values({line_edit.text()}, {line_edit_2.text()}, {line_edit_3.text()}, \'{line_edit_4.text()}\')"
            )
            rows = cursor.fetchall()
            
            for row in rows:
                print(f"{row}")
    except (Exception, pg.DatabaseError) as errors:
        if str(errors) == "no results to fetch":
            show_error(self, "Запрос выполнен", ui, "set")
        else:
            show_error(self, f"{errors}", ui, "set")
    finally:
        self.send_window.show()
        show_error(self, "\n***Соединение успешно закрыто***", ui, "add")
        connection.close()




#Product
def add_value_request_product(self, line_edit, line_edit_2, line_edit_3, line_edit_4):
    self.send_window = error.QtWidgets.QMainWindow()
    ui = error.Ui_ErrorWindow()
    ui.setupUi(self.send_window)
    connection = pg.connect(host=host, dbname=db_name, user=user, password=password)
    
    connection.autocommit = True

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"insert into product(id_product, name_product, price_product, description_product) values({line_edit.text()}, \'{line_edit_2.text()}\', {line_edit_3.text()}, \'{line_edit_4.text()}\')"
            )
            rows = cursor.fetchall()
            
            for row in rows:
                print(f"{row}")
    except (Exception, pg.DatabaseError) as errors:
        if str(errors) == "no results to fetch":
            show_error(self, "Запрос выполнен", ui, "set")
        else:
            show_error(self, f"{errors}", ui, "set")
    finally:
        self.send_window.show()
        show_error(self, "\n***Соединение успешно закрыто***", ui, "add")
        connection.close()





#ORDER
def add_value_request_order(self, line_edit, line_edit_2, line_edit_3, line_edit_4, line_edit_5):
    self.send_window = error.QtWidgets.QMainWindow()
    ui = error.Ui_ErrorWindow()
    ui.setupUi(self.send_window)
    connection = pg.connect(host=host, dbname=db_name, user=user, password=password)
    
    connection.autocommit = True

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"insert into orders(id_orders, id_client, id_product, value, date) values({line_edit.text()}, {line_edit_2.text()}, {line_edit_3.text()}, {line_edit_4.text()}, \'{line_edit_5.text()}\')"
            )
            rows = cursor.fetchall()
            
            for row in rows:
                print(f"{row}")
    except (Exception, pg.DatabaseError) as errors:
        if str(errors) == "no results to fetch":
            show_error(self, "Запрос выполнен", ui, "set")
        else:
            show_error(self, f"{errors}", ui, "set")
    finally:
        self.send_window.show()
        show_error(self, "\n***Соединение успешно закрыто***", ui, "add")
        connection.close()





#CLIENT
def add_value_request_client(self, line_edit, line_edit_2, line_edit_3, line_edit_4, line_edit_5):
    self.send_window = error.QtWidgets.QMainWindow()
    ui = error.Ui_ErrorWindow()
    ui.setupUi(self.send_window)
    connection = pg.connect(host=host, dbname=db_name, user=user, password=password)
    
    connection.autocommit = True

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"insert into client(id_client, name, surname, adres, value_contact) values({line_edit.text()}, \'{line_edit_2.text()}\', \'{line_edit_3.text()}\', \'{line_edit_4.text()}\', \'{line_edit_5.text()}\')"
            )
            rows = cursor.fetchall()
            
            for row in rows:
                print(f"{row}")
    except (Exception, pg.DatabaseError) as errors:
        if str(errors) == "no results to fetch":
            show_error(self, "Запрос выполнен", ui, "set")
        else:
            show_error(self, f"{errors}", ui, "set")
    finally:
        self.send_window.show()
        show_error(self, "\n***Соединение успешно закрыто***", ui, "add")
        connection.close()
       
