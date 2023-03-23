class Post:
    def __init__(self, id, title, contents, comments = []):
        self.id = id
        self.title = title
        self.contents = contents
        self.comments = comments

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        if self.comments == []:
            return f"{self.id} - {self.title}: {self.contents}"
        else:
            return f"{self.id} - {self.title}: {self.contents}, {self.comments}"