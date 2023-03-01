if self.password != "None":
    return self.password
else:
    self.mycursor.execute(f"SELECT user_password FROM apartment_name.tenants_logins WHERE house_number = {user};")
    try:
        self.password = self.mycursor.fetchall()[0][0]
        return self.password
    except:
        self.password = "None"

if self.password != "None":
    return self.password
else:
    self.mycursor.execute(f"SELECT user_password FROM apartment_name.tenants_logins WHERE phone_number = {user};")
    try:
        self.password = self.mycursor.fetchall()[0][0]
        return self.password
    except:
        self.password = "None"

if self.password != "None":
    return self.password
else:
    self.mycursor.execute(f"SELECT user_password FROM apartment_name.tenants_logins WHERE email_address = {user};")
    try:
        self.password = self.mycursor.fetchall()[0][0]
        return self.password
    except:
        self.password = "None"
        return self.password
