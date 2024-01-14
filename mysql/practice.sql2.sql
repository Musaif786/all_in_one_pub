use musaif;
drop table if exists solugenix;
create table if not exists solugenix(
 empid int not null,
 empname varchar(50) not null,
 empsalary int,
 primary key (empid,empname)
 
);

-- insert data
insert into solugenix(empid, empname, empsalary) values(1,"adam",25000),(2,"bob",30000),(3,"casey",40000);
select * from solugenix
where empsalary >= 30000;