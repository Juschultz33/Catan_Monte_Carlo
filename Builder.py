#%%
from RoleDice import *
from GetResorces import *
from BuildingRequirements import * 

def builder(r):
    # , three=False, t_brick=False, t_grain=False, t_ore=False, t_sheep=False):
    # Setting Important variables
    road = False
    settlement = False
    city = False
    devo = False
    count = 0
    robber = 0
    ro, s, c, d = 0, 0, 0, 0
    my_list = []
    card = {"sheep": 0,
            'brick': 0,
            'ore': 0,
            'grain': 0,
            'lumber': 0}
    
    # Loop through roles untill I get enough resorces
    # to build 1 or everything
    while True:
        if road == True and settlement == True and city == True and devo == True:
            my_list = [ro, s, c, d, robber]
            return my_list
        role = dice_role()
        count += 1
        card = get_resorces(role, r, card)
        # print(card)
        # Check Settlements
        if settlement == False:
            settlement = settlement_builder(card,r) # in BuildingRequirements
            if settlement == True:
                s = count
        # Check City
        if city == False:
            city = city_builder(card,r)
            if city == True:
                c = count
        # Check Devo Cards
        if devo == False:
            devo = devo_card(card,r)
            if devo == True:
                d = count
        # Check road
        if road == False:
            road = road_builder(card,r)
            if road == True:
                ro = count
        if role == 7:
            if sum(card.values()) > 7:
                robber += 1

# %%
