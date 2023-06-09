RECIPES
1. Extract nouns from the user stories or specification
# EXAMPLE USER STORY:
# (analyse only the relevant part - here the final line).

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep a list of all my recipes with their names.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep the average cooking time (in minutes) for each recipe.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to give a rating to each of the recipes (from 1 to 5).

Nouns:
> recipes, name, cooking time, rating

2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.

Record	        Properties
Recipe	        name, cooking time, rating

Name of the table (always plural): recipes

Column names: name, cooking time, rating

3. Decide the column types.
Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

# EXAMPLE:

id: SERIAL
name: text
cooking_time: int
rating: int


4. Write the SQL.
-- EXAMPLE
-- file: recipes.sql

-- Replace the table name, columm names and types.

CREATE TABLE movies (
  id SERIAL PRIMARY KEY,
  name text,
  cooking_time text,
  rating int
);

5. Create the table.
psql -h 127.0.0.1 recipe_directory < recipes.sql


MOVIES
1. Extract nouns from the user stories or specification
# EXAMPLE USER STORY:
# (analyse only the relevant part - here the final line).

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' titles.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' genres.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' release year.

Nouns:
> movies, title, genre, release year

2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.

Record	        Properties
Movie	        title, genre, release year

Name of the table (always plural): movies

Column names: title, genre, release year

3. Decide the column types.
Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

# EXAMPLE:

id: SERIAL
title: text
genre: text
release_year: int


4. Write the SQL.
-- EXAMPLE
-- file: student_directory_1.sql

-- Replace the table name, columm names and types.

CREATE TABLE movies (
  id SERIAL PRIMARY KEY,
  title text,
  genre text,
  release_year int
);

5. Create the table.
psql -h 127.0.0.1 movies_directory < movies_directory.sql


STUDENTS
1. Extract nouns from the user stories or specification
# EXAMPLE USER STORY:
# (analyse only the relevant part - here the final line).

As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.

Nouns:
> students, name, cohort

2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.

Record	        Properties
Student	        name, cohort

Name of the table (always plural): students

Column names: name, cohort

3. Decide the column types.
Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

# EXAMPLE:

id: SERIAL
name: text
cohort: text


4. Write the SQL.
-- EXAMPLE
-- file: student_directory_1.sql

-- Replace the table name, columm names and types.

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort text
);

5. Create the table.
psql -h 127.0.0.1 student_directory_1 < student_directory_1.sql