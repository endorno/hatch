drop table if exists users,eggs,cheers;

create table users (
user_id INT NOT NULL,
name VARCHAR(64) NOT NULL,
PRIMARY KEY (user_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table eggs(
user_id INT NOT NULL,
egg_id INT NOT NULL,
challenge text NOT NULL,
promise text NOT NULL,
do_when INT NOT NULL,
asin VARCHAR(128),
price INT,
title VARCHAR(255),
thumbnail text,
detail_link text,
PRIMARY KEY (user_id,egg_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table cheers(
user_id INT NOT NULL,
egg_id INT NOT NULL,
comment text,
PRIMARY KEY (egg_id,user_id),
KEY (user_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

