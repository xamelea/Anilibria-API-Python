from inspect import getmembers, isfunction
import anilibriaAPI3.api as apix

def concatfunc(alist):
    new = str()

    # traverse in the string
    for x in alist:
        new += x
    # return string
    return new


def get_functions(func):
    temp = getmembers(func, isfunction)
    result = list()
    for i in temp:
        result += [concatfunc(str(i[0]))]
    return result
def list_wrapper(list_argument):
    result = ''
    for i in list_argument:
        result += f'id: {i["id"]}\n' \
                  f'en name: {i["names"]["en"]}\n' \
                  f'ru name: {i["names"]["ru"]}\n'
    return result
