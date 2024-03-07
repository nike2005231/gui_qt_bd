import psycopg2 as pg
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from config import host, user, password, db_name
import sys
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\requset_table")
import request
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\Error")
import error

def show_error(self, text, element_class, mode) -> str:
    if mode == "set":
        element_class.textBrowser.setText(f"{text}")
    elif mode == "add":
        element_class.textBrowser.append(f"{text}")

def clear_table_main_bd(self, name_table):
    self.send_window = error.QtWidgets.QMainWindow()
    ui = error.Ui_ErrorWindow()
    ui.setupUi(self.send_window)
    connection = pg.connect(host=host, dbname=db_name, user=user, password=password)
    
    connection.autocommit = True

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"delete from {name_table}"
            )

    except (Exception, pg.DatabaseError) as errors:
        if str(errors) == "no results to fetch":
            show_error(self, "Запрос выполнен", ui, "set")
        else:
            show_error(self, f"{errors}", ui, "set")
    finally:
        self.send_window.show()
        show_error(self, "\n***Соединение успешно закрыто***", ui, "add")
        connection.close()

#Request
def request_window(self):
    self.send_window = error.QtWidgets.QMainWindow()
    ui = error.Ui_ErrorWindow()
    ui.setupUi(self.send_window)

    self.send_request = request.QtWidgets.QMainWindow()
    ui_request = request.Ui_MainWindow()
    ui_request.setupUi(self.send_request)
    user_input = self.textEdit.toPlainText()  # обращение к textEdit созданного экземпляра
    print(user_input)

    connection = pg.connect(host=host, dbname=db_name, user=user, password=password)
    
    connection.autocommit = True

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"{user_input}"
            )
            rows = cursor.fetchall()
            
            for row in rows:
                show_error(self, f"{row}", ui, "add")
    except (Exception, pg.DatabaseError) as errors:
        if str(errors) == "no results to fetch":
            show_error(self, "Запрос выполнен", ui, "set")
        else:
            show_error(self, f"{errors}", ui, "set")
    finally:
        self.send_window.show()
        show_error(self, "\n***Соединение успешно закрыто***", ui, "add")
        connection.close()

    

#Supplier
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

    except (Exception, pg.DatabaseError) as errors:
        if str(errors) == "no results to fetch":
            show_error(self, "Запрос выполнен", ui, "set")
        else:
            show_error(self, f"{errors}", ui, "set")
    finally:
        self.send_window.show()
        show_error(self, "\n***Соединение успешно закрыто***", ui, "add")
        connection.close()
       
