def sort_dicts_by_key(dict_list, sort_key):
    """
    Sorts a list of dictionaries by the specified key.

    :param dict_list: List[dict] - The list of dictionaries to sort.
    :param sort_key: str - The key to sort the dictionaries by.
    :return: List[dict] - The sorted list of dictionaries.
    """
    return sorted(dict_list, key=lambda d: d.get(sort_key))


