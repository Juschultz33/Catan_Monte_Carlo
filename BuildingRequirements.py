from BuildingResource import *

def road_builder(card, r):
    s = building_resource(card,r, n_brick=True, n_lumber=True)
    if s >= 2:
        return True
    else:
        return False


def settlement_builder(card, r):
    s = building_resource(card,r, n_brick=True, n_lumber=True,
                          n_sheep=True, n_grain=True, )
    if s >= 4:
        return True
    else:
        return False


def city_builder(card, r):
    s = building_resource(card,r, n_ore=True, n_grain=True, b_city=True, )
    if s >= 5:
        return True
    else:
        return False


def devo_card(card, r):
    s = building_resource(card, r, n_ore=True, n_grain=True, n_sheep=True)
    if s >= 3:
        return True
    else:
        return False
