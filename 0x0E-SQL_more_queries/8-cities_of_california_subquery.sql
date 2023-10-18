-- lists all the cities of california in the database
-- Results sorted in ASC by cities
SELECT id, name FROM cities
WHERE state_id = (
	SELECT  id
	FROM states
	WHERE name = 'California')
ORDER BY id ASC;
