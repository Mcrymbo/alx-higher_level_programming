-- script that creates a user user_0d_1
-- the user should have all the privileges
-- password is set
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY "user_0d_1_pwd";
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
