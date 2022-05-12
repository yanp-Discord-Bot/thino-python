class ThinoException(Exception):
    """Base exception class for nekos.py"""

    pass


class NothingFound(ThinoException):
    """The API didn't return anything"""

    pass


class EmptyArgument(ThinoException):
    """When no target is defined"""

    pass


class InvalidArgument(ThinoException):
    """Invalid argument within the category"""

    pass