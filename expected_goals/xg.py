import json
import pandas as pd

zone_dict = {}


# this function will first try to look up the zone in the dictionary,
# then if that doesn't work it uses if/else to find the zone
# and adds the result to the dictionary
def zone(x, y):
    coordinates = (x, y)
    if (coordinates in zone_dict):
        return zone_dict[coordinates]
    else if (x < 50):
        z = 0
        zone_dict[coordinates] = z
        return z
    else if (x < 70):
        if (y < 40):
            z = 1
            zone_dict[coordinates] = z
            return z
        else if (y < 60):
            z = 2
            zone_dict[coordinates] = z
            return z
        else:
            z = 3
            zone_dict[coordinates] = z
            return z
    else if (x < 80):
        if (y < 40):
            z = 4
            zone_dict[coordinates] = z
            return z
        else if (y < 60):
            z = 5
            zone_dict[coordinates] = z
            return z
        else:
            z = 6
            zone_dict[coordinates] = z
            return z
    else if (x < 85):
        if (y < 30):
            z = 7
            zone_dict[coordinates] = z
            return z
        else if (y < 40):
            z = 8
            zone_dict[coordinates] = z
            return z
        else if (y < 50):
            z = 9
            zone_dict[coordinates] = z
            return z
        else if (y < 60):
            z = 10
            zone_dict[coordinates] = z
            return z
        else if (y < 70):
            z = 11
            zone_dict[coordinates] = z
            return z
        else:
            z = 12
            zone_dict[coordinates] = z
            return z
    else if (x < 90):
        if (y < 25):
            z = 13
            zone_dict[coordinates] = z
            return z
        else if (y < 35):
            z = 14
            zone_dict[coordinates] = z
            return z
        else if (y < 45):
            z = 15
            zone_dict[coordinates] = z
            return z
        else if (y < 50):
            z = 16
            zone_dict[coordinates] = z
            return z
        else if (y < 55):
            z = 17
            zone_dict[coordinates] = z
            return z
        else if (y < 65):
            z = 18
            zone_dict[coordinates] = z
            return z
        else if (y < 75):
            z = 19
            zone_dict[coordinates] = z
            return z
        else:
            z = 20
            zone_dict[coordinates] = z
            return z
    else if (x < 95):
        if (y < 25):
            z = 21
            zone_dict[coordinates] = z
            return z
        else if (y < 35):
            z = 22
            zone_dict[coordinates] = z
            return z
        else if (y < 45):
            z = 23
            zone_dict[coordinates] = z
            return z
        else if (y < 50):
            z = 24
            zone_dict[coordinates] = z
            return z
        else if (y < 55):
            z = 25
            zone_dict[coordinates] = z
            return z
        else if (y < 65):
            z = 26
            zone_dict[coordinates] = z
            return z
        else if (y < 75):
            z = 27
            zone_dict[coordinates] = z
            return z
        else:
            z = 28
            zone_dict[coordinates] = z
            return z
    else:
        if (y < 25):
            z = 29
            zone_dict[coordinates] = z
            return z
        else if (y < 35):
            z = 30
            zone_dict[coordinates] = z
            return z
        else if (y < 45):
            z = 31
            zone_dict[coordinates] = z
            return z
        else if (y < 50):
            z = 32
            zone_dict[coordinates] = z
            return z
        else if (y < 55):
            z = 33
            zone_dict[coordinates] = z
            return z
        else if (y < 65):
            z = 34
            zone_dict[coordinates] = z
            return z
        else if (y < 75):
            z = 35
            zone_dict[coordinates] = z
            return z
        else:
            z = 36
            zone_dict[coordinates] = z
            return z

# create map of the zone definitions
