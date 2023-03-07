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

