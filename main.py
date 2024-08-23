import usrInput
import parseFile

def errorHandle(checkReturn):
    if isinstance(checkReturn, int) and checkReturn == 1:
        print("The path given was not valid. Exiting...")
        exit()
    elif isinstance(checkReturn, tuple) and not checkReturn:
        print("No valid files found to process. Exiting...")
        exit()

def printOutput(numFiles, numEmps):
    print("============================================================")
    print("---------------------Processing Summary---------------------")
    print("============================================================")
    print(f" Number of files processed: {numFiles}")
    print(f" Number of employee entries formatted and calculated: {numEmps}")

def startProcess(tup):
    numFiles = len(tup)
    totalEmps = 0

    for file in tup:
        # Get the JSON content
        empList = parseFile.getJSONContent(file)

        # Process each employee
        processedEmpList = parseFile.processEachEmp(empList)

        # Save the processed employees to a new formatted JSON file
        parseFile.generateFormattedFile(processedEmpList, file)

        # Update the total number of employees processed
        totalEmps += len(processedEmpList)

    # Print the summary
    printOutput(numFiles, totalEmps)

file_path = r"/Users/vivekparmar/Desktop/vivekparmar/core-python-project-advanced-full-sprint-vivek-parmar/testFiles"  # Update this path if necessary
valid_files = usrInput.checkPath(file_path, [])

# Handle errors
errorHandle(valid_files)

# Start processing the files
startProcess(valid_files)
