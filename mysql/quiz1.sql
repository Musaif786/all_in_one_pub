#quiz one
# create a database for ur compy and insert a emps data
drop database if exists solugenix;

create database if not exists solugenix;

use solugenix;

create table if not exists employees(
 empid int primary key not null,
 empname varchar(50) not null,
 empsalary int 
);


-- insert data
insert into employees(empid, empname, empsalary) values(1,"adam",25000),(2,"bob",30000),(3,"casey",40000);
select * from employees;