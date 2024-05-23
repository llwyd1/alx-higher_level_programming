-- Creates the database hbtn_0d_usa and the table states
-- in the hbtn_0d_usa database on your MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Selects the database hbtn_0d_usa
USE hbtn_0d_usa;
-- Creates the table states
CREATE TABLE IF NOT EXISTS cities (
	   id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
	   state_id INT,
	   FOREIGN KEY (state_id) REFERENCES states(id),
	   name VARCHAR(256) NOT NULL);
