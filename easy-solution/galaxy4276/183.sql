-- using sub query
SELECT Customers.name as 'Customers'
FROM Customers
where Customers.id not in
(
    select customerid from orders
);

-- using left join
SELECT Name AS 'Customers'
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.CustomerId
WHERE o.CustomerId IS NULL;
