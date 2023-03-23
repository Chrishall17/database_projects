Two Tables (Many-to-Many) Design Recipe Template
Copy this recipe template to design and create two related database tables having a Many-to-Many relationship.

1. Extract nouns from the user stories or specification
# EXAMPLE USER STORIES:

As a cinema company manager,
So I can keep track of movies being shown,
I want to keep a list of movies with their title and release date.

As a cinema company manager,
So I can keep track of movies being shown,
I want to keep a list of my cinemas with their city name (e.g 'London' or 'Manchester').

As a cinema company manager,
So I can keep track of movies being shown,
I want to be able to list which cinemas are showing a specific movie.

As a cinema company manager,
So I can keep track of movies being shown,
I want to be able to list which movies are being shown a specific cinema.

Nouns:
movies, title, release_date, cinemas, city_name

2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.

Record	        Properties
movies  	    title, release_date
cinemas	        city_name

Name of the first table (always plural): movies

Column names: title, release_date

Name of the second table (always plural): tags

Column names: tag

3. Decide the column types.
Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

# EXAMPLE:

Table: students
id: SERIAL
title: text
release_date: date

Table: cinemas
id: SERIAL
city: text

4. Design the Many-to-Many relationship
Make sure you can answer YES to these two questions:

Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No)
Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)
# EXAMPLE

1. Can one cinema have many movies? YES
2. Can one movie have many cinemas? YES
If you would answer "No" to one of these questions, you'll probably have to implement a One-to-Many relationship, which is simpler. Use the relevant design recipe in that case.

3. Design the Join Table
The join table usually contains two columns, which are two foreign keys, each one linking to a record in the two other tables.

The naming convention is movies_cinemas.

# EXAMPLE

Join table for tables: movies and cinemas
Join table name: movies_cinemas
Columns: movie_id, cinema_id

4. Write the SQL.
-- EXAMPLE
-- file: movies_cinemas.sql

-- Replace the table name, columm names and types.

-- Create the first table.
CREATE TABLE movies (
  id SERIAL PRIMARY KEY,
  title text
  release_year
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
5. Create the tables.
psql -h 127.0.0.1 movies_cinemas < movies_cinemas.sql


################################################################################################
Two Tables (Many-to-Many) Design Recipe Template
Copy this recipe template to design and create two related database tables having a Many-to-Many relationship.

1. Extract nouns from the user stories or specification
# EXAMPLE USER STORIES:

As a coach
So I can get to know all students
I want to keep a list of students' names.

As a coach
So I can get to know all students
I want to assign tags to students (for example, "happy", "excited", etc).

As a coach
So I can get to know all students
I want to be able to assign the same tag to many different students.

As a coach
So I can get to know all students
I want to be able to assign many different tags to a student.

Nouns:
students, names, tags

2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.

Record	        Properties
students	    name
tags	        tag

Name of the first table (always plural): students

Column names: name

Name of the second table (always plural): tags

Column names: tag

3. Decide the column types.
Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

# EXAMPLE:

Table: students
id: SERIAL
name: text

Table: tags
id: SERIAL
tag: text

4. Design the Many-to-Many relationship
Make sure you can answer YES to these two questions:

Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No)
Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)
# EXAMPLE

1. Can one tag have many students? YES
2. Can one student have many tags? YES
If you would answer "No" to one of these questions, you'll probably have to implement a One-to-Many relationship, which is simpler. Use the relevant design recipe in that case.

3. Design the Join Table
The join table usually contains two columns, which are two foreign keys, each one linking to a record in the two other tables.

The naming convention is table1_table2.

# EXAMPLE

Join table for tables: students and tags
Join table name: students_tags
Columns: student_id, tag_id

4. Write the SQL.
-- EXAMPLE
-- file: students_tags.sql

-- Replace the table name, columm names and types.

-- Create the first table.
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text
);

-- Create the second table.
CREATE TABLE tags (
  id SERIAL PRIMARY KEY,
  tag text
);

-- Create the join table.
CREATE TABLE students_tags (
  student_id int,
  tag_id int,
  constraint fk_student foreign key(student_id) references students(id) on delete cascade,
  constraint fk_tag foreign key(tag_id) references tags(id) on delete cascade,
  PRIMARY KEY (student_id, tag_id)
);
5. Create the tables.
psql -h 127.0.0.1 students_tags < students_tags.sql