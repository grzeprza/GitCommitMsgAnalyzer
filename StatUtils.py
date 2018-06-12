import re #use regex
from collections import OrderedDict

import matplotlib.pyplot as plt
import numpy as np
import itertools as it
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

def drawCommitAuthorHistogram(projectName, data, ylabel, xlabel):
    MIN, MAX = 1, len(data.keys())
    plt.figure()
    plt.hist(data.values(), bins=10 ** np.linspace(np.log10(MIN), np.log10(MAX), 100))
    plt.gca().set_xscale("log")
    plt.gca().set_yscale("log")
    drawHistogram(projectName,data, ylabel, xlabel)
    plt.show()

def drawHistogram(projectName, data, ylabel, xlabel):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(projectName)
    return plt


def drawWordPerCommitHistogram(projectName, data, ylabel, xlabel):
    MIN, MAX = 1, len(data.keys())
    plt.figure()
    plt.hist(data.values(), bins=10 ** np.linspace(np.log10(MIN), np.log10(MAX), 100))
    plt.gca().set_xscale("log")
    plt.gca().set_yscale("log")
    drawHistogram(projectName, data, ylabel, xlabel)
    plt.show()


def drawPartsOfSpeechBarChart(projName, partOfSpeechDict):
    # plt.bar(partOfSpeechDict)
    # plt.title(projName)
    # plt.draw()
    partOfSpeechDict = OrderedDict(sorted(partOfSpeechDict.items(), key=lambda x: x[1], reverse=True))
    objects = partOfSpeechDict.keys()
    y_pos = np.arange(len(objects))
    performance = partOfSpeechDict.values()

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Count')
    plt.title(projName)
    plt.gca().set_yscale("log")
    plt.xticks(rotation=90)

    plt.show()