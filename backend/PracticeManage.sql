create database Mindbyte;
use Mindbyte;
create table user(
	id int NOT NULL,
	username varchar (255),
    password varchar (255)
);

INSERT INTO user VALUES(1, "Mindbyte", "password");
INSERT INTO user VALUES(2, "Harsh", "Singh");
INSERT INTO user VALUES(3, "Rakesh", "R");
INSERT INTO user VALUES(4, "U", "U");
select * from user;

show tables


