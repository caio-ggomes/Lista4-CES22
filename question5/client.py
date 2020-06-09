from __future__ import annotations


class User:

    def __init__(self) -> None:
        self.author = False
        self.admin = False
    def publish(self, document) -> None:
        raise Exception("User isn't allowed to publish documents")
    def review(self, document, approved: bool) -> None:
        raise Exception("User isn't allowed to review documents")
    def isAuthor(self) -> bool:
        return self.author
    def isAdmin(self) -> bool:
        return self.admin


class Author(User):

    def __init__(self) -> None:
        self.author = True
        self.admin = False
    def publish(self, document) -> None:
        document.publish(self)


class Admin(User):

    def __init__(self) -> None:
        self.author = False
        self.admin = True
    def publish(self, document) -> None:
        document.publish(self)
    def review(self, document, approved: bool) -> None:
        document.review(self, approved)

