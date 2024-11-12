from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("flask_resize")
    __version_info__ = tuple(int(p) for p in __version__.split("."))
except PackageNotFoundError:
    __version__ = "unknown"
    __version_info__ = ()

__all__ = ["__version__", "__version_info__"]
