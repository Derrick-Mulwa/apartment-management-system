import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtGui

# connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

# execute the SQL query to retrieve the longblob file
cursor = conn.cursor()
query = "SELECT picture FROM apartment_name.properties"
cursor.execute(query)
result = [i for i in cursor][1]
image_data = result[0]

with open("myfile.png", "wb") as file:
    file.write(image_data)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QLabel widget and set its pixmap to an image file
        label = QLabel(self)
        pixmap = QPixmap('myfile.png')
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setGeometry(0, 0, pixmap.width(), pixmap.height())

        # Set the window properties
        self.setGeometry(100, 100, pixmap.width(), pixmap.height())
        self.setWindowTitle('QLabel with Image')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
