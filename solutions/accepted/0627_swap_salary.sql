/* https://leetcode.com/problems/swap-salary/submissions/ */
/* 627. Swap Salary */

/* Easy */
/* 251ms (37.61%) */
/* https://leetcode.com/submissions/detail/613018016/ */

/* # Write your MySQL query statement below */

update Salary
set sex = if(sex='m' , 'f','m')
