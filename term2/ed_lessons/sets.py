def intersection(set1, set2):
    pass




def union(set1, set2):
    result = []

    result.extend(set1)

    for i in set2 :
        if(set2[i] not in result):
            result.extend(set2[i])

    print(result)
    return result


def symmetric_difference(set1, set2):
    pass


set1 = ['1', '2', '3']
set2 = ['3', '5', '7', '10', '1']

intersection(set1, set2)