from enum import Enum #to create enum types

class TxtFileHeader(Enum) :
    ID = "ID:",
    AUTHOR = "AUTHOR:",
    COMMITTER = "COMMITTER:",
    SUBJECT = "SUBJECT:",
    BODY = "BODY:",
    ALL = "ALL:"

