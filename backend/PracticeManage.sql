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

create table skills(
	id int NOT NULL,
    skill varchar(255) NOT NULL,
    primary key(id)
);
INSERT INTO `mindbyte`.`skills` (`id`, `skill`) VALUES ('1', 'C++');
INSERT INTO `mindbyte`.`skills` (`id`, `skill`) VALUES ('2', 'Java');
INSERT INTO `mindbyte`.`skills` (`id`, `skill`) VALUES ('3', 'Python');
INSERT INTO `mindbyte`.`skills` (`id`, `skill`) VALUES ('4', 'Hadoop');
INSERT INTO `mindbyte`.`skills` (`id`, `skill`) VALUES ('5', 'Spark');
INSERT INTO `mindbyte`.`skills` (`id`, `skill`) VALUES ('6', 'ML');
INSERT INTO `mindbyte`.`skills` (`id`, `skill`) VALUES ('7', 'React');
select * from skills;

create table training(
	id int NOT NULL auto_increment,
    trainingname varchar(255) NOT NULL,
    startDate date NOT NULL,
    dueDate date NOT NULL,
    primary key(id)
);
drop table training;
select * from training;
create table projects(
	id int NOT NULL,
    clientname varchar(255) NOT NULL,
    projectname varchar(255) NOT NULL,
    startDate date NOT NULL,
    endDate date,
    skillsrequired int NOT NULL references skills(id),
    primary key(id)
);
alter table projects add foreign key (skillsrequired) references skills(id);

INSERT INTO projects VALUES(1, "Goldman Sachs & Co. LLC", "Global Market Surveillances", "2021-08-01", "2021-10-01", 4);
INSERT INTO projects VALUES(2, "Capital Group Companies Inc.", "Client Data Delivery", "2021-01-23", "2022-07-12", 7);
INSERT INTO projects VALUES(3, "Morgan Stanley Services Group", "Surveillance Model Uplift", "2021-10-01", "2022-03-01", 1);
INSERT INTO projects VALUES(4, "United Healthcare", "Data Migration", "2021-12-01", "2022-03-01", 2);
INSERT INTO projects VALUES(5, "KPMG LLP.", "Migration Factory", "2022-01-01", "2022-03-01", 3);
select * from projects;


create table employee(
	id int NOT NULL,
    employee_name varchar(255) NOT NULL,
    employee_role varchar(255) NOT NULL,
    designation varchar(255) NOT NULL,
    project int NOT NULL references projects(id),
    skill int NOT NULL references skills(id),
	PRIMARY KEY (id)
);
alter table employee add foreign key (project) references projects(id);
alter table employee add foreign key (skill) references skills(id);

INSERT INTO employee VALUES(1, "R Divya", "Software Engineering", "Analyst", 1,2);
INSERT INTO employee VALUES(2, "Rakesh", "Software Engineering", "Analyst", 2, 2);
INSERT INTO employee VALUES(3, "Bhuvan", "Software Engineering", "Analyst", 3, 4);
INSERT INTO employee VALUES(4, "Vipasha", "Software Engineering", "Analyst", 4,4);
INSERT INTO employee VALUES(5, "Harshvardhan", "Data Engineering", "Analyst", 5,3);
select * from employee;

drop table projects;
drop table employee;
drop table skills;

show databases;