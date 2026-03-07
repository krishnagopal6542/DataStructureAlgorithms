# Leet Code : 1282
from collections import defaultdict


def group_the_people(group_sizes):
    res = []
    hash_map = defaultdict(list)
    for person, grp_size in enumerate(group_sizes):
        if grp_size in hash_map and len(hash_map[grp_size]) == grp_size:
            res.append(hash_map[grp_size])
            hash_map[grp_size] = []
        hash_map[grp_size].append(person)

    for lists in hash_map.values():
        if lists:
            res.append(lists)

    return res


if __name__ == '__main__':
    groupSizes = [3, 3, 3, 3, 3, 1, 3]
    print(group_the_people(group_sizes=groupSizes))
