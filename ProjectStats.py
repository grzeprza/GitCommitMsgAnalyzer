from numpy import gradient

from StatUtils import getWords
from NLPmodule import getPartOfSpeechSummaryDict

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
    _wordsPerCommitsDict = None

    def __init__(self, commits):
        self.commits = commits
        self.numberOfCommits = len(commits)

    def countAvgCommitsPerUser(self):
        if self._avgCommitsPerUser == -1.0:
            nbrOfUsers = len(self.getUniqueAuthorsDict().keys())
            # print(str(self.numberOfCommits) + " / " + str(nbrOfUsers))
            self._avgCommitsPerUser = self.numberOfCommits / nbrOfUsers
        return self._avgCommitsPerUser

    def countOneCommitAuthorsNumber(self):
        counteOneCommiters = 0
        for value in self._uniqueAuthorsDict.values():
            if value == 1:
                counteOneCommiters += 1
        return counteOneCommiters

    def inspectUsedPartOfSpeech(self):
        if self._partOfSpeech is None:
            partOfSpeech = getPartOfSpeechSummaryDict(self.commits)
            # print(partOfSpeech)
            sum = 0
            self._partOfSpeech = dict()

            for (k,v) in partOfSpeech.items():
                # print (k + " " + v)
                sum += v

            for (k,v) in partOfSpeech.items():
                self._partOfSpeech.setdefault(k, round(v/sum,2) )

        return self._partOfSpeech


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


    def getWordsPerCommitsDict(self):
        if self._wordsPerCommitsDict is None:
            commitDict = dict()
            for commit in self.commits:
                if commitDict.get(commit._id, 0) == 0:
                    sumOfAllWords = 0
                    for line in commit._all:
                        sumOfAllWords += len(getWords(line[0]))
                    commitDict.setdefault(commit._id, sumOfAllWords)
                else:
                    print("Commits have the same id %s" % commit._id)
            self._wordsPerCommitsDict = commitDict
        return self._wordsPerCommitsDict

    def getPartOfSpeechDict(self):
        if self._partOfSpeech is None:
            self._partOfSpeech = getPartOfSpeechSummaryDict(self.commits)
        return self._partOfSpeech

    def __str__(self):
        return (
                "Word/Commit: " + str(self.countWordPerCommit()) + "\n" +
                "One Commit Authors: " + str(self.countOneCommitAuthorsNumber()) + "\n" +
                "Commit/User: " + str(self.countAvgCommitsPerUser()) + "\n" +
                "Authors count: " + str(len(self.getUniqueAuthorsDict())) + "\n" +
                "Commiters count: " + str(len(self.getUniqueCommitersDict())) + "\n"
                "Used parts of speech: " + str(self.getPartOfSpeechDict())
        )
