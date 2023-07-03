SELECT firstName, lastName, city, state
FROM Person left join Address
on Person.PersonId = Address.PersonId