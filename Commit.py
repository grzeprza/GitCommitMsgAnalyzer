from CommitStats import CommitStats

class Commit(object):
    _id = ""
    _author = ""
    _committer = ""
    _subject = ""
    _body = []
    _all = []

    def __str__(self):
        fullBody = ""
        fullAll = ""
        for bodyElem in self._body:
            fullBody += bodyElem[0].replace("\n", "LF").replace("\r", "CR")
        for allElem in self._all:
            fullAll += allElem[0].replace("\n", "LF").replace("\r", "CR")
        return self._id + "," + self._author + "," + self._committer + "," + self._subject + "," + fullBody + "," + fullAll + "\n"

    def readable(self):
        return self._id + ",\n" + self._author + ",\n" + self._committer + ",\n" + self._subject + ",\n" + str(len(self._body)) + ",\n" + str(len(self._all)) + "\n"
