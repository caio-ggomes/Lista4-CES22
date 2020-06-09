from __future__ import annotations


class State():

    def __init__(self, document) -> None:
        self.document = document
    def render(self, user) -> None:
        if user.isAdmin() or user.isAuthor():
            print("Document is in {0} state".format(self.__class__.__name__))
        else:
            raise Exception("User is neither an author nor an admin")
    def publish(self, user) -> None:
        raise Exception("Unable to publish document in {0} state".format(self.__class__.__name__))
    def review(self, user, approved: bool) -> None:
        raise Exception("Unable to review document in {0} state".format(self.__class__.__name__))
    def expire(self) -> None:
        raise Exception("Unable to expire document in {0} state".format(self.__class__.__name__))


class Draft(State):

    def publish(self, user) -> None:
        if user.isAdmin():
            self.document.changeState(Published(self.document))
        elif user.isAuthor():
            self.document.changeState(Moderation(self.document))
        else:
            raise Exception("User is neither an author nor an admin")


class Moderation(State):

    def review(self, user, approved: bool) -> None:
        if user.isAdmin():
            if approved:
                self.document.changeState(Published(self.document))
            else:
                self.document.changeState(Draft(self.document))
        else:
            raise Exception("User isn't allowed to review documents")


class Published(State):

    def expire(self) -> None:
        self.document.changeState(Draft(self.document))
