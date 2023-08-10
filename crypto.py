import string
import random


# Encrypts the text with the passcode. If the passcode is None, then
# the text is not modified
def encode_text(text, passcode=None):
    if passcode is None:
        return text
    random.seed(a=passcode)
    characters = " " + string.punctuation + string.digits + string.ascii_letters
    chars_list = list(characters)
    key_list = chars_list.copy()
    random.shuffle(key_list)
    aux_list = []
    for i in text:
        if i in key_list:
            char_index = key_list.index(i)
            aux_list.append(chars_list[char_index])
        else:
            aux_list.append(i)
    return "".join(aux_list)


# Decodes the text with the passcode. If the passcode is None, then
# the text is not modified
def decode_text(text, passcode=None):
    if passcode is None:
        return text
    random.seed(a=passcode)
    characters = " " + string.punctuation + string.digits + string.ascii_letters
    chars_list = list(characters)
    key_list = chars_list.copy()
    random.shuffle(key_list)
    aux_list = []
    for i in text:
        if i in chars_list:
            char_index = chars_list.index(i)
            aux_list.append(key_list[char_index])
        else:
            aux_list.append(i)
    return "".join(aux_list)


if __name__ == "__main__":
    txt = "patito"
    code = "yo"
    encoded_text = encode_text(txt, code)
    decoded_text = decode_text(encoded_text, code)
    print(txt)
    print(encoded_text)
    print(decoded_text)

