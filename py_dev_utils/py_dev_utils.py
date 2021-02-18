
import itertools 


def get_unique_idx(list_in):
    '''
    @usage get indices of unique items in a list. Only acccepts lists of hashable items (not dict)
    @param: list_in: list
    @return: list of indices of duplicates
    '''
    seen = set()
    list_out = []
    for idx, item in enumerate(list_in):
        if item not in seen:
            seen.add(item)
            list_out.append(idx)
    return list_out



def check_whether_iterator_empty(iterator):
    '''
    @usage: returns iterator if not empty, and None otherwise.
    NB: works for iterator, not iterable (i.e. not for a list)
    # source: https://code.activestate.com/recipes/413614-testing-for-an-empty-iterator/
    '''
    try:
        first = next(iterator)
    except:
        iterator = None
    else:
        iterator = itertools.chain([first], iterator)
    return iterator