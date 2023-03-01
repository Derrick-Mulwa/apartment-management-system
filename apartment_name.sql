DROP DATABASE IF EXISTS apartment_name;
CREATE DATABASE apartment_name;
USE apartment_name;
CREATE TABLE details(
id_number INT PRIMARY KEY,
first_name VARCHAR(100),
last_name VARCHAR(100),
phone_number VARCHAR(20),
email_address VARCHAR(150),
house_number VARCHAR(100),
occupation VARCHAR(100),
next_of_kin_first_name VARCHAR(100),
next_of_kin_last_name VARCHAR(100),
user_role VARCHAR(100),
photo LONGBLOB);

CREATE TABLE tenants_logins(
id_number INT PRIMARY KEY,
house_number VARCHAR(100),
phone_number VARCHAR(20),
email_address VARCHAR(100),
user_password VARCHAR(50));

CREATE TABLE rent_payments(
payment_id INT PRIMARY KEY AUTO_INCREMENT,
id_number INT,
amount DECIMAL(9, 2),
payment_date DATETIME,
transaction_cobe VARCHAR(100),
authorized_by VARCHAR(100));

INSERT INTO apartment_name.details(id_number, first_name, last_name, phone_number, email_address, house_number, occupation,
next_of_kin_first_name, next_of_kin_last_name, user_role) VALUES
(11217220, "Derrick", "Mkali", 254799368479, "anemail@gmail.com", "B16", "Student", "Kendrick", "Mulamwa", "Tenant"),
(32711242, "Angela", "Nyaboke", 254712348479, "angela19200@gmail.com", "A11", "Accountant", "Louis", "Cia", "Tenant"),
(47554865, "Ian", "Pweza", 254748556412, "ianfala1213@gmail.com", "J9", "Watchman", "Keovin", "Musyo", "Tenant"),
(24568121, "Ken", "Walibora", 254736951362, "kenwalibora@gmail.com", "M45", "Plumber", "Miss", "Wake", "Manager");

INSERT INTO tenants_logins(id_number,house_number,phone_number, email_address, user_password) VALUES
(11217220, "B16", 254799368479, "anemail@gmail.com", "Deriky1"),
(32711242, "A11", 254712348479, "angela19200@gmail.com", "Wowman"),
(47554865, "J9",  254748556412, "ianfala1213@gmail.com", "Tenant4"),
(24568121, "M45", 254736951362, "kenwalibora@gmail.com", "M45Karia")

