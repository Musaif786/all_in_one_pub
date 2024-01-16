CREATE TABLE if not exists test(
id INT,
name VARCHAR(20)
);

INSERT INTO test
(id,name) VALUES(2,"Musaif");

SELECT id, name FROM test;

# now alter practice
INSERT INTO demo VALUES(2,"Khan",20);

DROP TABLE IF EXISTS DEMO;

SELECT * FROM demo;

# renamed table name test to demo1
ALTER TABLE test
RENAME TO demo;

ALTER TABLE demo
MODIFY d_id varchar(50);

alter table demo
add column age int default(20);

alter table demo
drop column age;

update demo
set age = 30;

update demo
set age = 25
where age <= 30 OR age >= 20;