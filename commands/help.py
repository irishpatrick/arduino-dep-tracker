from .command import *
from .registry import *

class Help(Command):

    def call(self, flags=[], opts=[]):
        print("help window")

Registry.insert("help", Help())
