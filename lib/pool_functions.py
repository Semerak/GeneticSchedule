import random


def copy(pool):
    try:
        return pool.copy()
    except:
        return [e for e in pool]


def random_elements(pool_list, number_elements=-1):
    if number_elements == -1:
        number_elements = len(pool_list)
    if number_elements > len(pool_list):
        number_elements = len(pool_list)

    res = []
    pool_len = len(pool_list)
    copy_pool = copy(pool_list)
    for i in range(number_elements):
        element = copy_pool.pop(random.randint(0, pool_len - i - 1))
        res.append(element)

    return res
