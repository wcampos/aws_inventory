USE inventory;

CREATE TABLE profiles(
id SERIAL,
creation_date TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
name VARCHAR(255) NOT NULL,
access_key VARCHAR(255) NOT NULL,
secret_key VARCHAR(255) NOT NULL,
PRIMARY KEY(id)
);


select * from profiles;