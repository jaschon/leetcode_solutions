/* 595. Big Countries */
/* https://leetcode.com/problems/big-countries/ */
/* 436 (7.24%) */

select name, population, area from World 
where area >= 3000000
or population >= 25000000;




