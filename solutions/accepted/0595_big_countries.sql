/* 595. Big Countries */
/* https://leetcode.com/problems/big-countries/ */

/* Easy */
/* https://leetcode.com/submissions/detail/612402421/ */
/* 436 (7.24%) */

select name, population, area from World 
where area >= 3000000
or population >= 25000000;




