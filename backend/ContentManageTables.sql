create database Mindbyte;
use Mindbyte;
create table Test1(
	id int NOT NULL,
	first varchar (255),
    last varchar (255)
);
INSERT INTO Test1 VALUES(1, "Lorem", "Ipsum");
INSERT INTO Test1 VALUES(2, "Harsh", "Singh");
INSERT INTO Test1 VALUES(3, "Rakesh", "R");
INSERT INTO Test1 VALUES(4, "Mind", "Byte");
select * from Test1;