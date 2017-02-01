import math

# find item in a list
def find (item, list):
    for i in list:
        if item(i):
            return True
        else:
            return False
