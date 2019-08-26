from .registry import *

def call(cmd, flags=[], opts=[]):
    Registry.get(cmd).call(flags, opts)

def exists(cmd):
    return Registry.contains(cmd)
