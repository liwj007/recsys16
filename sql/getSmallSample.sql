# get the positive sample from table sample
create table sample1(select * from sample where label = 1);
# insert the random negative sample into the sample1
insert into sample1 select * from sample where id >=8530861*RAND() + 8974187 LIMIT 212091;
# read the records of sample1 into file sample_small.txt
select * from sample1 into outfile "D:\\sample_small.txt"
