'''
Main module of this package, allows to import based on platform, and have all the basic import by default
'''
import platform
import importlib

# Get PLATFORMform running
PLATFORM = platform.system()

# pylint: disable=invalid-name
Keyboard = importlib.import_module(PLATFORM + ".Keyboard")
Mouse = importlib.import_module(PLATFORM + ".Mouse")
Window = importlib.import_module(PLATFORM + ".Window")

def import_from_lt(stre, lt_toImport):
    '''Import the list, from a module.'''
    mdl = importlib.import_module(PLATFORM + "." + stre)
    return {k: getattr(mdl, k) for k in lt_toImport}

def import_from(stre, toImport):
    '''import a object from a module.'''
    mdl = importlib.import_module(PLATFORM + "." + stre)
    return {toImport: getattr(mdl, toImport)}

def import_all_from(stre):
    '''from module import *.'''
    # ref: https://stackoverflow.com/questions/43059267/how-to-do-from-module-import-using-importlib
    # Get a handle on the module
    mdl = importlib.import_module(PLATFORM + "." + stre)
    # Is there an __all__?  if so respect it
    if "__all__" in mdl.__dict__:
        names = mdl.__dict__["__all__"]
    else: # Otherwise we import all names that don't begin with _
        names = [x for x in mdl.__dict__ if not x.startswith("_")]

    return {k: getattr(mdl, k) for k in names}
