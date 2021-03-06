import os
#own
from scipy.io.arff.arffread import go_data

import FileUtils
import StatUtils
from StatUtils import drawHistogram
from StatUtils import analyzeComit
from ProjectStats import ProjectStats
from GoldenRulesStats import GoldenRulesStats
from ParamCorrelation import ParamCorrelation

file_path = FileUtils.chooseFile()

fileContent = ""
fileSeparated = str(file_path).split('/')
projectName = fileSeparated[len(fileSeparated)-1]
parseCommitsFromFile = True
genProjStats = True
genCommitAnalysis = True
genGoldenRulesStats = False
prodImages = False
saveResultToFile = True

# Parses commits based on headers =======================================================
if(parseCommitsFromFile):
    parsedCommits = FileUtils.parseFile(file_path)

    print("Succesfully parsed %d commits" % len(parsedCommits))
    fileContent += "Succesfully parsed %d commits\n" % len(parsedCommits)

else:
    print("\nParsing Commits form file skipped.\n")

print("\n")
fileContent += "\n"
# Gather project statistics =============================================================
if genProjStats and parseCommitsFromFile:
    projStatsTitle = "Project statistics"
    projStats = ProjectStats(parsedCommits)
    projStats.countAvgCommitsPerUser()
    projStats.countOneCommitAuthorsNumber()
    projStats.countWordPerCommit()
    projStats.inspectUsedPartOfSpeech()

    print("General project statistics:")
    print(projStats)
    fileContent += "General project statistics:\n"
    fileContent += str(projStats)
else:
    print("\nGenerating general project statistics skipped.\n")

print("\n")
fileContent +="\n"
# Analyze commits =======================================================================
if genCommitAnalysis and parseCommitsFromFile:
    analyzedCommits = []
    for commit in parsedCommits:
        analyzedCommits.append(analyzeComit(commitToAnal=commit))

    # for commitStat in analyzedCommits:
    #     print (commitStat.readible() + "\n")

    print("Succesfully analyzed %d commits" % len(analyzedCommits))
else:
    print("\nAnalyzing commits skipped.\n")

print("\n")
fileContent +="\n"
# Good and Bad commits classification ==================================================
if genCommitAnalysis and parseCommitsFromFile:
    totalSize = len(analyzedCommits)

    goodCommitsCount = 0;
    for commit in analyzedCommits:
        goodRules = 0
        if commit. _isSubjectLt50Char:
            goodRules = goodRules + 1
        if commit._subjectEndsWithoutDot:
            goodRules = goodRules + 1
        if commit._subjectStartWithCapitalLetter:
            goodRules = goodRules + 1
        if commit._isSubjectInImperativeMood:
            goodRules = goodRules + 1
        if commit._isBodyWrappedAt72Chars:
            goodRules = goodRules + 1
        if commit._subjectLineSeparatedFromBody:
            goodRules = goodRules + 1
        # if commit._isBodyExplenatory

        if goodRules >= 5:
            goodCommitsCount = goodCommitsCount + 1

    print (goodCommitsCount/totalSize)
    fileContent += "Proc of Good Commits: " + str(goodCommitsCount/totalSize)

print("\n")
fileContent +="\n"
# Perason Correlation between variables =================================================
if genCommitAnalysis and parseCommitsFromFile:
    pearsonCorrelation = ParamCorrelation(analyzedCommits)
    pearsonCorrelation.extractData()
    pearsonCorrelation.countCorrelation()

    print(str(pearsonCorrelation))
    fileContent += "Phi Correlation:\n"
    fileContent += str(pearsonCorrelation)

print("\n")
fileContent +="\n"
# Gather Golden Rules stats ===================================================================
if genGoldenRulesStats and genCommitAnalysis:
    grs = GoldenRulesStats(analyzedCommits)
    grs.countProcOfSubjectStartsWithCapitalLetter()
    grs.countProcOfSubjectLt50Char()
    grs.countProcOfSubjectInImperativeMood()
    grs.countProcOfSubjectEndsWithoutDot()
    grs.countProcOfBodyWrappedAt72Chars()
    grs.countProcOfBodyExplenatory()
    grs.countProcOfSubjectLineSeparatedFromBody()

    print("Golden Rules statistics:")
    print(str(grs))
    fileContent += "Golden Rules statistics:\n"
    fileContent += str(grs)
else:
    print("Gathering commits statistics skipped.\n")

# Produce image analysis ================================================================
if prodImages and genProjStats:
    StatUtils.drawCommitAuthorHistogram(str(projectName), projStats.getUniqueAuthorsDict(), "Authors Count", "Nbr of Commits")
    StatUtils.drawWordPerCommitHistogram(str(projectName), projStats.getWordsPerCommitsDict(), "Commits Count", "Nbr of Words")
    StatUtils.drawPartsOfSpeechBarChart(str(projectName), projStats.getPartOfSpeechDict())

# Save results to File ==================================================================
if saveResultToFile :
    if fileContent == "":
        print("No content to save to file")
        exit(0)
    summaryFile = open("./summary-" + projectName, "w")
    summaryFile.write(fileContent)
    summaryFile.close()
else:
    print("\nSaving results to file skipped.\n")
