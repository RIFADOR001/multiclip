import os
import json
from crypto import encode_text, decode_text
from termcolor import colored
import clipboard


# Saves the data on the file, with the key
# If the file does not exist, it is created
def save_data(file, data, key):
    folder = "multiclipboard_files"
    path = os.path.join(folder, file)
    try:
        with open(path, "r") as fl:
            my_dict = json.load(fl)
        my_dict[key] = [data]
        print(my_dict[key])
        with open(path, "w") as f:
            json.dump(my_dict, f)
    except FileNotFoundError:
        new_dict = dict()
        new_dict[key] = [data]
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
        print("File not found")
        return {}
    except NotADirectoryError:
        print("Not a directory")
        return {}
    return my_dict


# Loads the date from the indicated key and file
def load_data(file, key):
    my_dict = load_dict(file)
    return my_dict[key][0]


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
    key = input(f"Please write the key of the data you want: ").strip()
    my_dict = load_dict(file)
    # if not verify_available_key(path, key):
    if key in my_dict:
        crypto_data = load_data(file, key)
        data = decode_text(crypto_data, passcode)
        clipboard.copy(data)
        print(f"You have loaded: \n <<{data}>> \n")
    else:
        print("We could not find that key. \nNo data has been loaded...")


# Asks for a key to delete data from the file
def delete(file):
    key = input("Please enter the key of the data that you want to delete...\n")
    if not verify_available_key(file, key):
        delete_data(file, key)
        print("The data has been deleted...")
    else:
        print("We could not find that key. \nNo data has been deleted...")


# Displays a list of the keys on the file
def keys(file):
    my_dict = load_dict(file)
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
    print(colored(f'The file in use is {file}\n', 'yellow'))
    if passcode is not None:
        print(colored('A passcode is in use...', 'red'))


# Verifies if the directory exists. If not, it will be created
def check_directory(directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)


# If the user indicates, a file will be created
def create_file(file):
    my_path = os.path.dirname(__file__)  # <-- absolute dir the script is in
    folder = "multiclipboard_files"
    path = os.path.join(folder, file)
    path1 = os.path.join(my_path, folder)
    path2 = os.path.join(path1, file)
    script_path = os.path.abspath(__file__)  # i.e. /path/to/dir/foobar.py
    script_dir = os.path.split(script_path)[0]  # i.e. /path/to/dir/
    path3 = os.path.join(script_dir, folder)
    path4 = os.path.join(path3, file)
    pwd = os.getcwd()
    path5 = os.path.join(pwd, folder)
    path6 = os.path.join(path5, file)
    answer = None
    waiting = True
    while waiting:
        answer = input("The selected file does not exist. Do you want to create it? \n Yes or No \n").lower()
        if answer == "yes" or answer == "no":
            waiting = False
    if answer == "yes":
        new_dict = dict()
        with open(path6, "w") as f:
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


def add_note(file):
    folder = "multiclipboard_files"
    my_dict = load_dict(file)
    key = input("Enter the key to add note: ").strip()
    if key in my_dict.keys():
        note = input("Write your note to add: ").strip()
        my_dict[key].append(note)
        path = os.path.join(folder, file)
        with open(path, "w") as f:
            json.dump(my_dict, f)
    else:
        print("The key has not been found")


if __name__ == "__main__":
    create_file("cocoa001.json")
