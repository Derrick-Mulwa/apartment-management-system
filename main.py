from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
)


class Ui_Form(object):
    def __init__(self):
        self.mycursor = db.cursor()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1022, 494)
        Form.setMinimumSize(QtCore.QSize(1022, 494))
        Form.setMaximumSize(QtCore.QSize(1022, 494))
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(-40, 0, 1061, 521))
        self.stackedWidget.setStyleSheet("background-color:rgb(25, 25, 25)")
        self.stackedWidget.setObjectName("stackedWidget")
        self.PageLogin = QtWidgets.QWidget()
        self.PageLogin.setStyleSheet("QPushButton:hover{\n"
"backgroundr:white;\n"
"\n"
"}")
        self.PageLogin.setObjectName("PageLogin")
        self.label = QtWidgets.QLabel(self.PageLogin)
        self.label.setGeometry(QtCore.QRect(270, 30, 571, 431))
        self.label.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(33, 33, 33)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.PageLogin)
        self.label_2.setGeometry(QtCore.QRect(290, 70, 191, 16))
        self.label_2.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.PageLogin)
        self.label_3.setGeometry(QtCore.QRect(290, 170, 71, 16))
        self.label_3.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.PageLogin)
        self.label_5.setGeometry(QtCore.QRect(540, 380, 61, 16))
        self.label_5.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.led_LoginPage_Username = QtWidgets.QLineEdit(self.PageLogin)
        self.led_LoginPage_Username.setGeometry(QtCore.QRect(290, 100, 501, 41))
        self.led_LoginPage_Username.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.led_LoginPage_Username.setObjectName("led_LoginPage_Username")
        self.led_LoginPage_Password = QtWidgets.QLineEdit(self.PageLogin)
        self.led_LoginPage_Password.setGeometry(QtCore.QRect(290, 200, 501, 41))
        self.led_LoginPage_Password.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.led_LoginPage_Password.setObjectName("led_LoginPage_Password")
        self.led_LoginPage_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btn_LoginPage_Login = QtWidgets.QPushButton(self.PageLogin)
        self.btn_LoginPage_Login.setGeometry(QtCore.QRect(430, 280, 261, 51))
        self.btn_LoginPage_Login.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(6, 46, 175);\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"backgroundr:white;\n"
"\n"
"}\n"
"")
        self.btn_LoginPage_Login.setObjectName("btn_LoginPage_Login")
        self.btn_LoginPage_ForgotPassword = QtWidgets.QPushButton(self.PageLogin)
        self.btn_LoginPage_ForgotPassword.setGeometry(QtCore.QRect(644, 170, 131, 23))
        self.btn_LoginPage_ForgotPassword.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(171, 98, 255);\n"
"border-radius:10px\n"
"")
        self.btn_LoginPage_ForgotPassword.setObjectName("btn_LoginPage_ForgotPassword")
        self.btn_LoginPage_SignUp = QtWidgets.QPushButton(self.PageLogin)
        self.btn_LoginPage_SignUp.setGeometry(QtCore.QRect(510, 420, 111, 21))
        self.btn_LoginPage_SignUp.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(6, 46, 175);\n"
