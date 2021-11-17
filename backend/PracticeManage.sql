create database Mindbyte;
use Mindbyte;
create table user(
	id int NOT NULL,
	username varchar (255),
    password varchar (255)
);

create table project(
    id int NOT NULL,
    name varchar (255) NOT NULL,
    startDate date NOT NULL,
    endDate date NOT NULL,
    status varchar (255) NOT NULL
)

INSERT INTO user VALUES(1, "Mindbyte", "password");
INSERT INTO user VALUES(2, "Harsh", "Singh");
INSERT INTO user VALUES(3, "Rakesh", "R");
INSERT INTO user VALUES(4, "U", "U");
select * from user;

show tables


