import random
import math
from collections import Counter


#GLOBAL VARIABLES
MAX_NUMBER_SOCKS=100
ARRAY_SIZE=100


def sockMerchant(array):
    dictionary = Counter(array)
    pair_socks = 0
    for key in dictionary:
        pair_socks = pair_socks + math.floor(dictionary[key]/2)
    return pair_socks



def create_array(array_size):
    array = []
    for x in range(array_size):
        array.append(random.randint(1,MAX_NUMBER_SOCKS))
    return array



def tests():
    testArray = [1,2,1,2,1,3,2]
    assert sockMerchant(testArray) == 2


if __name__ == '__main__':
    print('Number of pair socks:', sockMerchant(create_array(ARRAY_SIZE)))