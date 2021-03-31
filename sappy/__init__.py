from pkg_resources import (
    DistributionNotFound as _DistributionNotFound,
    get_distribution as _get_distribution,
)


__project__ = "sappy"


try:
    __version__ = _get_distribution(__project__).version
except _DistributionNotFound:
    __version__ = "(local)"


VERSION = "{0} v{1}".format(__project__, __version__)
