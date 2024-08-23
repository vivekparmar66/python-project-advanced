import os
import json


def getJSONContent(file, handle_errors=True):
    """
    Reads the JSON file and returns its content as a list of dictionaries.

    Arguments:
    file -- str: The path to the JSON file.
    handle_errors -- bool: If True, prints error messages; if False, errors are suppressed.

    Returns:
    list: A list of dictionaries representing the employee entries, or an empty list if an error occurs.
    """
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        if handle_errors:
            print(f"File not found: {file}")
        return []
    except Exception as e:
        if handle_errors:
            print(f"An unexpected error occurred: {e}")
        return []



def generateEmail(firstname, lastname):
    """
    Generates a company email address based on the first name and last name.

    Arguments:
    firstname -- str: The employee's first name.
    lastname -- str: The employee's last name.

    Returns:
    str: The generated email address.
    """
    email = f"{firstname[0].lower()}{lastname.lower()}@comp.com"
    return email


import os
import json


def generateFormattedFile(empList, ogPath):
    """
    Saves the formatted employee data into a new JSON file.

    Arguments:
    empList -- list: A list of dictionaries representing the processed employee entries.
    ogPath -- str: The original file path.
    """
    # Get the directory and filename
    directory, filename = os.path.split(ogPath)

    # Create the new filename with "_formatted.json"
    formatted_filename = filename.replace(".json", "_formatted.json")

    # Create the full path for the new file
    formatted_path = os.path.join(directory, formatted_filename)

    # Write the data to the new file
    with open(formatted_path, 'w') as f:
        json.dump(empList, f, indent=4)

    # Print confirmation
    print(f"Formatted file saved to {formatted_path}")


def generateSalary(jobId, state):
    """
    Calculates the employee's salary based on their job ID and state.

    Arguments:
    jobId -- str: The job ID of the employee (e.g., IT_REP, SA_MNG).
    state -- str: The US state the employee is located in.

    Returns:
    float: The calculated salary.
    """
    base_salaries = {
        "SALES": 60000,
        "IT": 80000,
        "HR": 70000
    }

    department = jobId.split('_')[0]
    is_manager = jobId.endswith('MNG')

    salary = base_salaries.get(department.upper(), 0)

    if is_manager:
        salary *= 1.05

    if state.upper() in ["NY", "CA", "OR", "WA", "VT"]:
        salary *= 1.015

    return salary


def processEachEmp(empList):
    """
    Processes each employee entry to format and validate the data.

    Arguments:
    empList -- list: The list of dictionaries where each dictionary is an employee entry.

    Returns:
    list: A list of dictionaries where each dictionary is a processed employee entry.
    """
    processed_emps = []

    for emp in empList:
        # Validate phone number
        phone = validatePhoneNumber(emp.get("Phone Number", ""))
        if phone == 1:
            continue  # Skip if phone number is invalid

        # Validate zip code
        zip_code = validateZips(emp.get("Zip Code", ""))
        if zip_code == 1:
            continue  # Skip if zip code is invalid

        # Format names and addresses
        emp["First Name"] = emp.get("First Name", "").strip().title()
        emp["Last Name"] = emp.get("Last Name", "").strip().title()
        emp["Address Line 1"] = emp.get("Address Line 1", "").strip().title()
        emp["Address Line 2"] = emp.get("Address Line 2", "").strip().title()
        emp["City"] = emp.get("City", "").strip().title()
        emp["Job Title"] = emp.get("Job Title", "").strip().title()

        # Generate email
        emp["Email"] = generateEmail(emp["First Name"], emp["Last Name"])

        # Generate salary
        emp["Salary"] = generateSalary(emp["Job ID"], emp["State"])

        # Remove last entry if it exists (assuming it's not needed as per your description)
        if "I declare that the above information is accurate." in emp:
            del emp["I declare that the above information is accurate."]

        # Add the validated and formatted employee to the processed list
        processed_emps.append(emp)

    return processed_emps


def validatePhoneNumber(phoneNumber):
    """
    Validates a phone number to ensure it is a 10-digit number.

    Arguments:
    phoneNumber -- str: The phone number of the employee.

    Returns:
    int: The 10-digit phone number if valid, otherwise 1 to indicate an error.
    """
    phoneNumber = phoneNumber.strip()
    if len(phoneNumber) == 10 and phoneNumber.isdigit():
        return int(phoneNumber)
    return 1  # Invalid


def validateZips(zipCode):
    """
    Validates a zip code to ensure it is a 5-digit number.

    Arguments:
    zipCode -- str: The zip code of the employee.

    Returns:
    int: The 5-digit zip code if valid, otherwise 1 to indicate an error.
    """
    zipCode = zipCode.strip()
    if len(zipCode) == 5 and zipCode.isdigit():
        return int(zipCode)
    return 1  # Invalid


