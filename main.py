#own
import FileUtils
from StatUtils import drawHistogram
from StatUtils import analyzeComit
from ProjectStats import ProjectStats
file_path = FileUtils.chooseFile()

fileContent = ""
parseCommitsFromFile = False
genProjStats = False
genCommitAnalysis = False
saveResultToFile = False

# Parses commits based on headers =======================================================
if(parseCommitsFromFile):
    parsedCommits = FileUtils.parseFile(file_path)

    print("Succesfully parsed %d commits" % len(parsedCommits))
    fileContent += "Succesfully parsed %d commits\n\n" % len(parsedCommits)
else:
    print("\nParsing Commits form file skipped.\n")

# Gather project statistics =============================================================
if(genProjStats):
    projStatsTitle = "Project statistics"
    projStats = ProjectStats(parsedCommits)
    projStats.countAvgCommitsPerUser()
    projStats.countOneCommittersNumber()
    projStats.countWordPerCommit()
    # projStats.inspectUsedPartOfSpeech()
    print("Authors count : %d" % len(projStats.getUniqueAuthorsDict())) #TODO: ON kubernetes github - 1693, excel - 1980, program - 1997
    print("Commiters count : %d" % len(projStats.getUniqueCommitersDict())) #TODO: on kubernetes 1867
    print(projStats)
else:
    print("\nGenerating general project statistics skipped.\n")

# Analyze commits =======================================================================
if(genCommitAnalysis):
    analyzedCommits = []
    for commit in parsedCommits:
        analyzedCommits.append(analyzeComit(commitToAnal=commit))

    for commitStat in analyzedCommits:
        print (commitStat.readible() + "\n")

    print("Succesfully analyzed %d commits" % len(analyzedCommits))
else:
    print("\nAnalyzing commits skipped.\n")

# Save results to File ==================================================================
if(saveResultToFile):
    summaryFile = open("./summary.txt","w")
    summaryFile.write(fileContent)
    summaryFile.close()
else:
    print("\nSaving results to file skipped.\n")
