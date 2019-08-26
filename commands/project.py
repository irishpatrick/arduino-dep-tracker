from .command import *
from .registry import *

class Project(Command):

    def new(self):
        pass

    def list(self):
        pass

    def add(self):
        pass

    def rem(self):
        pass

    def call(self, flags=[], opts=[]):
        print("project")

Registry.insert("project", Project())
