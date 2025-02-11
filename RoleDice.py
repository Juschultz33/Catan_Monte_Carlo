##############################################################
# Funtion to add 2 dice role together
# values should be between 2 - 12
##############################################################

from random import randint

def dice_role():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    return d1 + d2