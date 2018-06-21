from tokenize import group

import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

def groupPartOfSpeech(tag):
    puntuaction = (".", ",", "?", "!", "'", "\"", ":", ";", "...", "[", "]", "(", ")", "#", "''", "`", "``")
    if str(tag).startswith(puntuaction):
        return '.'

    if str(tag).startswith("RB"):
        return 'Adverb'

    if str(tag).startswith("R"):
        return "Particle"

    if str(tag).startswith("VB"):
        return "Verb"

    if str(tag).startswith("JJ"):
        return "Adjective"

    if str(tag).startswith("NN"):
        return "Noun"

    if str(tag).startswith("PR"):
        return "Pronoun"

    return tag

def getPartOfSpeechSummaryDict(commits):
    partOfSpeechDict = dict()

    for commit in commits:
        lines = ""
        for line in commit._all:
            lines += str(line[0])
        # print(lines)
        wordos = nltk.word_tokenize(lines)
        # print(wordos)
        parsed = nltk.pos_tag(wordos)
        # print(parsed)
        tag = nltk.FreqDist(parsed)
        # print(tag.most_common())

        for (tag, count) in tag.most_common():
            groupedTag = groupPartOfSpeech(tag[1])
            if partOfSpeechDict.get(groupedTag, 0) == 0:
                partOfSpeechDict.setdefault(groupedTag, count)
            else:
                partOfSpeechDict[groupedTag] = partOfSpeechDict.get(groupedTag) + count
    return partOfSpeechDict

def isFirstWordImperative(sentence):

    #Problem: NLTK perceives VBP as NN
    #Solutions: insert "they" to force imperative mood
    #Source: https: // stackoverflow.com / questions / 9406093 / nltk - thinks - that - imperatives - are - nouns?utm_medium = organic & utm_source = google_rich_qa & utm_campaign = google_rich_qa1
    wordos = nltk.word_tokenize("They "+sentence)
    # print(wordos)
    parsed = nltk.pos_tag(wordos)
    # print(parsed)

    if len(parsed) <= 1:
        return False

    word,tag = parsed[1]
    if tag == "VBP":
        return True
    else:
        return False
