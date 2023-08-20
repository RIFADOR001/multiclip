from functions import *
from termcolor import colored


# clipboard.copy('<(")')
# data = clipboard.paste()
# print(data)
# SAVED_DATA = "clipboard.json"
# CRYPTO_SAVED_DATA = "cryptoclipboard.json"
# PASSCODE = "tacos"
# bug: the file doesn't display if it has not been used
# print ~~~~~~~~~~ or something every iteration of the while (colors
# Main function
def crypto_main():
    # Variable to keep running the program
    waiting = True
    # Passcode to be used
    passcode = None
    # Directory and file to be used
    folder = "multiclipboard_files"
    # file = "multiclipboard.json"
    file = "multi.json"
    # Dictironary with the commmands
    commands = commands_dict()
    # Length of the information to display
    length = 40
    # Verifies if the directory exists
    check_directory(folder)
    # Principal loop
    while waiting:
        print(colored("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", "green"))
        # Reads command, eliminates spaces at beginning and end and converts into lowercase
        command = input("Please write your command: \n(For more information use the command <<commands>>)\n")
        command = command.strip().lower()
        if command == "save":
            indicate_passcode_file(file, passcode)
            save(file, passcode)
        elif command == "load":
            indicate_passcode_file(file, passcode)
            load(file, passcode)
        elif command == "list":
            indicate_passcode_file(file)
            print_dict(load_dict(file), length)
        elif command == "delete":
            indicate_passcode_file(file)
            delete(file)
        elif command == "keys":
            indicate_passcode_file(file)
            keys(file)
        elif command == "close":
            waiting = False
        elif command == "commands":
            print_dict(commands)
        elif command == "set passcode":
            passcode = input("Please type your passcode: ")
        elif command == "erase passcode":
            passcode = None
        elif command == "change file":
            file = change_file(file)
        elif command == "length":
            length = enter_number()
        elif command == "files":
            list_files()
        # elif command == "show":
        #     print(passcode)
        elif command == "add note":
            add_note(file)
        else:
            print("Unknown command")
        print(colored(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<", "yellow"))


if __name__ == "__main__":
    # example_main()
    # better_main()
    crypto_main()
