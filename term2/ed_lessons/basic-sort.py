import random


def basic_sort(list):
    done = False
    iterations = 0
    while not done:
        done = True
        for i in range(len(list)-1):
            if list[i] > list [i+1]:
                temp = list[i+1]
                list[i+1] = list[i]
                list[i] = temp
                done = False
                iterations += 1
    print(f'elements: {len(list)}, iterations: {iterations}')



# def reverse_sort(list):
#     done = False
#     # iterations = 0
#     while not done:
#         done = True
#         for i in range(len(list)-1):
#             if list[i] < list [i+1]:
#                 temp = list[i+1]
#                 list[i+1] = list[i]
#                 list[i] = temp
#                 done = False
#                 # iterations += 1
#                 # print(f'iteration: {iterations}')
#     return list


# bubbleList = [300, 297, 291, 287, 281, 277, 274, 273, 270, 266, 264, 261, 258, 254, 252, 250, 248, 246, 243, 240, 237, 235, 233, 230, 228, 225, 223, 221, 218, 215, 213, 211, 209, 206, 203, 201, 200, 181, 174, 170, 163, 157, 152, 142, 140, 130, 124, 122, 118, 112, 109, 105, 102, 100, 94, 91, 87, 84, 81, 78, 74, 70, 66, 63, 60, 55, 52, 49, 47, 42, 40, 37, 34, 30, 27, 22, 17, 14, 11, 7, 3, 1]

def createList(length, low, high):
    list = []
    while len(list) < length:
        n = random.randint(low, high)
        if (n not in list):
            list.append(n)

    # Sorts list highest to lowest
    
    done = False
    while not done:
        done = True
        for i in range(len(list)-1):
            if list[i] < list [i+1]:
                temp = list[i+1]
                list[i+1] = list[i]
                list[i] = temp
                done = False
    
    basic_sort(list)



# bubbleList = createList(700, 1, 10000)

l1 = [24, 8]
# l2 = [50, 40, 25, 12]
# l3 = [140, 115, 100, 80, 77, 55, 44, 2]
# l4 = [293, 258, 227, 221, 207, 190, 160, 145, 140, 115, 100, 80, 77, 55, 44, 2]

createList(15, 1, 100)
createList(16, 1, 100)
createList(17, 1, 100)
createList(18, 1, 100)
createList(19, 1, 100)
createList(20, 1, 100)
createList(21, 1, 100)
createList(22, 1, 100)
createList(23, 1, 100)
createList(24, 1, 100)
createList(25, 1, 100)
createList(26, 1, 100)
createList(27, 1, 100)
createList(28, 1, 100)
createList(29, 1, 100)
createList(30, 1, 100)



# basic_sort(l1)
# basic_sort(l2)
# basic_sort(l3)
# basic_sort(l4)

