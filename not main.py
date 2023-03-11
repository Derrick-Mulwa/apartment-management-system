from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
import random
import smtplib
from datetime import datetime
import re

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
        self.label_4 = QtWidgets.QLabel(self.pageSignUp)
        self.label_4.setGeometry(QtCore.QRect(170, 10, 771, 471))
        self.label_4.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.pageSignUp)
        self.label_6.setGeometry(QtCore.QRect(180, 20, 201, 451))
        self.label_6.setStyleSheet("background-color: rgb(59, 59, 59);\n"
"border-radius: 10px")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.pageSignUp)
        self.label_7.setGeometry(QtCore.QRect(390, 20, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(59, 59, 59);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.lbl_pageSignUp_personalDetails = QtWidgets.QLabel(self.pageSignUp)
        self.lbl_pageSignUp_personalDetails.setGeometry(QtCore.QRect(180, 100, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        self.lbl_pageSignUp_personalDetails.setFont(font)
        self.lbl_pageSignUp_personalDetails.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border: 2px solid rgb(59, 59, 59);\n"
"border-left:6px solid rgb(255, 6, 18);\n"
"")
        self.lbl_pageSignUp_personalDetails.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_pageSignUp_personalDetails.setObjectName("lbl_pageSignUp_personalDetails")
        self.lbl_pageSignUp_nextofkin = QtWidgets.QLabel(self.pageSignUp)
        self.lbl_pageSignUp_nextofkin.setGeometry(QtCore.QRect(180, 200, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.lbl_pageSignUp_nextofkin.setFont(font)
        self.lbl_pageSignUp_nextofkin.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border: 2px solid rgb(59, 59, 59);\n"
"border-radius:5px\n"
"")
        self.lbl_pageSignUp_nextofkin.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_pageSignUp_nextofkin.setObjectName("lbl_pageSignUp_nextofkin")
        self.signUP = QtWidgets.QStackedWidget(self.pageSignUp)
        self.signUP.setGeometry(QtCore.QRect(400, 90, 531, 381))
        self.signUP.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"color: rgb(17, 17, 17);")
        self.signUP.setObjectName("signUP")
        self.pageSignUpPersonalDetails = QtWidgets.QWidget()
        self.pageSignUpPersonalDetails.setObjectName("pageSignUpPersonalDetails")
        self.label_8 = QtWidgets.QLabel(self.pageSignUpPersonalDetails)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_8.setObjectName("label_8")
        self.led_pageSignup_firstName = QtWidgets.QLineEdit(self.pageSignUpPersonalDetails)
        self.led_pageSignup_firstName.setGeometry(QtCore.QRect(20, 40, 171, 21))
        self.led_pageSignup_firstName.setStyleSheet("border:2px solid rgb(203, 203, 203);;\n"
"border-bottom: 2px solid rgb(15, 15, 15)")
        self.led_pageSignup_firstName.setObjectName("led_pageSignup_firstName")
        self.led_pageSignup_lastName = QtWidgets.QLineEdit(self.pageSignUpPersonalDetails)
        self.led_pageSignup_lastName.setGeometry(QtCore.QRect(280, 40, 171, 21))
        self.led_pageSignup_lastName.setStyleSheet("border:2px solid rgb(203, 203, 203);;\n"
"border-bottom: 2px solid rgb(15, 15, 15)")
        self.led_pageSignup_lastName.setObjectName("led_pageSignup_lastName")
        self.label_10 = QtWidgets.QLabel(self.pageSignUpPersonalDetails)
        self.label_10.setGeometry(QtCore.QRect(280, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_10.setObjectName("label_10")
        self.led_pageSignup_idNumber = QtWidgets.QLineEdit(self.pageSignUpPersonalDetails)
        self.led_pageSignup_idNumber.setGeometry(QtCore.QRect(20, 120, 171, 21))
        self.led_pageSignup_idNumber.setStyleSheet("border:2px solid rgb(203, 203, 203);;\n"
"border-bottom: 2px solid rgb(15, 15, 15)")
        self.led_pageSignup_idNumber.setObjectName("led_pageSignup_idNumber")
        self.label_9 = QtWidgets.QLabel(self.pageSignUpPersonalDetails)
        self.label_9.setGeometry(QtCore.QRect(20, 90, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_9.setObjectName("label_9")
        self.led_pageSignup_emailAddress = QtWidgets.QLineEdit(self.pageSignUpPersonalDetails)
        self.led_pageSignup_emailAddress.setGeometry(QtCore.QRect(280, 120, 171, 21))
        self.led_pageSignup_emailAddress.setStyleSheet("border:2px solid rgb(203, 203, 203);;\n"
"border-bottom: 2px solid rgb(15, 15, 15)")
        self.led_pageSignup_emailAddress.setObjectName("led_pageSignup_emailAddress")
        self.label_11 = QtWidgets.QLabel(self.pageSignUpPersonalDetails)
        self.label_11.setGeometry(QtCore.QRect(280, 90, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_11.setObjectName("label_11")
        self.led_pageSignup_phoneNumber = QtWidgets.QLineEdit(self.pageSignUpPersonalDetails)
        self.led_pageSignup_phoneNumber.setGeometry(QtCore.QRect(320, 200, 131, 21))
        self.led_pageSignup_phoneNumber.setStyleSheet("border:2px solid rgb(203, 203, 203);;\n"
"border-bottom: 2px solid rgb(15, 15, 15)")
        self.led_pageSignup_phoneNumber.setObjectName("led_pageSignup_phoneNumber")
        self.label_12 = QtWidgets.QLabel(self.pageSignUpPersonalDetails)
        self.label_12.setGeometry(QtCore.QRect(280, 170, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.pageSignUpPersonalDetails)
        self.label_13.setGeometry(QtCore.QRect(280, 200, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.pageSignUpPersonalDetails)
        self.label_14.setGeometry(QtCore.QRect(280, 250, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.pageSignUpPersonalDetails)
        self.label_15.setGeometry(QtCore.QRect(20, 240, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_15.setObjectName("label_15")
        self.btn_pageSignup_personalDetailsNext = QtWidgets.QPushButton(self.pageSignUpPersonalDetails)
        self.btn_pageSignup_personalDetailsNext.setGeometry(QtCore.QRect(340, 330, 121, 41))
        self.btn_pageSignup_personalDetailsNext.setStyleSheet("background-color: rgb(81, 171, 8);\n"
"border-radius:6px")
        self.btn_pageSignup_personalDetailsNext.setObjectName("btn_pageSignup_personalDetailsNext")
        self.led_pageSignup_occupation_2 = QtWidgets.QLineEdit(self.pageSignUpPersonalDetails)
        self.led_pageSignup_occupation_2.setGeometry(QtCore.QRect(20, 200, 171, 21))
        self.led_pageSignup_occupation_2.setStyleSheet("border:2px solid rgb(203, 203, 203);;\n"
"border-bottom: 2px solid rgb(15, 15, 15)")
        self.led_pageSignup_occupation_2.setText("")
        self.led_pageSignup_occupation_2.setObjectName("led_pageSignup_occupation_2")
        self.label_16 = QtWidgets.QLabel(self.pageSignUpPersonalDetails)
        self.label_16.setGeometry(QtCore.QRect(20, 170, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_16.setObjectName("label_16")
        self.layoutWidget = QtWidgets.QWidget(self.pageSignUpPersonalDetails)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 270, 122, 36))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rbn_pageSignUp_male = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbn_pageSignUp_male.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/icons8-user-male-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbn_pageSignUp_male.setIcon(icon)
        self.rbn_pageSignUp_male.setIconSize(QtCore.QSize(30, 30))
        self.rbn_pageSignUp_male.setChecked(True)
        self.rbn_pageSignUp_male.setObjectName("rbn_pageSignUp_male")
        self.horizontalLayout.addWidget(self.rbn_pageSignUp_male)
        self.rbn_pageSignUp_female = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbn_pageSignUp_female.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Downloads/icons8-female-user-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbn_pageSignUp_female.setIcon(icon1)
        self.rbn_pageSignUp_female.setIconSize(QtCore.QSize(30, 30))
        self.rbn_pageSignUp_female.setObjectName("rbn_pageSignUp_female")
        self.horizontalLayout.addWidget(self.rbn_pageSignUp_female)
        self.lbl_pageSignup_emailNotification = QtWidgets.QLabel(self.pageSignUpPersonalDetails)
        self.lbl_pageSignup_emailNotification.setGeometry(QtCore.QRect(280, 140, 221, 16))
        self.lbl_pageSignup_emailNotification.setStyleSheet("color: rgb(229, 6, 28);")
        self.lbl_pageSignup_emailNotification.setText("")
        self.lbl_pageSignup_emailNotification.setObjectName("lbl_pageSignup_emailNotification")
        self.lbl_pageSignup_IDNumberNotification = QtWidgets.QLabel(self.pageSignUpPersonalDetails)
        self.lbl_pageSignup_IDNumberNotification.setGeometry(QtCore.QRect(20, 140, 221, 16))
        self.lbl_pageSignup_IDNumberNotification.setStyleSheet("color: rgb(229, 6, 28);")
        self.lbl_pageSignup_IDNumberNotification.setText("")
        self.lbl_pageSignup_IDNumberNotification.setObjectName("lbl_pageSignup_IDNumberNotification")
        self.lbl_pageSignup_houseNumberNotification = QtWidgets.QLabel(self.pageSignUpPersonalDetails)
        self.lbl_pageSignup_houseNumberNotification.setGeometry(QtCore.QRect(20, 220, 221, 16))
        self.lbl_pageSignup_houseNumberNotification.setStyleSheet("color: rgb(229, 6, 28);")
        self.lbl_pageSignup_houseNumberNotification.setText("")
        self.lbl_pageSignup_houseNumberNotification.setObjectName("lbl_pageSignup_houseNumberNotification")
        self.lbl_pageSignup_phoneNumberNotification = QtWidgets.QLabel(self.pageSignUpPersonalDetails)
        self.lbl_pageSignup_phoneNumberNotification.setGeometry(QtCore.QRect(280, 220, 221, 16))
        self.lbl_pageSignup_phoneNumberNotification.setStyleSheet("color: rgb(229, 6, 28);")
        self.lbl_pageSignup_phoneNumberNotification.setText("")
        self.lbl_pageSignup_phoneNumberNotification.setObjectName("lbl_pageSignup_phoneNumberNotification")
        self.lbl_pageSignup_FirstNameNotification = QtWidgets.QLabel(self.pageSignUpPersonalDetails)
        self.lbl_pageSignup_FirstNameNotification.setGeometry(QtCore.QRect(20, 60, 221, 16))
        self.lbl_pageSignup_FirstNameNotification.setStyleSheet("color: rgb(229, 6, 28);")
        self.lbl_pageSignup_FirstNameNotification.setText("")
        self.lbl_pageSignup_FirstNameNotification.setObjectName("lbl_pageSignup_FirstNameNotification")
        self.lbl_pageSignup_lastNameNotification = QtWidgets.QLabel(self.pageSignUpPersonalDetails)
        self.lbl_pageSignup_lastNameNotification.setGeometry(QtCore.QRect(280, 60, 221, 16))
        self.lbl_pageSignup_lastNameNotification.setStyleSheet("color: rgb(229, 6, 28);")
        self.lbl_pageSignup_lastNameNotification.setText("")
        self.lbl_pageSignup_lastNameNotification.setObjectName("lbl_pageSignup_lastNameNotification")
        self.led_pageSignup_occupation = QtWidgets.QLineEdit(self.pageSignUpPersonalDetails)
        self.led_pageSignup_occupation.setGeometry(QtCore.QRect(280, 280, 171, 21))
        self.led_pageSignup_occupation.setStyleSheet("border:2px solid rgb(203, 203, 203);;\n"
"border-bottom: 2px solid rgb(15, 15, 15)")
        self.led_pageSignup_occupation.setText("")
        self.led_pageSignup_occupation.setObjectName("led_pageSignup_occupation")
        self.lbl_pageSignup_FillallNotification = QtWidgets.QLabel(self.pageSignUpPersonalDetails)
        self.lbl_pageSignup_FillallNotification.setGeometry(QtCore.QRect(70, 340, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.lbl_pageSignup_FillallNotification.setFont(font)
        self.lbl_pageSignup_FillallNotification.setStyleSheet("color: rgb(229, 6, 28);")
        self.lbl_pageSignup_FillallNotification.setText("")
        self.lbl_pageSignup_FillallNotification.setObjectName("lbl_pageSignup_FillallNotification")
        self.layoutWidget.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.btn_pageSignup_personalDetailsNext.raise_()
        self.label_16.raise_()
        self.lbl_pageSignup_emailNotification.raise_()
        self.led_pageSignup_emailAddress.raise_()
        self.lbl_pageSignup_IDNumberNotification.raise_()
        self.led_pageSignup_idNumber.raise_()
        self.lbl_pageSignup_houseNumberNotification.raise_()
        self.led_pageSignup_occupation_2.raise_()
        self.lbl_pageSignup_phoneNumberNotification.raise_()
        self.led_pageSignup_phoneNumber.raise_()
        self.lbl_pageSignup_FirstNameNotification.raise_()
        self.lbl_pageSignup_lastNameNotification.raise_()
        self.led_pageSignup_firstName.raise_()
        self.led_pageSignup_lastName.raise_()
        self.led_pageSignup_occupation.raise_()
        self.lbl_pageSignup_FillallNotification.raise_()
        self.signUP.addWidget(self.pageSignUpPersonalDetails)
        self.pageNextOfKin = QtWidgets.QWidget()
        self.pageNextOfKin.setObjectName("pageNextOfKin")
        self.lbl_pageSignUp_nextofkin_2 = QtWidgets.QLabel(self.pageNextOfKin)
        self.lbl_pageSignUp_nextofkin_2.setGeometry(QtCore.QRect(20, 0, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        self.lbl_pageSignUp_nextofkin_2.setFont(font)
        self.lbl_pageSignUp_nextofkin_2.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border: 2px solid rgb(59, 59, 59);\n"
"border-radius:5px\n"
"")
        self.lbl_pageSignUp_nextofkin_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_pageSignUp_nextofkin_2.setObjectName("lbl_pageSignUp_nextofkin_2")
        self.label_18 = QtWidgets.QLabel(self.pageNextOfKin)
        self.label_18.setGeometry(QtCore.QRect(20, 70, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_18.setObjectName("label_18")
        self.led_pageSignup_next_of_kinfirstName = QtWidgets.QLineEdit(self.pageNextOfKin)
        self.led_pageSignup_next_of_kinfirstName.setGeometry(QtCore.QRect(20, 100, 171, 21))
        self.led_pageSignup_next_of_kinfirstName.setStyleSheet("border:2px solid rgb(203, 203, 203);;\n"
"border-bottom: 2px solid rgb(15, 15, 15)")
        self.led_pageSignup_next_of_kinfirstName.setObjectName("led_pageSignup_next_of_kinfirstName")
        self.label_20 = QtWidgets.QLabel(self.pageNextOfKin)
        self.label_20.setGeometry(QtCore.QRect(300, 70, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_20.setObjectName("label_20")
        self.led_pageSignup_next_of_kinLastName = QtWidgets.QLineEdit(self.pageNextOfKin)
        self.led_pageSignup_next_of_kinLastName.setGeometry(QtCore.QRect(300, 100, 171, 21))
        self.led_pageSignup_next_of_kinLastName.setStyleSheet("border:2px solid rgb(203, 203, 203);;\n"
"border-bottom: 2px solid rgb(15, 15, 15)")
        self.led_pageSignup_next_of_kinLastName.setObjectName("led_pageSignup_next_of_kinLastName")
        self.label_25 = QtWidgets.QLabel(self.pageNextOfKin)
        self.label_25.setGeometry(QtCore.QRect(300, 140, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_25.setObjectName("label_25")
        self.led_pageSignup_next_of_kinemailAddress = QtWidgets.QLineEdit(self.pageNextOfKin)
        self.led_pageSignup_next_of_kinemailAddress.setGeometry(QtCore.QRect(300, 170, 171, 21))
        self.led_pageSignup_next_of_kinemailAddress.setStyleSheet("border:2px solid rgb(203, 203, 203);;\n"
"border-bottom: 2px solid rgb(15, 15, 15)")
        self.led_pageSignup_next_of_kinemailAddress.setText("")
        self.led_pageSignup_next_of_kinemailAddress.setObjectName("led_pageSignup_next_of_kinemailAddress")
        self.label_26 = QtWidgets.QLabel(self.pageNextOfKin)
        self.label_26.setGeometry(QtCore.QRect(20, 220, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_26.setObjectName("label_26")
        self.led_pageSignup_next_of_kin_phoneNumber = QtWidgets.QLineEdit(self.pageNextOfKin)
        self.led_pageSignup_next_of_kin_phoneNumber.setGeometry(QtCore.QRect(60, 170, 131, 21))
        self.led_pageSignup_next_of_kin_phoneNumber.setStyleSheet("border:2px solid rgb(203, 203, 203);;\n"
"border-bottom: 2px solid rgb(15, 15, 15)")
        self.led_pageSignup_next_of_kin_phoneNumber.setObjectName("led_pageSignup_next_of_kin_phoneNumber")
        self.label_27 = QtWidgets.QLabel(self.pageNextOfKin)
        self.label_27.setGeometry(QtCore.QRect(20, 170, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.pageNextOfKin)
        self.label_28.setGeometry(QtCore.QRect(20, 140, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_28.setObjectName("label_28")
        self.combo_pageSignup_next_of_kin_relationship = QtWidgets.QComboBox(self.pageNextOfKin)
        self.combo_pageSignup_next_of_kin_relationship.setGeometry(QtCore.QRect(20, 250, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        self.combo_pageSignup_next_of_kin_relationship.setFont(font)
        self.combo_pageSignup_next_of_kin_relationship.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.combo_pageSignup_next_of_kin_relationship.setToolTipDuration(3)
        self.combo_pageSignup_next_of_kin_relationship.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.combo_pageSignup_next_of_kin_relationship.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 5px;\n"
"color: rgb(172, 172, 172);")
        self.combo_pageSignup_next_of_kin_relationship.setObjectName("combo_pageSignup_next_of_kin_relationship")
        self.combo_pageSignup_next_of_kin_relationship.addItem("")
        self.combo_pageSignup_next_of_kin_relationship.addItem("")
        self.combo_pageSignup_next_of_kin_relationship.addItem("")
        self.combo_pageSignup_next_of_kin_relationship.addItem("")
        self.combo_pageSignup_next_of_kin_relationship.addItem("")
        self.combo_pageSignup_next_of_kin_relationship.addItem("")
        self.combo_pageSignup_next_of_kin_relationship.addItem("")
        self.btn_pageSignup_pageNexofKin_next = QtWidgets.QPushButton(self.pageNextOfKin)
        self.btn_pageSignup_pageNexofKin_next.setGeometry(QtCore.QRect(370, 320, 121, 41))
        self.btn_pageSignup_pageNexofKin_next.setStyleSheet("background-color: rgb(81, 171, 8);\n"
"border-radius:6px")
        self.btn_pageSignup_pageNexofKin_next.setObjectName("btn_pageSignup_pageNexofKin_next")
        self.led_pageSignup_next_of_kinAddress = QtWidgets.QLineEdit(self.pageNextOfKin)
        self.led_pageSignup_next_of_kinAddress.setGeometry(QtCore.QRect(300, 250, 171, 21))
        self.led_pageSignup_next_of_kinAddress.setStyleSheet("border:2px solid rgb(203, 203, 203);;\n"
"border-bottom: 2px solid rgb(15, 15, 15)")
        self.led_pageSignup_next_of_kinAddress.setText("")
        self.led_pageSignup_next_of_kinAddress.setObjectName("led_pageSignup_next_of_kinAddress")
        self.label_29 = QtWidgets.QLabel(self.pageNextOfKin)
        self.label_29.setGeometry(QtCore.QRect(300, 220, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_29.setObjectName("label_29")
        self.btn_pageSignup_page_NextofKin_back = QtWidgets.QPushButton(self.pageNextOfKin)
        self.btn_pageSignup_page_NextofKin_back.setGeometry(QtCore.QRect(10, 320, 121, 41))
        self.btn_pageSignup_page_NextofKin_back.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius:6px;\n"
"border: 2px solid rgb(66, 66, 255)")
        self.btn_pageSignup_page_NextofKin_back.setObjectName("btn_pageSignup_page_NextofKin_back")
        self.lbl_pageSignup_NextOfKin_FirstNameNotification = QtWidgets.QLabel(self.pageNextOfKin)
        self.lbl_pageSignup_NextOfKin_FirstNameNotification.setGeometry(QtCore.QRect(20, 120, 221, 16))
        self.lbl_pageSignup_NextOfKin_FirstNameNotification.setStyleSheet("color: rgb(229, 6, 28);")
        self.lbl_pageSignup_NextOfKin_FirstNameNotification.setText("")
        self.lbl_pageSignup_NextOfKin_FirstNameNotification.setObjectName("lbl_pageSignup_NextOfKin_FirstNameNotification")
        self.lbl_pageSignup_nextfKin_LastNameNotification = QtWidgets.QLabel(self.pageNextOfKin)
        self.lbl_pageSignup_nextfKin_LastNameNotification.setGeometry(QtCore.QRect(300, 120, 221, 16))
        self.lbl_pageSignup_nextfKin_LastNameNotification.setStyleSheet("color: rgb(229, 6, 28);")
        self.lbl_pageSignup_nextfKin_LastNameNotification.setText("")
        self.lbl_pageSignup_nextfKin_LastNameNotification.setObjectName("lbl_pageSignup_nextfKin_LastNameNotification")
        self.lbl_pageSignup_NextofKin_PhoneNumberNotification = QtWidgets.QLabel(self.pageNextOfKin)
        self.lbl_pageSignup_NextofKin_PhoneNumberNotification.setGeometry(QtCore.QRect(20, 190, 221, 16))
        self.lbl_pageSignup_NextofKin_PhoneNumberNotification.setStyleSheet("color: rgb(229, 6, 28);")
        self.lbl_pageSignup_NextofKin_PhoneNumberNotification.setText("")
        self.lbl_pageSignup_NextofKin_PhoneNumberNotification.setObjectName("lbl_pageSignup_NextofKin_PhoneNumberNotification")
        self.lbl_pageSignup_Fillall_NOK_Notification = QtWidgets.QLabel(self.pageNextOfKin)
        self.lbl_pageSignup_Fillall_NOK_Notification.setGeometry(QtCore.QRect(160, 330, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.lbl_pageSignup_Fillall_NOK_Notification.setFont(font)
        self.lbl_pageSignup_Fillall_NOK_Notification.setStyleSheet("color: rgb(229, 6, 28);")
        self.lbl_pageSignup_Fillall_NOK_Notification.setText("")
        self.lbl_pageSignup_Fillall_NOK_Notification.setObjectName("lbl_pageSignup_Fillall_NOK_Notification")
        self.lbl_pageSignUp_nextofkin_2.raise_()
        self.label_18.raise_()
        self.label_20.raise_()
        self.label_25.raise_()
        self.led_pageSignup_next_of_kinemailAddress.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.label_28.raise_()
        self.combo_pageSignup_next_of_kin_relationship.raise_()
        self.btn_pageSignup_pageNexofKin_next.raise_()
        self.led_pageSignup_next_of_kinAddress.raise_()
        self.label_29.raise_()
        self.btn_pageSignup_page_NextofKin_back.raise_()
        self.lbl_pageSignup_NextOfKin_FirstNameNotification.raise_()
        self.led_pageSignup_next_of_kinfirstName.raise_()
        self.lbl_pageSignup_nextfKin_LastNameNotification.raise_()
        self.led_pageSignup_next_of_kinLastName.raise_()
        self.lbl_pageSignup_NextofKin_PhoneNumberNotification.raise_()
        self.led_pageSignup_next_of_kin_phoneNumber.raise_()
        self.lbl_pageSignup_Fillall_NOK_Notification.raise_()
        self.signUP.addWidget(self.pageNextOfKin)
        self.pagePassword = QtWidgets.QWidget()
        self.pagePassword.setObjectName("pagePassword")
        self.label_21 = QtWidgets.QLabel(self.pagePassword)
        self.label_21.setGeometry(QtCore.QRect(30, 80, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_21.setObjectName("label_21")
        self.btn_pageSignup_pagePassword_back = QtWidgets.QPushButton(self.pagePassword)
        self.btn_pageSignup_pagePassword_back.setGeometry(QtCore.QRect(190, 320, 121, 41))
        self.btn_pageSignup_pagePassword_back.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius:6px;\n"
"border: 2px solid rgb(66, 66, 255)")
        self.btn_pageSignup_pagePassword_back.setObjectName("btn_pageSignup_pagePassword_back")
        self.lbl_pageSignUp_nextofkin_3 = QtWidgets.QLabel(self.pagePassword)
        self.lbl_pageSignUp_nextofkin_3.setGeometry(QtCore.QRect(30, 0, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        self.lbl_pageSignUp_nextofkin_3.setFont(font)
        self.lbl_pageSignUp_nextofkin_3.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border: 2px solid rgb(59, 59, 59);\n"
"border-radius:5px\n"
"")
        self.lbl_pageSignUp_nextofkin_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_pageSignUp_nextofkin_3.setObjectName("lbl_pageSignUp_nextofkin_3")
        self.btn_pageSignup_signUp = QtWidgets.QPushButton(self.pagePassword)
        self.btn_pageSignup_signUp.setGeometry(QtCore.QRect(190, 220, 121, 41))
        self.btn_pageSignup_signUp.setStyleSheet("background-color: rgb(81, 171, 8);\n"
"border-radius:6px")
        self.btn_pageSignup_signUp.setObjectName("btn_pageSignup_signUp")
        self.led_pageSignup_newPassword = QtWidgets.QLineEdit(self.pagePassword)
        self.led_pageSignup_newPassword.setGeometry(QtCore.QRect(30, 110, 181, 31))
        self.led_pageSignup_newPassword.setStyleSheet("border: 2px solid rgb(15, 15, 15);\n"
"\n"
"border-radius: 10px;\n"
"")
        self.led_pageSignup_newPassword.setObjectName("led_pageSignup_newPassword")
        self.label_31 = QtWidgets.QLabel(self.pagePassword)
        self.label_31.setGeometry(QtCore.QRect(290, 80, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.label_31.setObjectName("label_31")
        self.led_pageSignup_repeatPassword = QtWidgets.QLineEdit(self.pagePassword)
        self.led_pageSignup_repeatPassword.setGeometry(QtCore.QRect(290, 110, 211, 31))
        self.led_pageSignup_repeatPassword.setStyleSheet("border: 2px solid rgb(15, 15, 15);\n"
"\n"
"border-radius: 10px;\n"
"")
        self.led_pageSignup_repeatPassword.setObjectName("led_pageSignup_repeatPassword")
        self.lbl_pagePassword_NewpasswordNotification = QtWidgets.QLabel(self.pagePassword)
        self.lbl_pagePassword_NewpasswordNotification.setGeometry(QtCore.QRect(30, 140, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_pagePassword_NewpasswordNotification.setFont(font)
        self.lbl_pagePassword_NewpasswordNotification.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.lbl_pagePassword_NewpasswordNotification.setText("")
        self.lbl_pagePassword_NewpasswordNotification.setObjectName("lbl_pagePassword_NewpasswordNotification")
        self.lbl_pagePassword_RepeatPasswordNotification = QtWidgets.QLabel(self.pagePassword)
        self.lbl_pagePassword_RepeatPasswordNotification.setGeometry(QtCore.QRect(290, 140, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_pagePassword_RepeatPasswordNotification.setFont(font)
        self.lbl_pagePassword_RepeatPasswordNotification.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius: 10px;\n"
"color: rgb(17, 17, 17);")
        self.lbl_pagePassword_RepeatPasswordNotification.setText("")
        self.lbl_pagePassword_RepeatPasswordNotification.setObjectName("lbl_pagePassword_RepeatPasswordNotification")
        self.lbl_pageSignup_Fillall_Password_Notification = QtWidgets.QLabel(self.pagePassword)
        self.lbl_pageSignup_Fillall_Password_Notification.setGeometry(QtCore.QRect(160, 180, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.lbl_pageSignup_Fillall_Password_Notification.setFont(font)
        self.lbl_pageSignup_Fillall_Password_Notification.setStyleSheet("color: rgb(229, 6, 28);")
        self.lbl_pageSignup_Fillall_Password_Notification.setText("")
        self.lbl_pageSignup_Fillall_Password_Notification.setObjectName("lbl_pageSignup_Fillall_Password_Notification")
        self.label_21.raise_()
        self.btn_pageSignup_pagePassword_back.raise_()
        self.lbl_pageSignUp_nextofkin_3.raise_()
        self.btn_pageSignup_signUp.raise_()
        self.label_31.raise_()
        self.lbl_pagePassword_NewpasswordNotification.raise_()
        self.led_pageSignup_newPassword.raise_()
        self.lbl_pagePassword_RepeatPasswordNotification.raise_()
        self.led_pageSignup_repeatPassword.raise_()
        self.lbl_pageSignup_Fillall_Password_Notification.raise_()
        self.signUP.addWidget(self.pagePassword)
        self.btn_PageSignUp_BacktoLogin = QtWidgets.QPushButton(self.pageSignUp)
        self.btn_PageSignUp_BacktoLogin.setGeometry(QtCore.QRect(210, 410, 121, 41))
        self.btn_PageSignUp_BacktoLogin.setStyleSheet("border-radius:6px;\n"
"background-color: rgb(7, 65, 255);\n"
"border: 2px solid rgb(66, 66, 255)")
        self.btn_PageSignUp_BacktoLogin.setObjectName("btn_PageSignUp_BacktoLogin")
        self.lbl_pageSignUp_password = QtWidgets.QLabel(self.pageSignUp)
        self.lbl_pageSignUp_password.setGeometry(QtCore.QRect(180, 300, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.lbl_pageSignUp_password.setFont(font)
        self.lbl_pageSignUp_password.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border: 2px solid rgb(59, 59, 59);\n"
"border-radius:5px\n"
"")
        self.lbl_pageSignUp_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_pageSignUp_password.setObjectName("lbl_pageSignUp_password")
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
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.pageHomepage)
        self.stackedWidget_2.setGeometry(QtCore.QRect(190, 0, 881, 511))
        self.stackedWidget_2.setStyleSheet("background-color: rgb(113, 113, 113);")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.pageRealHomepage = QtWidgets.QWidget()
        self.pageRealHomepage.setObjectName("pageRealHomepage")
        self.label_32 = QtWidgets.QLabel(self.pageRealHomepage)
        self.label_32.setGeometry(QtCore.QRect(240, 140, 411, 131))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(20)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(36, 36, 36);")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.lbl_pageHomepage_welcomeUser_2 = QtWidgets.QLabel(self.pageRealHomepage)
        self.lbl_pageHomepage_welcomeUser_2.setGeometry(QtCore.QRect(0, 20, 871, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.lbl_pageHomepage_welcomeUser_2.setFont(font)
        self.lbl_pageHomepage_welcomeUser_2.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);")
        self.lbl_pageHomepage_welcomeUser_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_pageHomepage_welcomeUser_2.setObjectName("lbl_pageHomepage_welcomeUser_2")
        self.stackedWidget_2.addWidget(self.pageRealHomepage)
        self.pagePayRent = QtWidgets.QWidget()
        self.pagePayRent.setObjectName("pagePayRent")
        self.stackedWidget_2.addWidget(self.pagePayRent)
        self.pageChat = QtWidgets.QWidget()
        self.pageChat.setObjectName("pageChat")
        self.label_33 = QtWidgets.QLabel(self.pageChat)
        self.label_33.setGeometry(QtCore.QRect(10, 110, 181, 211))
        self.label_33.setStyleSheet("background-color: rgb(52, 52, 52);\n"
"border-radius: 8px")
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.ted_pageChat_chatbox = QtWidgets.QTextEdit(self.pageChat)
        self.ted_pageChat_chatbox.setGeometry(QtCore.QRect(210, 10, 641, 401))
        self.ted_pageChat_chatbox.setStyleSheet("background-color: rgb(52, 52, 52);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);")
        self.ted_pageChat_chatbox.setObjectName("ted_pageChat_chatbox")
        self.led_pageChat_message = QtWidgets.QLineEdit(self.pageChat)
        self.led_pageChat_message.setGeometry(QtCore.QRect(212, 419, 501, 41))
        self.led_pageChat_message.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px")
        self.led_pageChat_message.setObjectName("led_pageChat_message")
        self.btn_pageChat_send = QtWidgets.QPushButton(self.pageChat)
        self.btn_pageChat_send.setGeometry(QtCore.QRect(730, 422, 111, 41))
        self.btn_pageChat_send.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-radius: 4px")
        self.btn_pageChat_send.setObjectName("btn_pageChat_send")
        self.btn_pageChat_chatWithManager = QtWidgets.QPushButton(self.pageChat)
        self.btn_pageChat_chatWithManager.setGeometry(QtCore.QRect(30, 140, 141, 61))
        self.btn_pageChat_chatWithManager.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(0, 255, 0);\n"
"border-top: 2px solid rgb(81, 81, 81);\n"
"border-bottom: 2px solid rgb(81, 81, 81)")
        self.btn_pageChat_chatWithManager.setObjectName("btn_pageChat_chatWithManager")
        self.btn_pageChat_chatWithOwner = QtWidgets.QPushButton(self.pageChat)
        self.btn_pageChat_chatWithOwner.setGeometry(QtCore.QRect(30, 230, 141, 61))
        self.btn_pageChat_chatWithOwner.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(0, 255, 0);\n"
"border-top: 2px solid rgb(81, 81, 81);\n"
"border-bottom: 2px solid rgb(81, 81, 81)")
        self.btn_pageChat_chatWithOwner.setObjectName("btn_pageChat_chatWithOwner")
        self.stackedWidget_2.addWidget(self.pageChat)
        self.pageReport_a_complaint = QtWidgets.QWidget()
        self.pageReport_a_complaint.setObjectName("pageReport_a_complaint")
        self.label_34 = QtWidgets.QLabel(self.pageReport_a_complaint)
        self.label_34.setGeometry(QtCore.QRect(160, 20, 631, 461))
        self.label_34.setStyleSheet("border-radius:7px;\n"
"background-color: rgb(170, 170, 127);")
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.pageReport_a_complaint)
        self.label_35.setGeometry(QtCore.QRect(300, 85, 91, 21))
        self.label_35.setStyleSheet("border-radius:7px;\n"
"background-color: rgb(170, 170, 127);")
        self.label_35.setObjectName("label_35")
        self.ted_pageReportAComplaint_describeComplaint = QtWidgets.QTextEdit(self.pageReport_a_complaint)
        self.ted_pageReportAComplaint_describeComplaint.setGeometry(QtCore.QRect(250, 210, 471, 201))
        self.ted_pageReportAComplaint_describeComplaint.setStyleSheet("border-radius:7px;\n"
"background-color: rgb(170, 170, 127);\n"
"color: rgb(39, 39, 39);\n"
"border: 2px solid black")
        self.ted_pageReportAComplaint_describeComplaint.setObjectName("ted_pageReportAComplaint_describeComplaint")
        self.date_pageReport_a_complaint_date_of_incedence = QtWidgets.QDateEdit(self.pageReport_a_complaint)
        self.date_pageReport_a_complaint_date_of_incedence.setGeometry(QtCore.QRect(420, 80, 181, 31))
        self.date_pageReport_a_complaint_date_of_incedence.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"border-radius: 4px;\n"
"border: 2px solid black")
        self.date_pageReport_a_complaint_date_of_incedence.setObjectName("date_pageReport_a_complaint_date_of_incedence")
        self.label_36 = QtWidgets.QLabel(self.pageReport_a_complaint)
        self.label_36.setGeometry(QtCore.QRect(280, 129, 111, 31))
        self.label_36.setStyleSheet("border-radius:7px;\n"
"background-color: rgb(170, 170, 127);")
        self.label_36.setObjectName("label_36")
        self.combo_pageReportAComplaint_category_of_complaint = QtWidgets.QComboBox(self.pageReport_a_complaint)
        self.combo_pageReportAComplaint_category_of_complaint.setGeometry(QtCore.QRect(420, 130, 181, 31))
        self.combo_pageReportAComplaint_category_of_complaint.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"border-radius: 4px;\n"
"border: 2px solid black")
        self.combo_pageReportAComplaint_category_of_complaint.setObjectName("combo_pageReportAComplaint_category_of_complaint")
        self.combo_pageReportAComplaint_category_of_complaint.addItem("")
        self.combo_pageReportAComplaint_category_of_complaint.addItem("")
        self.combo_pageReportAComplaint_category_of_complaint.addItem("")
        self.combo_pageReportAComplaint_category_of_complaint.addItem("")
        self.combo_pageReportAComplaint_category_of_complaint.addItem("")
        self.combo_pageReportAComplaint_category_of_complaint.addItem("")
        self.combo_pageReportAComplaint_category_of_complaint.addItem("")
        self.combo_pageReportAComplaint_category_of_complaint.addItem("")
        self.combo_pageReportAComplaint_category_of_complaint.addItem("")
        self.label_37 = QtWidgets.QLabel(self.pageReport_a_complaint)
        self.label_37.setGeometry(QtCore.QRect(420, 180, 111, 31))
        self.label_37.setStyleSheet("border-radius:7px;\n"
"background-color: rgb(170, 170, 127);")
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.pageReport_a_complaint)
        self.label_38.setGeometry(QtCore.QRect(160, 20, 631, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("border-radius:7px;\n"
"background-color: rgb(170, 170, 127);")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.btn_pageReportAComplaint_backToHomepage = QtWidgets.QPushButton(self.pageReport_a_complaint)
        self.btn_pageReportAComplaint_backToHomepage.setGeometry(QtCore.QRect(190, 430, 111, 41))
        self.btn_pageReportAComplaint_backToHomepage.setStyleSheet("background-color:rgb(255, 32, 43);\n"
"border-radius:10px\n"
"")
        self.btn_pageReportAComplaint_backToHomepage.setObjectName("btn_pageReportAComplaint_backToHomepage")
        self.btn_pageReportAComplaint_submitComplaint = QtWidgets.QPushButton(self.pageReport_a_complaint)
        self.btn_pageReportAComplaint_submitComplaint.setGeometry(QtCore.QRect(570, 430, 171, 41))
        self.btn_pageReportAComplaint_submitComplaint.setStyleSheet("background-color:rgb(67, 203, 99);\n"
"border-radius:10px\n"
"")
        self.btn_pageReportAComplaint_submitComplaint.setObjectName("btn_pageReportAComplaint_submitComplaint")
        self.label_34.raise_()
        self.label_35.raise_()
        self.date_pageReport_a_complaint_date_of_incedence.raise_()
        self.label_36.raise_()
        self.combo_pageReportAComplaint_category_of_complaint.raise_()
        self.label_37.raise_()
        self.ted_pageReportAComplaint_describeComplaint.raise_()
        self.label_38.raise_()
        self.btn_pageReportAComplaint_backToHomepage.raise_()
        self.btn_pageReportAComplaint_submitComplaint.raise_()
        self.stackedWidget_2.addWidget(self.pageReport_a_complaint)
        self.label_19 = QtWidgets.QLabel(self.pageHomepage)
        self.label_19.setGeometry(QtCore.QRect(40, -20, 151, 521))
        self.label_19.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(0, 255, 0)")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_30 = QtWidgets.QLabel(self.pageHomepage)
        self.label_30.setGeometry(QtCore.QRect(70, 10, 91, 91))
        self.label_30.setStyleSheet("background-color: rgb(0, 255, 0)")
        self.label_30.setText("")
        self.label_30.setPixmap(QtGui.QPixmap("icons/user.png"))
        self.label_30.setScaledContents(True)
        self.label_30.setObjectName("label_30")
        self.lbl_pageHomepage_welcomeUser = QtWidgets.QLabel(self.pageHomepage)
        self.lbl_pageHomepage_welcomeUser.setGeometry(QtCore.QRect(40, 110, 151, 21))
        self.lbl_pageHomepage_welcomeUser.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: rgb(20, 20, 20);")
        self.lbl_pageHomepage_welcomeUser.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_pageHomepage_welcomeUser.setObjectName("lbl_pageHomepage_welcomeUser")
        self.btn_pageHomepage_payRent = QtWidgets.QPushButton(self.pageHomepage)
        self.btn_pageHomepage_payRent.setGeometry(QtCore.QRect(30, 180, 181, 61))
        self.btn_pageHomepage_payRent.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(0, 255, 0);\n"
"border-top: 3px solid rgb(81, 81, 81);\n"
"border-bottom: 2px solid rgb(81, 81, 81)")
        self.btn_pageHomepage_payRent.setObjectName("btn_pageHomepage_payRent")
        self.btn_pageHomepage_chat = QtWidgets.QPushButton(self.pageHomepage)
        self.btn_pageHomepage_chat.setGeometry(QtCore.QRect(30, 240, 181, 61))
        self.btn_pageHomepage_chat.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(0, 255, 0);\n"
"border-top: 2px solid rgb(81, 81, 81);\n"
"border-bottom: 2px solid rgb(81, 81, 81)")
        self.btn_pageHomepage_chat.setObjectName("btn_pageHomepage_chat")
        self.btn_pageHomepage_reportacomplaint = QtWidgets.QPushButton(self.pageHomepage)
        self.btn_pageHomepage_reportacomplaint.setGeometry(QtCore.QRect(30, 300, 181, 61))
        self.btn_pageHomepage_reportacomplaint.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(0, 255, 0);\n"
"border-top: 2px solid rgb(81, 81, 81);\n"
"border-bottom: 2px solid rgb(81, 81, 81)")
        self.btn_pageHomepage_reportacomplaint.setObjectName("btn_pageHomepage_reportacomplaint")
        self.btn_pageHomepage_checkAvailableProperties = QtWidgets.QPushButton(self.pageHomepage)
        self.btn_pageHomepage_checkAvailableProperties.setGeometry(QtCore.QRect(30, 360, 181, 61))
        self.btn_pageHomepage_checkAvailableProperties.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(0, 255, 0);\n"
"border-top: 2px solid rgb(81, 81, 81);\n"
"border-bottom: 3px solid rgb(81, 81, 81)")
        self.btn_pageHomepage_checkAvailableProperties.setObjectName("btn_pageHomepage_checkAvailableProperties")
        self.btn_pageHomepage_logout = QtWidgets.QPushButton(self.pageHomepage)
        self.btn_pageHomepage_logout.setGeometry(QtCore.QRect(60, 440, 101, 41))
        self.btn_pageHomepage_logout.setStyleSheet("background-color:rgb(255, 32, 43);\n"
"border-radius:10px\n"
"")
        self.btn_pageHomepage_logout.setObjectName("btn_pageHomepage_logout")
        self.label_19.raise_()
        self.label_30.raise_()
        self.lbl_pageHomepage_welcomeUser.raise_()
        self.btn_pageHomepage_payRent.raise_()
        self.btn_pageHomepage_chat.raise_()
        self.btn_pageHomepage_reportacomplaint.raise_()
        self.btn_pageHomepage_checkAvailableProperties.raise_()
        self.btn_pageHomepage_logout.raise_()
        self.stackedWidget_2.raise_()
        self.stackedWidget.addWidget(self.pageHomepage)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        self.signUP.setCurrentIndex(0)
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
        self.label_7.setText(_translate("Form", "SIGN UP"))
        self.lbl_pageSignUp_personalDetails.setText(_translate("Form", "Personal Details"))
        self.lbl_pageSignUp_nextofkin.setText(_translate("Form", "Next of kin"))
        self.label_8.setText(_translate("Form", "First Name *"))
        self.led_pageSignup_firstName.setPlaceholderText(_translate("Form", "John"))
        self.led_pageSignup_lastName.setPlaceholderText(_translate("Form", "Doe"))
        self.label_10.setText(_translate("Form", "Last Name *"))
        self.led_pageSignup_idNumber.setPlaceholderText(_translate("Form", "12345678"))
        self.label_9.setText(_translate("Form", "ID/Passport Number *"))
        self.led_pageSignup_emailAddress.setPlaceholderText(_translate("Form", "johndoe@abc.com"))
        self.label_11.setText(_translate("Form", "Email address *"))
        self.led_pageSignup_phoneNumber.setPlaceholderText(_translate("Form", "712345678"))
        self.label_12.setText(_translate("Form", "Phone Number *"))
        self.label_13.setText(_translate("Form", "+254"))
        self.label_14.setText(_translate("Form", "Occupation"))
        self.label_15.setText(_translate("Form", "Gender"))
        self.btn_pageSignup_personalDetailsNext.setText(_translate("Form", "NEXT"))
        self.led_pageSignup_occupation_2.setPlaceholderText(_translate("Form", "G11"))
        self.label_16.setText(_translate("Form", "House Number *"))
        self.led_pageSignup_occupation.setPlaceholderText(_translate("Form", "Accountant"))
        self.lbl_pageSignUp_nextofkin_2.setText(_translate("Form", "Next of kin"))
        self.label_18.setText(_translate("Form", "First Name *"))
        self.led_pageSignup_next_of_kinfirstName.setPlaceholderText(_translate("Form", "John"))
        self.label_20.setText(_translate("Form", "Last Name *"))
        self.led_pageSignup_next_of_kinLastName.setPlaceholderText(_translate("Form", "John"))
        self.label_25.setText(_translate("Form", "Email Address"))
        self.led_pageSignup_next_of_kinemailAddress.setPlaceholderText(_translate("Form", "mynextofkin@abc.com"))
        self.label_26.setText(_translate("Form", "Relationship"))
        self.led_pageSignup_next_of_kin_phoneNumber.setPlaceholderText(_translate("Form", "712345678"))
        self.label_27.setText(_translate("Form", "+254"))
        self.label_28.setText(_translate("Form", "Phone Number *"))
        self.combo_pageSignup_next_of_kin_relationship.setItemText(0, _translate("Form", "Father"))
        self.combo_pageSignup_next_of_kin_relationship.setItemText(1, _translate("Form", "Mother"))
        self.combo_pageSignup_next_of_kin_relationship.setItemText(2, _translate("Form", "Brother"))
        self.combo_pageSignup_next_of_kin_relationship.setItemText(3, _translate("Form", "Sister"))
        self.combo_pageSignup_next_of_kin_relationship.setItemText(4, _translate("Form", "Spouse"))
        self.combo_pageSignup_next_of_kin_relationship.setItemText(5, _translate("Form", "Child"))
        self.combo_pageSignup_next_of_kin_relationship.setItemText(6, _translate("Form", "Close relative"))
        self.btn_pageSignup_pageNexofKin_next.setText(_translate("Form", "Next"))
        self.led_pageSignup_next_of_kinAddress.setPlaceholderText(_translate("Form", "Donholm, Nairobi"))
        self.label_29.setText(_translate("Form", "Address"))
        self.btn_pageSignup_page_NextofKin_back.setText(_translate("Form", "Back"))
        self.label_21.setText(_translate("Form", "New Password"))
        self.btn_pageSignup_pagePassword_back.setText(_translate("Form", "Back"))
        self.lbl_pageSignUp_nextofkin_3.setText(_translate("Form", "Password"))
        self.btn_pageSignup_signUp.setText(_translate("Form", "Sign Up"))
        self.led_pageSignup_newPassword.setPlaceholderText(_translate("Form", "mypassword"))
        self.label_31.setText(_translate("Form", "Repeat Password"))
        self.led_pageSignup_repeatPassword.setPlaceholderText(_translate("Form", "mypassword"))
        self.btn_PageSignUp_BacktoLogin.setText(_translate("Form", "Back to Login Page"))
        self.lbl_pageSignUp_password.setText(_translate("Form", "Password"))
        self.lbl_pageForgotPassword_email.setText(_translate("Form", "Enter your Email Address"))
        self.btn_pageForgotPassword_continue.setText(_translate("Form", "Continue"))
        self.led_pageForgotPassword_Username.setPlaceholderText(_translate("Form", "   abc@ayz.com"))
        self.btn_pageForgotPassword_BacktoLogin.setText(_translate("Form", "Back to Login"))
        self.label_24.setText(_translate("Form", "RESET PASSWORD"))
        self.btn_pageForgotPassword_verifyCode.setText(_translate("Form", "Verify code"))
        self.lbl_pageForgotPassword_verificationcode.setText(_translate("Form", "Enter verification code"))
        self.btn_pageForgotPassword_updatePassword.setText(_translate("Form", "Update Password"))
        self.label_32.setText(_translate("Form", "RENT DETAILS\n"
"Days Remaining: 24\n"
"Rent Arreas: KSH2400"))
        self.lbl_pageHomepage_welcomeUser_2.setText(_translate("Form", "Welcome user"))
        self.btn_pageChat_send.setText(_translate("Form", "SEND"))
        self.btn_pageChat_chatWithManager.setText(_translate("Form", "Chat with Manager"))
        self.btn_pageChat_chatWithOwner.setText(_translate("Form", "Chat with Owner"))
        self.label_35.setText(_translate("Form", "Date of incidence"))
        self.label_36.setText(_translate("Form", "Category of complaint"))
        self.combo_pageReportAComplaint_category_of_complaint.setItemText(0, _translate("Form", "Noise"))
        self.combo_pageReportAComplaint_category_of_complaint.setItemText(1, _translate("Form", "Payments"))
        self.combo_pageReportAComplaint_category_of_complaint.setItemText(2, _translate("Form", "Maintenance and Repairs"))
        self.combo_pageReportAComplaint_category_of_complaint.setItemText(3, _translate("Form", "House Hygene"))
        self.combo_pageReportAComplaint_category_of_complaint.setItemText(4, _translate("Form", "Water"))
        self.combo_pageReportAComplaint_category_of_complaint.setItemText(5, _translate("Form", "Electricity"))
        self.combo_pageReportAComplaint_category_of_complaint.setItemText(6, _translate("Form", "Other tenants/Neighbours"))
        self.combo_pageReportAComplaint_category_of_complaint.setItemText(7, _translate("Form", "House Management"))
        self.combo_pageReportAComplaint_category_of_complaint.setItemText(8, _translate("Form", "Other"))
        self.label_37.setText(_translate("Form", "Describe Complaint"))
        self.label_38.setText(_translate("Form", "REPORT A COMPLAINT"))
        self.btn_pageReportAComplaint_backToHomepage.setText(_translate("Form", "Back to homepage"))
        self.btn_pageReportAComplaint_submitComplaint.setText(_translate("Form", "SUBMIT COMPLAINT"))
        self.lbl_pageHomepage_welcomeUser.setText(_translate("Form", "Welcome user"))
        self.btn_pageHomepage_payRent.setText(_translate("Form", "Pay Rent"))
        self.btn_pageHomepage_chat.setText(_translate("Form", "Chat"))
        self.btn_pageHomepage_reportacomplaint.setText(_translate("Form", "Report a complaint"))
        self.btn_pageHomepage_checkAvailableProperties.setText(_translate("Form", "Check available properties"))
        self.btn_pageHomepage_logout.setText(_translate("Form", "LOGOUT"))

        # Mambo yangu

        # from PyQt5 import QtCore, QtGui, QtWidgets
        # import mysql.connector
        # import random
        # import smtplib
        # import re

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

        # self.btn_pageSignup_personalDetailsNext.clicked.connect(self.next_signup_page)
        self.btn_pageSignup_pageNexofKin_next.clicked.connect(self.btn_pageSignup_pageNexofKin_next_clicked)
        self.btn_pageSignup_pagePassword_back.clicked.connect(self.btn_pageSignup_pagePassword_back_clicked)
        self.btn_pageSignup_page_NextofKin_back.clicked.connect(self.btn_pageSignup_page_NextofKin_back_clicked)

        self.btn_pageHomepage_chat.clicked.connect(self.btn_pageHomepage_chat_clicked)
        self.btn_pageHomepage_reportacomplaint.clicked.connect(self.btn_pageHomepage_reportacomplaint_clicked)
        self.btn_pageReportAComplaint_backToHomepage.clicked.connect(
                self.btn_pageReportAComplaint_backToHomepage_clicked)

        # Registration

        self.edited_FirstName_signup = False
        self.edited_LastName_signup = False
        self.edited_email_signup = False
        self.edited_idNumber_signup = False
        self.edited_phoneNumber_signup = False
        self.edited_houseNumber_signup = False
        self.edited_NOK_FirstName_signup = False
        self.edited_NOK_LastName_signup = False
        self.edited_NOK_email_signup = False
        self.edited_NOK_phoneNumber_signup = False

        self.led_pageSignup_firstName.editingFinished.connect(self.led_pageSignup_firstName_edit)
        self.led_pageSignup_lastName.editingFinished.connect(self.led_pageSignup_lastName_edit)
        self.led_pageSignup_idNumber.editingFinished.connect(self.led_pageSignup_idNumber_edit)
        self.led_pageSignup_phoneNumber.editingFinished.connect(self.led_pageSignup_phoneNumber_edit)
        self.led_pageSignup_emailAddress.editingFinished.connect(self.led_pageSignup_emailAddress_edit)
        self.led_pageSignup_occupation_2.editingFinished.connect(self.led_pageSignup_occupation_2_edit)
        self.btn_pageSignup_personalDetailsNext.clicked.connect(self.btn_pageSignup_personalDetailsNext_clicked)
        self.led_pageSignup_next_of_kinfirstName.editingFinished.connect(self.led_pageSignup_next_of_kinfirstName_edit)
        self.led_pageSignup_next_of_kinLastName.editingFinished.connect(self.led_pageSignup_next_of_kinLastName_edit)
        self.led_pageSignup_next_of_kinemailAddress.editingFinished.connect(
                self.led_pageSignup_next_of_kinemailAddress_edit)
        self.led_pageSignup_next_of_kin_phoneNumber.editingFinished.connect(
                self.led_pageSignup_next_of_kin_phoneNumber_edit)
        self.btn_pageSignup_signUp.clicked.connect(self.btn_pageSignup_signUp_clicked)
        self.led_pageSignup_newPassword.editingFinished.connect(self.led_pageSignup_newPassword_edit)
        self.led_pageSignup_repeatPassword.editingFinished.connect(self.led_pageSignup_repeatPassword_edit)

    def led_pageSignup_repeatPassword_edit(self):
        password_strength = self.is_strong_password(self.led_pageSignup_repeatPassword.text())

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.lbl_pagePassword_RepeatPasswordNotification.setFont(font)

        if (self.led_pageSignup_repeatPassword.text() == self.led_pageSignup_newPassword.text()):
            if password_strength is True:
                self.led_pageSignup_repeatPassword.setStyleSheet("border: 2px solid rgb(0, 136, 0);"
                                                              "border-radius: 10px;")
                self.lbl_pagePassword_RepeatPasswordNotification.setText("")
        else:
             self.lbl_pagePassword_RepeatPasswordNotification.setText("Password don't match")

    def btn_pageSignup_signUp_clicked(self):
        password_strength = self.is_strong_password(self.led_pageSignup_newPassword.text())

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)

        self.lbl_pagePassword_NewpasswordNotification.setFont(font)

        if password_strength is True:
            self.lbl_pageSignup_Fillall_Password_Notification.setText("")
            self.signup_password = self.led_pageSignup_newPassword.text()

            try:
                self.mycursor.execute(f"INSERT INTO apartment_name.details"
                                  f"(id_number, first_name, last_name, phone_number, email_address, "
                                  f"house_number, gender, occupation,next_of_kin_first_name, next_of_kin_last_name,"
                                  f" next_of_kin_phone_number, next_of_kin_email_address,next_of_kin_relationship, "
                                  f"next_of_kin_address, date_registered) VALUES('{self.signup_idNumber}', '{self.signup_firstName}', "
                                  f"'{self.signup_lastName}', '{self.signup_phoneNumber}', '{self.signup_emailAddress}', "
                                  f"'{self.signup_housenumber}', '{self.signup_gender}', '{self.signup_occupation}', "
                                  f"'{self.signup_NOK_firstName}', '{self.signup_NOK_lastName}', "
                                  f"'{self.signup_NOK_phoneNumber}', '{self.signup_NOK_emailAddress}', "
                                  f"'{self.signup_relationsip_NOK}', '{self.signup_address_NOK}', "
                                  f"'{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');")
                self.db.commit()

                self.mycursor.execute(f"INSERT INTO apartment_name.tenants_logins(id_number, house_number, phone_number,email_address, "
                                      f"user_password) VALUES ('{self.signup_idNumber}', '{self.signup_housenumber}', "
                                      f"'{self.signup_phoneNumber}', '{self.signup_emailAddress}' , "
                                      f"'{self.signup_password}');")
                self.db.commit()
                warning = QMessageBox()
                warning.setWindowTitle("ACCOUNT CREATED SUCCESSFULLY")
                warning.setIcon(QMessageBox.Information)
                warning.setText("Your account was created successfully. \nPlease Login to use your account")
                x = warning.exec_()

                self.signUP.setCurrentWidget(self.pageSignUpPersonalDetails)
                self.to_pageLogin()
            except:
                warning = QMessageBox()
                warning.setWindowTitle("WARNING")
                warning.setIcon(QMessageBox.Critical)
                warning.setText("An error prevented your account from being created")
                x = warning.exec_()
                self.signUP.setCurrentWidget(self.pageSignUpPersonalDetails)

        else:
            self.lbl_pageSignup_Fillall_Password_Notification.setText("Password doesn't meet requirments")
            self.lbl_pageSignup_Fillall_Password_Notification.adjustSize()

    def led_pageSignup_newPassword_edit(self):
        self.lbl_pagePassword_NewpasswordNotification.setStyleSheet("color: rgb(229, 6, 28);")

        password_strength = self.is_strong_password(self.led_pageSignup_newPassword.text())

        if password_strength is True:
            self.led_pageSignup_newPassword.setStyleSheet("border: 2px solid rgb(0, 136, 0);"
                                                          "border-radius: 10px;")
            self.lbl_pagePassword_NewpasswordNotification.setText("")

        else:

            font = QtGui.QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(8)

            self.lbl_pagePassword_NewpasswordNotification.setFont(font)
            self.lbl_pagePassword_NewpasswordNotification.setStyleSheet("color: rgb(229, 6, 28);")

            self.led_pageSignup_newPassword.setStyleSheet("border: 2px solid rgb(213, 5, 15);"
                                                          "border-radius: 10px;")
            self.lbl_pagePassword_NewpasswordNotification.setText(password_strength)
            self.lbl_pagePassword_NewpasswordNotification.adjustSize()




    def is_strong_password(self, password):
        if len(password) < 8:
            return "Password is short"

        # Password must contain at least one lowercase letter
        if not re.search(r"[a-z]", password):
            return "Password must contain at least one lowercase letter"

        # Password must contain at least one uppercase letter
        if not re.search(r"[A-Z]", password):
            return "Password must contain at least one uppercase letter"

        if not re.search(r"\d", password):
            return "Password must contain at least one digit"

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return "Password must contain at least one special character"

        return True

    def led_pageSignup_next_of_kin_phoneNumber_edit(self):
            edited_text = self.led_pageSignup_next_of_kin_phoneNumber.text()

            if edited_text != "":
                    try:
                            for i in edited_text:
                                    int(i)

                            if len(edited_text) == 9:
                                    self.edited_NOK_phoneNumber_signup = True
                                    self.led_pageSignup_next_of_kin_phoneNumber.setStyleSheet(
                                            "border:2px solid rgb(203, 203, 203);;"
                                            "border-bottom: 2px solid rgb(0, 136, 0)")
                                    self.lbl_pageSignup_NextofKin_PhoneNumberNotification.setText("")

                                    self.signup_NOK_phoneNumber = "254"+edited_text

                            else:
                                    self.led_pageSignup_next_of_kin_phoneNumber.setStyleSheet(
                                            "border:2px solid rgb(203, 203, 203);;"
                                            "border-bottom: 2px solid rgb(255, 7, 11)")
                                    self.lbl_pageSignup_NextofKin_PhoneNumberNotification.setText(
                                            "Number of digits is more/less than expected!")

                                    self.edited_NOK_phoneNumber_signup = False

                    except:
                            self.led_pageSignup_next_of_kin_phoneNumber.setStyleSheet(
                                    "border:2px solid rgb(203, 203, 203);;"
                                    "border-bottom: 2px solid rgb(255, 7, 11)")
                            self.lbl_pageSignup_NextofKin_PhoneNumberNotification.setText(
                                    "Field should contain digits only")
                            self.edited_NOK_phoneNumber_signup = False


            else:
                    self.led_pageSignup_next_of_kin_phoneNumber.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                                              "border-bottom: 2px solid rgb(255, 7, 11)")
                    self.lbl_pageSignup_NextofKin_PhoneNumberNotification.setText("Phone number cannot be blank!")
                    self.edited_NOK_phoneNumber_signup = False

    def led_pageSignup_next_of_kinemailAddress_edit(self):
            edited_text = self.led_pageSignup_next_of_kinemailAddress.text().strip().lower()
            valid_mail = self.is_valid_email(edited_text)

            if valid_mail is True:
                self.edited_NOK_email_signup = True
                self.led_pageSignup_next_of_kinemailAddress.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                                              "border-bottom: 2px solid rgb(0, 136, 0)")

                self.signup_NOK_emailAddress = edited_text

            else:
                self.led_pageSignup_next_of_kinemailAddress.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                                              "border-bottom: 2px solid rgb(255, 7, 11)")
                self.edited_NOK_email_signup = False
                self.signup_NOK_emailAddress = "NOT STATED"

    def led_pageSignup_next_of_kinfirstName_edit(self):
            edited_text = self.led_pageSignup_next_of_kinfirstName.text().strip()

            if edited_text != "":
                    self.edited_NOK_FirstName_signup = True
                    self.led_pageSignup_next_of_kinfirstName.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                                           "border-bottom: 2px solid rgb(0, 136, 0)")
                    self.lbl_pageSignup_NextOfKin_FirstNameNotification.setText("")

                    self.signup_NOK_firstName = edited_text

            else:
                    self.led_pageSignup_next_of_kinfirstName.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                                           "border-bottom: 2px solid rgb(255, 7, 11)")
                    self.lbl_pageSignup_NextOfKin_FirstNameNotification.setText("First name cannot be blank!")
                    self.edited_NOK_FirstName_signup = False

    def led_pageSignup_next_of_kinLastName_edit(self):
            edited_text = self.led_pageSignup_next_of_kinLastName.text().strip()

            if edited_text != "":
                    self.edited_NOK_LastName_signup = True
                    self.led_pageSignup_next_of_kinLastName.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                                          "border-bottom: 2px solid rgb(0, 136, 0)")
                    self.lbl_pageSignup_nextfKin_LastNameNotification.setText("")

                    self.signup_NOK_lastName = edited_text

            else:
                    self.led_pageSignup_next_of_kinLastName.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                                          "border-bottom: 2px solid rgb(255, 7, 11)")
                    self.lbl_pageSignup_nextfKin_LastNameNotification.setText("First name cannot be blank!")
                    self.edited_NOK_LastName_signup = False

    def led_pageSignup_firstName_edit(self):
            edited_text = self.led_pageSignup_firstName.text().strip()

            if edited_text != "":
                    self.edited_FirstName_signup = True
                    self.led_pageSignup_firstName.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                                "border-bottom: 2px solid rgb(0, 136, 0)")
                    self.lbl_pageSignup_FirstNameNotification.setText("")

                    self.signup_firstName = edited_text

            else:
                    self.led_pageSignup_firstName.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                                "border-bottom: 2px solid rgb(255, 7, 11)")
                    self.lbl_pageSignup_FirstNameNotification.setText("First name cannot be blank!")
                    self.edited_FirstName_signup = False

    def led_pageSignup_lastName_edit(self):
            edited_text = self.led_pageSignup_lastName.text().strip()

            if edited_text != "":
                    self.edited_LastName_signup = True
                    self.led_pageSignup_lastName.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                               "border-bottom: 2px solid rgb(0, 136, 0)")
                    self.lbl_pageSignup_lastNameNotification.setText("")
                    self.signup_lastName = edited_text


            else:
                    self.led_pageSignup_lastName.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                               "border-bottom: 2px solid rgb(255, 7, 11)")
                    self.lbl_pageSignup_lastNameNotification.setText("Last name cannot be blank!")
                    self.edited_LastName_signup = False

    def led_pageSignup_idNumber_edit(self):
            edited_text = self.led_pageSignup_idNumber.text()

            if edited_text != "":
                    try:
                            for i in edited_text:
                                    int(i)

                            if len(edited_text) >= 8 and len(edited_text) <= 9:
                                    self.edited_idNumber_signup = True
                                    self.led_pageSignup_idNumber.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                                               "border-bottom: 2px solid rgb(0, 136, 0)")
                                    self.lbl_pageSignup_IDNumberNotification.setText("")

                                    self.signup_idNumber = edited_text

                            else:
                                    self.led_pageSignup_idNumber.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                                               "border-bottom: 2px solid rgb(255, 7, 11)")
                                    self.lbl_pageSignup_IDNumberNotification.setText(
                                            "Number of digits is more/less than expected!")

                                    self.edited_idNumber_signup = False

                    except:
                            self.led_pageSignup_idNumber.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                                       "border-bottom: 2px solid rgb(255, 7, 11)")
                            self.lbl_pageSignup_IDNumberNotification.setText("Field should contain digits only")
                            self.edited_idNumber_signup = False


            else:
                    self.led_pageSignup_idNumber.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                               "border-bottom: 2px solid rgb(255, 7, 11)")
                    self.lbl_pageSignup_IDNumberNotification.setText("ID/Passport number cannot be blank!")
                    self.edited_idNumber_signup = False

    def led_pageSignup_phoneNumber_edit(self):
            edited_text = self.led_pageSignup_phoneNumber.text()

            if edited_text != "":
                    try:
                            for i in edited_text:
                                    int(i)

                            if len(edited_text) == 9:
                                    self.edited_phoneNumber_signup = True
                                    self.led_pageSignup_phoneNumber.setStyleSheet(
                                            "border:2px solid rgb(203, 203, 203);;"
                                            "border-bottom: 2px solid rgb(0, 136, 0)")
                                    self.lbl_pageSignup_phoneNumberNotification.setText("")

                                    self.signup_phoneNumber = "254"+edited_text

                            else:
                                    self.led_pageSignup_phoneNumber.setStyleSheet(
                                            "border:2px solid rgb(203, 203, 203);;"
                                            "border-bottom: 2px solid rgb(255, 7, 11)")
                                    self.lbl_pageSignup_phoneNumberNotification.setText(
                                            "Number of digits is more/less than expected!")

                                    self.edited_phoneNumber_signup = False

                    except:
                            self.led_pageSignup_phoneNumber.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                                          "border-bottom: 2px solid rgb(255, 7, 11)")
                            self.lbl_pageSignup_phoneNumberNotification.setText("Field should contain digits only")
                            self.edited_phoneNumber_signup = False


            else:
                    self.led_pageSignup_phoneNumber.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                                  "border-bottom: 2px solid rgb(255, 7, 11)")
                    self.lbl_pageSignup_phoneNumberNotification.setText("Phone number cannot be blank!")
                    self.edited_phoneNumber_signup = False

    def is_valid_email(self, email_to_validate):
            if not email_to_validate:
                    return False

            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

            if re.match(pattern, email_to_validate):
                    return True
            else:
                    return False

    def led_pageSignup_emailAddress_edit(self):
            edited_text = self.led_pageSignup_emailAddress.text().strip().lower()
            valid_mail = self.is_valid_email(edited_text)

            if valid_mail is True:
                    self.edited_email_signup = True
                    self.led_pageSignup_emailAddress.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                                   "border-bottom: 2px solid rgb(0, 136, 0)")
                    self.lbl_pageSignup_emailNotification.setText("")

                    self.signup_emailAddress = edited_text

            else:
                    self.led_pageSignup_emailAddress.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                                   "border-bottom: 2px solid rgb(255, 7, 11)")
                    self.lbl_pageSignup_emailNotification.setText("Email address is invalid!")

                    self.edited_email_signup = False

    def led_pageSignup_occupation_2_edit(self):
            edited_text = self.led_pageSignup_occupation_2.text().strip()

            if edited_text != "":
                    self.edited_houseNumber_signup = True
                    self.led_pageSignup_occupation_2.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                                   "border-bottom: 2px solid rgb(0, 136, 0)")
                    self.lbl_pageSignup_houseNumberNotification.setText("")
                    self.signup_housenumber = edited_text


            else:
                    self.led_pageSignup_occupation_2.setStyleSheet("border:2px solid rgb(203, 203, 203);;"
                                                                   "border-bottom: 2px solid rgb(255, 7, 11)")
                    self.lbl_pageSignup_houseNumberNotification.setText("House Number cannot be blank!")
                    self.edited_houseNumber_signup = False


    def btn_pageSignup_personalDetailsNext_clicked(self):
            self.signup_occupation = self.led_pageSignup_occupation.text()

            warning = QMessageBox()
            warning.setWindowTitle("WARNING")
            warning.setIcon(QMessageBox.Critical)
            if self.signup_occupation == "":
                self.signup_occupation = "NOT STATED"

            if self.rbn_pageSignUp_male.isChecked():
                    self.signup_gender = "Male"
            if self.rbn_pageSignUp_female.isChecked():
                    self.signup_gender = "Female"

            if (self.edited_FirstName_signup is True) and (self.edited_LastName_signup is True) and \
                    (self.edited_idNumber_signup is True) and (self.edited_email_signup is True) and \
                    (self.edited_houseNumber_signup is True) and (self.edited_phoneNumber_signup is True):

                    self.mycursor.execute(f"SELECT COUNT(*) FROM apartment_name.details "
                                          f"WHERE id_number = '{self.signup_idNumber}'")
                    result = self.mycursor.fetchone()[0]

                    if result > 0:

                        warning.setText("ID Number entered is already linked to an account!")
                        x = warning.exec_()

                    else:
                        self.mycursor.execute(f"SELECT COUNT(*) FROM apartment_name.details "
                                                  f"WHERE email_address = '{self.signup_emailAddress}'")
                        result = self.mycursor.fetchone()[0]
                        if result > 0:
                                warning.setText("Email Address entered is already linked to an account!")
                                x = warning.exec_()
                        else:
                            self.mycursor.execute(f"SELECT COUNT(*) FROM apartment_name.details "
                                                  f"WHERE phone_number = '254{self.signup_phoneNumber}'")
                            result = self.mycursor.fetchone()[0]
                            if result > 0:
                                warning.setText("Phone Number entered is already linked to an account!")
                                x = warning.exec_()
                            else:
                                self.mycursor.execute(f"SELECT COUNT(*) FROM apartment_name.details "
                                                          f"WHERE house_number = '{self.signup_housenumber}'")
                                result = self.mycursor.fetchone()[0]
                                if result > 0:
                                    warning.setText("House Number entered is already linked to an account!")
                                    x = warning.exec_()
                                else:
                                    self.next_signup_page()
                                    self.lbl_pageSignup_FillallNotification.setText("")

            else:
                warning.setText("Enter all required fields with * appropriately")
                x = warning.exec_()
                self.lbl_pageSignup_FillallNotification.setText("Enter all required fields with *")
                self.lbl_pageSignup_FillallNotification.adjustSize()

    def to_pageLogin(self):
            self.stackedWidget.setCurrentWidget(self.PageLogin)
            self.stackedWidget_2.setCurrentWidget(self.pageRealHomepage)

    def to_pageSignup(self):
            self.stackedWidget.setCurrentWidget(self.pageSignUp)

    def to_pageForgotpassword(self):
            self.stackedWidget.setCurrentWidget(self.pageForgotPassword)

    def to_pageHomepage(self):
            self.stackedWidget.setCurrentWidget(self.pageHomepage)

    def get_password(self, user):
            try:
                    self.mycursor.execute(
                            f"SELECT user_password FROM apartment_name.tenants_logins WHERE id_number = {user};")
                    password = self.mycursor.fetchall()[0][0]
                    self.session_user_id = user
                    return password
            except:
                    try:
                            self.mycursor.execute(
                                    f"SELECT user_password FROM apartment_name.tenants_logins WHERE house_number = '{user}';")
                            password = self.mycursor.fetchall()[0][0]

                            self.mycursor.execute(
                                    f"SELECT id_number FROM apartment_name.tenants_logins WHERE house_number = '{user}';")
                            self.session_user_id = self.mycursor.fetchall()[0][0]

                            return password
                    except:
                            try:
                                    self.mycursor.execute(
                                            f"SELECT user_password FROM apartment_name.tenants_logins WHERE phone_number = {user};")
                                    password = self.mycursor.fetchall()[0][0]

                                    self.mycursor.execute(
                                            f"SELECT id_number FROM apartment_name.tenants_logins WHERE phone_number = {user};")
                                    self.session_user_id = self.mycursor.fetchall()[0][0]

                                    return password
                            except:
                                    try:
                                            self.mycursor.execute(
                                                    f"SELECT user_password FROM apartment_name.tenants_logins WHERE email_address = '{user}';")

                                            password = self.mycursor.fetchall()[0][0]

                                            self.mycursor.execute(
                                                    f"SELECT id_number FROM apartment_name.tenants_logins WHERE email_address = '{user}';")

                                            self.session_user_id = self.mycursor.fetchall()[0][0]

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

                    self.mycursor.execute(
                            f"SELECT first_name FROM apartment_name.details WHERE id_number = '{self.session_user_id}';")

                    self.session_user_firstName = self.mycursor.fetchall()[0][0]

                    self.lbl_pageHomepage_welcomeUser.setText(f"Welcome {self.session_user_firstName}")
                    self.lbl_pageHomepage_welcomeUser_2.setText(f"Welcome {self.session_user_firstName}")

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
                            self.lbl_pageForgotPassword_emailNotification.setText(
                                    "Verification code has been sent to your email")
                            self.lbl_pageForgotPassword_emailNotification.setStyleSheet("color: rgb(56, 255, 12);"
                                                                                        "background-color: rgb(61, 61, 61);")

                            try:
                                    self.led_pageForgotPassword_Username.setStyleSheet(
                                            "background-color: rgb(61, 61, 61);"
                                            "color: rgb(255, 255, 255);"
                                            "border: 2px solid rgb(100, 197, 26);"
                                            "border-radius:5px;")
                                    self.verification_code = self.get_otp()
                                    self.mycursor.execute(f"SELECT first_name FROM apartment_name.details "
                                                          f"WHERE email_address = '{self.resetpass_send_email_address}';")
                                    self.resetpass_first_name = str(self.mycursor.fetchall()[0][0])
                                    self.sendmail(self.resetpass_send_email_address, self.resetpass_first_name,
                                                  self.verification_code)
                                    self.btn_pageForgotPassword_continue.hide()
                                    self.lbl_pageForgotPassword_verificationcode.show()
                                    self.led_pageForgotPassword_verificationCode.show()
                                    self.btn_pageForgotPassword_verifyCode.show()
                                    self.lbl_pageForgotPassword_verificationcode.setText("Enter Verification Code")
                            except:
                                    self.lbl_pageForgotPassword_emailNotification.setText(
                                            "There was an error sending verification code."
                                            "Please check your internet.")

                                    self.lbl_pageForgotPassword_emailNotification.setStyleSheet(
                                            "color: rgb(255, 44, 7);"
                                            "background-color: rgb(61, 61, 61);")

                    else:
                            self.lbl_pageForgotPassword_emailNotification.setText(
                                    "Email address is not linked to any account")
                            self.lbl_pageForgotPassword_emailNotification.setStyleSheet("color: rgb(255, 44, 7);"
                                                                                        "background-color: rgb(61, 61, 61);")

            except:
                    self.lbl_pageForgotPassword_emailNotification.setText(
                            "An error occurred! Please restart the application")
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

                    self.lbl_pageForgotPassword_emailNotification.setText(
                            "Password length should be greater than 8 characters")
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

                            self.mycursor.execute(
                                    f"UPDATE apartment_name.tenants_logins SET user_password = '{new_password}' "
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
                            self.lbl_pageForgotPassword_verificationNotification.setText(
                                    "Password changed successfully!")

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

    def next_signup_page(self):
            self.signUP.setCurrentWidget(self.pageNextOfKin)
            self.lbl_pageSignUp_nextofkin.setStyleSheet("background-color: rgb(203, 203, 203);"
                                                        "border: 2px solid rgb(59, 59, 59);"
                                                        "border-left:6px solid rgb(255, 6, 18);")
            self.lbl_pageSignUp_personalDetails.setStyleSheet("background-color: rgb(203, 203, 203);"
                                                              "border: 2px solid rgb(59, 59, 59);"
                                                              "border-radius:5px")

    def btn_pageSignup_pageNexofKin_next_clicked(self):
        if (self.edited_NOK_FirstName_signup is True) and \
                (self.edited_NOK_LastName_signup is True) and (self.edited_NOK_phoneNumber_signup is True):
            self.signUP.setCurrentWidget(self.pagePassword)
            self.lbl_pageSignUp_password.setStyleSheet("background-color: rgb(203, 203, 203);"
                                                       "border: 2px solid rgb(59, 59, 59);"
                                                       "border-left:6px solid rgb(255, 6, 18);")
            self.lbl_pageSignUp_nextofkin.setStyleSheet("background-color: rgb(203, 203, 203);"
                                                        "border: 2px solid rgb(59, 59, 59);"
                                                        "border-radius:5px")

            self.lbl_pageSignup_Fillall_NOK_Notification.setText("")

        else:
            warning = QMessageBox()
            warning.setWindowTitle("WARNING")
            warning.setIcon(QMessageBox.Critical)
            warning.setText("Enter all required fields with *")
            x = warning.exec_()
            self.lbl_pageSignup_Fillall_NOK_Notification.setText("Enter all required fields with *")

        self.signup_relationsip_NOK = self.combo_pageSignup_next_of_kin_relationship.currentText()
        self.signup_address_NOK = self.led_pageSignup_next_of_kinAddress.text()
        if self.signup_address_NOK == "":
            self.signup_address_NOK = "NOT STATED"


    def btn_pageSignup_pagePassword_back_clicked(self):
            self.signUP.setCurrentWidget(self.pageNextOfKin)
            self.lbl_pageSignUp_nextofkin.setStyleSheet("background-color: rgb(203, 203, 203);"
                                                        "border: 2px solid rgb(59, 59, 59);"
                                                        "border-left:6px solid rgb(255, 6, 18);")
            self.lbl_pageSignUp_password.setStyleSheet("background-color: rgb(203, 203, 203);"
                                                       "border: 2px solid rgb(59, 59, 59);"
                                                       "border-radius:5px")

    def btn_pageSignup_page_NextofKin_back_clicked(self):
            self.signUP.setCurrentWidget(self.pageSignUpPersonalDetails)
            self.lbl_pageSignUp_personalDetails.setStyleSheet("background-color: rgb(203, 203, 203);"
                                                              "border: 2px solid rgb(59, 59, 59);"
                                                              "border-left:6px solid rgb(255, 6, 18);")
            self.lbl_pageSignUp_nextofkin.setStyleSheet("background-color: rgb(203, 203, 203);"
                                                        "border: 2px solid rgb(59, 59, 59);"
                                                        "border-radius:5px")

    def btn_pageHomepage_chat_clicked(self):
            self.stackedWidget_2.setCurrentWidget(self.pageChat)

    def btn_pageHomepage_reportacomplaint_clicked(self):
            self.stackedWidget_2.setCurrentWidget(self.pageReport_a_complaint)

    def btn_pageReportAComplaint_backToHomepage_clicked(self):
            self.stackedWidget_2.setCurrentWidget(self.pageRealHomepage)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
