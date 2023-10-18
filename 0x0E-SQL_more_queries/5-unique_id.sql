-- creates table unique_id
-- database passed as mysql argumen
CREATE TABLE IF NOT EXISTS unique_id(
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
);
