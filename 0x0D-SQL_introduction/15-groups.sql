-- list number of records with the same score
-- list sorted by number of records
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY score DESC;
