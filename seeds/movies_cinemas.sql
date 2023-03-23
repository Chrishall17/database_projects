-- Create the first table.
CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title text,
    release_date date
);

-- Create the second table.
CREATE TABLE cinemas (
    id SERIAL PRIMARY KEY,
    city text
);

-- Create the join table.
CREATE TABLE movies_cinemas (
    movie_id int,
    cinema_id int,
    constraint fk_movie foreign key(movie_id) references movies(id) on delete cascade,
    constraint fk_cinema foreign key(cinema_id) references cinemas(id) on delete cascade,
    PRIMARY KEY (movie_id, cinema_id)
);

INSERT INTO movies (title, release_date) VALUES ('Equilibrum', '2003-03-14');
INSERT INTO cinemas (city) VALUES ('Leeds');
INSERT INTO movies_cinemas (movie_id, cinema_id) VALUES (1, 1);