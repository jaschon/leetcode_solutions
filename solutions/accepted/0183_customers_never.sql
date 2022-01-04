/* https://leetcode.com/problems/customers-who-never-order/ */
/* 183. Customers Who Never Order */

/* Easy */
/* 525ms (27.72%) */
/* https://leetcode.com/submissions/detail/613008909/ */

/* # Write your MySQL query statement below */
select c.name as Customers from Customers c
left join Orders as o on o.customerId = c.id
where o.id is NULL


