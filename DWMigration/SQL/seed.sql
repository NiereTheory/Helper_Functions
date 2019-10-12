create table if not exists test_tbl (
	id integer primary key
	, first_name text
	, last_name text
);

-- truncate table test_tbl;
delete from test_tbl;

insert into test_tbl (first_name, last_name)
values 
('Ben', 'Niere'),
('John', 'Doe');

insert into test_tbl (first_name, last_name)
select first_name, last_name from test_tbl
-- run this a few times