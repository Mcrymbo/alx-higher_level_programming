-- lists all cities contained in the database
-- result sorted in ascending order
SELECT cities.id AS id, cities.name AS name, states.name AS name
FROM cities
JOIN states
ON cities.state_id = states.id
ORDER BY id ASC;
