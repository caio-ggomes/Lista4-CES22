from __future__ import annotations
from state import Draft


class Document():

    def __init__(self) -> None:
        self.state = Draft(self)
    def render(self, user) -> None:
        self.state.render(user)
    def publish(self, user) -> None:
        self.state.publish(user)
    def review(self, user, approved: bool) -> None:
        self.state.review(user, approved)
    def expire(self) -> None:
        self.state.expire()
    def changeState(self, state) -> None:
        self.state = state