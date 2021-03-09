def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    if incoming_list is None or len(incoming_list) == 0:
        return 0
    elif len(incoming_list) == 1:
        return incoming_list[0]
    big = incoming_list[0]
    for num in incoming_list:
        if num >= big:
            big = num
    return big


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    if incoming_list is None or len(incoming_list) == 0:
        return 0
    elif len(incoming_list) == 1:
        return incoming_list[0]
    least = incoming_list[0]
    for num in incoming_list:
        if least >= num:
            least = num
    return least


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    if incoming_list is None or len(incoming_list) == 0:
        return 0
    total = 0
    for num in incoming_list:
        total = total + num
    return total


def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    longest_length = 0
    return_key = ""
    if incoming_dict is None or len(incoming_dict) == 0:
        return None
    for key, val in incoming_dict.items():
        if len(val) > longest_length:
            longest_length = len(val)
            return_key = key
    return return_key
