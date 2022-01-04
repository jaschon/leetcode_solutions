/* 181. Employees Earning More Than Their Managers */
/* https://leetcode.com/problems/employees-earning-more-than-their-managers/ */

/* Easy */
/* https://leetcode.com/submissions/detail/612960194/ */
/* 297ms */

/* # Write your MySQL query statement below */
select e.name as Employee from Employee as e
left join Employee as m on e.managerId = m.id
where e.salary > m.salary


