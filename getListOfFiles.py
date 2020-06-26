import os

def getListOfFiles(dirName):
    """
    Get a list of files in folder and subfolders of dirName
	:param dirName: relative or absolute path to the directory
	:return: List of files
    """

    listOfFile = os.listdir(dirName)
    allFiles = []

    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles += getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles
