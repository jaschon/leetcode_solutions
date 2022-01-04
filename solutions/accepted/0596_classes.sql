/* 596. Classes More Than 5 Students */
/* https://leetcode.com/problems/classes-more-than-5-students/submissions/ */

/* Easy */
/* 286ms (49.90%) */
/* https://leetcode.com/submissions/detail/613022994/ */

/* # Write your MySQL query statement below */
select class from Courses
group by class
having count(*) > 4

