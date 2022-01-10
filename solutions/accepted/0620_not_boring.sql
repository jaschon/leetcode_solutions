/* 620. Not Boring Movies */
/* https://leetcode.com/problems/not-boring-movies/ */

/* Result: https://leetcode.com/submissions/detail/617240700/ */
/* Time: 179ms (79.44%) */


/* # Write your MySQL query statement below */
select * from Cinema
where mod(id,2) <> 0 and description != "boring"
order by rating desc
