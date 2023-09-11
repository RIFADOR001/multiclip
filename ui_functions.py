import os
import json
from crypto import encode_text, decode_text
from termcolor import colored
import clipboard
from functions import load_dict, save_data


def dict_to_string(my_dict):
    text = '\n'.join(f"{x}: {my_dict[x]}" for x in my_dict.keys())
    return text

def ui_save(file, data, key, passcode=None):
    # data = clipboard.paste()
    my_dict = load_dict(file)
    if key in my_dict:
        return -1
        print("That key is already in use. \nThe data was not saved.")
    else:
        crypto_data = encode_text(data, passcode)
        save_data(file, crypto_data, key)
        return 0
        print("The data has been saved...")

# Loads the data from the file. If a passcode is set, it will be decrypted
def ui_load(file, key, passcode=None):
    my_dict = load_dict(file)
    if key in my_dict:
        data = my_dict[key][0]
        clipboard.copy(data)
        return 0
        print(f"You have loaded: \n <<{data}>> \n")
    else:
        return -1
        print("We could not find that key. \nNo data has been loaded...")



