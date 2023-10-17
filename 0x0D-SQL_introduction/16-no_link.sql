-- lists all records of the table
-- result display score and name
-- result listed by descending score
-- ignores row without name value
SELECT score, name FROM second_table where name IS NOT NULL
ORDER BY score DESC;
