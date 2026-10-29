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
    PERMISSION = 8
    DEPENDENCY = 9
    TIMEOUT = 10
    NETWORK = 11
    CANCELLED = 12
    NOT_EXECUTABLE = 126
    NOT_FOUND = 127
    INTERRUPTED = 130
