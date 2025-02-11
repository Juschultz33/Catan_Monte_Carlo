def building_resource(card, n_brick=False, n_lumber=False, n_ore=False, three=False,
                      n_grain=False, n_sheep=False, b_city=False, t_brick=False,
                      t_lumber=False, t_grain=False, t_ore=False, t_sheep=False):
    
    trade_values = {'brick': 4, 'lumber': 4, 'grain': 4, 'ore': 4, 'sheep': 4}
    
    if three:
        for key in trade_values:
            trade_values[key] = 3
    
    specific_trades = {'brick': t_brick, 'lumber': t_lumber, 'grain': t_grain, 'ore': t_ore, 'sheep': t_sheep}
    for resource, trade in specific_trades.items():
        if trade:
            trade_values[resource] = 2
    
    s = 0
    
    def calculate_points(resource, need_exact, b_city_limit=None):
        nonlocal s
        trade_value = trade_values[resource]
        if need_exact:
            if b_city_limit is not None:
                s += min(card[resource], b_city_limit)
                s += (card[resource] - min(card[resource], b_city_limit)) // trade_value
            else:
                if card[resource] > 0:
                    s += 1
                    s += (card[resource] - 1) // trade_value
        else:
            s += card[resource] // trade_value
    
    calculate_points('brick', n_brick)
    calculate_points('lumber', n_lumber)
    calculate_points('sheep', n_sheep)
    
    if n_grain:
        if b_city:
            calculate_points('grain', True, b_city_limit=2)
        else:
            calculate_points('grain', True)
    else:
        calculate_points('grain', False)
    
    if n_ore:
        if b_city:
            calculate_points('ore', True, b_city_limit=3)
        else:
            calculate_points('ore', True)
    else:
        calculate_points('ore', False)
    
    return s
