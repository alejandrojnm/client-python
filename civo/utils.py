"""
File to handle all utils
"""


def filter_list(data: dict, filter: str) -> list:
    """
    Function to handle filter in all list of the api
    :param filter: the filter in this format (label:Home, id:6224cd2b-d416-4e92-bdbb-db60521c8eb9)
    :param data: object json
    :return: the found object in json format
    """
    filter_split = filter.split(':')
    search_in = filter_split[0]
    search = filter_split[1]

    try:
        search = int(search)
    except ValueError:
        pass

    try:
        data_search = data['items']
    except TypeError:
        data_search = data

    return [element for element in data_search if element[search_in] == search]
