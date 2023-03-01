DROP DATABASE IF EXISTS apartments;
CREATE DATABASE apartments;
USE apartments;


CREATE TABLE apartments_details(
apartment_id INT PRIMARY KEY AUTO_INCREMENT,
apartment_username VARCHAR(100),
apartment_name VARCHAR(100),
owners_name VARCHAR(100),
owners_username VARCHAR(100),
managers_name VARCHAR(100),
managers_username VARCHAR(100),
date_registered DATETIME,
owners_password VARCHAR(50),
managers_password VARCHAR(100)
);

INSERT INTO apartments_details(apartment_username, apartment_name, owners_name, managers_name, date_registered, managers_password) VALUES 
("belevue001", "Belevue", "Peter", "Ken Kasungu", "2020-10-22 21:12:41", "Kasungu")