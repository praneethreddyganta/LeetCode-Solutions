# Write your MySQL query statement below
# Need to work on this question again
select e.name as employee from employee e 
join Employee m 
on e.managerId=m.id
where e.salary>m.salary