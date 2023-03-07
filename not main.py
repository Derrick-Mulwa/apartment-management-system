<<<<<<< HEAD
# Mambo yangu
# import mysql.connector
# import random
# import smtplib

self.db = mysql.connector.connect(
    user="root",
    host="localhost",
    password="root")

self.mycursor = self.db.cursor()

self.led_LoginPage_Password.setEchoMode(QtWidgets.QLineEdit.Password)
self.reset_password_step = 0
# Hide signup page widgets
self.btn_pageForgotPassword_updatePassword.hide()
self.btn_pageForgotPassword_verifyCode.hide()
self.led_pageForgotPassword_newpassword.hide()
self.led_pageForgotPassword_confirmPassword.hide()
self.led_pageForgotPassword_verificationCode.hide()
self.lbl_pageForgotPassword_verificationcode.hide()
self.led_pageForgotPassword_confirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)
self.led_pageForgotPassword_newpassword.setEchoMode(QtWidgets.QLineEdit.Password)

self.btn_LoginPage_Login.clicked.connect(lambda: self.loginpage_btnlogin())
self.btn_LoginPage_SignUp.clicked.connect(lambda: self.to_pageSignup())
self.btn_LoginPage_ForgotPassword.clicked.connect(lambda: self.to_pageForgotpassword())
self.btn_pageHomepage_logout.clicked.connect(lambda: self.to_pageLogin())
self.btn_pageForgotPassword_BacktoLogin.clicked.connect(lambda: self.button_pageForgotPassword_BacktoLogin())
self.btn_PageSignUp_BacktoLogin.clicked.connect(lambda: self.to_pageLogin())
self.led_LoginPage_Username.editingFinished.connect(self.led_authentic_username)
self.led_pageForgotPassword_newpassword.editingFinished.connect(self.goodpass)

self.btn_pageForgotPassword_continue.clicked.connect(self.button_continue)
self.btn_pageForgotPassword_verifyCode.clicked.connect(self.button_verifyCode)
self.btn_pageForgotPassword_updatePassword.clicked.connect(self.button_forgotpassword_updatepassword)


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
        password = self.mycursor.fetchall()[0][0]
        return password
    except:
        try:
            self.mycursor.execute(
                f"SELECT user_password FROM apartment_name.tenants_logins WHERE house_number = '{user}';")
=======
import time

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import random
import smtplib


class Ui_Form(object):
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
"border: 2px solid white;\n"
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
        self.lbl_pageLogin_username = QtWidgets.QLabel(self.PageLogin)
        self.lbl_pageLogin_username.setGeometry(QtCore.QRect(300, 140, 191, 16))
        self.lbl_pageLogin_username.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 26, 10)")
        self.lbl_pageLogin_username.setText("")
        self.lbl_pageLogin_username.setObjectName("lbl_pageLogin_username")
        self.lbl_pageLogin_password = QtWidgets.QLabel(self.PageLogin)
        self.lbl_pageLogin_password.setGeometry(QtCore.QRect(300, 240, 191, 16))
        self.lbl_pageLogin_password.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 26, 10)")
        self.lbl_pageLogin_password.setText("")
        self.lbl_pageLogin_password.setObjectName("lbl_pageLogin_password")
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.btn_LoginPage_Login.raise_()
        self.btn_LoginPage_ForgotPassword.raise_()
        self.btn_LoginPage_SignUp.raise_()
        self.lbl_pageLogin_username.raise_()
        self.led_LoginPage_Username.raise_()
        self.lbl_pageLogin_password.raise_()
        self.led_LoginPage_Password.raise_()
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
        self.layoutWidget = QtWidgets.QWidget(self.pageSignUp)
        self.layoutWidget.setGeometry(QtCore.QRect(480, 90, 151, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rbtn_PageSignup_Male = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbtn_PageSignup_Male.setStyleSheet("color: rgb(255, 255, 255);")
        self.rbtn_PageSignup_Male.setObjectName("rbtn_PageSignup_Male")
        self.horizontalLayout.addWidget(self.rbtn_PageSignup_Male)
        self.rbtn_PageSignup_Female = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbtn_PageSignup_Female.setStyleSheet("color: rgb(255, 255, 255);")
        self.rbtn_PageSignup_Female.setObjectName("rbtn_PageSignup_Female")
        self.horizontalLayout.addWidget(self.rbtn_PageSignup_Female)
        self.stackedWidget.addWidget(self.pageSignUp)
        self.pageForgotPassword = QtWidgets.QWidget()
        self.pageForgotPassword.setObjectName("pageForgotPassword")
        self.label_17 = QtWidgets.QLabel(self.pageForgotPassword)
        self.label_17.setGeometry(QtCore.QRect(260, 40, 501, 331))
        self.label_17.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(61, 61, 61);\n"
"")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.lbl_pageForgotPassword_email = QtWidgets.QLabel(self.pageForgotPassword)
        self.lbl_pageForgotPassword_email.setGeometry(QtCore.QRect(350, 120, 131, 31))
        self.lbl_pageForgotPassword_email.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(61, 61, 61);\n"
"")
        self.lbl_pageForgotPassword_email.setObjectName("lbl_pageForgotPassword_email")
        self.btn_pageForgotPassword_continue = QtWidgets.QPushButton(self.pageForgotPassword)
        self.btn_pageForgotPassword_continue.setGeometry(QtCore.QRect(450, 230, 141, 41))
        self.btn_pageForgotPassword_continue.setStyleSheet("background-color:rgb(255, 32, 43);\n"
"border-radius:10px\n"
"")
        self.btn_pageForgotPassword_continue.setObjectName("btn_pageForgotPassword_continue")
        self.led_pageForgotPassword_Username = QtWidgets.QLineEdit(self.pageForgotPassword)
        self.led_pageForgotPassword_Username.setGeometry(QtCore.QRect(350, 150, 361, 31))
        self.led_pageForgotPassword_Username.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius:5px;")
        self.led_pageForgotPassword_Username.setObjectName("led_pageForgotPassword_Username")
        self.btn_pageForgotPassword_BacktoLogin = QtWidgets.QPushButton(self.pageForgotPassword)
        self.btn_pageForgotPassword_BacktoLogin.setGeometry(QtCore.QRect(260, 40, 141, 51))
        self.btn_pageForgotPassword_BacktoLogin.setStyleSheet("background-color:rgb(22, 172, 5);\n"
"border-radius:10px;\n"
"border-bottom-left-radius: 0px\n"
"")
        self.btn_pageForgotPassword_BacktoLogin.setObjectName("btn_pageForgotPassword_BacktoLogin")
        self.label_22 = QtWidgets.QLabel(self.pageForgotPassword)
        self.label_22.setGeometry(QtCore.QRect(260, 40, 501, 51))
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(108, 108, 108);\n"
"border-radius:15px;\n"
"\n"
"")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.pageForgotPassword)
        self.label_23.setGeometry(QtCore.QRect(260, 60, 501, 31))
        self.label_23.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(108, 108, 108);\n"
