# Mambo yangu

from random import randint

# db = mysql.connector.connect(
#     user="root",
#     host="localhost",
#     password="root"
# )
#
# def __init__(self):
#     self.mycursor = db.cursor()

self.led_LoginPage_Password.setEchoMode(QtWidgets.QLineEdit.Password)

self.btn_LoginPage_Login.clicked.connect(lambda: self.loginpage_btnlogin())
self.btn_LoginPage_SignUp.clicked.connect(lambda: self.to_pageSignup())
self.btn_LoginPage_ForgotPassword.clicked.connect(lambda: self.to_pageForgotpassword())
self.btn_pageHomepage_logout.clicked.connect(lambda: self.to_pageLogin())
self.btn_pageForgotPassword_BacktoLogin.clicked.connect(lambda: self.to_pageLogin())
self.btn_PageSignUp_BacktoLogin.clicked.connect(lambda: self.to_pageLogin())
self.led_LoginPage_Username.editingFinished.connect(self.led_authentic_username)
self.led_PageForgotPPassword_Username.editingFinished.connect(self.led_authentic_username_forgotpassword)


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
            password = self.mycursor.fetchall()[0][0]
            return password
        except:
            try:
                self.mycursor.execute(
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