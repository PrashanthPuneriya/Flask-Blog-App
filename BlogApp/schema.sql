DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS blogs;
CREATE TABLE users(
    id serial PRIMARY KEY,
    first_name VARCHAR (255) NOT NULL,
    last_name VARCHAR (255),
    email VARCHAR (255),
    password VARCHAR (255)
);
CREATE TABLE blogs(
    id serial PRIMARY KEY,
    title VARCHAR (255) NOT NULL,
    content TEXT,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);