import sys
import os
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTableView
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtSql import QSqlDatabase, QSqlTableModel



class Register(QMainWindow):
    def __init__(self):
        super(Register, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui_admin = Ui_Admin()
        self.ui.setupUi(self)
        
        self.ui.btn_login.clicked.connect(self.auth)
        self.ui.btn_register.clicked.connect(self.reg)
        
       
        self.base_lane_edit = [self.ui.lineEditLog, self.ui.lineEditPass]

#============================================================================
#авторизация
    def auth(self):
        name = self.ui.lineEditLog.text()
        passw = self.ui.lineEditPass.text()
        
        try:
            user = login(name, passw)  
            print(user)
            
            position_id = user['dol']  
        
            
                    
            if position_id == 1:  # Например, 1 - это ID для администратора
                self.open_ui_admin()
            elif position_id == 2:  # 2 - это ID для работника
                self.open_ui_rabotnik()
            elif position_id == 3:  # 3 - это ID для менеджера
                self.open_ui_manager()
            else:
                QMessageBox.warning(self, "Ошибка", "Неизвестная должность")
    
        except Exception as e:
            print("Error occurred:", str(e))
            QMessageBox.warning(self, "Ошибка", str(e))

    #====================================================================    
    #функция для закрытия окна 
    def end(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Register()
    window.show()   
    sys.exit(app.exec())