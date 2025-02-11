# Function that gets resorces when you
# role the right number


def get_resorces(role, r, card):
    if role in r['sheep']:
        card['sheep'] += r['sheep'].count(role)
    if role in r['brick']:
        card['brick'] += r['brick'].count(role)
    if role in r['ore']:
        card['ore'] += r['ore'].count(role)
    if role in r['grain']:
        card['grain'] += r['grain'].count(role)
    if role in r['lumber']:
        card['lumber'] += r['lumber'].count(role)
    return card