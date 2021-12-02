/*
# 196. Delete Duplicate Emails
# https://leetcode.com/problems/delete-duplicate-emails/
# Easy
# Accepted!
# 981ms (15.06%)
# https://leetcode.com/submissions/detail/595973400/
*/


delete p1 from Person p1
inner join Person p2
where p2.id < p1.id and p1.email = p2.email;


