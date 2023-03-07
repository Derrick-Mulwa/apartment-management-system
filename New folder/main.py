import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QTextCharFormat, QColor
import mysql.connector
from datetime import datetime, date, time
import random
import threading
from PyQt5.QtGui import QTextCursor


class Ui_Form(object):
    # def __init__(self):
    #     self.update_messages()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(404, 435)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 381, 331))
        self.textEdit.setReadOnly(False)
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 369, 291, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 370, 75, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "send"))

        self.pushButton.clicked.connect(self.update_messages)
        threading.Thread(target=self.update_messages()).start()


    def update_messages(self):
        on = True
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )

        mycursor = db.cursor()
        sent_to = ["Kenitto", "Sophia", "Alex", "Brighton"]
        mycursor.execute(f"INSERT INTO apartment_name.messages(date_sent, sent_from, sent_to, message )"
                         f" VALUES('{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}', 'Ken', "
                         f"'{random.choice(sent_to)}', '{self.lineEdit.text()}');")
        db.commit()

        mycursor.execute("SELECT * FROM apartment_name.messages WHERE sent_from = 'Ken' or sent_to = 'Ken' ORDER BY date_sent;")
        messagelist = [i for i in mycursor]
        display_message = ''

        for i in messagelist:
            time = f"[{i[1]}] "
            if i[2] == "Ken":
                message = time + "YOU: "
            else:
                message = time + i[2].upper() + ": "

            message += f"{i[4]}\n\n"

            display_message += message

        self.textEdit.setText(display_message)
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QTextCursor.End, QTextCursor.MoveAnchor)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.setReadOnly(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
