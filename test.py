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


def authentic_username(self, username):
    autenticity = self.get_password(username)
    if autenticity == "None":
        return False
    else:
        return True


def led_uthentic_username(self):
    is_username_authentic = self.authentic_username(self.led_LoginPage_Username.text())
    self.led_LoginPage_Username.setStyleSheet(

    )


def loginpage_btnlogin(self):
    self.username = self.led_LoginPage_Username.text()
    print(self.username)
    self.entered_password = self.led_LoginPage_Password.text()

    self.user_password = self.get_password(self.username)

    if self.user_password == self.entered_password:
        self.to_pageHomepage()

    else:
        print("User does not exist!")