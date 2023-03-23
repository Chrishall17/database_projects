from lib.post_repository import PostRepository
from lib.post import Post
from lib.comment import Comment

"""
When we call PostRepository#all
We get a list of Post objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/blog_posts.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new PostRepository

    posts = repository.all() 

    assert posts == [
        Post(1, "My Morning", "Wake Up")
    ]

"""
When we call PostRepository#find
We get a single Post object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/blog_posts.sql")
    repository = PostRepository(db_connection)

    post = repository.find(1)
    assert post == Post(1, "My Morning", "Wake Up")

"""
When we call PostRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/blog_posts.sql")
    repository = PostRepository(db_connection)

    repository.create(Post(None, "My Lunch", "Bacon"))

    result = repository.all()
    assert result == [
        Post(1, "My Morning", "Wake Up"),
        Post(2, "My Lunch", "Bacon")
    ]

"""
When we call PostRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/blog_posts.sql")
    repository = PostRepository(db_connection)
    repository.delete(1)

    result = repository.all()
    assert result == [

    ]

"""
When we call PostRepository#find_with_comments
We return Post with Comment 
"""
def test_find_with_comments(db_connection):
    db_connection.seed("seeds/blog_posts.sql")
    repository = PostRepository(db_connection)
    post = repository.find_with_comments(1)
    assert post == Post(1, "My Morning", "Wake Up", [
        Comment(1, "Mick", "Cool", 1)
    ])