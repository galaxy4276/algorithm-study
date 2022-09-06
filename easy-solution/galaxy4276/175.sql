SELECT
    p.firstName, p.lastName, addr.city, addr.state
FROM Person p
LEFT JOIN Address addr
ON p.personId = addr.personId;
