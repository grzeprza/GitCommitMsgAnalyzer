import os
#own
import FileUtils
import StatUtils
from StatUtils import drawHistogram
from StatUtils import analyzeComit
from ProjectStats import ProjectStats

file_path = FileUtils.chooseFile()

fileContent = ""
fileSeparated = str(file_path).split('/')
projectName = fileSeparated[len(fileSeparated)-1]
parseCommitsFromFile = True
genProjStats = True
genCommitAnalysis = False
prodImages = True
saveResultToFile = False

# Parses commits based on headers =======================================================
if(parseCommitsFromFile):
    parsedCommits = FileUtils.parseFile(file_path)

    print("Succesfully parsed %d commits" % len(parsedCommits))
    fileContent += "Succesfully parsed %d commits\n\n" % len(parsedCommits)

else:
    print("\nParsing Commits form file skipped.\n")

# Gather project statistics =============================================================
if(genProjStats and parseCommitsFromFile):
    projStatsTitle = "Project statistics"
    projStats = ProjectStats(parsedCommits)
    projStats.countAvgCommitsPerUser()
    projStats.countOneCommitAuthorsNumber()
    projStats.countWordPerCommit()
    # projStats.inspectUsedPartOfSpeech()

    print(projStats)
    fileContent += str(projStats)
else:
    print("\nGenerating general project statistics skipped.\n")

# Analyze commits =======================================================================
if(genCommitAnalysis and parseCommitsFromFile):
    analyzedCommits = []
    for commit in parsedCommits:
        analyzedCommits.append(analyzeComit(commitToAnal=commit))

    for commitStat in analyzedCommits:
        print (commitStat.readible() + "\n")

    print("Succesfully analyzed %d commits" % len(analyzedCommits))
else:
    print("\nAnalyzing commits skipped.\n")
# Produce image analysis ================================================================
if(prodImages and genProjStats):
    # StatUtils.drawCommitAuthorHistogram(str(projectName), projStats.getUniqueAuthorsDict(), "Authors Count", "Nbr of Commits")
    # StatUtils.drawWordPerCommitHistogram(str(projectName), projStats.getWordsPerCommitsDict(), "Commits Count", "Nbr of Words")
    StatUtils.drawPartsOfSpeechBarChart(str(projectName), projStats.getPartOfSpeechDict())
# Save results to File ==================================================================
if(saveResultToFile):
    if(fileContent == ""):
        print("No content to save to file")
        exit(0)
    summaryFile = open("./summary.txt","w")
    summaryFile.write(fileContent)
    summaryFile.close()
else:
    print("\nSaving results to file skipped.\n")
