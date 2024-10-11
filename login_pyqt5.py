'''
pip install pyqt5
pip install PyQt5Designer

'''

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.QtGui import QPixmap
from resources.ui.Login_ui import Ui_MainWindow


class MainApp(QMainWindow):
    
    
    def __init__(self):
        '''
        super (MainPyForm, self).__init__()
        loadUi('pyMainForm.ui', self)
        self.setWindowTitle('Notes Automation')
        '''
        # Initialized Window Form        
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  
        
        pixmap = QPixmap('resources/images/login.png')
        self.ui.label_logo.setPixmap(pixmap)
        self.ui.label_logo.resize(128, 128)
        
        self.ui.pushButton_login.clicked.connect(self.login)
        
        
       
    def login(self):
        # Predefined username and password
        valid_username = "XXX"
        valid_password = "XXX"

        username = self.ui.lineEdit_username.text()
        password = self.ui.lineEdit_password.text()

        if username == valid_username and password == valid_password:
            QtWidgets.QMessageBox.information(self, "Access Granted", "Welcome!")
        else:
            QtWidgets.QMessageBox.critical(self, "Access Denied", "Invalid credentials, please try again.")

        # clear the fields
        self.clear_fields()
            
      
    def clear_fields(self):
        self.ui.lineEdit_username.setText("") 
        self.ui.lineEdit_password.setText("")    
        self.ui.lineEdit_username.setFocus()

     
        
'''
app = QApplication(sys.argv)
widget = MainPyForm()
widget.show()
sys.exit(app.exec())
'''
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainApp()
    widget.show()
    sys.exit(app.exec())

