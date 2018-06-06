class GoldenRulesStats(object):
    #list of commits
    commits = []
    #number of commits
    numberOfCommits = 0

    #golden rules statistics
    procOf_SubjectLt50Char = 0.0
    procOf_subjectEndsWithoutDot = 0.0
    procOf_subjectStartWithCapitalLetter = 0.0
    procOf_SubjectInImperativeMood = 0.0
    procOf_BodyWrappedAt72Chars = 0.0
    procOf_subjectLineSeparatedFromBody = 0.0
    procOf_BodyExplenatory = 0.0

    def __init__(self, commits):
        self.commits = commits
        self.numberOfCommits = len(commits)

    def countProcOfSubjectLt50Char(self):
        pass

    def countProcOfSubjectEndsWithoutDot(self):
        pass

    def countProcOfSubjectStartsWithCapitalLetter(self):
        pass

    def countProcOfSubjectInImperativeMood(self):
        pass

    def countProcOfBodyWrappedAt72Chars(self):
        pass

    def countProcOfSubjectLineSeparatedFromBody(self):
        pass

    def countProcOfBodyExplenatory(self):
        pass