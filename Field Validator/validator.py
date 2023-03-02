import re

"""
Programm to validate input fields
There must be 5 fields, format:
Name: ...
e-mail: ...
Age: ...
Website: ...
BusinessTime: ...
"""

# Switch files to check program
#file = "valid_input.txt"
file = "unvalid_input.txt"

# Function to extract fileds from the file 
# You will get dictionary (example {"field 1": "..."})
def extractingFields(file):
    # Error handling to check if file exists
    try:
        with open(file) as file:
            lines = file.readlines()
            word_list = {}
            # Must be 5 lines 
            for i in range(5):
                word_list["field " + str(i+1)] = lines[i].rstrip()
            return word_list
    except FileNotFoundError:
        print("[-] Cannot open the file")
        return False


# Function to validate name 
# Return True or False + Errors
def nameValidation(field):
    # 3 because: filed Name, Name, Surname
    if len(field.split(" ")) == 3:
        # [1:3] - do not need field name
        name, surname = field.split(" ")[1:3]
        # Check if strings are capitilised
        if name[0].isupper() and surname[0].isupper():
            return True
        else:
            print("[-] Name or Surname is not capitalised")
            return False
    # Handling the posibility to have a middle name
    # 4 because: filed Name, Name, Middle name, Surname
    elif len(field.split(" ")) == 4:
        # [1:4] - do not need field name
        name, middlename, surname = field.split(" ")[1:4]
        # Check if strings are capitilised
        if name[0].isupper() and surname[0].isupper() and middlename[0].isupper():
            return True
        else:
            print("[-] Name, Surname or MiddleName is not capitalised")
            return False
    else:
        print("[-] Invalid Name")
        return False
    

# Function to validate email
# Return True or False + Errors
def emailValidation(field):
    email = field.split(" ")[1]
    # Main check to make validation faster
    if email and '@' in email:
        username, domain = email.split("@")
        # Using this site https://regex101.com/ to create regex pattern
        username_pattern = r"^(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])"
        domain_pattern = r"^((?![-])(?!.*[.]{2})[a-zA-Z0-9.]+(?<![-]))\.([a-zA-Z]{2,})"
        # function fullmatch to validate if every charecter match pattern
        if re.fullmatch(username_pattern, username) and re.fullmatch(domain_pattern, domain):
                return True
        else:
            print("[-] Email do not match the standarts of email")
            return False
    else:
        print("[-] Email is Invalid")
        return False


# Function to validate age
# Return True or False + Errors
def ageValidator(field):
    # Check happens using try except 
    try:
        field = int(field.split(" ")[1])
    except ValueError:
        print("[-] Age is Invalid")
        return False
    return int(field)
        

# Function to validate website
# Return True or False + Errors
def websiteValidator(field):
    web = field.split(" ")[1]
    # Using this site https://regex101.com/ to create regex pattern
    # Not working for all websites, but the simplest can check
    # Email shoud start with www.
    pattern = r"^www[.](?![-])(?<![_])+[a-zA-Z0-9]+.*"
    if re.fullmatch(pattern, web):
        return True
    else:
        print("[-] Website is invalid")
        return False


# Function to validate time
# Return True or False + Errors
def timeValidator(field):
    time = field.split(" ")[1]
    # Using this site https://regex101.com/ to create regex pattern
    pattern = r"^([0-1]?[0-9]|2[0-3]):[0-5][0-9]-([0-1]?[0-9]|2[0-3]):[0-5][0-9]$"
    if re.fullmatch(pattern, time):
        return True
    else:
        print("[-] Time is invalid")
        return False


# Main Function to obtain all boolean values and make final check
if __name__ == "__main__":
    fields = extractingFields(file)
    name = nameValidation(fields["field 1"])
    email = emailValidation(fields["field 2"])
    age = ageValidator(fields["field 3"])
    website = websiteValidator(fields["field 4"])
    businesstime = timeValidator(fields["field 5"])

    # Final check
    if name and email and age and website and businesstime:
        print("All fields are valid")
    else:
        print("Check mistakes above please")