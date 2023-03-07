import sys
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLineEdit
from PyQt5.QtCore import Qt, pyqtSignal, QObject, pyqtSlot, QThread

class Communicate(QObject):
    new_message = pyqtSignal(str)

class ClientThread(QThread):
    def __init__(self, communicate):
        super().__init__()
        self.communicate = communicate

    def run(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 5555))

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            self.communicate.new_message.emit(message)

class ChatApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the GUI
        self.message_history = QTextEdit()
        self.message_input = QLineEdit()
        self.send_button = QPushButton("Send")

        # Create the layout
        hbox = QHBoxLayout()
        hbox.addWidget(self.message_input)
        hbox.addWidget(self.send_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.message_history)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        # Connect signals and slots
        self.send_button.clicked.connect(self.send_message)
        self.message_input.returnPressed.connect(self.send_button.click)

        # Set up the back-end
        self.communicate = Communicate()
        self.communicate.new_message.connect(self.add_message_to_history)

        self.client_thread = ClientThread(self.communicate)
        self.client_thread.start()

    @pyqtSlot()
    def send_message(self):
        message = self.message_input.text()
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 5555))
        client_socket.send(message.encode('utf-8'))
        client_socket.close()
        self.message_input.clear()

    @pyqtSlot(str)
    def add_message_to_history(self, message):
        self.message_history.append(message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_app = ChatApp()
    chat_app.show()
    sys.exit(app.exec_())
