-- creates a table id_not_null on mysql server
-- database passed as sql argument
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256)
);
