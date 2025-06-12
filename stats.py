def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    char_dict = {}
    text_lower = text.lower()
    for char in text_lower:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def create_list_from_dict(dict):
    dict_array = []
    for key in dict:
        dict_array.append({'char': key, 'num': dict[key]})
    dict_array.sort(reverse=True, key=sort_on)
    return dict_array