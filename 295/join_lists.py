from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if lst_of_lst == []:
        return None
    result = []
    for lst in lst_of_lst:
        result += lst
        if lst == lst_of_lst[-1]:
            break
        result.append(sep)
    return result
