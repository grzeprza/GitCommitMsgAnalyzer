import re #use regex
#own
from CommitStats import CommitStats

def analyzeComit(commitToAnal):
    stats = CommitStats(commitId= commitToAnal._id, author= commitToAnal._author)
    stats.isS50Ch(subject=commitToAnal._subject)
    stats.subjectEndsWithoutDot(subject=commitToAnal._subject)
    stats.subjectStartsWithCapitalLetter(subject=commitToAnal._subject)
    stats.subjectLineSeparatedWithBody(body= commitToAnal._body, all=commitToAnal._all)
    stats.bodyWrapped72Chars(body= commitToAnal._body)
    return stats

def binaryValue(variable):
        return 1 if variable is True else 0

def getWords(text):
    #returns array containing words from sentence
    return re.compile('\w+').findall(text)

def drawHistogram(data, ylabel, xlabel, isLogY, bins):
    pass