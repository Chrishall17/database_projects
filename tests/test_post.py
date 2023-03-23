from lib.post import Post

"""
Post constructs with an id, title and author name
"""
def test_post_constructs():
    post = Post(1, 'Title', 'Content')
    assert post.id == 1
    assert post.title == 'Title'
    assert post.contents == 'Content'

"""
We can format post to strings nicely
"""
def test_posts_format_nicely():
    post = Post(1, 'Title', 'Content')
    assert str(post) == "1 - Title: Content"

"""
We can compare two identical posts
And have them be equal
"""
def test_posts_are_equal():
    post1 = Post(1, 'Title', 'Content')
    post2 = Post(1, 'Title', 'Content')
    assert post1 == post2