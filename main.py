filename = input("File to save: ")

with open(filename + "file.txt", "w") as file:
    file.write(input("Insert file text: "))

counter_dict = {}
with open(filename + "file.txt") as file:
    line = file.readline()
    while line:
        line = line.strip()

        if line in counter_dict:
            counter_dict[line] += 1
        else:
            counter_dict[line] = 1

        line = file.readline()

        print(counter_dict)