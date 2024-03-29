DROP DATABASE IF EXISTS apartment_name;
CREATE DATABASE apartment_name;
USE apartment_name;

CREATE TABLE details(
id_number VARCHAR(10) PRIMARY KEY,
first_name VARCHAR(100),
last_name VARCHAR(100),
phone_number VARCHAR(20),
email_address VARCHAR(150),
house_number VARCHAR(100),
gender VARCHAR(30),
occupation VARCHAR(100),
date_of_commencing_tenancy DATE,
next_of_kin_first_name VARCHAR(100),
next_of_kin_last_name VARCHAR(100),
next_of_kin_phone_number VARCHAR(100),
next_of_kin_email_address VARCHAR(100),
next_of_kin_relationship VARCHAR(30),
next_of_kin_address VARCHAR(100),
photo LONGBLOB);

CREATE TABLE tenants_logins(
id_number VARCHAR(10) PRIMARY KEY,
house_number VARCHAR(100),
phone_number VARCHAR(20),
email_address VARCHAR(100),
user_password VARCHAR(50),
user VARCHAR(100));

CREATE TABLE payments(
payment_id INT PRIMARY KEY AUTO_INCREMENT,
house_number VARCHAR(10),
tenants_name VARCHAR(200),
payment_reason VARCHAR(100),
payment_code VARCHAR(100),
payment_method VARCHAR(100),
amount DECIMAL(9, 2),
payment_date DATETIME,
verified_Not_Verified VARCHAR(100),
valid_invalid VARCHAR(100),
balance_when_verified DECIMAL(9, 2));

CREATE TABLE accounts(
house_number VARCHAR(10) PRIMARY KEY,
balance decimal(8,2)
);

CREATE TRIGGER add_rent
AFTER INSERT ON details
FOR EACH ROW
INSERT INTO  accounts(house_number, balance) VALUES 
(NEW.house_number,  16000);


CREATE TABLE messages(
message_id int PRIMARY KEY AUTO_INCREMENT,
date_sent datetime, 
sent_from VARCHAR(100),
sent_to VARCHAR(100),
message VARCHAR(10000));

CREATE TABLE message_updator(
message_update_id INT PRIMARY KEY AUTO_INCREMENT,
message_id int
);


CREATE TRIGGER insert_message_id
AFTER INSERT ON messages
FOR EACH ROW
INSERT INTO  message_updator(message_id) VALUES (NEW.message_id);

INSERT INTO apartment_name.details(id_number, first_name, last_name, phone_number, email_address, house_number, date_of_commencing_tenancy , occupation,
next_of_kin_first_name, next_of_kin_last_name) VALUES
(11217220, "Derrick", "Mkali", 254799368479, "mbalukaderrik@gmail.com", "B16", "2023-01-11", "Student", "Kendrick", "Mulamwa"),
(32711242, "Angela", "Nyaboke", 254712348479, "angela19200@gmail.com", "A11", "2020-03-19", "Accountant", "Louis", "Cia"),
(07554865, "Ian", "Pweza", 254748556412, "ianfala1213@gmail.com", "J9", "2022-07-30", "Watchman", "Keovin", "Musyo"),
(11602891, "Mwalimu", "Lucy", 254714647101, "mwalimu@gmail.com", "F18", "2020-02-1", "Manager", "Eddy", "Butitta"),
(24568121, "Ken", "Walibora", 254736951362, "kenwalibora@gmail.com", "M45", "2023-03-11", "Plumber", "Miss", "Wake");

INSERT INTO tenants_logins(id_number,house_number,phone_number, email_address, user_password, user) VALUES
(11217220, "B16", 254799368479, "mbalukaderrik@gmail.com", ".", "TENANT"),
(32711242, "A11", 254712348479, "angela19200@gmail.com", "Wowman", "TENANT"),
(07554865, "J9",  254748556412, "ianfala1213@gmail.com", "Tenant4", "TENANT"),
(11602891, "F18", 254714647101, "mwalimu@gmail.com", ".", "MANAGER"),
(24568121, "M45", 254736951362, "kenwalibora@gmail.com", "M45Karia", "TENANT");

CREATE TABLE complaints(
complaint_id INT PRIMARY KEY AUTO_INCREMENT,
complaint_date_posted DATETIME,
house_number VARCHAR(100),
tenants_name VARCHAR(100),
date_of_incedence DATE,
complaint_category VARCHAR(100),
complaint_description VARCHAR(3000));

CREATE TABLE repairs(
repair_id INT PRIMARY KEY AUTO_INCREMENT,
house_number VARCHAR(100),
tenants_name VARCHAR(100),
category VARCHAR(100),
scheduled_date DATE,
description VARCHAR(1000),
sorted VARCHAR(100));


CREATE TABLE vacate_notice(
vacation_id INT PRIMARY KEY AUTO_INCREMENT,
house_number VARCHAR(100),
tenants_name VARCHAR(100),
vacation_date DATE,
reason VARCHAR(1000),
reimbursement_channel VARCHAR(100),
account_number VARCHAR(100),
sorted VARCHAR(100));


CREATE TABLE properties(
property_id INT PRIMARY KEY AUTO_INCREMENT,
house_number VARCHAR(100),
picture longblob);



