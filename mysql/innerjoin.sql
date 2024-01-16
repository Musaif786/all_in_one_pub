# this is for joins

#drop database joinsdb;

CREATE DATABASE if not exists joindb;
use joindb;

create table if not exists a(
id int,
name varchar(50)
);

insert into a
values(101,"adam"),(102,"khan"),(103,"md");

select * from a;

create table if not exists b(
id int,
course varchar(50)
);

insert into b
values(102,"ENG"),(103,"IT"),(106,"BSC");

select * from b;

#inner join
select a.id,a.name,b.course from a
inner join b
on a.id = b.id;

# left join
select a.id,a.name,b.course from a
left join b
on a.id = b.id;

select a.id,a.name,b.course from a
left join b
on a.id = b.id
where b.course is not null;

#right join
select a.id,a.name,b.course from a
right join b
on a.id = b.id;