from importlib.metadata import PackageNotFoundError, version

__project__ = "sappy"


try:
    __version__ = version(__project__)
except PackageNotFoundError:
    __version__ = "(local)"


VERSION = "{0} v{1}".format(__project__, __version__)

del PackageNotFoundError
del version
