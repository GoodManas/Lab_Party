
import sys
import os
import MySQLdb as mdb

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QMessageBox

from api.user import login, register, get_all_users, add_bron, uchet

from ui.admin import Ui_Admin
from ui.main_menu import Ui_Main
from ui.history import Ui_History
from ui.book import Ui_Book
from ui.auth import Ui_Auth
from ui.Bron import Ui_Bron
from ui.ui_reservation import UiReservationSystem

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Auth()
        self.ui.setupUi(self)

        self.ui.btn_Login.clicked.connect(self.auth)
        self.ui.btn_register.clicked.connect(self.reg)

    def open_ui_rab(self):
        self.main_dialog = QDialog(self)
        self.ui_main = Ui_Main()
        self.ui_main.setupUi(self.main_dialog)
        self.ui_main.history.clicked.connect(self.open_ui_history)
        self.ui_main.available_rooms.clicked.connect(self.open_ui_avibra)
        self.main_dialog.show()

    def auth(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        try:
            user = login(name, passw)
            print(user)
            position_id = user['id_role']
            if position_id == 1:
                self.open_ui_admin()                                                                
            elif position_id == 2:
                self.open_ui_student()
            elif position_id == 3:
                self.open_ui_manager()
            else:
                QMessageBox.warning(self, "Ошибка", "Неизвестная должность")
        except Exception as e:
            print("Error occurred:", str(e))
            QMessageBox.warning(self, "Ошибка", str(e))

    def open_ui_history(self):
        self.history_dialog = QDialog(self)
        self.ui_history = Ui_History()
        self.ui_history.setupUi(self.history_dialog)
        self.history_dialog.show()

    def open_ui_admin(self):
        self.admin_dialog = QDialog(self)
        self.ui_admin = Ui_Admin()
        self.ui_admin.setupUi(self.admin_dialog)
        self.admin_dialog.show()

    def open_ui_student(self):
        self.rab_widget = QWidget()
        self.ui_reservation = UiReservationSystem()
        self.ui_reservation.setupUi(self.rab_widget)
        
       


        self.ui_reservation.button_reserve.clicked.connect(self.zaverzirivat)

        self.rab_widget.show()

    def open_ui_avibra(self):
        self.avibra_widget = QWidget()
        self.ui_reservation = UiReservationSystem()
        self.ui_reservation.setupUi(self.avibra_widget)
        self.avibra_widget.show()

    def open_ui_Bron(self):
        self.bron_dialog = QDialog(self)
        self.ui_bron = Ui_Bron()
        self.ui_bron.setupUi(self.bron_dialog)
        self.ui_bron.button_book.clicked.connect(self.add_Born)
        self.bron_dialog.show()

    def add_Born(self):
        id = self.ui.lineEdit.text()
        add_bron(id)
    
    def zaverzirivat(self):
        name = self.ui_reservation.lineEdit_professor.text()
        room = self.ui_reservation.lineEdit_room.text()
        

        uchet(name,room)



    def end(self):
        self.close()

    def reg(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        register(name, passw)
        print('Author registered')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Register()
    window.show()
    sys.exit(app.exec())
