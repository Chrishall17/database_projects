from lib.comment import Comment

"""
Comment constructs with an id, title and author name
"""
def test_comment_constructs():
    comment = Comment(1, 'Author', 'Content', 1)
    assert comment.id == 1
    assert comment.author == 'Author'
    assert comment.content == 'Content'
    assert comment.post_id == 1

"""
We can format comment to strings nicely
"""
def test_comments_format_nicely():
    comment = Comment(1, 'Author', 'Content', 1)
    assert str(comment) == "1 - Author: Content, 1"

"""
We can compare two identical comments
And have them be equal
"""
def test_comments_are_equal():
    comment1 = Comment(1, 'Author', 'Content', 1)
    comment2 = Comment(1, 'Author', 'Content', 1)
    assert comment1 == comment2