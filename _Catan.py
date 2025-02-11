# %%
# Load in packages
from random import randint
import pandas as pd
import altair as alt
import numpy as np
from RoleDice import *
from BuildingResource import *
from GetResorces import *
from BuildingRequirements import *
from Builder import *



# %%
# This is the recorse list.
r = {"sheep": [3, 3],
     'brick': [4, 4],
     'ore': [8],
     'grain': [8],
     'lumber': [4, 4, 2, 2, 2, 2]}

card = {"sheep": 0,
        'brick': 0,
        'ore': 0,
        'grain': 0,
        'lumber': 0}

three = False
t_brick = False
t_lumber = False
t_grain = False
t_ore = False
t_sheep = True

# %%
# Run the simulation x number of times


# List to accumulate rows
rows = []

for i in range(1000):
    my_list = builder(r, three=three, t_brick=t_brick,
                      t_grain=t_grain, t_ore=t_ore, t_sheep=t_sheep)
    
    # Append the dictionary to the rows list
    rows.append({"settlement_builder": my_list[1], "road_builder": my_list[0],
                 'city_builder': my_list[2], 'devo_card': my_list[3],
                 'robber': my_list[4]})

# Create DataFrame from the list of rows
df = pd.DataFrame(rows)

df


# %%
data = {'col1': [1, 2], 'col2': [3, 4]}
df1 = pd.DataFrame(data)
print("DataFrame from dictionary:\n", df1)
# %%


# From a list of lists
data = [[1, 2], [3, 4]]
df2 = pd.DataFrame(data, columns=['col1', 'col2'])
print("\nDataFrame from list of lists:\n", df2)


# %%
# From a list of dictionaries
data = [{'col1': 1, 'col2': 3}, {'col1': 2, 'col2': 4}]
df3 = pd.DataFrame(data)
print("\nDataFrame from list of dictionaries:\n", df3)