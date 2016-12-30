# Given a list_of_ints, find the highest_product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.


def highest_product(int_list):

    highest_three = (int_list[0],int_list[1], int_list[2])

    for n in int_list:
        if n > min(highest_three):
            highest_three.remove(min(highest_three))
            highest_three.add(n)

    highest_three_list = [(highest_three)]

    return highest_three_list[0]*highest_three_list[1]*highest_three_list[2]

#work with negative number, sorting O(NlogN)

def highest_product(int_list):

    int_list.sort()
    positive_three = int_list[-1] * int_list[-2] * int_list[-3]
    negative_two = 1

    if int_list[0] < 0 and int_list[1] < 0 :
        negative_two = int_list[0]*int_list[1]*int_list[-1]

    return max(negative_two, positive_three)


#O(n) runtime and O(1) space

def highest_product(int_list):

    highest_product_of_3 = 1
    highest_product_of_2 = 1
    highest = 1
    lowest_product_of_2 = 1
    lowest = 1

    for n in int_list:

        if n * highest_product_of_2 > highest_product_of_3:
            highest_product_of_3 = n * highest_product_of_2

        if n * highest > highest_product_of_2:
            highest_product_of_2 = n * highest

        if n > highest:
            highest = n

        if n * lowest_product_of_2 > highest_product_of_3:
            highest_product_of_3 = n * lowest_product_of_2

        if n * lowest < lowest_product_of_2:
            lowest_product_of_2 = n * lowest

        if n < lowest:
            lowest = n

    return highest_product_of_3

#cleaner solution

from itertools import islice

def highest_product(int_list):

    highest_product_of_3 = int_list[0] * int_list[1] * int_list[2]
    highest_product_of_2 = int_list[0] * int_list[1]
    lowest_product_of_2 = int_list[0] * int_list[1]
    highest = max(int_list[0], int_list[1])
    lowest = min(int_list[0], int_list[1])


    for current in islice(int_list, 2, None):

        highest_product_of_3 = max(highest_product_of_3, 
                                    n * highest_product_of_2,
                                    n * lowest_product_of_2)

        highest_product_of_2 = max(highest_product_of_2,
                                     n * highest,
                                     n * lowest)

        highest_product_of_2 = min(highest_product_of_2,
                                     n * highest,
                                     n * lowest)

        highest = max(highest, current)
        lowest = min(lowest, current)

    return highest_product_of_3







