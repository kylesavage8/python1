import os
import re

if __name__ == '__main__':
    if os.access("access.txt", os.F_OK):
        print("The file exists.")

    f = open("access.txt", "r")
    getlines = f.readlines()

    for line in getlines:
        findingstuff = re.findall(".$", line)
        for i in findingstuff:
            if i == "%":
                print(f"Line: {line}")
                print(f"The last character is {i} in the sentence above.")

    if os.access("access.txt", os.F_OK):
        print("The file access.txt exists.")
    try:
        os.renames("access.txt", "new_access.txt")
        print("Changed access.txt to new_access.txt")
        if os.access("access.txt", os.F_OK):
            print("The file access.txt no longer exists.")
    except:
        pass
    if "Users" in os.getcwd():
        print("Username is: ", re.split("\\\\", os.getcwd())[2])
    print("Drive is: ", re.split('\\\\', os.getcwd())[0])



