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

create table projects(
	id int NOT NULL,
    clientname varchar(255) NOT NULL,
    projectname varchar(255) NOT NULL,
    startDate date NOT NULL,
    endDate date,
    skillsrequired varchar(255) NOT NULL,
    projectstatus varchar(255) NOT NULL
);
INSERT INTO projects VALUES(1, "Goldman Sachs", "Trade Surveillances", "2021-10-01", "2021-08-01", "Java, Hadoop", "Active");
INSERT INTO projects VALUES(2, "American Express", "Credit Fraud Detection", "2021-01-23", "2022-7-12", "Python, Javascripts", "Active");
INSERT INTO projects VALUES(3, "Morgan Stanley", "Engineering Initiatives", "2021-10-01", "2022-03-01", "Hadoop, HBase, Java", "Active");
select * from projects;

create table employee(
	id int NOT NULL,
    employee_name varchar(255) NOT NULL,
    employee_role varchar(255) NOT NULL,
    designation varchar(255) NOT NULL,
    skill varchar(255) NOT NULL
);
INSERT INTO employee VALUES(1, "R Divya", "Software Engineering", "Analyst", "Python, ML");
INSERT INTO employee VALUES(2, "Rakesh", "Software Engineering", "Analyst", "Python, ML");
INSERT INTO employee VALUES(3, "Bhuvan", "Software Engineering", "Analyst", "Python, ML");
INSERT INTO employee VALUES(4, "Vipasha", "Software Engineering", "Analyst", "Python, ML");
INSERT INTO employee VALUES(5, "Harshvardhan", "Data Engineering", "Analyst", "C++, Hadoop");
select * from employee;

show tables



