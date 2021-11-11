create database Mindbyte;
use Mindbyte;
create table LoginTable(
	id int NOT NULL,
	username varchar (255),
    password varchar (255)
);

INSERT INTO LoginTable VALUES(1, "Mindbyte", "password");
INSERT INTO LoginTable VALUES(2, "Harsh", "Singh");
INSERT INTO LoginTable VALUES(3, "Rakesh", "R");
INSERT INTO LoginTable VALUES(4, "U", "U");
select * from LoginTable;