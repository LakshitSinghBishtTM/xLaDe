from enum import IntEnum


class ExitCode(IntEnum):
    OK = 0
    FAILURE = 1
    USAGE = 2
    ENVIRONMENT = 3
    CONFIG = 4
    IO = 5
    INTERNAL = 6
    UNKNOWN = 7
    INTERRUPTED = 130
