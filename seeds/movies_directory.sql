CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title text,
    genre text,
    release_year int
);

INSERT INTO movies (title, genre, release_year) VALUES ('Matrix', 'Action', 1999);