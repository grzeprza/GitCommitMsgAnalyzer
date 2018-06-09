from StatUtils import getWords

class ProjectStats(object):

    #list of commits
    commits = []
    #number of commits
    numberOfCommits = -1

    #general statistic
    _avgCommitsPerUser = -1.0
    _countOneCommitersNumber = -1.0
    _partOfSpeech = None
    _wordPerCommit = -1.0

    #helpful variables
    #dictionary (author name, nbr of commits)
    _uniqueAuthorsDict = None
    _uniqueCommitersDict = None

    def __init__(self, commits):
        self.commits = commits
        self.numberOfCommits = len(commits)

    def countAvgCommitsPerUser(self):
        if self._avgCommitsPerUser == -1.0:
            nbrOfUsers = len(self.getUniqueAuthorsDict().keys())
            # print(str(self.numberOfCommits) + " / " + str(nbrOfUsers))
            self._avgCommitsPerUser = self.numberOfCommits / nbrOfUsers
        return self._avgCommitsPerUser

    def countOneCommittersNumber(self):
        counteOneCommiters = 0
        for value in self._uniqueAuthorsDict.values():
            if value == 1:
                counteOneCommiters += 1
        return counteOneCommiters

    def inspectUsedPartOfSpeech(self):
        raise NotImplemented("Used Part Of Speech Stats not implemented")

    def countWordPerCommit(self):
        if self._wordPerCommit == -1.0:
            sumOfAllWords = 0
            for commit in self.commits:
                for line in commit._all:
                    sumOfAllWords += len(getWords(line[0]))
            self._wordPerCommit = sumOfAllWords / self.numberOfCommits
        return self._wordPerCommit

    def getUniqueAuthorsDict(self):
        if self._uniqueAuthorsDict is None:
            authorsDict = dict()
            for commit in self.commits:
                if authorsDict.get(commit._author, 0) == 0:
                    nbrOfCommits = 0
                    authorsDict.setdefault(commit._author, 0)
                else:
                    nbrOfCommits = authorsDict.get(commit._author)
                authorsDict[commit._author] = (nbrOfCommits + 1)
            self._uniqueAuthorsDict = authorsDict
        return self._uniqueAuthorsDict

    def getUniqueCommitersDict(self):
        if self._uniqueCommitersDict is None:
            commitersDict = dict()
            for commit in self.commits:
                if commitersDict.get(commit._committer, 0) == 0:
                    nbrOfCommits = 0
                    commitersDict.setdefault(commit._committer, 0)
                else:
                    nbrOfCommits = commitersDict.get(commit._committer)
                commitersDict[commit._committer] = (nbrOfCommits + 1)
            self._uniqueCommitersDict = commitersDict
        return self._uniqueCommitersDict

    def __str__(self):
        return (
                "Word/Commit: " + str(self.countWordPerCommit()) + "\n" +
                "One Committers: " + str(self.countOneCommittersNumber()) + "\n" +
                "Commit/User: " + str(self.countAvgCommitsPerUser()) + "\n" +
                "Authors count: " + str(len(self.getUniqueAuthorsDict())) + "\n" +
                "Commiters count: " + str(len(self.getUniqueCommitersDict()))
        )



