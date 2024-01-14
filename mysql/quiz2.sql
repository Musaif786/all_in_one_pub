# quiz 2 & 3
#2 write the query to find avg marks in each city in ascending order
#3. for the given table find the total payment according to each payment method

#3ans
drop table if exists bank;
create table if not exists bank(
 customer_id int primary key,
 customer varchar(50),
 pay_mode varchar(50),
 city varchar(40)
);

insert into bank(customer_id,customer,pay_mode,city) values(101,"Ahmed","netbanking","portland"),(102,"Ethan","Credit card","miami"),(103,"Musaif","Credit card","Hyderabad"),(104,"Noman","debit card","delhi"),(105,"manu","credit card","Hyderabad"),(106,"Don","netbanking","delhi");

select pay_mode, count(city) from bank
group by pay_mode
having count(city) >=2;
