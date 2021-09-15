# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def my_functionname():
    # Get the user's name
    name = input("What is your name:")
    # Print the user's name
    print(f' Hello {name}')

def my_functionnumber():
    # Get the user's number
    number = int(input("What number do you want:"))
    number = number * number
    # Print the user's number by multiply that number by itself
    print(f'Your number is:',number)

def my_functionword():
    # Get the user's for any word
    word = input('What is your word:')
    count = len(word)
    # Print the user's word and counts how many letters are in that word
    print(f'Your word is {word}',count)

#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    my_functionname()
    my_functionnumber()
    my_functionword()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
