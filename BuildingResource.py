def building_resource(card,r, n_brick=False, n_lumber=False, n_ore=False,
                      n_grain=False, n_sheep=False, b_city=False, ):

    # We need to set the trading amount for each resources.
    # There might be a way to do this better but I think this works.
    # We set this equal to 4 start but it will change
    s = 0
    b_trade = 4
    l_trade = 4
    g_trade = 4
    o_trade = 4
    s_trade = 4

    # if we have a 3:1 trade everything needs to be at least 3:1
    if 'three' in r['trade']:
        b_trade = 3
        l_trade = 3
        g_trade = 3
        o_trade = 3
        s_trade = 3

    # The following code is to change for 2:1 for every resource.
    if 'brick' in r['trade']:
        b_trade = 2

    if 'lumber' in r['trade']:
        l_trade = 2

    if 'grain' in r['trade']:
        g_trade = 2

    if 'ore' in r['trade']:
        o_trade = 2

    if 'sheep' in r['trade']:
        s_trade = 2

    # Brick
    if n_brick == True:
        if card['brick'] > 0:
            s += 1
            s += (card['brick']-1)//b_trade
    else:
        s += card['brick']//b_trade

    # Lumber
    if n_lumber == True:
        if card['lumber'] > 0:
            s += 1
            s += (card['lumber']-1)//l_trade
    else:
        s += card['lumber']//l_trade

    # Sheep
    if n_sheep == True:
        if card['sheep'] > 0:
            s += 1
            s += (card['sheep']-1)//s_trade
    else:
        s += card['sheep']//s_trade

    # Grain
    if n_grain == True:
        if b_city == True:
            if card['grain'] <= 2:
                s += card['grain']
            else:
                s += 2
                s += (card['grain']-2)//g_trade
        else:
            if card['grain'] > 0:
                s += 1
                s += (card['grain']-1)//g_trade
    else:
        s += card['grain']//g_trade

    # ore
    if n_ore == True:
        if b_city == True:
            if card['ore'] <= 3:
                s += card['ore']
            else:
                s += 3
                s += (card['ore']-3)//o_trade
        else:
            if card['ore'] > 0:
                s += 1
                s += (card['ore']-1)//o_trade
    else:
        s += card['ore']//o_trade

    return s