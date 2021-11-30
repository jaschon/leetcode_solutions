/*
# https://leetcode.com/problems/duplicate-emails/submissions/
# 182. Duplicate Emails
# Easy
# Accepted!
# 341ms (50.75%)
#https://leetcode.com/submissions/detail/595133076/
*/

select email from Person 
group by email
having count(*) > 1;