"\n"
"")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.pageForgotPassword)
        self.label_24.setGeometry(QtCore.QRect(410, 40, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(36)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(108, 108, 108);\n"
"\n"
"")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.lbl_pageForgotPassword_emailNotification = QtWidgets.QLabel(self.pageForgotPassword)
        self.lbl_pageForgotPassword_emailNotification.setGeometry(QtCore.QRect(350, 170, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_pageForgotPassword_emailNotification.setFont(font)
        self.lbl_pageForgotPassword_emailNotification.setStyleSheet("color:rgb(255, 44, 7);\n"
"background-color: rgb(61, 61, 61);\n"
"")
        self.lbl_pageForgotPassword_emailNotification.setText("")
        self.lbl_pageForgotPassword_emailNotification.setObjectName("lbl_pageForgotPassword_emailNotification")
        self.btn_pageForgotPassword_verifyCode = QtWidgets.QPushButton(self.pageForgotPassword)
        self.btn_pageForgotPassword_verifyCode.setGeometry(QtCore.QRect(450, 310, 141, 41))
        self.btn_pageForgotPassword_verifyCode.setStyleSheet("background-color:rgb(255, 32, 43);\n"
"border-radius:10px\n"
"")
        self.btn_pageForgotPassword_verifyCode.setObjectName("btn_pageForgotPassword_verifyCode")
        self.led_pageForgotPassword_verificationCode = QtWidgets.QLineEdit(self.pageForgotPassword)
        self.led_pageForgotPassword_verificationCode.setGeometry(QtCore.QRect(350, 240, 361, 31))
        self.led_pageForgotPassword_verificationCode.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius:5px;")
        self.led_pageForgotPassword_verificationCode.setObjectName("led_pageForgotPassword_verificationCode")
        self.lbl_pageForgotPassword_verificationcode = QtWidgets.QLabel(self.pageForgotPassword)
        self.lbl_pageForgotPassword_verificationcode.setGeometry(QtCore.QRect(350, 210, 231, 31))
        self.lbl_pageForgotPassword_verificationcode.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(61, 61, 61);\n"
"")
        self.lbl_pageForgotPassword_verificationcode.setObjectName("lbl_pageForgotPassword_verificationcode")
        self.lbl_pageForgotPassword_verificationNotification = QtWidgets.QLabel(self.pageForgotPassword)
        self.lbl_pageForgotPassword_verificationNotification.setGeometry(QtCore.QRect(350, 270, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_pageForgotPassword_verificationNotification.setFont(font)
        self.lbl_pageForgotPassword_verificationNotification.setStyleSheet("color:rgb(255, 44, 7);\n"
"background-color: rgb(61, 61, 61);\n"
"")
        self.lbl_pageForgotPassword_verificationNotification.setText("")
        self.lbl_pageForgotPassword_verificationNotification.setObjectName("lbl_pageForgotPassword_verificationNotification")
        self.btn_pageForgotPassword_updatePassword = QtWidgets.QPushButton(self.pageForgotPassword)
        self.btn_pageForgotPassword_updatePassword.setGeometry(QtCore.QRect(450, 310, 141, 41))
        self.btn_pageForgotPassword_updatePassword.setStyleSheet("background-color: rgb(16, 255, 12);\n"
"border-radius:10px\n"
"")
        self.btn_pageForgotPassword_updatePassword.setObjectName("btn_pageForgotPassword_updatePassword")
        self.led_pageForgotPassword_newpassword = QtWidgets.QLineEdit(self.pageForgotPassword)
        self.led_pageForgotPassword_newpassword.setGeometry(QtCore.QRect(350, 150, 361, 31))
        self.led_pageForgotPassword_newpassword.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius:5px;")
        self.led_pageForgotPassword_newpassword.setObjectName("led_pageForgotPassword_newpassword")
        self.led_pageForgotPassword_confirmPassword = QtWidgets.QLineEdit(self.pageForgotPassword)
        self.led_pageForgotPassword_confirmPassword.setGeometry(QtCore.QRect(350, 240, 361, 31))
        self.led_pageForgotPassword_confirmPassword.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius:5px;")
        self.led_pageForgotPassword_confirmPassword.setObjectName("led_pageForgotPassword_confirmPassword")
        self.label_17.raise_()
        self.lbl_pageForgotPassword_email.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.btn_pageForgotPassword_BacktoLogin.raise_()
        self.label_24.raise_()
        self.lbl_pageForgotPassword_emailNotification.raise_()
        self.btn_pageForgotPassword_verifyCode.raise_()
        self.lbl_pageForgotPassword_verificationcode.raise_()
        self.lbl_pageForgotPassword_verificationNotification.raise_()
        self.led_pageForgotPassword_verificationCode.raise_()
        self.btn_pageForgotPassword_updatePassword.raise_()
        self.led_pageForgotPassword_newpassword.raise_()
        self.led_pageForgotPassword_confirmPassword.raise_()
        self.led_pageForgotPassword_Username.raise_()
        self.btn_pageForgotPassword_continue.raise_()
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
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Apartment Manager"))
        self.label_2.setText(_translate("Form", "USERNAME"))
        self.label_3.setText(_translate("Form", "PASSWORD"))
        self.label_5.setText(_translate("Form", "NEW USER?"))
        self.led_LoginPage_Username.setPlaceholderText(_translate("Form", "   ID number / Email address / House number / Phone number"))
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
        self.lbl_pageForgotPassword_email.setText(_translate("Form", "Enter your Email Address"))
        self.btn_pageForgotPassword_continue.setText(_translate("Form", "Continue"))
        self.led_pageForgotPassword_Username.setPlaceholderText(_translate("Form", "   abc@ayz.com"))
        self.btn_pageForgotPassword_BacktoLogin.setText(_translate("Form", "Back to Login"))
        self.label_24.setText(_translate("Form", "RESET PASSWORD"))
        self.btn_pageForgotPassword_verifyCode.setText(_translate("Form", "Verify code"))
        self.lbl_pageForgotPassword_verificationcode.setText(_translate("Form", "Enter verification code"))
        self.btn_pageForgotPassword_updatePassword.setText(_translate("Form", "Update Password"))
        self.label_19.setText(_translate("Form", "WELCOME TO HOMEPAGE"))
        self.btn_pageHomepage_logout.setText(_translate("Form", "LOGOUT"))



        # Mambo yangu
        self.db = mysql.connector.connect(
            user="root",
            host="localhost",
            password="root")

        self.mycursor = self.db.cursor()

        self.led_LoginPage_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.reset_password_step = 0
        # Hide signup page widgets
        self.btn_pageForgotPassword_updatePassword.hide()
        self.btn_pageForgotPassword_verifyCode.hide()
        self.led_pageForgotPassword_newpassword.hide()
        self.led_pageForgotPassword_confirmPassword.hide()
        self.led_pageForgotPassword_verificationCode.hide()
        self.lbl_pageForgotPassword_verificationcode.hide()
        self.led_pageForgotPassword_confirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.led_pageForgotPassword_newpassword.setEchoMode(QtWidgets.QLineEdit.Password)


        self.btn_LoginPage_Login.clicked.connect(lambda: self.loginpage_btnlogin())
        self.btn_LoginPage_SignUp.clicked.connect(lambda: self.to_pageSignup())
        self.btn_LoginPage_ForgotPassword.clicked.connect(lambda: self.to_pageForgotpassword())
        self.btn_pageHomepage_logout.clicked.connect(lambda: self.to_pageLogin())
        self.btn_pageForgotPassword_BacktoLogin.clicked.connect(lambda: self.button_pageForgotPassword_BacktoLogin())
        self.btn_PageSignUp_BacktoLogin.clicked.connect(lambda: self.to_pageLogin())
        self.led_LoginPage_Username.editingFinished.connect(self.led_authentic_username)
        self.led_pageForgotPassword_newpassword.editingFinished.connect(self.goodpass)

        self.btn_pageForgotPassword_continue.clicked.connect(self.button_continue)
        self.btn_pageForgotPassword_verifyCode.clicked.connect(self.button_verifyCode)
        self.btn_pageForgotPassword_updatePassword.clicked.connect(self.button_forgotpassword_updatepassword)


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
>>>>>>> 2e247db49e69325ed3abcfbf1aecb037cdd540c4
            password = self.mycursor.fetchall()[0][0]
            return password
        except:
            try:
                self.mycursor.execute(
<<<<<<< HEAD
                    f"SELECT user_password FROM apartment_name.tenants_logins WHERE phone_number = {user};")
=======
                    f"SELECT user_password FROM apartment_name.tenants_logins WHERE house_number = '{user}';")
>>>>>>> 2e247db49e69325ed3abcfbf1aecb037cdd540c4
                password = self.mycursor.fetchall()[0][0]
                return password
            except:
                try:
                    self.mycursor.execute(
<<<<<<< HEAD
                        f"SELECT user_password FROM apartment_name.tenants_logins WHERE email_address = '{user}';")

                    password = self.mycursor.fetchall()[0][0]
                    return password
                except:
                    password = "None"
                    return password


def authentic_username(self, username):
    autenticity = self.get_password(username)
    if autenticity == "None":
        return False
    else:
        return True


def led_authentic_username(self):
    is_username_authentic = self.authentic_username(self.led_LoginPage_Username.text())
    print(self.led_LoginPage_Username.text())
    print(is_username_authentic)

    if is_username_authentic is False:
        self.led_LoginPage_Username.setStyleSheet("background-color: rgb(33, 33, 33);"
                                                  "color: rgb(255, 255, 255);"
                                                  "border: 2px solid red;"
                                                  "border-radius: 10px;")
        self.lbl_pageLogin_username.setText("Username does not exist")
    else:
        self.led_LoginPage_Username.setStyleSheet("background-color: rgb(33, 33, 33);"
                                                  "color: rgb(255, 255, 255);"
                                                  "border: 2px solid rgb(79, 223, 12);"
                                                  "border-radius: 10px;")
        self.lbl_pageLogin_username.setText("")


def loginpage_btnlogin(self):
    self.username = self.led_LoginPage_Username.text()
    print(self.username)
    self.entered_password = self.led_LoginPage_Password.text()

    self.user_password = self.get_password(self.username)

    if self.user_password == self.entered_password:
        self.led_LoginPage_Password.setStyleSheet("background-color: rgb(33, 33, 33);"
                                                  "color: rgb(255, 255, 255);"
                                                  "border: 2px solid white;"
                                                  "border-radius: 10px;")
        self.lbl_pageLogin_password.setText("")

        self.to_pageHomepage()

    else:
        if self.user_password == "None":
            self.lbl_pageLogin_password.setText("You entered a username that does not exist!")
            self.lbl_pageLogin_password.adjustSize()

        else:
            self.led_LoginPage_Password.setStyleSheet("background-color: rgb(33, 33, 33);"
                                                      "color: rgb(255, 255, 255);"
                                                      "border: 2px solid red;"
                                                      "border-radius: 10px;")
            self.lbl_pageLogin_password.setText("Incorrect Password. Please try again!")
            self.lbl_pageLogin_password.adjustSize()


def led_authentic_username_forgotpassword(self):
    username = self.led_PageForgotPPassword_Username.text()
    legit = self.authentic_username(username)
    if legit is True:
        self.lbl_resetPassword_usernameNotiication = QtWidgets.QLabel(self.pageForgotPassword)
        self.lbl_resetPassword_usernameNotiication.setGeometry(QtCore.QRect(440, 100, 241, 31))
        self.lbl_resetPassword_usernameNotiication.setStyleSheet("color:rgb(23, 255, 11);\n"
                                                                 "background-color: rgb(61, 61, 61);\n"
                                                                 "")
        self.lbl_resetPassword_usernameNotiication.setObjectName("lbl_resetPassword_usernameNotiication")
        self.lbl_resetPassword_usernameNotiication.setText("OTP code has been sent to your email address")


def get_otp(self):
    otp = ""
    for i in range(6):
        otp = otp + (str(random.randint(0, 9)))

    return otp


def sendmail(self, send_email_address, firstName, otp):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    email_password = "gqtkvoyoqagcfhby"

    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("derrickmulwa.programming@gmail.com", email_password)
    company = "Friends Corner"
    body = f"Dear {firstName},\n\nWe have received a request to reset " \
           f"the password for your account. To proceed with this request, use the following verification " \
           f"code:\n\n{otp}\n\nPlease enter this code on the password reset page to confirm your identity and continue" \
           f" with the password reset process.\nIf you did not make this request, please disregard this email and " \
           f"ensure that your account is secure. Thank you for using our service.\n\nBest regards,\n" \
           f"{company}."

    subject = "RESET YOUR FRIENDSCORNER PASSWORD."

    message = f'subject: {subject} \n\n{body}'

    server.sendmail(
        "derrickmulwa.programming@gmail.com",
        send_email_address,
        message)


def button_continue(self):
    self.reset_password_step = 1
    self.resetpass_send_email_address = self.led_pageForgotPassword_Username.text()
    try:
        self.mycursor.execute(f"SELECT EXISTS(SELECT * FROM apartment_name.tenants_logins "
                              f"WHERE email_address = '{self.resetpass_send_email_address}');")
        exists = str(self.mycursor.fetchall()[0][0])
        if exists == "1":
            self.lbl_pageForgotPassword_emailNotification.setText("Verification code has been sent to your email")
            self.lbl_pageForgotPassword_emailNotification.setStyleSheet("color: rgb(56, 255, 12);"
                                                                        "background-color: rgb(61, 61, 61);")

            try:
                self.led_pageForgotPassword_Username.setStyleSheet("background-color: rgb(61, 61, 61);"
                                                                   "color: rgb(255, 255, 255);"
                                                                   "border: 2px solid rgb(100, 197, 26);"
                                                                   "border-radius:5px;")
                self.verification_code = self.get_otp()
                self.mycursor.execute(f"SELECT first_name FROM apartment_name.details "
                                      f"WHERE email_address = '{self.resetpass_send_email_address}';")
                self.resetpass_first_name = str(self.mycursor.fetchall()[0][0])
                self.sendmail(self.resetpass_send_email_address, self.resetpass_first_name, self.verification_code)
                self.btn_pageForgotPassword_continue.hide()
                self.lbl_pageForgotPassword_verificationcode.show()
                self.led_pageForgotPassword_verificationCode.show()
                self.btn_pageForgotPassword_verifyCode.show()
                self.lbl_pageForgotPassword_verificationcode.setText("Enter Verification Code")
            except:
                self.lbl_pageForgotPassword_emailNotification.setText("There was an error sending verification code."
                                                                      "Please check your internet connection.")
                self.lbl_pageForgotPassword_emailNotification.adjustSize()
                self.lbl_pageForgotPassword_emailNotification.setStyleSheet("color: rgb(255, 44, 7);"
                                                                            "background-color: rgb(61, 61, 61);")

        else:
            self.lbl_pageForgotPassword_emailNotification.setText("Email address is not linked to any account")
            self.lbl_pageForgotPassword_emailNotification.setStyleSheet("color: rgb(255, 44, 7);"
                                                                        "background-color: rgb(61, 61, 61);")

    except:
        self.lbl_pageForgotPassword_emailNotification.setText("An error occurred! Please restart the application")
        self.lbl_pageForgotPassword_emailNotification.setStyleSheet("color: rgb(255, 44, 7);"
                                                                    "background-color: rgb(61, 61, 61);")


def button_verifyCode(self):
    self.reset_password_step = 2
    user_code = self.led_pageForgotPassword_verificationCode.text()

    if user_code == self.verification_code:
        self.led_pageForgotPassword_verificationCode.hide()
        self.led_pageForgotPassword_Username.hide()
        self.btn_pageForgotPassword_verifyCode.hide()

        self.led_pageForgotPassword_newpassword.show()
        self.led_pageForgotPassword_confirmPassword.show()
        self.btn_pageForgotPassword_updatePassword.show()

        self.lbl_pageForgotPassword_verificationNotification.setText("")
        self.lbl_pageForgotPassword_emailNotification.setText("")
        self.lbl_pageForgotPassword_email.setText("New password")
        self.lbl_pageForgotPassword_verificationcode.setText("Repeat Password")

    else:
        self.lbl_pageForgotPassword_verificationNotification.setText("Incorrect code!")


def button_pageForgotPassword_BacktoLogin(self):
    try:
        if self.reset_password_step == 0:
            self.to_pageLogin()
        elif self.reset_password_step == 1 or self.lbl_pageForgotPassword_verificationcode.text() == "Incorrect code!":
            self.led_pageForgotPassword_Username.show()
            self.lbl_pageForgotPassword_email.setText("Enter your Email Address")
            self.lbl_pageForgotPassword_emailNotification.setText("")
            self.led_pageForgotPassword_Username.clear()
            self.btn_pageForgotPassword_continue.show()
            self.stackedWidget.setCurrentWidget(self.PageLogin)
            self.lbl_pageForgotPassword_verificationcode.hide()
            self.btn_pageForgotPassword_verifyCode.hide()

            self.led_pageForgotPassword_verificationCode.hide()

            self.led_pageForgotPassword_Username.show()
            self.lbl_pageForgotPassword_email.setText("Enter your Email Address")
            self.lbl_pageForgotPassword_emailNotification.setText("")
            self.led_pageForgotPassword_Username.clear()
            self.btn_pageForgotPassword_continue.show()
            self.stackedWidget.setCurrentWidget(self.PageLogin)

        elif self.reset_password_step == 2:
            self.lbl_pageForgotPassword_verificationcode.hide()
            self.btn_pageForgotPassword_updatePassword.hide()
            self.led_pageForgotPassword_newpassword.hide()
            self.led_pageForgotPassword_confirmPassword.hide()

            self.led_pageForgotPassword_Username.show()
            self.lbl_pageForgotPassword_email.setText("Enter your Email Address")
            self.lbl_pageForgotPassword_emailNotification.setText("")
            self.lbl_pageForgotPassword_verificationNotification.setText("")

            self.led_pageForgotPassword_Username.clear()
            self.btn_pageForgotPassword_continue.show()
            self.stackedWidget.setCurrentWidget(self.PageLogin)

    except:
        self.led_pageForgotPassword_confirmPassword.hide()
        self.led_pageForgotPassword_confirmPassword.hide()
        self.lbl_pageForgotPassword_verificationcode.setText("")
        self.led_pageForgotPassword_Username.show()
        self.lbl_pageForgotPassword_email.setText("Enter your Email Address")
        self.led_pageForgotPassword_Username.clear()
        self.lbl_resetPassword_usernameNotiication.setText("")
        self.btn_pageForgotPassword_continue.show()
        self.stackedWidget.setCurrentWidget(self.PageLogin)


def goodpass(self):
    if len(self.led_pageForgotPassword_newpassword.text()) >= 8:
        self.led_pageForgotPassword_newpassword.setStyleSheet("background-color: rgb(61, 61, 61);"
                                                              "color: rgb(255, 255, 255);"
                                                              "border: 2px solid rgb(100, 197, 26);"
                                                              "border-radius:5px;")
        self.lbl_pageForgotPassword_emailNotification.setText("Strong Password")
        self.lbl_pageForgotPassword_emailNotification.setStyleSheet("color: rgb(100, 197, 26);"
                                                                    "background-color: rgb(61, 61, 61);")
    else:
        self.led_pageForgotPassword_newpassword.setStyleSheet("background-color: rgb(61, 61, 61);"
                                                              "color: rgb(255, 255, 255);"
                                                              "border: 2px solid red;"
                                                              "border-radius:5px;")

        self.lbl_pageForgotPassword_emailNotification.setText("Password length should be greater than 8 characters")
        self.lbl_pageForgotPassword_emailNotification.setStyleSheet("color: rgb(255, 44, 7);"
                                                                    "background-color: rgb(61, 61, 61);")


def button_forgotpassword_updatepassword(self):
    new_password = self.led_pageForgotPassword_newpassword.text()
    confirm_password = self.led_pageForgotPassword_confirmPassword.text()

    if len(new_password) >= 8:
        self.led_pageForgotPassword_newpassword.setStyleSheet("background-color: rgb(61, 61, 61);"
                                                              "color: rgb(255, 255, 255);"
                                                              "border: 2px solid rgb(100, 197, 26);"
                                                              "border-radius:5px;")
        if new_password == confirm_password:
            print(self.resetpass_send_email_address)
            self.mycursor.execute(f"SELECT id_number FROM apartment_name.tenants_logins "
                                  f"WHERE email_address = '{self.resetpass_send_email_address}';")

            primary_key = str(self.mycursor.fetchall()[0][0])
            print(f"Done here: {primary_key}")

            self.mycursor.execute(f"UPDATE apartment_name.tenants_logins SET user_password = '{new_password}' "
                                  f"WHERE id_number = '{primary_key}';")
            self.db.commit()

            server = smtplib.SMTP('smtp.gmail.com', 587)
            email_password = "gqtkvoyoqagcfhby"

            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login("derrickmulwa.programming@gmail.com", email_password)
            company = "Friends Corner"

            body = f"Dear {self.resetpass_first_name} \n\nThis email is to confirm that the password for your " \
                   f"account has been successfully" \
                   f" changed. If you did not make this change, please contact our support team immediately. \n\nIf " \
                   f"you did make this change, please keep your new password secure and do not share it with anyone." \
                   f" We recommend that you choose a strong, unique password that is not easy to guess and update it" \
                   f" regularly to ensure the security of your account. \n\nIf you experience any issues logging in " \
                   f"with your new password, please contact our support team for assistance. Thank you for using " \
                   f"our service. \n\nBest regards,\n{company}"

            subject = "FRIENDSCORNER'S PASSWORD CHANGE."

            message = f'subject: {subject} \n\n{body}'

            server.sendmail(
                "derrickmulwa.programming@gmail.com",
                self.resetpass_send_email_address,
                message)

            self.stackedWidget.setCurrentWidget(self.PageLogin)
            self.lbl_pageForgotPassword_verificationNotification.setText("Password changed successfully!")

            self.lbl_pageForgotPassword_verificationcode.hide()
            self.btn_pageForgotPassword_updatePassword.hide()
            self.led_pageForgotPassword_newpassword.hide()
            self.led_pageForgotPassword_confirmPassword.hide()

            self.led_pageForgotPassword_Username.show()
            self.lbl_pageForgotPassword_email.setText("Enter your Email Address")
            self.lbl_pageForgotPassword_emailNotification.setText("")
            self.lbl_pageForgotPassword_verificationNotification.setText("")

            self.led_pageForgotPassword_Username.clear()
            self.btn_pageForgotPassword_continue.show()

            self.stackedWidget.setCurrentWidget(self.PageLogin)

        else:
            self.lbl_pageForgotPassword_verificationNotification.setText("Passwords do not match!")
    else:
        self.lbl_pageForgotPassword_emailNotification.setText("Password length should be greater than 8")

=======
                        f"SELECT user_password FROM apartment_name.tenants_logins WHERE phone_number = {user};")
                    password = self.mycursor.fetchall()[0][0]
                    return password
                except:
                    try:
                        self.mycursor.execute(
                            f"SELECT user_password FROM apartment_name.tenants_logins WHERE email_address = '{user}';")

                        password = self.mycursor.fetchall()[0][0]
                        return password
                    except:
                        password = "None"
                        return password

    def authentic_username(self, username):
        autenticity = self.get_password(username)
        if autenticity == "None":
            return False
        else:
            return True

    def led_authentic_username(self):
        is_username_authentic = self.authentic_username(self.led_LoginPage_Username.text())
        print(self.led_LoginPage_Username.text())
        print(is_username_authentic)

        if is_username_authentic is False:
            self.led_LoginPage_Username.setStyleSheet("background-color: rgb(33, 33, 33);"
                                                      "color: rgb(255, 255, 255);"
                                                      "border: 2px solid red;"
                                                      "border-radius: 10px;")
            self.lbl_pageLogin_username.setText("Username does not exist")
        else:
            self.led_LoginPage_Username.setStyleSheet("background-color: rgb(33, 33, 33);"
                                                      "color: rgb(255, 255, 255);"
                                                      "border: 2px solid rgb(79, 223, 12);"
                                                      "border-radius: 10px;")
            self.lbl_pageLogin_username.setText("")


    def loginpage_btnlogin(self):

        self.username = self.led_LoginPage_Username.text()
        print(self.username)
        self.entered_password = self.led_LoginPage_Password.text()

        self.user_password = self.get_password(self.username)

        if self.user_password == self.entered_password:
            self.led_LoginPage_Password.setStyleSheet("background-color: rgb(33, 33, 33);"
                                                      "color: rgb(255, 255, 255);"
                                                      "border: 2px solid white;"
                                                      "border-radius: 10px;")
            self.lbl_pageLogin_password.setText("")

            self.to_pageHomepage()

        else:
            if self.user_password == "None":
                self.lbl_pageLogin_password.setText("You entered a username that does not exist!")
                self.lbl_pageLogin_password.adjustSize()

            else:
                self.led_LoginPage_Password.setStyleSheet("background-color: rgb(33, 33, 33);"
                                                          "color: rgb(255, 255, 255);"
                                                          "border: 2px solid red;"
                                                          "border-radius: 10px;")
                self.lbl_pageLogin_password.setText("Incorrect Password. Please try again!")
                self.lbl_pageLogin_password.adjustSize()

    def led_authentic_username_forgotpassword(self):
        username = self.led_PageForgotPPassword_Username.text()
        legit = self.authentic_username(username)
        if legit is True:
            self.lbl_resetPassword_usernameNotiication = QtWidgets.QLabel(self.pageForgotPassword)
            self.lbl_resetPassword_usernameNotiication.setGeometry(QtCore.QRect(440, 100, 241, 31))
            self.lbl_resetPassword_usernameNotiication.setStyleSheet("color:rgb(23, 255, 11);\n"
                                                                     "background-color: rgb(61, 61, 61);\n"
                                                                     "")
            self.lbl_resetPassword_usernameNotiication.setObjectName("lbl_resetPassword_usernameNotiication")
            self.lbl_resetPassword_usernameNotiication.setText("OTP code has been sent to your email address")

    def get_otp(self):
        otp = ""
        for i in range(6):
           otp = otp + (str(random.randint(0, 9)))

        return otp


    def sendmail(self, send_email_address, firstName, otp):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        email_password = "gqtkvoyoqagcfhby"

        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("derrickmulwa.programming@gmail.com", email_password)
        company = "Friends Corner"
        body = f"Dear {firstName},\n\nWe have received a request to reset " \
               f"the password for your account. To proceed with this request, use the following verification " \
               f"code:\n\n{otp}\n\nPlease enter this code on the password reset page to confirm your identity and continue" \
               f" with the password reset process.\n\nIf you did not make this request, please disregard this email and " \
               f"ensure that your account is secure. Thank you for using our service.\n\nBest regards,\n\n" \
               f"{company}."

        subject = "RESET YOUR FRIENDSCORNER PASSWORD."

        message = f'subject: {subject} \n\n{body}'

        server.sendmail(
                "derrickmulwa.programming@gmail.com",
                send_email_address,
                message)

    def button_continue(self):
        self.reset_password_step = 1
        self.resetpass_send_email_address = self.led_pageForgotPassword_Username.text()
        try:
            self.mycursor.execute(f"SELECT EXISTS(SELECT * FROM apartment_name.tenants_logins "
                                  f"WHERE email_address = '{self.resetpass_send_email_address}');")
            exists = str(self.mycursor.fetchall()[0][0])
            if exists == "1":
                self.lbl_pageForgotPassword_emailNotification.setText("Verification code has been sent to your email")
                self.lbl_pageForgotPassword_emailNotification.setStyleSheet("color: rgb(56, 255, 12);"
                                                                            "background-color: rgb(61, 61, 61);")

                try:
                    self.led_pageForgotPassword_Username.setStyleSheet("background-color: rgb(61, 61, 61);"
                                                                       "color: rgb(255, 255, 255);"
                                                                       "border: 2px solid rgb(100, 197, 26);"
                                                                       "border-radius:5px;")
                    self.verification_code = self.get_otp()
                    self.mycursor.execute(f"SELECT first_name FROM apartment_name.details "
                                              f"WHERE email_address = '{self.resetpass_send_email_address}';")
                    self.resetpass_first_name = str(self.mycursor.fetchall()[0][0])
                    self.sendmail(self.resetpass_send_email_address, self.resetpass_first_name, self.verification_code)
                    self.btn_pageForgotPassword_continue.hide()
                    self.lbl_pageForgotPassword_verificationcode.show()
                    self.led_pageForgotPassword_verificationCode.show()
                    self.btn_pageForgotPassword_verifyCode.show()
                    self.lbl_pageForgotPassword_verificationcode.setText("Enter Verification Code")
                except:
                    self.lbl_pageForgotPassword_emailNotification.setText("There was an error sending verification code."
                                                                          "Please check your internet connection.")
                    self.lbl_pageForgotPassword_emailNotification.adjustSize()
                    self.lbl_pageForgotPassword_emailNotification.setStyleSheet("color: rgb(255, 44, 7);"
                                                                                "background-color: rgb(61, 61, 61);")

            else:
                self.lbl_pageForgotPassword_emailNotification.setText("Email address is not linked to any account")
                self.lbl_pageForgotPassword_emailNotification.setStyleSheet("color: rgb(255, 44, 7);"
                                                                            "background-color: rgb(61, 61, 61);")

        except:
                self.lbl_pageForgotPassword_emailNotification.setText("An error occurred! Please restart the application")
                self.lbl_pageForgotPassword_emailNotification.setStyleSheet("color: rgb(255, 44, 7);"
                                                                            "background-color: rgb(61, 61, 61);")
    def button_verifyCode(self):
        self.reset_password_step = 2
        user_code = self.led_pageForgotPassword_verificationCode.text()

        if user_code == self.verification_code:
            self.led_pageForgotPassword_verificationCode.hide()
            self.led_pageForgotPassword_Username.hide()
            self.btn_pageForgotPassword_verifyCode.hide()

            self.led_pageForgotPassword_newpassword.show()
            self.led_pageForgotPassword_confirmPassword.show()
            self.btn_pageForgotPassword_updatePassword.show()

            self.lbl_pageForgotPassword_verificationNotification.setText("")
            self.lbl_pageForgotPassword_emailNotification.setText("")
            self.lbl_pageForgotPassword_email.setText("New password")
            self.lbl_pageForgotPassword_verificationcode.setText("Repeat Password")

        else:
            self.lbl_pageForgotPassword_verificationNotification.setText("Incorrect code!")

    def button_pageForgotPassword_BacktoLogin(self):
        try:
            if self.reset_password_step == 0:
                self.to_pageLogin()
            elif self.reset_password_step == 1 or self.lbl_pageForgotPassword_verificationcode.text() == "Incorrect code!":
                self.led_pageForgotPassword_Username.show()
                self.lbl_pageForgotPassword_email.setText("Enter your Email Address")
                self.lbl_pageForgotPassword_emailNotification.setText("")
                self.led_pageForgotPassword_Username.clear()
                self.btn_pageForgotPassword_continue.show()
                self.stackedWidget.setCurrentWidget(self.PageLogin)
                self.lbl_pageForgotPassword_verificationcode.hide()
                self.btn_pageForgotPassword_verifyCode.hide()

                self.led_pageForgotPassword_verificationCode.hide()

                self.led_pageForgotPassword_Username.show()
                self.lbl_pageForgotPassword_email.setText("Enter your Email Address")
                self.lbl_pageForgotPassword_emailNotification.setText("")
                self.led_pageForgotPassword_Username.clear()
                self.btn_pageForgotPassword_continue.show()
                self.stackedWidget.setCurrentWidget(self.PageLogin)

            elif self.reset_password_step == 2:
                self.lbl_pageForgotPassword_verificationcode.hide()
                self.btn_pageForgotPassword_updatePassword.hide()
                self.led_pageForgotPassword_newpassword.hide()
                self.led_pageForgotPassword_confirmPassword.hide()

                self.led_pageForgotPassword_Username.show()
                self.lbl_pageForgotPassword_email.setText("Enter your Email Address")
                self.lbl_pageForgotPassword_emailNotification.setText("")
                self.lbl_pageForgotPassword_verificationNotification.setText("")

                self.led_pageForgotPassword_Username.clear()
                self.btn_pageForgotPassword_continue.show()
                self.stackedWidget.setCurrentWidget(self.PageLogin)

        except:
            self.led_pageForgotPassword_confirmPassword.hide()
            self.led_pageForgotPassword_confirmPassword.hide()
            self.lbl_pageForgotPassword_verificationcode.setText("")
            self.led_pageForgotPassword_Username.show()
            self.lbl_pageForgotPassword_email.setText("Enter your Email Address")
            self.led_pageForgotPassword_Username.clear()
            self.lbl_resetPassword_usernameNotiication.setText("")
            self.btn_pageForgotPassword_continue.show()
            self.stackedWidget.setCurrentWidget(self.PageLogin)

    def goodpass(self):
        if len(self.led_pageForgotPassword_newpassword.text()) >= 8:
            self.led_pageForgotPassword_newpassword.setStyleSheet("background-color: rgb(61, 61, 61);"
                                                                  "color: rgb(255, 255, 255);"
                                                                  "border: 2px solid rgb(100, 197, 26);"
                                                                  "border-radius:5px;")
            self.lbl_pageForgotPassword_emailNotification.setText("Strong Password")
            self.lbl_pageForgotPassword_emailNotification.setStyleSheet("color: rgb(100, 197, 26);"
                                                                        "background-color: rgb(61, 61, 61);")
        else:
            self.led_pageForgotPassword_newpassword.setStyleSheet("background-color: rgb(61, 61, 61);"
                                                                  "color: rgb(255, 255, 255);"
                                                                  "border: 2px solid red;"
                                                                  "border-radius:5px;")

            self.lbl_pageForgotPassword_emailNotification.setText("Password length should be greater than 8 characters")
            self.lbl_pageForgotPassword_emailNotification.setStyleSheet("color: rgb(255, 44, 7);"
                                                                        "background-color: rgb(61, 61, 61);")

    def button_forgotpassword_updatepassword(self):
        new_password = self.led_pageForgotPassword_newpassword.text()
        confirm_password = self.led_pageForgotPassword_confirmPassword.text()

        if len(new_password) >= 8:
            self.led_pageForgotPassword_newpassword.setStyleSheet("background-color: rgb(61, 61, 61);"
                                                                  "color: rgb(255, 255, 255);"
                                                                  "border: 2px solid rgb(100, 197, 26);"
                                                                  "border-radius:5px;")
            if new_password == confirm_password:
                print(self.resetpass_send_email_address)
                self.mycursor.execute(f"SELECT id_number FROM apartment_name.tenants_logins "
                                      f"WHERE email_address = '{self.resetpass_send_email_address}';")

                primary_key = str(self.mycursor.fetchall()[0][0])
                print(f"Done here: {primary_key}")

                self.mycursor.execute(f"UPDATE apartment_name.tenants_logins SET user_password = '{new_password}' "
                                      f"WHERE id_number = '{primary_key}';")

                server = smtplib.SMTP('smtp.gmail.com', 587)
                email_password = "gqtkvoyoqagcfhby"

                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login("derrickmulwa.programming@gmail.com", email_password)
                company = "Friends Corner"

                body = f"Dear {self.resetpass_first_name} \n\nThis email is to confirm that the password for your " \
                       f"account has been successfully" \
                       f" changed. If you did not make this change, please contact our support team immediately. \n\nIf " \
                       f"you did make this change, please keep your new password secure and do not share it with anyone." \
                       f" We recommend that you choose a strong, unique password that is not easy to guess and update it" \
                       f" regularly to ensure the security of your account. \n\nIf you experience any issues logging in " \
                       f"with your new password, please contact our support team for assistance. Thank you for using " \
                       f"our service. \n\nBest regards,\n{company}"

                subject = "FRIENDSCORNER'S PASSWORD CHANGE."

                message = f'subject: {subject} \n\n{body}'

                server.sendmail(
                        "derrickmulwa.programming@gmail.com",
                        self.resetpass_send_email_address,
                        message)

                self.stackedWidget.setCurrentWidget(self.PageLogin)
                self.lbl_pageForgotPassword_verificationNotification.setText("Password changed successfully!")

                self.lbl_pageForgotPassword_verificationcode.hide()
                self.btn_pageForgotPassword_updatePassword.hide()
                self.led_pageForgotPassword_newpassword.hide()
                self.led_pageForgotPassword_confirmPassword.hide()

                self.led_pageForgotPassword_Username.show()
                self.lbl_pageForgotPassword_email.setText("Enter your Email Address")
                self.lbl_pageForgotPassword_emailNotification.setText("")
                self.lbl_pageForgotPassword_verificationNotification.setText("")

                self.led_pageForgotPassword_Username.clear()
                self.btn_pageForgotPassword_continue.show()

                self.stackedWidget.setCurrentWidget(self.PageLogin)

            else:
                self.lbl_pageForgotPassword_verificationNotification.setText("Passwords do not match!")
        else:
            self.lbl_pageForgotPassword_emailNotification.setText("Password length should be greater than 8")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
>>>>>>> 2e247db49e69325ed3abcfbf1aecb037cdd540c4
