from lib.post import Post
from lib.comment import Comment

class PostRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"], row["contents"])
            posts.append(item)
        return posts

    def find(self, post_id):
        rows = self._connection.execute(
            'SELECT * from posts WHERE id = %s', [post_id])
        row = rows[0]
        return Post(row["id"], row["title"], row["contents"])

    def create(self, post):
        self._connection.execute('INSERT INTO posts (title, contents) VALUES (%s, %s)', [
                                post.title, post.contents])
        return None

    def delete(self, post_id):
        self._connection.execute(
            'DELETE FROM posts WHERE id = %s', [post_id])
        return None
    
    def find_with_comments(self, post_id):
        rows = self._connection.execute(
            "SELECT posts.id AS post_id, posts.title, posts.contents, comments.id AS comment_id, comments.author, comments.content " \
            "FROM posts JOIN comments ON posts.id = comments.post_id " \
            "WHERE posts.id = %s", [post_id])
        comments = []
        for row in rows:
            comment = Comment(row["comment_id"], row["author"], row["content"], row ["post_id"])
            comments.append(comment)

        return Post(rows[0]["post_id"], rows[0]["title"], rows[0]["contents"], comments)