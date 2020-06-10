###########################
# 6.0002 Problem Set 1a: Space Cows
# Name: Bennai Nabil
# Time: June 8th 2020

from ps1_partition import get_partitions
import time
from os import system

system("clear")
# ================================
# Part A: Transporting Space Cows
# ================================

# * Problem 1  ==> Activity Done


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cowsData = dict()

    with open(filename) as f:
        read_data = f.read()
        dataList = read_data.split("\n")
        for couple in dataList:
            name, weight = couple.split(',')
            cowsData[name] = int(weight)
    f.closed

    return cowsData


# print(load_cows("ps1_cow_data.txt"))

"""
Output of the dictionnary of cows:

{'Maggie': 3.0, 'Herman': 7.0, 'Betsy': 9.0, 'Oreo': 6.0, 'Moo Moo': 3.0,
    'Milkshake': 2.0, 'Millie': 5.0, 'Lola': 2.0, 'Florence': 2.0, 'Henrietta': 9.0}
"""

# * Problem 2 ==> Activity Done


def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cowsCopy = {k: v for k, v in sorted(
        cows.items(), key=lambda item: item[1], reverse=True)}
    result = []
    while len(cowsCopy) != 0:
        boxWeight = 0.0
        tmp_array = []
        for cowName in list(cowsCopy.keys()):
            if (cowsCopy[cowName] <= limit - boxWeight):
                tmp_array.append(cowName)
                boxWeight += cowsCopy[cowName]
                del cowsCopy[cowName]
        result.append(tmp_array)
    return result


# dicCows = load_cows("ps1_cow_data.txt")
# greedy_cow_transport(dicCows)
# for numTrip, trip in enumerate(greedy_cow_transport(dicCows)):
#     print(f"Trip n°{numTrip+1}: {trip}")


# * Problem 3 ==> Activity done


def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    # generating a list contains all possible partitions of cows
    possible_partitions = list(get_partitions(cows.keys()))
    # sorting list by the length of all partitions
    possible_partitions.sort(key=len)
    # initializing the desired list of lists that has the fewest trips
    result_partition = possible_partitions[0]
    # iterating through each possible partition
    for partition in possible_partitions:
        # initializing the empty list which will contain the weight of each trip in a partition and satisfy the required limits
        # e.g. partition = [[1,2,3,4],[5]] <=> trip_weights = [10, 5] with default limit => this is result partition
        # e.g. partition = [[1,2,3],[4,5,6]] <=> trip_weights = [] with default limit cause sum of [4,5,6] > limit
        trip_weights = []
        for trips in partition:
            weight = 0
            for trip in trips:
                weight += cows[trip]
            if weight > limit:
                break
            else:
                trip_weights.append(weight)
        # this condition will immediately return the first desired partition in the possible partitions list
        if len(trip_weights) != 0 and len(trip_weights) == len(partition):
            result_partition = partition
            break
    return result_partition


# Problem 4


def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass
