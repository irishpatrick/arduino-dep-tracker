from .command import *
from .registry import *

class Default(Command):

    def call(self, flags=[], opts=[]):
        print("default statement")

Registry.insert("", Default())
Registry.insert("default", Default())
