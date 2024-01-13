# 620. Not Boring Movies
# Write your MySQL query statement below
select id, movie, description, rating from Cinema
where (id % 2 = 1) AND (description != "boring")
order by rating desc