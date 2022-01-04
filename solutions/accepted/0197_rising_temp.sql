/* https://leetcode.com/problems/rising-temperature/ */
/* 197. Rising Temperature */

/* Easy */
/* 286ms (97.60%) */
/* https://leetcode.com/submissions/detail/613034190/ */

/* # Write your MySQL query statement below */

select c1.id from Weather c1
inner join Weather c2 on date(c1.recordDate) = date_add(c2.recordDate, INTERVAL 1 DAY)
where c2.temperature < c1.temperature




