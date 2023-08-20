import clipboard
import json
from crypto import encode_text, decode_text
from termcolor import colored
import os

# clipboard.copy('<(")')
# data = clipboard.paste()
# print(data)

# SAVED_DATA = "clipboard.json"
# CRYPTO_SAVED_DATA = "cryptoclipboard.json"
# PASSCODE = "tacos"

# bug: the file doesn't display if it has not been used
# print ~~~~~~~~~~ or something every iteration of the while (colors


# Saves the data on the file, with the key
# If the file does not exist, it is created
def save_data(file, data, key):
    folder = "multiclipboard_files"
    path = os.path.join(folder, file)
    try:
        with open(path, "r") as fl:
            my_dict = json.load(fl)
        my_dict[key] = data
        with open(path, "w") as f:
            json.dump(my_dict, f)
    except FileNotFoundError:
        new_dict = dict()
        new_dict[key] = data
        with open(path, "w") as f:
            json.dump(new_dict, f)


# Loads the dictionary from the file
def load_dict(file):
    folder = "multiclipboard_files"
    path = os.path.join(folder, file)
    try:
        with open(path, "r") as f:
            my_dict = json.load(f)
    except FileNotFoundError:
        return {}
    except NotADirectoryError:
        return {}
    return my_dict


# Loads the date from the indicated key and file
def load_data(file, key):
    folder = "multiclipboard_files"
    path = os.path.join(folder, file)
    my_dict = load_dict(path)
    return my_dict[key]


# Deletes the data with the indicated key in the file
def delete_data(file, key):
    folder = "multiclipboard_files"
    path = os.path.join(folder, file)
    with open(path, "r") as fl:
        my_dict = json.load(fl)
    del my_dict[key]
    with open(path, "w") as f:
        json.dump(my_dict, f)


# Verifies if the key is available to avoid overwriting data
def verify_available_key(file, key):
    folder = "multiclipboard_files"
    path = os.path.join(folder, file)
    my_dict = load_dict(file)
    if key in my_dict:
        return False
    return True


# Saves the data into the file. If a passcode is set, the data is encrypted
def save(file, passcode=None):
    data = clipboard.paste()
    folder = "multiclipboard_files"
    path = os.path.join(folder, file)
    key = input(f"Please write a key for this data:  \n <<{data}>> \n").strip()
    if verify_available_key(path, key):
        crypto_data = encode_text(data, passcode)
        save_data(file, crypto_data, key)
        print("The data has been saved...")
    else:
        print("That key is already in use. \nThe data was not saved.")


# Loads the data from the file. If a passcode is set, it will be decrypted
def load(file, passcode=None):
    folder = "multiclipboard_files"
    path = os.path.join(folder, file)
    key = input(f"Please write the key of the data you want: ").strip()
    if not verify_available_key(path, key):
        crypto_data = load_data(path, key)
        data = decode_text(crypto_data, passcode)
        clipboard.copy(data)
        print(f"You have loaded: \n <<{data}>> \n")
    else:
        print("We could not find that key. \nNo data has been loaded...")


# Asks for a key to delete data from the file
def delete(file):
    # folder = "multiclipboard_files"
    # path = os.path.join(folder, file)
    key = input("Please enter the key of the data that you want to delete...\n")
    if not verify_available_key(file, key):
        delete_data(file, key)
        print("The data has been deleted...")
    else:
        print("We could not find that key. \nNo data has been deleted...")


# Displays a list of the keys on the file
def keys(file):
    folder = "multiclipboard_files"
    path = os.path.join(folder, file)
    my_dict = load_dict(path)
    print(list(my_dict.keys()))


# A dictionary with the commands (and explanations) is defined. The user can check the commands
def commands_dict():
    command_dict = dict()
    command_dict["save"] = "Save the clipboard data into the selected file"
    command_dict["load"] = "Load into the clipboard the data represented by the selected key"
    command_dict["delete"] = "Delete the data on the file associated to the key"
    command_dict["keys"] = "Display the list of keys"
    command_dict["change file"] = "Selects a different file to write and load data"
    command_dict["files"] = "Displays the files saved"
    command_dict["set passcode"] = "Sets a passcode to be used to write and load data"
    command_dict["erase passcode"] = "Resets the passcode, so the written and loaded data use no passcode"
    command_dict["commands"] = "Displays the list of commands"
    command_dict["length"] = "Changes the maximum of characters to show when listing data"
    command_dict["close"] = "Closes the program"
    return command_dict


# Prints a dictionary. It is possible to indicate length of the data displayed to avoid too many characters
# on screen. The characters are printed with colors
def print_dict(my_dict, length=None):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for k in my_dict.keys():
        print(f'{colored(k, "yellow")}: {colored(my_dict[k][:length], "green")}')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Gets a number from the user to define length of the data to show
def enter_number():
    n = None
    waiting = True
    while waiting:
        try:
            n = int(input("Please enter the desired length: "))
            if n < 5:
                print("The value needs to be bigger than 4")
            else:
                waiting = False
        except ValueError:
            print("You need to enter a number")
    return n


# If a passcode is set, it will be indicated. The current file is also indicated
def indicate_passcode_file(file, passcode=None):
    # print(colored('hello', 'red'), colored('world', 'green'))
    folder = "multiclipboard_files"
    path = os.path.join(folder, file)
    print(colored(f'The file in use is {path}\n', 'yellow'))
    if passcode is not None:
        print(colored('A passcode is in use...', 'red'))


# Verifies if the directory exists. If not, it will be created
def check_directory(directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)


# If the user indicates, a file will be created
def create_file(file):
    folder = "multiclipboard_files"
    path = os.path.join(folder, file)
    waiting = True
    while waiting:
        answer = input("The selected file does not exist. Do you want to create it? \n Yes or No \n").lower()
        if answer == "yes" or answer == "no":
            waiting = False
    if answer == "yes":
        new_dict = dict()
        with open(path, "w") as f:
            json.dump(new_dict, f)
        return True
    else:
        print("Please select an existing file")
        return False


# Gives format to be sure that the file used is always a json
def make_json(file):
    if file[-5:] == ".json":
        return file
    return file+".json"


# Displays the list of files available
def list_files():
    print("The available files are the following...")
    print(os.listdir("multiclipboard_files"))


# Changes file to the indicated one. If it doesn't exist, it can be created
def change_file(file):
    folder = "multiclipboard_files"
    aux_file = make_json(input("Please enter the name of the file that you want to use: "))
    aux_path = os.path.join(folder, aux_file)
    if not os.path.isfile(aux_path):
        if create_file(file):
            file = aux_file
    else:
        return aux_file
    return file

# Main function
def crypto_main():
    # Variable to keep running the program
    waiting = True
    # Passcode to be used
    passcode = None
    # Directory and file to be used
    folder = "multiclipboard_files"
    file = "multiclipboard.json"
    path = os.path.join(folder, file)
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
        else:
            print("Unknown command")
        print(colored(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<", "yellow"))


if __name__ == "__main__":
    # example_main()
    # better_main()
    crypto_main()

