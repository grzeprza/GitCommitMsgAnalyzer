from NLPmodule import isFirstWordImperative

class CommitStats(object):
    _commitId = ""
    _author = ""
    _isSubjectLt50Char = False
    _subjectEndsWithoutDot = False
    _subjectStartWithCapitalLetter = False
    _isSubjectInImperativeMood = False
    _isBodyWrappedAt72Chars = False
    _subjectLineSeparatedFromBody = False
    _isBodyExplenatory = False

    def __init__(self, author, commitId):
        self._author = author
        self._commitId = commitId

    def isS50Ch(self, subject):
       # check whether subject has 50 chars
        if len(subject) <= 50:
            self._isSubjectLt50Char =  True
        else:
            self._isSubjectLt50Char = False

    def subjectEndsWithoutDot(self, subject):
        #check whether subject ends with dot
        if str(subject).endswith("."):
            self._subjectEndsWithoutDot = False
        else:
            self._subjectEndsWithoutDot = True

    def subjectStartsWithCapitalLetter(self,subject):
        #check whether subject starts with capital letter
        try:
            if str(subject)[0] == str(subject)[0].upper():
                self._subjectStartWithCapitalLetter = True
            else:
                self._subjectStartWithCapitalLetter = False
        except IndexError:
            print ("subjectStartsWithCapitalLetter:" + str(subject))
            self._subjectStartWithCapitalLetter = False

    def subjectInImperativeMood(self, subject):
       if isFirstWordImperative(subject):
           self._isSubjectInImperativeMood = True
       else:
           self._isSubjectInImperativeMood = False

    def bodyWrapped72Chars(self, body):
        #check whether body is wrapped at 72 chars
        for line in body:
            if len(str(line[0])) <= 72:
                self._isBodyWrappedAt72Chars = True
            else:
                self._isBodyWrappedAt72Chars = False
                return False

    def subjectLineSeparatedWithBody(self, body, all):
        #check whther subject and body are separated by line

        try:
            if (body[0])[0] is not None and len(all) >= 1 and all[1] != "" and str((all[1])[0]).startswith("\r\n"):
                self._subjectLineSeparatedFromBody = True
            else:
                self._subjectLineSeparatedFromBody = False
        except IndexError:
            print ("Report missed parsing in subjectLineSeparatedWithBody: "+ str(body) + ", " + str(all))
            self._subjectLineSeparatedFromBody = False

    def bodyExaplanation(self, body):
        #check whether body is answersing correct questions
        raise NotImplemented("Body Explanation not implemented")

    def readible(self):
        return ("Id: " + self._commitId + "\n" +
              "S50Ch: " + str(self._isSubjectLt50Char) + "\n" +
              "!Dot: " + str(self._subjectEndsWithoutDot) + "\n" +
              "Cap: " + str(self._subjectStartWithCapitalLetter) + "\n" +
              "B72Ch: " + str(self._isBodyWrappedAt72Chars) + "\n" +
              "SLB: " + str(self._subjectLineSeparatedFromBody) + "\n" +
              "Exp: " + str(self._isBodyExplenatory) + "\n" +
              "Imp: " + str(self._isSubjectInImperativeMood) )

    def __str__(self):
        return (self._commitId + "," + str(self._isSubjectLt50Char) +
                "," + str(self._subjectEndsWithoutDot) +
                "," + str(self._subjectStartWithCapitalLetter) +
                "," + str(self._isBodyWrappedAt72Chars) +
                "," + str(self._subjectLineSeparatedFromBody) +
                "," + str(self._isBodyExplenatory) +
                "," + str(self._isSubjectInImperativeMood) )