"border-radius: 4px")
        self.btn_LoginPage_SignUp.setObjectName("btn_LoginPage_SignUp")
        self.stackedWidget.addWidget(self.PageLogin)
        self.pageSignUp = QtWidgets.QWidget()
        self.pageSignUp.setObjectName("pageSignUp")
        self.btn_PageSignUp_signup = QtWidgets.QPushButton(self.pageSignUp)
        self.btn_PageSignUp_signup.setGeometry(QtCore.QRect(290, 410, 271, 31))
        self.btn_PageSignUp_signup.setStyleSheet("background-color: rgb(43, 166, 16);\n"
"border-radius:10px")
        self.btn_PageSignUp_signup.setObjectName("btn_PageSignUp_signup")
        self.label_4 = QtWidgets.QLabel(self.pageSignUp)
        self.label_4.setGeometry(QtCore.QRect(60, 40, 81, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.pageSignUp)
        self.label_6.setGeometry(QtCore.QRect(160, 190, 81, 16))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.pageSignUp)
        self.label_7.setGeometry(QtCore.QRect(420, 110, 81, 16))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.pageSignUp)
        self.label_8.setGeometry(QtCore.QRect(160, 110, 81, 16))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.pageSignUp)
        self.label_9.setGeometry(QtCore.QRect(320, 40, 81, 16))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.pageSignUp)
        self.label_10.setGeometry(QtCore.QRect(670, 110, 81, 16))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.pageSignUp)
        self.label_11.setGeometry(QtCore.QRect(820, 40, 81, 16))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.pageSignUp)
        self.label_12.setGeometry(QtCore.QRect(50, 335, 81, 21))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.pageSignUp)
        self.label_13.setGeometry(QtCore.QRect(330, 340, 81, 16))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.pageSignUp)
        self.label_14.setGeometry(QtCore.QRect(80, 260, 921, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(43, 166, 16);\n"
"border-radius:10px;\n"
"\n"
"color: rgb(255, 255, 255);")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.led_PageSignup_FirstName = QtWidgets.QLineEdit(self.pageSignUp)
        self.led_PageSignup_FirstName.setGeometry(QtCore.QRect(130, 30, 171, 31))
        self.led_PageSignup_FirstName.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(255, 255, 255);")
        self.led_PageSignup_FirstName.setObjectName("led_PageSignup_FirstName")
        self.led_PageSignup_Username = QtWidgets.QLineEdit(self.pageSignUp)
        self.led_PageSignup_Username.setGeometry(QtCore.QRect(230, 180, 171, 31))
        self.led_PageSignup_Username.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(255, 255, 255);")
        self.led_PageSignup_Username.setObjectName("led_PageSignup_Username")
        self.led_PageSignup_LastName = QtWidgets.QLineEdit(self.pageSignUp)
        self.led_PageSignup_LastName.setGeometry(QtCore.QRect(380, 30, 161, 31))
        self.led_PageSignup_LastName.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(255, 255, 255);")
        self.led_PageSignup_LastName.setObjectName("led_PageSignup_LastName")
        self.led_PageSignup_IDNumber = QtWidgets.QLineEdit(self.pageSignUp)
        self.led_PageSignup_IDNumber.setGeometry(QtCore.QRect(230, 100, 171, 31))
        self.led_PageSignup_IDNumber.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(255, 255, 255);")
        self.led_PageSignup_IDNumber.setObjectName("led_PageSignup_IDNumber")
        self.led_PageSignup_HouseNumber = QtWidgets.QLineEdit(self.pageSignUp)
        self.led_PageSignup_HouseNumber.setGeometry(QtCore.QRect(900, 30, 151, 31))
        self.led_PageSignup_HouseNumber.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(255, 255, 255);")
        self.led_PageSignup_HouseNumber.setObjectName("led_PageSignup_HouseNumber")
        self.led_PageSignup_NOKastName = QtWidgets.QLineEdit(self.pageSignUp)
        self.led_PageSignup_NOKastName.setGeometry(QtCore.QRect(420, 330, 241, 31))
        self.led_PageSignup_NOKastName.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(255, 255, 255);")
        self.led_PageSignup_NOKastName.setObjectName("led_PageSignup_NOKastName")
        self.led_PageSignup_NOKFirstName = QtWidgets.QLineEdit(self.pageSignUp)
        self.led_PageSignup_NOKFirstName.setGeometry(QtCore.QRect(140, 330, 161, 31))
        self.led_PageSignup_NOKFirstName.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(255, 255, 255);")
        self.led_PageSignup_NOKFirstName.setObjectName("led_PageSignup_NOKFirstName")
        self.led_PageSignup_Phonenumber = QtWidgets.QLineEdit(self.pageSignUp)
        self.led_PageSignup_Phonenumber.setGeometry(QtCore.QRect(750, 100, 161, 31))
        self.led_PageSignup_Phonenumber.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(255, 255, 255);")
        self.led_PageSignup_Phonenumber.setObjectName("led_PageSignup_Phonenumber")
        self.label_15 = QtWidgets.QLabel(self.pageSignUp)
        self.label_15.setGeometry(QtCore.QRect(570, 30, 81, 31))
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.led_PageSignup_EmailAddress = QtWidgets.QLineEdit(self.pageSignUp)
        self.led_PageSignup_EmailAddress.setGeometry(QtCore.QRect(620, 30, 191, 31))
        self.led_PageSignup_EmailAddress.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(255, 255, 255);")
        self.led_PageSignup_EmailAddress.setObjectName("led_PageSignup_EmailAddress")
        self.label_16 = QtWidgets.QLabel(self.pageSignUp)
        self.label_16.setGeometry(QtCore.QRect(720, 340, 81, 16))
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.led_PageSignup_NOKPhoneNumber = QtWidgets.QLineEdit(self.pageSignUp)
        self.led_PageSignup_NOKPhoneNumber.setGeometry(QtCore.QRect(810, 330, 241, 31))
        self.led_PageSignup_NOKPhoneNumber.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(255, 255, 255);")
        self.led_PageSignup_NOKPhoneNumber.setObjectName("led_PageSignup_NOKPhoneNumber")
        self.btn_PageSignUp_BacktoLogin = QtWidgets.QPushButton(self.pageSignUp)
        self.btn_PageSignUp_BacktoLogin.setGeometry(QtCore.QRect(800, 410, 121, 31))
        self.btn_PageSignUp_BacktoLogin.setStyleSheet("background-color:rgb(255, 32, 43);\n"
"border-radius:10px")
        self.btn_PageSignUp_BacktoLogin.setObjectName("btn_PageSignUp_BacktoLogin")
        self.label_20 = QtWidgets.QLabel(self.pageSignUp)
        self.label_20.setGeometry(QtCore.QRect(420, 190, 81, 16))
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_20.setObjectName("label_20")
        self.led_PageSignup_Password = QtWidgets.QLineEdit(self.pageSignUp)
        self.led_PageSignup_Password.setGeometry(QtCore.QRect(480, 180, 171, 31))
        self.led_PageSignup_Password.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(255, 255, 255);")
        self.led_PageSignup_Password.setObjectName("led_PageSignup_Password")
        self.label_21 = QtWidgets.QLabel(self.pageSignUp)
        self.label_21.setGeometry(QtCore.QRect(680, 180, 81, 31))
        self.label_21.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_21.setObjectName("label_21")
        self.led_PageSignup_RepeatPassword = QtWidgets.QLineEdit(self.pageSignUp)
        self.led_PageSignup_RepeatPassword.setGeometry(QtCore.QRect(740, 180, 171, 31))
        self.led_PageSignup_RepeatPassword.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(255, 255, 255);")
        self.led_PageSignup_RepeatPassword.setObjectName("led_PageSignup_RepeatPassword")
        self.widget = QtWidgets.QWidget(self.pageSignUp)
        self.widget.setGeometry(QtCore.QRect(480, 90, 151, 51))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rbtn_PageSignup_Male = QtWidgets.QRadioButton(self.widget)
        self.rbtn_PageSignup_Male.setStyleSheet("color: rgb(255, 255, 255);")
        self.rbtn_PageSignup_Male.setObjectName("rbtn_PageSignup_Male")
        self.horizontalLayout.addWidget(self.rbtn_PageSignup_Male)
        self.rbtn_PageSignup_Female = QtWidgets.QRadioButton(self.widget)
        self.rbtn_PageSignup_Female.setStyleSheet("color: rgb(255, 255, 255);")
        self.rbtn_PageSignup_Female.setObjectName("rbtn_PageSignup_Female")
        self.horizontalLayout.addWidget(self.rbtn_PageSignup_Female)
        self.stackedWidget.addWidget(self.pageSignUp)
        self.pageForgotPassword = QtWidgets.QWidget()
        self.pageForgotPassword.setObjectName("pageForgotPassword")
        self.label_17 = QtWidgets.QLabel(self.pageForgotPassword)
        self.label_17.setGeometry(QtCore.QRect(260, 40, 541, 381))
        self.label_17.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(61, 61, 61);\n"
"")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.pageForgotPassword)
        self.label_18.setGeometry(QtCore.QRect(350, 120, 51, 31))
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(61, 61, 61);\n"
"")
        self.label_18.setObjectName("label_18")
        self.btn_pageForgotPassword_ResetPassword = QtWidgets.QPushButton(self.pageForgotPassword)
        self.btn_pageForgotPassword_ResetPassword.setGeometry(QtCore.QRect(460, 230, 141, 41))
        self.btn_pageForgotPassword_ResetPassword.setStyleSheet("background-color:rgb(255, 32, 43);\n"
"border-radius:10px\n"
"")
        self.btn_pageForgotPassword_ResetPassword.setObjectName("btn_pageForgotPassword_ResetPassword")
        self.led_PageForgotPPassword_Username = QtWidgets.QLineEdit(self.pageForgotPassword)
        self.led_PageForgotPPassword_Username.setGeometry(QtCore.QRect(430, 120, 241, 31))
        self.led_PageForgotPPassword_Username.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius:5px;")
        self.led_PageForgotPPassword_Username.setObjectName("led_PageForgotPPassword_Username")
        self.btn_pageForgotPassword_BacktoLogin = QtWidgets.QPushButton(self.pageForgotPassword)
        self.btn_pageForgotPassword_BacktoLogin.setGeometry(QtCore.QRect(460, 360, 141, 31))
        self.btn_pageForgotPassword_BacktoLogin.setStyleSheet("background-color:rgb(22, 172, 5);\n"
"border-radius:10px\n"
"")
        self.btn_pageForgotPassword_BacktoLogin.setObjectName("btn_pageForgotPassword_BacktoLogin")
        self.stackedWidget.addWidget(self.pageForgotPassword)
        self.pageHomepage = QtWidgets.QWidget()
        self.pageHomepage.setObjectName("pageHomepage")
        self.label_19 = QtWidgets.QLabel(self.pageHomepage)
        self.label_19.setGeometry(QtCore.QRect(30, 0, 1031, 501))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(36)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgb(34, 255, 10);")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.btn_pageHomepage_logout = QtWidgets.QPushButton(self.pageHomepage)
        self.btn_pageHomepage_logout.setGeometry(QtCore.QRect(470, 400, 141, 41))
        self.btn_pageHomepage_logout.setStyleSheet("background-color:rgb(255, 32, 43);\n"
"border-radius:10px\n"
"")
        self.btn_pageHomepage_logout.setObjectName("btn_pageHomepage_logout")
        self.stackedWidget.addWidget(self.pageHomepage)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        self.led_LoginPage_Username.editingFinished.connect(self.led_LoginPage_Username.selectAll)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Apartment Manager"))
        self.label_2.setText(_translate("Form", "USERNAME"))
        self.label_3.setText(_translate("Form", "PASSWORD"))
        self.label_5.setText(_translate("Form", "NEW USER?"))
        self.btn_LoginPage_Login.setText(_translate("Form", "LOG IN"))
        self.btn_LoginPage_ForgotPassword.setText(_translate("Form", "FORGOT PASSWORD"))
        self.btn_LoginPage_SignUp.setText(_translate("Form", "SIGN UP"))
        self.btn_PageSignUp_signup.setText(_translate("Form", "SIGN UP"))
        self.label_4.setText(_translate("Form", "First Name"))
        self.label_6.setText(_translate("Form", "Username"))
        self.label_7.setText(_translate("Form", "Gender"))
        self.label_8.setText(_translate("Form", "ID Number"))
        self.label_9.setText(_translate("Form", "Last Name"))
        self.label_10.setText(_translate("Form", "Phone Number"))
        self.label_11.setText(_translate("Form", "House Number"))
        self.label_12.setText(_translate("Form", "First Name"))
        self.label_13.setText(_translate("Form", "Last Name"))
        self.label_14.setText(_translate("Form", "NEXT OF KIN\'S DETAILS"))
        self.label_15.setText(_translate("Form", "Email\n"
"Address"))
        self.label_16.setText(_translate("Form", "Phone Number"))
        self.btn_PageSignUp_BacktoLogin.setText(_translate("Form", "BACK TO LOGIN PAGE"))
        self.label_20.setText(_translate("Form", "Password"))
        self.label_21.setText(_translate("Form", "Repeat\n"
"Password"))
        self.rbtn_PageSignup_Male.setText(_translate("Form", "MALE"))
        self.rbtn_PageSignup_Female.setText(_translate("Form", "FEMALE"))
        self.label_18.setText(_translate("Form", "Username"))
        self.btn_pageForgotPassword_ResetPassword.setText(_translate("Form", "Reset Password"))
        self.btn_pageForgotPassword_BacktoLogin.setText(_translate("Form", "Back to Login"))
        self.label_19.setText(_translate("Form", "WELCOME TO HOMEPAGE"))
        self.btn_pageHomepage_logout.setText(_translate("Form", "LOGOUT"))

        # Mambo yangu

        self.btn_LoginPage_Login.clicked.connect(lambda: self.loginpage_btnlogin())
        self.btn_LoginPage_SignUp.clicked.connect(lambda: self.to_pageSignup())
        self.btn_LoginPage_ForgotPassword.clicked.connect(lambda: self.to_pageForgotpassword())
        self.btn_pageHomepage_logout.clicked.connect(lambda: self.to_pageLogin())
        self.btn_pageForgotPassword_BacktoLogin.clicked.connect(lambda: self.to_pageLogin())
        self.btn_PageSignUp_BacktoLogin.clicked.connect(lambda: self.to_pageLogin())

    def to_pageLogin(self):
        self.stackedWidget.setCurrentWidget(self.PageLogin)

    def to_pageSignup(self):
        self.stackedWidget.setCurrentWidget(self.pageSignUp)

    def to_pageForgotpassword(self):
        self.stackedWidget.setCurrentWidget(self.pageForgotPassword)

    def to_pageHomepage(self):
        self.stackedWidget.setCurrentWidget(self.pageHomepage)


    def get_password(self, user):

        try:
            self.mycursor.execute(f"SELECT user_password FROM apartment_name.tenants_logins WHERE id_number = {user};")
            self.password = self.mycursor.fetchall()[0][0]
            return self.password
        except:
            try:
                self.mycursor.execute(
                    f"SELECT user_password FROM apartment_name.tenants_logins WHERE house_number = '{user}';")
                self.password = self.mycursor.fetchall()[0][0]
                return self.password
            except:
                try:
                    self.mycursor.execute(
                        f"SELECT user_password FROM apartment_name.tenants_logins WHERE phone_number = {user};")
                    self.password = self.mycursor.fetchall()[0][0]
                    return self.password
                except:
                    try:
                        self.mycursor.execute(
                        f"SELECT user_password FROM apartment_name.tenants_logins WHERE email_address = '{user}';")

                        self.password = self.mycursor.fetchall()[0][0]
                        return self.password
                    except:
                        self.password = "None"
                        return self.password


    def loginpage_btnlogin(self):
        self.username = self.led_LoginPage_Username.text()
        print(self.username)
        self.entered_password = self.led_LoginPage_Password.text()

        self.user_password = self.get_password(self.username)

        if self.user_password == self.entered_password:
            self.to_pageHomepage()

        else:
            print("User does not exist!")






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

