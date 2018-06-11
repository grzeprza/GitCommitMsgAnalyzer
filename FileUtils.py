import tkinter as tk
from tkinter import filedialog # to display file dialog
import sys #returning status on termination
import codecs #to open files with different coding

#own
from TxtFileHeaderEnum import TxtFileHeader
from Commit import Commit

def extractText(header, line):

    text = line.replace(header.value[0], "")
    # print(str(header.value) + " - " + text)
    noenters = text.replace("\n", "")
    return noenters.replace("\r", "")

def chooseFile():
    root = tk.Tk()
    root.withdraw()
    file_path =  filedialog.askopenfilename()
    if file_path == "":
        sys.exit("No file selected")

    return file_path

def parseFile(file_path):
    readsBody = False
    readsAll = False
    commits = []
    with codecs.open(file_path, encoding="utf8", errors='replace') as file:
        commit = Commit()
        commit._all = []
        commit._body = []
        for line in file:
            if readsBody:
                if not line.startswith(TxtFileHeader.ALL.value[0], 0, 10):
                    commit._body.append([line])
                else:
                    readsBody = False

            if readsAll:
                if not line.startswith(TxtFileHeader.ID.value[0], 0, 10):
                    commit._all.append([line])
                else:
                    readsAll = False

            if line.startswith(TxtFileHeader.ID.value[0], 0, 10):
                if commit._id != "":
                    commits.append(commit)
                    commit = Commit()
                    commit._body = []
                    commit._all = []
                commit._id = extractText(TxtFileHeader.ID, line)

            elif line.startswith(TxtFileHeader.AUTHOR.value[0], 0, 10):
                commit._author = extractText(TxtFileHeader.AUTHOR, line)

            elif line.startswith(TxtFileHeader.COMMITTER.value[0], 0, 10):
                commit._committer = extractText(TxtFileHeader.COMMITTER, line)

            elif line.startswith(TxtFileHeader.SUBJECT.value[0], 0, 10):
                commit._subject = extractText(TxtFileHeader.SUBJECT, line)

            elif line.startswith(TxtFileHeader.BODY.value[0], 0, 10):
                text = extractText(TxtFileHeader.BODY, line)
                commit._body.append([text])
                if len(text) > 0:
                    readsBody = True

            elif line.startswith(TxtFileHeader.ALL.value[0], 0, 10):
                text = extractText(TxtFileHeader.ALL, line)
                commit._all.append([text])
                if len(text) > 0:
                    readsAll = True
        commits.append(commit)
    return commits
