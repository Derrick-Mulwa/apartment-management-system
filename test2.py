import mysql.connector

mycursor.execute(
                            f"SELECT user_password FROM apartment_name.tenants_logins WHERE email_address = '{user}';")

                        password = self.mycursor.fetchall()[0][0]
                        return password