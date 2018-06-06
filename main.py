
#own
import FileUtils
from StatUtils import drawHistogram
from StatUtils import analyzeComit
from ProjectStats import ProjectStats
file_path = FileUtils.chooseFile()

#parses commits based on headers
parsedCommits = FileUtils.parseFile(file_path)

print("Succesfully parsed %d commits" % len(parsedCommits))
#
# analyzedCommits = []
# for commit in parsedCommits:
#     analyzedCommits.append(analyzeComit(commitToAnal=commit))

# for commitStat in analyzedCommits:
#     print (commitStat.readible() + "\n")

# print("Succesfully analyzed %d commits" % len(analyzedCommits))

projStats = ProjectStats(parsedCommits)
projStats.countAvgCommitsPerUser()
projStats.countOneCommittersNumber()
projStats.countWordPerCommit()
# projStats.inspectUsedPartOfSpeech()

print(projStats)
# summaryFile = open("./summary.txt", "w")
# for committs in parsedCommits:
#     print(committs, end="", flush=True)
#     summaryFile.write(str(committs))
#     # print("\n")
#
# summaryFile.close()

