#use musaif;
#create database test1;
-- create database if not exists test1;
#drop database test1;
-- drop database if exists test1;
-- means just a comment
-- create table employees(
-- empid int primary key,
-- empname varchar(22),
-- empylocation varchar(15)
-- );

-- select * from employees;
-- select empname from employees;
-- insert into employees values(123,"Mohammed Musaif","hyderabad");

-- show databases;

# deleting or droping db
drop table if exists teacher;
drop table if exists dept;

# creating table
# parent table
CREATE TABLE dept(
id INT PRIMARY KEY,
name VARCHAR(50)
);

# inserting data
INSERT INTO dept
VALUES(101,"english"),(102,"Maths"),(103,"Science");

#updating id
update dept
set id = 104
where id = 101;

# printing data
select * from dept;



# child table bcz we are using foreign key
CREATE TABLE teacher(
id INT PRIMARY KEY,
name VARCHAR(50),
dept_id INT,
foreign key (dept_id) references dept(id)
on update cascade
on delete cascade
);


INSERT INTO teacher
VALUES(101,"Musaif",101),(102,"Khan",102),(103,"Manu",103);

select * from teacher;

-- select * into newtable
-- from teacher
-- where id =103;

INSERT INTO teacher
VALUES(110,"Musaif",104),(108,"Khan",103),(109,"Manu",103),(106,"musaif",103),(105,"Manu",102);


select count(id) from teacher
group by name;


-- debricated
-- backup database musaif
-- to disk = 'D:\Vscode-All scripts\All_in_one';

select * from m;

alter table m
modify column lname varchar(100);

-- Adding column-- 
alter table m
add lastname varchar(30);

-- Remove column
alter table m
drop column lastname;

-- Rename column
alter table m
rename column lastname to lname

-- show tables;

