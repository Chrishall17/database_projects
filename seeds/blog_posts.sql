-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS posts CASCADE;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    contents text
);

CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    author text,
    content text,
    post_id int,
    constraint fk_post foreign key(post_id) references posts(id) on delete cascade
);

INSERT INTO posts (title, contents) VALUES ('My Morning', 'Wake Up');

INSERT INTO comments (author, content, post_id) VALUES ('Mick', 'Cool', 1);