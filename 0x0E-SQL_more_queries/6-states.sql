-- Creates the database hbtn_0d_usa and the table states
-- in the hbtn_0d_usa database on your MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Selects the database hbtn_0d_usa
USE hbtn_0d_usa;
-- Creates the table states
CREATE TABLE IF NOT EXISTS states (
	   id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
	   name VARCHAR(256) NOT NULL);
