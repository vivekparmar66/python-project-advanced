
import os.path

def checkPath(filePath, dataFiles):
    print(f"Checking path: {filePath}")
    if not os.path.exists(filePath):
        raise FileNotFoundError(f"The path '{filePath}' does not exist.")

    elif os.path.isdir(filePath):
        for file in os.listdir(filePath):
            checkPath(os.path.join(filePath, file), dataFiles)
    elif filePath.endswith(".json"):
        dataFiles.append(filePath)
    return tuple(dataFiles)

def getUsrInput(msg):
    """
    Prompts the user with a given message and returns their input.

    Arguments:
    msg -- str: The message to prompt the user.

    Returns:
    str: The user’s input.
    """
    return input(f"{msg}: ")
