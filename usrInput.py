import os.path


def checkPath(filePath, dataFiles):
    if not os.path.exists(filePath):
        print(filePath + " does not exist.")
        return "doesn't exist"
    elif os.path.isdir(filePath):
        for file in os.listdir(filePath):
            checkPath(os.path.join(filePath, file), dataFiles)
    elif filePath.endswith("_formatted.json"):
        dataFiles.append(filePath)
    return tuple(dataFiles)
