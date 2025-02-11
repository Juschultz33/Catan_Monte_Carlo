from BuildingResource import *

def road_builder(card, three=False, t_brick=False, t_grain=False, t_ore=False, t_sheep=False):
    s = building_resource(card, n_brick=True, n_lumber=True, three=three, t_brick=t_brick,
                          t_grain=t_grain, t_ore=t_ore, t_sheep=t_sheep)
    if s >= 2:
        return True
    else:
        return False


def settlement_builder(card, three=False, t_brick=False, t_grain=False, t_ore=False, t_sheep=False):
    s = building_resource(card, n_brick=True, n_lumber=True,
                          n_sheep=True, n_grain=True, three=three, t_brick=t_brick,
                          t_grain=t_grain, t_ore=t_ore, t_sheep=t_sheep)
    if s >= 4:
        return True
    else:
        return False


def city_builder(card, three=False, t_brick=False, t_grain=False, t_ore=False, t_sheep=False):
    s = building_resource(card, n_ore=True, n_grain=True, b_city=True, three=three, t_brick=t_brick,
                          t_grain=t_grain, t_ore=t_ore, t_sheep=t_sheep)
    if s >= 5:
        return True
    else:
        return False


def devo_card(card, three=False, t_brick=False, t_grain=False, t_ore=False, t_sheep=False):
    s = building_resource(card, n_ore=True, n_grain=True, n_sheep=True, three=three, t_brick=t_brick,
                          t_grain=t_grain, t_ore=t_ore, t_sheep=t_sheep)
    if s >= 3:
        return True
    else:
        return False
