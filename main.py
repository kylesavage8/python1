import re
import os

if __name__ == '__main__':
    if os.access("regex.txt", os.F_OK):
        print("File is there.")
    # Make f_ok open the regex.txt to read the file
    f = open("regex.txt", "r")
    getlines = f.readlines()
    # Make a for loop so le = line gets the line
    for le in getlines:
        locateitems = re.locateall(".$", le)
        # Make a nested for loop so i = "%"
        for i in locateitems:
            if i == "%":
                # Print the line
                print(f"le: {le}")
                # Print the final character in the previous line
                print(f"Final character is {i} in the previous print line")
    # Make a if statement to check if the regex.txt file is still there
    if os.access("regex.txt", os.F_OK):
        print("File regex.txt is there.")
    try:
        # Rename the text file to something else
        os.rename("regex.txt", "new_regex.txt")
        # Print the new text file
        print("Renamed regex.txt -> new_regex.txt")
        if os.access("regex.txt", os.F_OK):
            # Print to check if the original text file was properly removed
            print("File regex.txt was removed.")
    except:
        pass
    # Make an if statement to return the absolute path of the working directory
    if "Current computer accounts" in os.getcwd():
        print("Login name: ", re.split("\\\\", os.getcwd())[2])
        print("Current directory: ", re.split('\\\\', os.getcwd())[0])