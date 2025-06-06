import os
import MySQLdb as mdb

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QByteArray, QRect, Qt
from PySide6.QtWidgets import QMainWindow 
from api.user import login, register

from ui.admin import Ui_Admin
from ui.main_menu import Ui_Main
from ui.history import Ui_History
from ui.book import Ui_Book
from ui.auth import Ui_Auth






class Register(QMainWindow):
    def __init__(self):
        super(Register, self).__init__()
        self.ui = Ui_Auth()
        self.ui.setupUi(self)

        self.ui.btn_Login.clicked.connect(self.auth)
        self.ui.btn_register.clicked.connect(self.reg)


    def open_ui_rab(self):
        main = QDialog(self)
        self.main = Ui_Main()
        self.main.setupUi(main) 
        
        self.main.history.clicked.connect(self.open_ui_history)
        self.main.available_rooms.clicked.connect(self.open_ui_avibra)
        
        main.exec()   


    def auth(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        
        try:
            user = login(name, passw)  
            print(user)
            
            position_id = user['id_role']  
        
            
                    
            if position_id == 1:  # Например, 1 - это ID для администратора
                self.open_ui_admin()
            elif position_id == 2:  # 2 - это ID для работника
                self.open_ui_rab()
            elif position_id == 3:  # 3 - это ID для менеджера
                self.open_ui_manager()
            else:
                QMessageBox.warning(self, "Ошибка", "Неизвестная должность")
    
        except Exception as e:
            print("Error occurred:", str(e))
            QMessageBox.warning(self, "Ошибка", str(e))


    def open_ui_history(self):
        image = QDialog(self)
        self.image = Ui_History()
        self.image.setupUi(image) 
        
        
        
        image.exec()
    
    def open_ui_admin(self):
        admin = QDialog(self)
        self.admin = Ui_Admin()
        self.admin.setupUi(admin) 
        
        
        
        admin.exec()
    
    def open_ui_avibra(self):
        avibra = QDialog(self)
        self.avibra = Ui_Book()
        self.avibra.setupUi(avibra)
 

 
        avibra.exec()

    def end(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.close()
    
    def reg(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        register(name, passw)
        print('Autor')



if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Register()
    window.show()   
    sys.exit(app.exec())
>>>>>>> 96d59d092d4628cbb9b37fcbebd145eb19b60051
