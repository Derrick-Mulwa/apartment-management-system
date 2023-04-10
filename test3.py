from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create the button and connect it to the file dialog
        btn = QPushButton('Select JPG', self)
        btn.clicked.connect(self.showFileDialog)

        # Set the window properties
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('JPG File Selector')
        self.show()

    def showFileDialog(self):
        # Create a file dialog
        fileDialog = QFileDialog()

        # Set the file type filter
        fileDialog.setNameFilter("JPG files (*.jpg)")

        # Get the file path
        filePath, _ = fileDialog.getOpenFileName(self, "Select JPG", "", "JPG files (*.jpg)")

        # Do something with the file path, such as displaying the image
        print(filePath)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

