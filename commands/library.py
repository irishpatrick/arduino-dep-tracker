from .command import *
from .registry import *
import core

class Library(Command):

    def create(self, fn):
        lib = core.Library()
        lib.opendir(fn)

    def list(self):
        pass

    def call(self, flags=[], opts=[]):
        if len(opts) < 2:
            return
        if opts[0] == "create":
            self.create(opts[1])

Registry.insert("library", Library())
