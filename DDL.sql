drop table if exists users,eggs,cheer_list;

create table users (
user_id INT NOT NULL,
name VARCHAR(64) NOT NULL,
PRIMARY KEY (user_id)
);

create table eggs(
user_id INT NOT NULL,
egg_id INT NOT NULL,
challenge text NOT NULL,
promise text NOT NULL,
PRIMARY KEY (user_id,egg_id)
);

create table cheer_list(
user_id INT NOT NULL,
egg_id INT NOT NULL,
comment text,
PRIMARY KEY (egg_id,user_id),
KEY (user_id)
);

