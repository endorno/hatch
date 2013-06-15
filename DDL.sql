drop table if exists users,eggs,cheer_list;

create table users (
user_id INT NOT NULL AUTO_INCREMENT,
raw_password CHAR(32) NOT NULL,
name VARCHAR(64) NOT NULL,
PRIMARY KEY (user_id)
);
create table eggs(
egg_id INT NOT NULL AUTO_INCREMENT,
content text NOT NULL,
PRIMARY KEY (egg_id)
);
create table cheer_list(
user_id INT NOT NULL,
egg_id INT NOT NULL
);

