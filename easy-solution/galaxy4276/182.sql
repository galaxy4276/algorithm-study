-- using sub query
SELECT Email
FROM (
    SELECT Email, count(Email) as num
    FROM Person
    GROUP BY Email
) as statistic
WHERE num > 1;

-- using having
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1;
