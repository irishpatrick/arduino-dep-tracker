import pickle
import tarfile
import os

class Library:
    def __init__(self):
        self.name = ""
        self.version = ""
        self.author = ""
        self.maintainer = ""
        self.archive = ""
        self.files = []

    def parse_propertes(self, props):
        for line in props:
            if line.startswith("name="):
                self.name = line.split("=")[1][:-1]
            elif line.startswith("version="):
                self.version = line.split("=")[1][:-1]
            elif line.startswith("author="):
                self.author = line.split("=")[1][:-1]
            elif line.startswith("maintainer="):
                self.maintainer = line.split("="):[1][:-1]


    def opendir(self, fn):
        # check for valid library properties
        props = []
        with open(os.path.join(fn, "library.properties"), "r") as fp:
            props.extend(fp.readlines())

        # parse properties
        self.parse_propertes(props)

        # list all library files
        for (dirpath, dirnames, filenames) in os.walk(fn):
            for name in filenames:
                self.files.append(os.path.join(dirpath, name))

        # create archive

        # pickle and write
