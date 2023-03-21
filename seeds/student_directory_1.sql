-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name text,
    cohort text
);

-- Finally, we add any records that are needed for the tests to run

