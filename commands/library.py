from .command import *
from .registry import *
import core

class Library(Command):

    def create(self):
        pass

    def list(self):
        pass

    def call(self, flags=[], opts=[]):
        print("library")

Registry.insert("library", Library())
