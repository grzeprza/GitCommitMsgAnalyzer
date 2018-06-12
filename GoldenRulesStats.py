class GoldenRulesStats(object):
    #list of commits
    commits = []
    #number of commits
    numberOfCommits = 0

    #golden rules statistics
    procOf_SubjectLt50Char = None
    procOf_subjectEndsWithoutDot = None
    procOf_subjectStartWithCapitalLetter = None
    procOf_SubjectInImperativeMood = None
    procOf_BodyWrappedAt72Chars = None
    procOf_subjectLineSeparatedFromBody = None
    procOf_BodyExplenatory = None

    def __init__(self, commits):
        self.commits = commits
        self.numberOfCommits = len(commits)

    def countProcOfSubjectLt50Char(self):
        if self.procOf_SubjectLt50Char is None:
            passedCount = 0
            for commit in self.commits:
                if commit._isSubjectLt50Char:
                    passedCount += 1
            self.procOf_SubjectLt50Char = round(passedCount/self.numberOfCommits, 2)
        return self.procOf_SubjectLt50Char

    def countProcOfSubjectEndsWithoutDot(self):
        if self.procOf_subjectEndsWithoutDot is None:
            passedCount = 0
            for commit in self.commits:
                if commit._subjectEndsWithoutDot:
                    passedCount += 1
            self.procOf_subjectEndsWithoutDot = round(passedCount/self.numberOfCommits, 2)
        return self.procOf_subjectEndsWithoutDot

    def countProcOfSubjectStartsWithCapitalLetter(self):
        if self.procOf_subjectStartWithCapitalLetter is None:
            passedCount = 0
            for commit in self.commits:
                if commit._subjectStartWithCapitalLetter:
                    passedCount += 1
            self.procOf_subjectStartWithCapitalLetter = round(passedCount/self.numberOfCommits, 2)
        return self.procOf_subjectStartWithCapitalLetter

    def countProcOfSubjectInImperativeMood(self):
        if self.procOf_SubjectInImperativeMood is None:
            passedCount = 0
            for commit in self.commits:
                if commit._isSubjectInImperativeMood:
                    passedCount += 1
            self.procOf_SubjectInImperativeMood = round(passedCount/self.numberOfCommits, 2)
        return self.procOf_SubjectInImperativeMood

    def countProcOfBodyWrappedAt72Chars(self):
        if self.procOf_BodyWrappedAt72Chars is None:
            passedCount = 0
            for commit in self.commits:
                if commit._isBodyWrappedAt72Chars:
                    passedCount += 1
            self.procOf_BodyWrappedAt72Chars = round(passedCount/self.numberOfCommits, 2)
        return self.procOf_BodyWrappedAt72Chars

    def countProcOfSubjectLineSeparatedFromBody(self):
        if self.procOf_subjectLineSeparatedFromBody is None:
            passedCount = 0
            for commit in self.commits:
                if commit._subjectLineSeparatedFromBody:
                    passedCount += 1
            self.procOf_subjectLineSeparatedFromBody = round(passedCount/self.numberOfCommits, 2)
        return self.procOf_subjectLineSeparatedFromBody

    def countProcOfBodyExplenatory(self):
        if self.procOf_BodyExplenatory is None:
            passedCount = 0
            for commit in self.commits:
                if commit._isBodyExplenatory:
                    passedCount += 1
            self.procOf_BodyExplenatory = round(passedCount/self.numberOfCommits, 2)
        return self.procOf_BodyExplenatory

    def __str__(self):
        return ("S50Ch: " + str(self.countProcOfSubjectLt50Char()) + "\n" +
              "!Dot: " + str(self.countProcOfSubjectEndsWithoutDot()) + "\n" +
              "Cap: " + str(self.countProcOfSubjectStartsWithCapitalLetter()) + "\n" +
              "B72Ch: " + str(self.countProcOfBodyWrappedAt72Chars()) + "\n" +
              "SLB: " + str(self.countProcOfSubjectLineSeparatedFromBody()) + "\n" +
              "Exp: " + str(self.countProcOfBodyExplenatory()) + "\n" +
              "Imp: " + str(self.countProcOfSubjectInImperativeMood()) )
