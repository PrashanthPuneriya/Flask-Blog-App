DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS blogs CASCADE;
DROP TABLE IF EXISTS sessions CASCADE;

CREATE TABLE users(
    id serial PRIMARY KEY,
    first_name VARCHAR (255) NOT NULL,
    last_name VARCHAR (255),
    email VARCHAR (255) NOT NULL UNIQUE,
    password VARCHAR (255) NOT NULL
);

CREATE TABLE blogs(
    id serial PRIMARY KEY,
    title VARCHAR (255) NOT NULL,
    content TEXT,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE sessions(
    id serial PRIMARY KEY,
    session_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE
);
