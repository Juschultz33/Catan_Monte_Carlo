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
################################################################################
# r is the resourses list. If you have a settlement on a 2 lumber, 6 ore and 10
# grain then lumber would have 2, ore has 6 and grain has 10. If the settlement 
# was a city then the list would be lumber: [2,2], ore:[6,6] and grain:[10,10]
################################################################################

# This is the resourse list.
r = {"sheep": [5],
     'brick': [6],
     'ore': [8],
     'grain': [9],
     'lumber': [10,4],
     'trade': ['lumber']}

card = {"sheep": 0,
        'brick': 0,
        'ore': 0,
        'grain': 0,
        'lumber': 0}

# %%
rows = []

for i in range(1000):
    my_list = builder(r)

    
    # Append the dictionary to the rows list
    rows.append({"settlement_builder": my_list[1], "road_builder": my_list[0],
                 'city_builder': my_list[2], 'devo_card': my_list[3],
                 'robber': my_list[4]})

# Create DataFrame from the list of rows
df = pd.DataFrame(rows)

df


# %%

################################################################################
# This is the board in code. When putting the board together, ensure that the
# 1 -> 1 boarder peace in in the bottom left, hex1 is that hexigon that touches
# that boarder peace. hex2 is the peice to hex1 right. It then is build from 
# bottom to top left to right. This is important for the trade ports later
################################################################################
hex1 = [1,"brick", 3]
hex2 = [2,"grain", 8]
hex3 = [3,"grain", 4]
hex4 = [4,"desert", 0]
hex5 = [5,"ore", 5]
hex6 = [6,"brick", 3]
hex7 = [7,"ore", 6]
hex8 = [8,"grain",11]
hex9 = [9,"lumber",4]
hex10 = [10,"sheep", 8]
hex11 = [11,"lumber",10]
hex12 = [12,"sheep",5]
hex13 = [13,"grain",12]
hex14 = [14,"lumber",9]
hex15 = [15,"sheep",11]
hex16 = [16,"lumber",9]
hex17 = [17,"sheep",6]
hex18 = [18,"brick",10]
hex19 = [19,"ore",2]

 #%%
# Combine all the lists into a list of lists
Board = [hex1, hex2, hex3, hex4, hex5, hex6, hex7, hex8, hex9, hex10, 
		 hex11, hex12, hex13, hex14, hex15, hex16, hex17, hex18, hex19]

# Create a DataFrame
gameboard = pd.DataFrame(Board, columns=["HexNum", "Resource", "Value"])




# %%

################################################################################
# r# is a referce to what the resourse hex is. r1 is what values is given from 
# hex1. This step is going to be used to find what resourse and roles you get
# at a given intersection. Note: Trade will be changed in the following section
################################################################################

r1 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[0][1]
value = gameboard.loc[0][2]
if resource in r1:
	r1[resource].append(value)

r2 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[1][1]
value = gameboard.loc[1][2]
if resource in r2:
	r2[resource].append(value)

r3 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[2][1]
value = gameboard.loc[2][2]
if resource in r3:
	r3[resource].append(value)

r4 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[3][1]
value = gameboard.loc[3][2]
if resource in r4:
	r4[resource].append(value)

r5 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[4][1]
value = gameboard.loc[4][2]
if resource in r5:
	r5[resource].append(value)

r6 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[5][1]
value = gameboard.loc[5][2]
if resource in r6:
	r6[resource].append(value)

r7 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[6][1]
value = gameboard.loc[6][2]
if resource in r7:
	r7[resource].append(value)

r8 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[7][1]
value = gameboard.loc[7][2]
if resource in r8:
	r8[resource].append(value)

r9 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[8][1]
value = gameboard.loc[8][2]
if resource in r9:
	r9[resource].append(value)

r10 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[9][1]
value = gameboard.loc[9][2]
if resource in r10:
	r10[resource].append(value)

r11 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[10][1]
value = gameboard.loc[10][2]
if resource in r11:
	r11[resource].append(value)

r12 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[11][1]
value = gameboard.loc[11][2]
if resource in r12:
	r12[resource].append(value)

r13 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[12][1]
value = gameboard.loc[12][2]
if resource in r13:
	r13[resource].append(value)

r14 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[13][1]
value = gameboard.loc[13][2]
if resource in r14:
	r14[resource].append(value)

r15 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[14][1]
value = gameboard.loc[14][2]
if resource in r15:
	r15[resource].append(value)

r16 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[15][1]
value = gameboard.loc[15][2]
if resource in r16:
	r16[resource].append(value)

r17 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[16][1]
value = gameboard.loc[16][2]
if resource in r17:
	r17[resource].append(value)

r18 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[17][1]
value = gameboard.loc[17][2]
if resource in r18:
	r18[resource].append(value)

r19 = {'sheep': [],'brick': [],'ore': [],'grain': [], 'lumber': [],'trade': []}
resource = gameboard.loc[18][1]
value = gameboard.loc[18][2]
if resource in r19:
	r19[resource].append(value)


# %%
################################################################################
# i# is the intersection number. intersection start to the left of 1 -> 1 boarder
# and moved from left to right and bottom to top. Currently we are hard coding 
# trade based on the base game. However you can change trade ports (they are 
# given in the game). that change May be coming later.
################################################################################

i1 = r1.copy()
i1['intersection'] = [1,2,9]

i2 = r1.copy()
i2['intersection'] = [1,2,3]

i3 = {}
for key in r1:
	i3[key] = r1[key] + r2[key] 
i3['trade'] = ['sheep']
i3['intersection'] = [2,3,4,11]

i4 = r2.copy()
i4['trade'] = ['sheep']
i4['intersection'] = [3,4,5]

i5 = {}
for key in r2:
	i5[key] = r2[key] + r3[key]
i5['intersection'] = [4,5,6,13]

i6 = r3.copy()
i6['trade'] = ['three']
i6['intersection'] = [5,6,7]

i7 = r3.copy()
i7['trade'] = ['three']
i7['intersection'] = [6,7,13]

i8 = r4.copy()
i8['trade'] = ['three']
i8['intersection'] = [18,8,9]

i9 = {}
for key in r1:
	i9[key] = r4[key] + r1[key]
i9['trade'] = ['three']
i9['intersection'] = [1,8,9,10]

i10 = {}
for key in r1:
	i10[key] = r4[key] + r5[key] + r1[key]
i10['intersection'] = [9,10,11,20]

i11 = {}
for key in r1:
	i11[key] = r1[key] + r2[key] + r5[key]
i11['intersection'] = [10,11,12,3]

i12 = {}
for key in r1:
	i12[key] = r2[key] + r5[key] + r6[key]
i12['intersection'] = [11,12,13,22]

i13 = {}
for key in r1:
	i13[key] = r2[key] + r3[key] + r6[key]
i13['intersection'] = [5,12,13,14]

i14 = {}
for key in r1:
	i14[key] = r3[key] + r6[key] + r7[key]
i14['intersection'] = [13,14,15,24]

i15 = {}
for key in r1:
	i15[key] = r3[key] + r7[key]
i15['intersection'] = [7,14,15,16]

i16 = r7.copy()
i16['trade'] = ['ore']
i16['intersection'] = [15,16,26]

i17 = r8.copy()
i17['trade'] = ['three']
i17['intersection'] = [17,18,28]

i18 = {}
for key in r1:
	i18[key] = r4[key] + r8[key]
i18['intersection'] = [8,17,18,19]

i19 = {}
for key in r1:
	i19[key] = r4[key] + r8[key] + r9[key]
i19['intersection'] = [18,19,20,30]

i20 = {}
for key in r1:
	i20[key] = r4[key] + r5[key] + r9[key]
i20['intersection'] = [10,19,20,21]

i21 = {}
for key in r1:
	i21[key] = r5[key] + r9[key]+r10[key]
i21['intersection'] = [20,21,22,32]

i22 = {}
for key in r1:
	i22[key] = r5[key] + r6[key] + r10[key]
i22['intersection'] = [12,21,22,23]

i23 = {}
for key in r1:
	i23[key] = r6[key] + r10[key] + r11[key]
i23['intersection'] = [22,23,24,34]

i24 = {}
for key in r1:
	i24[key] = r6[key] + r7[key] + r11[key]
i24['intersection'] = [14,23,24,25]

i25 = {}
for key in r1:
	i25[key] = r7[key] + r11[key] + r12[key]
i25['intersection'] = [24,25,26,35]

i26 = {}
for key in r1:
	i26[key] = r7[key] + r12[key]
i26['trade'] = ['ore']
i26['intersection'] = [16,25,26,27]

i27 = r12.copy()
i27['intersection'] = [26,27,38]

i28 = r8.copy()
i28['trade'] = ['three']
i28['intersection'] = [17,28,29]

i29 = {}
for key in r1:
	i29[key] = r8[key] + r13[key]
i29['intersection'] = [28,29,30,39]

i30 = {}
for key in r1:
	i30[key] = r8[key] + r9[key] + r13[key]
i30['intersection'] = [19,27,30,31]

i31 = {}
for key in r1:
	i31[key] = r9[key] + r13[key] + r14[key]
i31['intersection'] = [30,31,32,41]

i32 = {}
for key in r1:
	i32[key] = r9[key] + r10[key] + r14[key]
i32['intersection'] = [21,31,32,33]

i33 = {}
for key in r1:
	i33[key] = r10[key] + r14[key] + r15[key]
i33['intersection'] = [32,33,34,43]

i34 = {}
for key in r1:
	i34[key] = r10[key] + r11[key] + r15[key]
i34['intersection'] = [23,33,34,35]

i35 = {}
for key in r1:
	i35[key] = r11[key] + r15[key] + r16[key]
i35['intersection'] = [34,35,36,45]

i36 = {}
for key in r1:
	i36[key] = r11[key] + r12[key] + r16[key]
i36['intersection'] = [25,35,36,37]

i37 = {}
for key in r1:
	i37[key] = r12[key] + r16[key]
i37['trade'] = ['grain']
i37['intersection'] = [36,37,38,47]

i38 = r12.copy()
i38['intersection'] = [27,37,38]

i39 = r13.copy()
i39['trade'] = ['brick']
i39['intersection'] = [29,39,40]

i40 = {}
for key in r1:
	i40[key] = r13[key] + r17[key]
i40['trade'] = ['brick']
i40['intersection'] = [39,40,41,48]

i41 = {}
for key in r1:
	i41[key] = r13[key] + r14[key] + r17[key]
i41['intersection'] = [31,40,41,42]

i42 = {}
for key in r1:
	i42[key] = r14[key] + r17[key] + r18[key]
i42['intersection'] = [41,42,43,50]

i43 = {}
for key in r1:
	i43[key] = r14[key] + r15[key] + r18[key]
i43['intersection'] = [33,42,43,44]

i44 = {}
for key in r1:
	i44[key] = r15[key] + r18[key] + r19[key]
i44['intersection'] = [43,44,45,52]

i45 = {}
for key in r1:
	i45[key] = r15[key] + r16[key] + r19[key]
i45['intersection'] = [35,44,45,46]

i46 = {}
for key in r1:
	i46[key] = r16[key] + r19[key]
i46['intersection'] = [45,46,47,54]

i47 = r16.copy()
i47['trade'] = ['grain']
i47['intersection'] = [37,46,47]

i48 = r17.copy()
i48['intersection'] = [40,48,49]

i49 = r17.copy()
i49['intersection'] = [48,49,50]

i50 = {}
for key in r1:
	i50[key] = r17[key] + r18[key]
i50['trade'] = ['lumber']
i50['intersection'] = [42,49,50,51]

i51 = r18
i15['trade'] = ['lumber']
i51['intersection'] = [50,51,52]

i52 = {}
for key in r1:
	i52[key] = r18[key] + r19[key]
i52['intersection'] = [44,51,52,53]

i53 = r19
i53['trade'] = ['three']
i53['intersection'] = [52,53,54]

i54 = r19
i54['trade'] = ['three']
i54['intersection'] = [46,53,54]

# %%
dicts = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12,
		i13, i14, i15, i16, i17, i18, i19, i20, i21, i22,
		i23, i24, i25, i26, i27, i28, i29, i30, i31, i32, i33, 
		i34, i35, i36, i37, i38, i39, i40, i41, i42, i43, i44,
		i45, i46, i47, i48, i49, i50, i51, i52, i53, i54]
# %%

for i in range(0,54):
	for j in range(1,55):
		if (i + 1) < j:
			if j in dicts[i]['intersection']:
				pass
			else: 
				section_name = f'section{i+1}{j}'
				print(f'{section_name} = {{}}')
				print(f'for key in i{i+1}.keys():')
				print('\tif key == "trade":')
				print(f'\t\t{section_name}[key] = list(set(i{i+1}[key] + i{j}[key]))')
				print('\tif key == "intersection":')
				print(f'\t\tpass')
				print('\telse:')
				print(f'\t\t{section_name}[key] = i{i+1}[key] + i{j}[key]')
				print('\n')
				print(f'sections.append({section_name})')
				print('\n')


# %%
sections = []

section13 = {}
for key in i1.keys():
	if key == "trade":
		section13[key] = list(set(i1[key] + i3[key]))
	if key == "intersection":
		pass
	else:
		section13[key] = i1[key] + i3[key]


sections.append(section13)


section14 = {}
for key in i1.keys():
	if key == "trade":
		section14[key] = list(set(i1[key] + i4[key]))
	if key == "intersection":
		pass
	else:
		section14[key] = i1[key] + i4[key]


sections.append(section14)


section15 = {}
for key in i1.keys():
	if key == "trade":
		section15[key] = list(set(i1[key] + i5[key]))
	if key == "intersection":
		pass
	else:
		section15[key] = i1[key] + i5[key]


sections.append(section15)


section16 = {}
for key in i1.keys():
	if key == "trade":
		section16[key] = list(set(i1[key] + i6[key]))
	if key == "intersection":
		pass
	else:
		section16[key] = i1[key] + i6[key]


sections.append(section16)


section17 = {}
for key in i1.keys():
	if key == "trade":
		section17[key] = list(set(i1[key] + i7[key]))
	if key == "intersection":
		pass
	else:
		section17[key] = i1[key] + i7[key]


sections.append(section17)


section18 = {}
for key in i1.keys():
	if key == "trade":
		section18[key] = list(set(i1[key] + i8[key]))
	if key == "intersection":
		pass
	else:
		section18[key] = i1[key] + i8[key]


sections.append(section18)


section110 = {}
for key in i1.keys():
	if key == "trade":
		section110[key] = list(set(i1[key] + i10[key]))
	if key == "intersection":
		pass
	else:
		section110[key] = i1[key] + i10[key]


sections.append(section110)


section111 = {}
for key in i1.keys():
	if key == "trade":
		section111[key] = list(set(i1[key] + i11[key]))
	if key == "intersection":
		pass
	else:
		section111[key] = i1[key] + i11[key]


sections.append(section111)


section112 = {}
for key in i1.keys():
	if key == "trade":
		section112[key] = list(set(i1[key] + i12[key]))
	if key == "intersection":
		pass
	else:
		section112[key] = i1[key] + i12[key]


sections.append(section112)


section113 = {}
for key in i1.keys():
	if key == "trade":
		section113[key] = list(set(i1[key] + i13[key]))
	if key == "intersection":
		pass
	else:
		section113[key] = i1[key] + i13[key]


sections.append(section113)


section114 = {}
for key in i1.keys():
	if key == "trade":
		section114[key] = list(set(i1[key] + i14[key]))
	if key == "intersection":
		pass
	else:
		section114[key] = i1[key] + i14[key]


sections.append(section114)


section115 = {}
for key in i1.keys():
	if key == "trade":
		section115[key] = list(set(i1[key] + i15[key]))
	if key == "intersection":
		pass
	else:
		section115[key] = i1[key] + i15[key]


sections.append(section115)


section116 = {}
for key in i1.keys():
	if key == "trade":
		section116[key] = list(set(i1[key] + i16[key]))
	if key == "intersection":
		pass
	else:
		section116[key] = i1[key] + i16[key]


sections.append(section116)


section117 = {}
for key in i1.keys():
	if key == "trade":
		section117[key] = list(set(i1[key] + i17[key]))
	if key == "intersection":
		pass
	else:
		section117[key] = i1[key] + i17[key]


sections.append(section117)


section118 = {}
for key in i1.keys():
	if key == "trade":
		section118[key] = list(set(i1[key] + i18[key]))
	if key == "intersection":
		pass
	else:
		section118[key] = i1[key] + i18[key]


sections.append(section118)


section119 = {}
for key in i1.keys():
	if key == "trade":
		section119[key] = list(set(i1[key] + i19[key]))
	if key == "intersection":
		pass
	else:
		section119[key] = i1[key] + i19[key]


sections.append(section119)


section120 = {}
for key in i1.keys():
	if key == "trade":
		section120[key] = list(set(i1[key] + i20[key]))
	if key == "intersection":
		pass
	else:
		section120[key] = i1[key] + i20[key]


sections.append(section120)


section121 = {}
for key in i1.keys():
	if key == "trade":
		section121[key] = list(set(i1[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section121[key] = i1[key] + i21[key]


sections.append(section121)


section122 = {}
for key in i1.keys():
	if key == "trade":
		section122[key] = list(set(i1[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section122[key] = i1[key] + i22[key]


sections.append(section122)


section123 = {}
for key in i1.keys():
	if key == "trade":
		section123[key] = list(set(i1[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section123[key] = i1[key] + i23[key]


sections.append(section123)


section124 = {}
for key in i1.keys():
	if key == "trade":
		section124[key] = list(set(i1[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section124[key] = i1[key] + i24[key]


sections.append(section124)


section125 = {}
for key in i1.keys():
	if key == "trade":
		section125[key] = list(set(i1[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section125[key] = i1[key] + i25[key]


sections.append(section125)


section126 = {}
for key in i1.keys():
	if key == "trade":
		section126[key] = list(set(i1[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section126[key] = i1[key] + i26[key]


sections.append(section126)


section127 = {}
for key in i1.keys():
	if key == "trade":
		section127[key] = list(set(i1[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section127[key] = i1[key] + i27[key]


sections.append(section127)


section128 = {}
for key in i1.keys():
	if key == "trade":
		section128[key] = list(set(i1[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section128[key] = i1[key] + i28[key]


sections.append(section128)


section129 = {}
for key in i1.keys():
	if key == "trade":
		section129[key] = list(set(i1[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section129[key] = i1[key] + i29[key]


sections.append(section129)


section130 = {}
for key in i1.keys():
	if key == "trade":
		section130[key] = list(set(i1[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section130[key] = i1[key] + i30[key]


sections.append(section130)


section131 = {}
for key in i1.keys():
	if key == "trade":
		section131[key] = list(set(i1[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section131[key] = i1[key] + i31[key]


sections.append(section131)


section132 = {}
for key in i1.keys():
	if key == "trade":
		section132[key] = list(set(i1[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section132[key] = i1[key] + i32[key]


sections.append(section132)


section133 = {}
for key in i1.keys():
	if key == "trade":
		section133[key] = list(set(i1[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section133[key] = i1[key] + i33[key]


sections.append(section133)


section134 = {}
for key in i1.keys():
	if key == "trade":
		section134[key] = list(set(i1[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section134[key] = i1[key] + i34[key]


sections.append(section134)


section135 = {}
for key in i1.keys():
	if key == "trade":
		section135[key] = list(set(i1[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section135[key] = i1[key] + i35[key]


sections.append(section135)


section136 = {}
for key in i1.keys():
	if key == "trade":
		section136[key] = list(set(i1[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section136[key] = i1[key] + i36[key]


sections.append(section136)


section137 = {}
for key in i1.keys():
	if key == "trade":
		section137[key] = list(set(i1[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section137[key] = i1[key] + i37[key]


sections.append(section137)


section138 = {}
for key in i1.keys():
	if key == "trade":
		section138[key] = list(set(i1[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section138[key] = i1[key] + i38[key]


sections.append(section138)


section139 = {}
for key in i1.keys():
	if key == "trade":
		section139[key] = list(set(i1[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section139[key] = i1[key] + i39[key]


sections.append(section139)


section140 = {}
for key in i1.keys():
	if key == "trade":
		section140[key] = list(set(i1[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section140[key] = i1[key] + i40[key]


sections.append(section140)


section141 = {}
for key in i1.keys():
	if key == "trade":
		section141[key] = list(set(i1[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section141[key] = i1[key] + i41[key]


sections.append(section141)


section142 = {}
for key in i1.keys():
	if key == "trade":
		section142[key] = list(set(i1[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section142[key] = i1[key] + i42[key]


sections.append(section142)


section143 = {}
for key in i1.keys():
	if key == "trade":
		section143[key] = list(set(i1[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section143[key] = i1[key] + i43[key]


sections.append(section143)


section144 = {}
for key in i1.keys():
	if key == "trade":
		section144[key] = list(set(i1[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section144[key] = i1[key] + i44[key]


sections.append(section144)


section145 = {}
for key in i1.keys():
	if key == "trade":
		section145[key] = list(set(i1[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section145[key] = i1[key] + i45[key]


sections.append(section145)


section146 = {}
for key in i1.keys():
	if key == "trade":
		section146[key] = list(set(i1[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section146[key] = i1[key] + i46[key]


sections.append(section146)


section147 = {}
for key in i1.keys():
	if key == "trade":
		section147[key] = list(set(i1[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section147[key] = i1[key] + i47[key]


sections.append(section147)


section148 = {}
for key in i1.keys():
	if key == "trade":
		section148[key] = list(set(i1[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section148[key] = i1[key] + i48[key]


sections.append(section148)


section149 = {}
for key in i1.keys():
	if key == "trade":
		section149[key] = list(set(i1[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section149[key] = i1[key] + i49[key]


sections.append(section149)


section150 = {}
for key in i1.keys():
	if key == "trade":
		section150[key] = list(set(i1[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section150[key] = i1[key] + i50[key]


sections.append(section150)


section151 = {}
for key in i1.keys():
	if key == "trade":
		section151[key] = list(set(i1[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section151[key] = i1[key] + i51[key]


sections.append(section151)


section152 = {}
for key in i1.keys():
	if key == "trade":
		section152[key] = list(set(i1[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section152[key] = i1[key] + i52[key]


sections.append(section152)


section153 = {}
for key in i1.keys():
	if key == "trade":
		section153[key] = list(set(i1[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section153[key] = i1[key] + i53[key]


sections.append(section153)


section154 = {}
for key in i1.keys():
	if key == "trade":
		section154[key] = list(set(i1[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section154[key] = i1[key] + i54[key]


sections.append(section154)


section24 = {}
for key in i2.keys():
	if key == "trade":
		section24[key] = list(set(i2[key] + i4[key]))
	if key == "intersection":
		pass
	else:
		section24[key] = i2[key] + i4[key]


sections.append(section24)


section25 = {}
for key in i2.keys():
	if key == "trade":
		section25[key] = list(set(i2[key] + i5[key]))
	if key == "intersection":
		pass
	else:
		section25[key] = i2[key] + i5[key]


sections.append(section25)


section26 = {}
for key in i2.keys():
	if key == "trade":
		section26[key] = list(set(i2[key] + i6[key]))
	if key == "intersection":
		pass
	else:
		section26[key] = i2[key] + i6[key]


sections.append(section26)


section27 = {}
for key in i2.keys():
	if key == "trade":
		section27[key] = list(set(i2[key] + i7[key]))
	if key == "intersection":
		pass
	else:
		section27[key] = i2[key] + i7[key]


sections.append(section27)


section28 = {}
for key in i2.keys():
	if key == "trade":
		section28[key] = list(set(i2[key] + i8[key]))
	if key == "intersection":
		pass
	else:
		section28[key] = i2[key] + i8[key]


sections.append(section28)


section29 = {}
for key in i2.keys():
	if key == "trade":
		section29[key] = list(set(i2[key] + i9[key]))
	if key == "intersection":
		pass
	else:
		section29[key] = i2[key] + i9[key]


sections.append(section29)


section210 = {}
for key in i2.keys():
	if key == "trade":
		section210[key] = list(set(i2[key] + i10[key]))
	if key == "intersection":
		pass
	else:
		section210[key] = i2[key] + i10[key]


sections.append(section210)


section211 = {}
for key in i2.keys():
	if key == "trade":
		section211[key] = list(set(i2[key] + i11[key]))
	if key == "intersection":
		pass
	else:
		section211[key] = i2[key] + i11[key]


sections.append(section211)


section212 = {}
for key in i2.keys():
	if key == "trade":
		section212[key] = list(set(i2[key] + i12[key]))
	if key == "intersection":
		pass
	else:
		section212[key] = i2[key] + i12[key]


sections.append(section212)


section213 = {}
for key in i2.keys():
	if key == "trade":
		section213[key] = list(set(i2[key] + i13[key]))
	if key == "intersection":
		pass
	else:
		section213[key] = i2[key] + i13[key]


sections.append(section213)


section214 = {}
for key in i2.keys():
	if key == "trade":
		section214[key] = list(set(i2[key] + i14[key]))
	if key == "intersection":
		pass
	else:
		section214[key] = i2[key] + i14[key]


sections.append(section214)


section215 = {}
for key in i2.keys():
	if key == "trade":
		section215[key] = list(set(i2[key] + i15[key]))
	if key == "intersection":
		pass
	else:
		section215[key] = i2[key] + i15[key]


sections.append(section215)


section216 = {}
for key in i2.keys():
	if key == "trade":
		section216[key] = list(set(i2[key] + i16[key]))
	if key == "intersection":
		pass
	else:
		section216[key] = i2[key] + i16[key]


sections.append(section216)


section217 = {}
for key in i2.keys():
	if key == "trade":
		section217[key] = list(set(i2[key] + i17[key]))
	if key == "intersection":
		pass
	else:
		section217[key] = i2[key] + i17[key]


sections.append(section217)


section218 = {}
for key in i2.keys():
	if key == "trade":
		section218[key] = list(set(i2[key] + i18[key]))
	if key == "intersection":
		pass
	else:
		section218[key] = i2[key] + i18[key]


sections.append(section218)


section219 = {}
for key in i2.keys():
	if key == "trade":
		section219[key] = list(set(i2[key] + i19[key]))
	if key == "intersection":
		pass
	else:
		section219[key] = i2[key] + i19[key]


sections.append(section219)


section220 = {}
for key in i2.keys():
	if key == "trade":
		section220[key] = list(set(i2[key] + i20[key]))
	if key == "intersection":
		pass
	else:
		section220[key] = i2[key] + i20[key]


sections.append(section220)


section221 = {}
for key in i2.keys():
	if key == "trade":
		section221[key] = list(set(i2[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section221[key] = i2[key] + i21[key]


sections.append(section221)


section222 = {}
for key in i2.keys():
	if key == "trade":
		section222[key] = list(set(i2[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section222[key] = i2[key] + i22[key]


sections.append(section222)


section223 = {}
for key in i2.keys():
	if key == "trade":
		section223[key] = list(set(i2[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section223[key] = i2[key] + i23[key]


sections.append(section223)


section224 = {}
for key in i2.keys():
	if key == "trade":
		section224[key] = list(set(i2[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section224[key] = i2[key] + i24[key]


sections.append(section224)


section225 = {}
for key in i2.keys():
	if key == "trade":
		section225[key] = list(set(i2[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section225[key] = i2[key] + i25[key]


sections.append(section225)


section226 = {}
for key in i2.keys():
	if key == "trade":
		section226[key] = list(set(i2[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section226[key] = i2[key] + i26[key]


sections.append(section226)


section227 = {}
for key in i2.keys():
	if key == "trade":
		section227[key] = list(set(i2[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section227[key] = i2[key] + i27[key]


sections.append(section227)


section228 = {}
for key in i2.keys():
	if key == "trade":
		section228[key] = list(set(i2[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section228[key] = i2[key] + i28[key]


sections.append(section228)


section229 = {}
for key in i2.keys():
	if key == "trade":
		section229[key] = list(set(i2[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section229[key] = i2[key] + i29[key]


sections.append(section229)


section230 = {}
for key in i2.keys():
	if key == "trade":
		section230[key] = list(set(i2[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section230[key] = i2[key] + i30[key]


sections.append(section230)


section231 = {}
for key in i2.keys():
	if key == "trade":
		section231[key] = list(set(i2[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section231[key] = i2[key] + i31[key]


sections.append(section231)


section232 = {}
for key in i2.keys():
	if key == "trade":
		section232[key] = list(set(i2[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section232[key] = i2[key] + i32[key]


sections.append(section232)


section233 = {}
for key in i2.keys():
	if key == "trade":
		section233[key] = list(set(i2[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section233[key] = i2[key] + i33[key]


sections.append(section233)


section234 = {}
for key in i2.keys():
	if key == "trade":
		section234[key] = list(set(i2[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section234[key] = i2[key] + i34[key]


sections.append(section234)


section235 = {}
for key in i2.keys():
	if key == "trade":
		section235[key] = list(set(i2[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section235[key] = i2[key] + i35[key]


sections.append(section235)


section236 = {}
for key in i2.keys():
	if key == "trade":
		section236[key] = list(set(i2[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section236[key] = i2[key] + i36[key]


sections.append(section236)


section237 = {}
for key in i2.keys():
	if key == "trade":
		section237[key] = list(set(i2[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section237[key] = i2[key] + i37[key]


sections.append(section237)


section238 = {}
for key in i2.keys():
	if key == "trade":
		section238[key] = list(set(i2[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section238[key] = i2[key] + i38[key]


sections.append(section238)


section239 = {}
for key in i2.keys():
	if key == "trade":
		section239[key] = list(set(i2[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section239[key] = i2[key] + i39[key]


sections.append(section239)


section240 = {}
for key in i2.keys():
	if key == "trade":
		section240[key] = list(set(i2[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section240[key] = i2[key] + i40[key]


sections.append(section240)


section241 = {}
for key in i2.keys():
	if key == "trade":
		section241[key] = list(set(i2[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section241[key] = i2[key] + i41[key]


sections.append(section241)


section242 = {}
for key in i2.keys():
	if key == "trade":
		section242[key] = list(set(i2[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section242[key] = i2[key] + i42[key]


sections.append(section242)


section243 = {}
for key in i2.keys():
	if key == "trade":
		section243[key] = list(set(i2[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section243[key] = i2[key] + i43[key]


sections.append(section243)


section244 = {}
for key in i2.keys():
	if key == "trade":
		section244[key] = list(set(i2[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section244[key] = i2[key] + i44[key]


sections.append(section244)


section245 = {}
for key in i2.keys():
	if key == "trade":
		section245[key] = list(set(i2[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section245[key] = i2[key] + i45[key]


sections.append(section245)


section246 = {}
for key in i2.keys():
	if key == "trade":
		section246[key] = list(set(i2[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section246[key] = i2[key] + i46[key]


sections.append(section246)


section247 = {}
for key in i2.keys():
	if key == "trade":
		section247[key] = list(set(i2[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section247[key] = i2[key] + i47[key]


sections.append(section247)


section248 = {}
for key in i2.keys():
	if key == "trade":
		section248[key] = list(set(i2[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section248[key] = i2[key] + i48[key]


sections.append(section248)


section249 = {}
for key in i2.keys():
	if key == "trade":
		section249[key] = list(set(i2[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section249[key] = i2[key] + i49[key]


sections.append(section249)


section250 = {}
for key in i2.keys():
	if key == "trade":
		section250[key] = list(set(i2[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section250[key] = i2[key] + i50[key]


sections.append(section250)


section251 = {}
for key in i2.keys():
	if key == "trade":
		section251[key] = list(set(i2[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section251[key] = i2[key] + i51[key]


sections.append(section251)


section252 = {}
for key in i2.keys():
	if key == "trade":
		section252[key] = list(set(i2[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section252[key] = i2[key] + i52[key]


sections.append(section252)


section253 = {}
for key in i2.keys():
	if key == "trade":
		section253[key] = list(set(i2[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section253[key] = i2[key] + i53[key]


sections.append(section253)


section254 = {}
for key in i2.keys():
	if key == "trade":
		section254[key] = list(set(i2[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section254[key] = i2[key] + i54[key]


sections.append(section254)


section35 = {}
for key in i3.keys():
	if key == "trade":
		section35[key] = list(set(i3[key] + i5[key]))
	if key == "intersection":
		pass
	else:
		section35[key] = i3[key] + i5[key]


sections.append(section35)


section36 = {}
for key in i3.keys():
	if key == "trade":
		section36[key] = list(set(i3[key] + i6[key]))
	if key == "intersection":
		pass
	else:
		section36[key] = i3[key] + i6[key]


sections.append(section36)


section37 = {}
for key in i3.keys():
	if key == "trade":
		section37[key] = list(set(i3[key] + i7[key]))
	if key == "intersection":
		pass
	else:
		section37[key] = i3[key] + i7[key]


sections.append(section37)


section38 = {}
for key in i3.keys():
	if key == "trade":
		section38[key] = list(set(i3[key] + i8[key]))
	if key == "intersection":
		pass
	else:
		section38[key] = i3[key] + i8[key]


sections.append(section38)


section39 = {}
for key in i3.keys():
	if key == "trade":
		section39[key] = list(set(i3[key] + i9[key]))
	if key == "intersection":
		pass
	else:
		section39[key] = i3[key] + i9[key]


sections.append(section39)


section310 = {}
for key in i3.keys():
	if key == "trade":
		section310[key] = list(set(i3[key] + i10[key]))
	if key == "intersection":
		pass
	else:
		section310[key] = i3[key] + i10[key]


sections.append(section310)


section312 = {}
for key in i3.keys():
	if key == "trade":
		section312[key] = list(set(i3[key] + i12[key]))
	if key == "intersection":
		pass
	else:
		section312[key] = i3[key] + i12[key]


sections.append(section312)


section313 = {}
for key in i3.keys():
	if key == "trade":
		section313[key] = list(set(i3[key] + i13[key]))
	if key == "intersection":
		pass
	else:
		section313[key] = i3[key] + i13[key]


sections.append(section313)


section314 = {}
for key in i3.keys():
	if key == "trade":
		section314[key] = list(set(i3[key] + i14[key]))
	if key == "intersection":
		pass
	else:
		section314[key] = i3[key] + i14[key]


sections.append(section314)


section315 = {}
for key in i3.keys():
	if key == "trade":
		section315[key] = list(set(i3[key] + i15[key]))
	if key == "intersection":
		pass
	else:
		section315[key] = i3[key] + i15[key]


sections.append(section315)


section316 = {}
for key in i3.keys():
	if key == "trade":
		section316[key] = list(set(i3[key] + i16[key]))
	if key == "intersection":
		pass
	else:
		section316[key] = i3[key] + i16[key]


sections.append(section316)


section317 = {}
for key in i3.keys():
	if key == "trade":
		section317[key] = list(set(i3[key] + i17[key]))
	if key == "intersection":
		pass
	else:
		section317[key] = i3[key] + i17[key]


sections.append(section317)


section318 = {}
for key in i3.keys():
	if key == "trade":
		section318[key] = list(set(i3[key] + i18[key]))
	if key == "intersection":
		pass
	else:
		section318[key] = i3[key] + i18[key]


sections.append(section318)


section319 = {}
for key in i3.keys():
	if key == "trade":
		section319[key] = list(set(i3[key] + i19[key]))
	if key == "intersection":
		pass
	else:
		section319[key] = i3[key] + i19[key]


sections.append(section319)


section320 = {}
for key in i3.keys():
	if key == "trade":
		section320[key] = list(set(i3[key] + i20[key]))
	if key == "intersection":
		pass
	else:
		section320[key] = i3[key] + i20[key]


sections.append(section320)


section321 = {}
for key in i3.keys():
	if key == "trade":
		section321[key] = list(set(i3[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section321[key] = i3[key] + i21[key]


sections.append(section321)


section322 = {}
for key in i3.keys():
	if key == "trade":
		section322[key] = list(set(i3[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section322[key] = i3[key] + i22[key]


sections.append(section322)


section323 = {}
for key in i3.keys():
	if key == "trade":
		section323[key] = list(set(i3[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section323[key] = i3[key] + i23[key]


sections.append(section323)


section324 = {}
for key in i3.keys():
	if key == "trade":
		section324[key] = list(set(i3[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section324[key] = i3[key] + i24[key]


sections.append(section324)


section325 = {}
for key in i3.keys():
	if key == "trade":
		section325[key] = list(set(i3[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section325[key] = i3[key] + i25[key]


sections.append(section325)


section326 = {}
for key in i3.keys():
	if key == "trade":
		section326[key] = list(set(i3[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section326[key] = i3[key] + i26[key]


sections.append(section326)


section327 = {}
for key in i3.keys():
	if key == "trade":
		section327[key] = list(set(i3[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section327[key] = i3[key] + i27[key]


sections.append(section327)


section328 = {}
for key in i3.keys():
	if key == "trade":
		section328[key] = list(set(i3[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section328[key] = i3[key] + i28[key]


sections.append(section328)


section329 = {}
for key in i3.keys():
	if key == "trade":
		section329[key] = list(set(i3[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section329[key] = i3[key] + i29[key]


sections.append(section329)


section330 = {}
for key in i3.keys():
	if key == "trade":
		section330[key] = list(set(i3[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section330[key] = i3[key] + i30[key]


sections.append(section330)


section331 = {}
for key in i3.keys():
	if key == "trade":
		section331[key] = list(set(i3[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section331[key] = i3[key] + i31[key]


sections.append(section331)


section332 = {}
for key in i3.keys():
	if key == "trade":
		section332[key] = list(set(i3[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section332[key] = i3[key] + i32[key]


sections.append(section332)


section333 = {}
for key in i3.keys():
	if key == "trade":
		section333[key] = list(set(i3[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section333[key] = i3[key] + i33[key]


sections.append(section333)


section334 = {}
for key in i3.keys():
	if key == "trade":
		section334[key] = list(set(i3[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section334[key] = i3[key] + i34[key]


sections.append(section334)


section335 = {}
for key in i3.keys():
	if key == "trade":
		section335[key] = list(set(i3[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section335[key] = i3[key] + i35[key]


sections.append(section335)


section336 = {}
for key in i3.keys():
	if key == "trade":
		section336[key] = list(set(i3[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section336[key] = i3[key] + i36[key]


sections.append(section336)


section337 = {}
for key in i3.keys():
	if key == "trade":
		section337[key] = list(set(i3[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section337[key] = i3[key] + i37[key]


sections.append(section337)


section338 = {}
for key in i3.keys():
	if key == "trade":
		section338[key] = list(set(i3[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section338[key] = i3[key] + i38[key]


sections.append(section338)


section339 = {}
for key in i3.keys():
	if key == "trade":
		section339[key] = list(set(i3[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section339[key] = i3[key] + i39[key]


sections.append(section339)


section340 = {}
for key in i3.keys():
	if key == "trade":
		section340[key] = list(set(i3[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section340[key] = i3[key] + i40[key]


sections.append(section340)


section341 = {}
for key in i3.keys():
	if key == "trade":
		section341[key] = list(set(i3[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section341[key] = i3[key] + i41[key]


sections.append(section341)


section342 = {}
for key in i3.keys():
	if key == "trade":
		section342[key] = list(set(i3[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section342[key] = i3[key] + i42[key]


sections.append(section342)


section343 = {}
for key in i3.keys():
	if key == "trade":
		section343[key] = list(set(i3[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section343[key] = i3[key] + i43[key]


sections.append(section343)


section344 = {}
for key in i3.keys():
	if key == "trade":
		section344[key] = list(set(i3[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section344[key] = i3[key] + i44[key]


sections.append(section344)


section345 = {}
for key in i3.keys():
	if key == "trade":
		section345[key] = list(set(i3[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section345[key] = i3[key] + i45[key]


sections.append(section345)


section346 = {}
for key in i3.keys():
	if key == "trade":
		section346[key] = list(set(i3[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section346[key] = i3[key] + i46[key]


sections.append(section346)


section347 = {}
for key in i3.keys():
	if key == "trade":
		section347[key] = list(set(i3[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section347[key] = i3[key] + i47[key]


sections.append(section347)


section348 = {}
for key in i3.keys():
	if key == "trade":
		section348[key] = list(set(i3[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section348[key] = i3[key] + i48[key]


sections.append(section348)


section349 = {}
for key in i3.keys():
	if key == "trade":
		section349[key] = list(set(i3[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section349[key] = i3[key] + i49[key]


sections.append(section349)


section350 = {}
for key in i3.keys():
	if key == "trade":
		section350[key] = list(set(i3[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section350[key] = i3[key] + i50[key]


sections.append(section350)


section351 = {}
for key in i3.keys():
	if key == "trade":
		section351[key] = list(set(i3[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section351[key] = i3[key] + i51[key]


sections.append(section351)


section352 = {}
for key in i3.keys():
	if key == "trade":
		section352[key] = list(set(i3[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section352[key] = i3[key] + i52[key]


sections.append(section352)


section353 = {}
for key in i3.keys():
	if key == "trade":
		section353[key] = list(set(i3[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section353[key] = i3[key] + i53[key]


sections.append(section353)


section354 = {}
for key in i3.keys():
	if key == "trade":
		section354[key] = list(set(i3[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section354[key] = i3[key] + i54[key]


sections.append(section354)


section46 = {}
for key in i4.keys():
	if key == "trade":
		section46[key] = list(set(i4[key] + i6[key]))
	if key == "intersection":
		pass
	else:
		section46[key] = i4[key] + i6[key]


sections.append(section46)


section47 = {}
for key in i4.keys():
	if key == "trade":
		section47[key] = list(set(i4[key] + i7[key]))
	if key == "intersection":
		pass
	else:
		section47[key] = i4[key] + i7[key]


sections.append(section47)


section48 = {}
for key in i4.keys():
	if key == "trade":
		section48[key] = list(set(i4[key] + i8[key]))
	if key == "intersection":
		pass
	else:
		section48[key] = i4[key] + i8[key]


sections.append(section48)


section49 = {}
for key in i4.keys():
	if key == "trade":
		section49[key] = list(set(i4[key] + i9[key]))
	if key == "intersection":
		pass
	else:
		section49[key] = i4[key] + i9[key]


sections.append(section49)


section410 = {}
for key in i4.keys():
	if key == "trade":
		section410[key] = list(set(i4[key] + i10[key]))
	if key == "intersection":
		pass
	else:
		section410[key] = i4[key] + i10[key]


sections.append(section410)


section411 = {}
for key in i4.keys():
	if key == "trade":
		section411[key] = list(set(i4[key] + i11[key]))
	if key == "intersection":
		pass
	else:
		section411[key] = i4[key] + i11[key]


sections.append(section411)


section412 = {}
for key in i4.keys():
	if key == "trade":
		section412[key] = list(set(i4[key] + i12[key]))
	if key == "intersection":
		pass
	else:
		section412[key] = i4[key] + i12[key]


sections.append(section412)


section413 = {}
for key in i4.keys():
	if key == "trade":
		section413[key] = list(set(i4[key] + i13[key]))
	if key == "intersection":
		pass
	else:
		section413[key] = i4[key] + i13[key]


sections.append(section413)


section414 = {}
for key in i4.keys():
	if key == "trade":
		section414[key] = list(set(i4[key] + i14[key]))
	if key == "intersection":
		pass
	else:
		section414[key] = i4[key] + i14[key]


sections.append(section414)


section415 = {}
for key in i4.keys():
	if key == "trade":
		section415[key] = list(set(i4[key] + i15[key]))
	if key == "intersection":
		pass
	else:
		section415[key] = i4[key] + i15[key]


sections.append(section415)


section416 = {}
for key in i4.keys():
	if key == "trade":
		section416[key] = list(set(i4[key] + i16[key]))
	if key == "intersection":
		pass
	else:
		section416[key] = i4[key] + i16[key]


sections.append(section416)


section417 = {}
for key in i4.keys():
	if key == "trade":
		section417[key] = list(set(i4[key] + i17[key]))
	if key == "intersection":
		pass
	else:
		section417[key] = i4[key] + i17[key]


sections.append(section417)


section418 = {}
for key in i4.keys():
	if key == "trade":
		section418[key] = list(set(i4[key] + i18[key]))
	if key == "intersection":
		pass
	else:
		section418[key] = i4[key] + i18[key]


sections.append(section418)


section419 = {}
for key in i4.keys():
	if key == "trade":
		section419[key] = list(set(i4[key] + i19[key]))
	if key == "intersection":
		pass
	else:
		section419[key] = i4[key] + i19[key]


sections.append(section419)


section420 = {}
for key in i4.keys():
	if key == "trade":
		section420[key] = list(set(i4[key] + i20[key]))
	if key == "intersection":
		pass
	else:
		section420[key] = i4[key] + i20[key]


sections.append(section420)


section421 = {}
for key in i4.keys():
	if key == "trade":
		section421[key] = list(set(i4[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section421[key] = i4[key] + i21[key]


sections.append(section421)


section422 = {}
for key in i4.keys():
	if key == "trade":
		section422[key] = list(set(i4[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section422[key] = i4[key] + i22[key]


sections.append(section422)


section423 = {}
for key in i4.keys():
	if key == "trade":
		section423[key] = list(set(i4[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section423[key] = i4[key] + i23[key]


sections.append(section423)


section424 = {}
for key in i4.keys():
	if key == "trade":
		section424[key] = list(set(i4[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section424[key] = i4[key] + i24[key]


sections.append(section424)


section425 = {}
for key in i4.keys():
	if key == "trade":
		section425[key] = list(set(i4[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section425[key] = i4[key] + i25[key]


sections.append(section425)


section426 = {}
for key in i4.keys():
	if key == "trade":
		section426[key] = list(set(i4[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section426[key] = i4[key] + i26[key]


sections.append(section426)


section427 = {}
for key in i4.keys():
	if key == "trade":
		section427[key] = list(set(i4[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section427[key] = i4[key] + i27[key]


sections.append(section427)


section428 = {}
for key in i4.keys():
	if key == "trade":
		section428[key] = list(set(i4[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section428[key] = i4[key] + i28[key]


sections.append(section428)


section429 = {}
for key in i4.keys():
	if key == "trade":
		section429[key] = list(set(i4[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section429[key] = i4[key] + i29[key]


sections.append(section429)


section430 = {}
for key in i4.keys():
	if key == "trade":
		section430[key] = list(set(i4[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section430[key] = i4[key] + i30[key]


sections.append(section430)


section431 = {}
for key in i4.keys():
	if key == "trade":
		section431[key] = list(set(i4[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section431[key] = i4[key] + i31[key]


sections.append(section431)


section432 = {}
for key in i4.keys():
	if key == "trade":
		section432[key] = list(set(i4[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section432[key] = i4[key] + i32[key]


sections.append(section432)


section433 = {}
for key in i4.keys():
	if key == "trade":
		section433[key] = list(set(i4[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section433[key] = i4[key] + i33[key]


sections.append(section433)


section434 = {}
for key in i4.keys():
	if key == "trade":
		section434[key] = list(set(i4[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section434[key] = i4[key] + i34[key]


sections.append(section434)


section435 = {}
for key in i4.keys():
	if key == "trade":
		section435[key] = list(set(i4[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section435[key] = i4[key] + i35[key]


sections.append(section435)


section436 = {}
for key in i4.keys():
	if key == "trade":
		section436[key] = list(set(i4[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section436[key] = i4[key] + i36[key]


sections.append(section436)


section437 = {}
for key in i4.keys():
	if key == "trade":
		section437[key] = list(set(i4[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section437[key] = i4[key] + i37[key]


sections.append(section437)


section438 = {}
for key in i4.keys():
	if key == "trade":
		section438[key] = list(set(i4[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section438[key] = i4[key] + i38[key]


sections.append(section438)


section439 = {}
for key in i4.keys():
	if key == "trade":
		section439[key] = list(set(i4[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section439[key] = i4[key] + i39[key]


sections.append(section439)


section440 = {}
for key in i4.keys():
	if key == "trade":
		section440[key] = list(set(i4[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section440[key] = i4[key] + i40[key]


sections.append(section440)


section441 = {}
for key in i4.keys():
	if key == "trade":
		section441[key] = list(set(i4[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section441[key] = i4[key] + i41[key]


sections.append(section441)


section442 = {}
for key in i4.keys():
	if key == "trade":
		section442[key] = list(set(i4[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section442[key] = i4[key] + i42[key]


sections.append(section442)


section443 = {}
for key in i4.keys():
	if key == "trade":
		section443[key] = list(set(i4[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section443[key] = i4[key] + i43[key]


sections.append(section443)


section444 = {}
for key in i4.keys():
	if key == "trade":
		section444[key] = list(set(i4[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section444[key] = i4[key] + i44[key]


sections.append(section444)


section445 = {}
for key in i4.keys():
	if key == "trade":
		section445[key] = list(set(i4[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section445[key] = i4[key] + i45[key]


sections.append(section445)


section446 = {}
for key in i4.keys():
	if key == "trade":
		section446[key] = list(set(i4[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section446[key] = i4[key] + i46[key]


sections.append(section446)


section447 = {}
for key in i4.keys():
	if key == "trade":
		section447[key] = list(set(i4[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section447[key] = i4[key] + i47[key]


sections.append(section447)


section448 = {}
for key in i4.keys():
	if key == "trade":
		section448[key] = list(set(i4[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section448[key] = i4[key] + i48[key]


sections.append(section448)


section449 = {}
for key in i4.keys():
	if key == "trade":
		section449[key] = list(set(i4[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section449[key] = i4[key] + i49[key]


sections.append(section449)


section450 = {}
for key in i4.keys():
	if key == "trade":
		section450[key] = list(set(i4[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section450[key] = i4[key] + i50[key]


sections.append(section450)


section451 = {}
for key in i4.keys():
	if key == "trade":
		section451[key] = list(set(i4[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section451[key] = i4[key] + i51[key]


sections.append(section451)


section452 = {}
for key in i4.keys():
	if key == "trade":
		section452[key] = list(set(i4[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section452[key] = i4[key] + i52[key]


sections.append(section452)


section453 = {}
for key in i4.keys():
	if key == "trade":
		section453[key] = list(set(i4[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section453[key] = i4[key] + i53[key]


sections.append(section453)


section454 = {}
for key in i4.keys():
	if key == "trade":
		section454[key] = list(set(i4[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section454[key] = i4[key] + i54[key]


sections.append(section454)


section57 = {}
for key in i5.keys():
	if key == "trade":
		section57[key] = list(set(i5[key] + i7[key]))
	if key == "intersection":
		pass
	else:
		section57[key] = i5[key] + i7[key]


sections.append(section57)


section58 = {}
for key in i5.keys():
	if key == "trade":
		section58[key] = list(set(i5[key] + i8[key]))
	if key == "intersection":
		pass
	else:
		section58[key] = i5[key] + i8[key]


sections.append(section58)


section59 = {}
for key in i5.keys():
	if key == "trade":
		section59[key] = list(set(i5[key] + i9[key]))
	if key == "intersection":
		pass
	else:
		section59[key] = i5[key] + i9[key]


sections.append(section59)


section510 = {}
for key in i5.keys():
	if key == "trade":
		section510[key] = list(set(i5[key] + i10[key]))
	if key == "intersection":
		pass
	else:
		section510[key] = i5[key] + i10[key]


sections.append(section510)


section511 = {}
for key in i5.keys():
	if key == "trade":
		section511[key] = list(set(i5[key] + i11[key]))
	if key == "intersection":
		pass
	else:
		section511[key] = i5[key] + i11[key]


sections.append(section511)


section512 = {}
for key in i5.keys():
	if key == "trade":
		section512[key] = list(set(i5[key] + i12[key]))
	if key == "intersection":
		pass
	else:
		section512[key] = i5[key] + i12[key]


sections.append(section512)


section514 = {}
for key in i5.keys():
	if key == "trade":
		section514[key] = list(set(i5[key] + i14[key]))
	if key == "intersection":
		pass
	else:
		section514[key] = i5[key] + i14[key]


sections.append(section514)


section515 = {}
for key in i5.keys():
	if key == "trade":
		section515[key] = list(set(i5[key] + i15[key]))
	if key == "intersection":
		pass
	else:
		section515[key] = i5[key] + i15[key]


sections.append(section515)


section516 = {}
for key in i5.keys():
	if key == "trade":
		section516[key] = list(set(i5[key] + i16[key]))
	if key == "intersection":
		pass
	else:
		section516[key] = i5[key] + i16[key]


sections.append(section516)


section517 = {}
for key in i5.keys():
	if key == "trade":
		section517[key] = list(set(i5[key] + i17[key]))
	if key == "intersection":
		pass
	else:
		section517[key] = i5[key] + i17[key]


sections.append(section517)


section518 = {}
for key in i5.keys():
	if key == "trade":
		section518[key] = list(set(i5[key] + i18[key]))
	if key == "intersection":
		pass
	else:
		section518[key] = i5[key] + i18[key]


sections.append(section518)


section519 = {}
for key in i5.keys():
	if key == "trade":
		section519[key] = list(set(i5[key] + i19[key]))
	if key == "intersection":
		pass
	else:
		section519[key] = i5[key] + i19[key]


sections.append(section519)


section520 = {}
for key in i5.keys():
	if key == "trade":
		section520[key] = list(set(i5[key] + i20[key]))
	if key == "intersection":
		pass
	else:
		section520[key] = i5[key] + i20[key]


sections.append(section520)


section521 = {}
for key in i5.keys():
	if key == "trade":
		section521[key] = list(set(i5[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section521[key] = i5[key] + i21[key]


sections.append(section521)


section522 = {}
for key in i5.keys():
	if key == "trade":
		section522[key] = list(set(i5[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section522[key] = i5[key] + i22[key]


sections.append(section522)


section523 = {}
for key in i5.keys():
	if key == "trade":
		section523[key] = list(set(i5[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section523[key] = i5[key] + i23[key]


sections.append(section523)


section524 = {}
for key in i5.keys():
	if key == "trade":
		section524[key] = list(set(i5[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section524[key] = i5[key] + i24[key]


sections.append(section524)


section525 = {}
for key in i5.keys():
	if key == "trade":
		section525[key] = list(set(i5[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section525[key] = i5[key] + i25[key]


sections.append(section525)


section526 = {}
for key in i5.keys():
	if key == "trade":
		section526[key] = list(set(i5[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section526[key] = i5[key] + i26[key]


sections.append(section526)


section527 = {}
for key in i5.keys():
	if key == "trade":
		section527[key] = list(set(i5[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section527[key] = i5[key] + i27[key]


sections.append(section527)


section528 = {}
for key in i5.keys():
	if key == "trade":
		section528[key] = list(set(i5[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section528[key] = i5[key] + i28[key]


sections.append(section528)


section529 = {}
for key in i5.keys():
	if key == "trade":
		section529[key] = list(set(i5[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section529[key] = i5[key] + i29[key]


sections.append(section529)


section530 = {}
for key in i5.keys():
	if key == "trade":
		section530[key] = list(set(i5[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section530[key] = i5[key] + i30[key]


sections.append(section530)


section531 = {}
for key in i5.keys():
	if key == "trade":
		section531[key] = list(set(i5[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section531[key] = i5[key] + i31[key]


sections.append(section531)


section532 = {}
for key in i5.keys():
	if key == "trade":
		section532[key] = list(set(i5[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section532[key] = i5[key] + i32[key]


sections.append(section532)


section533 = {}
for key in i5.keys():
	if key == "trade":
		section533[key] = list(set(i5[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section533[key] = i5[key] + i33[key]


sections.append(section533)


section534 = {}
for key in i5.keys():
	if key == "trade":
		section534[key] = list(set(i5[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section534[key] = i5[key] + i34[key]


sections.append(section534)


section535 = {}
for key in i5.keys():
	if key == "trade":
		section535[key] = list(set(i5[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section535[key] = i5[key] + i35[key]


sections.append(section535)


section536 = {}
for key in i5.keys():
	if key == "trade":
		section536[key] = list(set(i5[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section536[key] = i5[key] + i36[key]


sections.append(section536)


section537 = {}
for key in i5.keys():
	if key == "trade":
		section537[key] = list(set(i5[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section537[key] = i5[key] + i37[key]


sections.append(section537)


section538 = {}
for key in i5.keys():
	if key == "trade":
		section538[key] = list(set(i5[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section538[key] = i5[key] + i38[key]


sections.append(section538)


section539 = {}
for key in i5.keys():
	if key == "trade":
		section539[key] = list(set(i5[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section539[key] = i5[key] + i39[key]


sections.append(section539)


section540 = {}
for key in i5.keys():
	if key == "trade":
		section540[key] = list(set(i5[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section540[key] = i5[key] + i40[key]


sections.append(section540)


section541 = {}
for key in i5.keys():
	if key == "trade":
		section541[key] = list(set(i5[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section541[key] = i5[key] + i41[key]


sections.append(section541)


section542 = {}
for key in i5.keys():
	if key == "trade":
		section542[key] = list(set(i5[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section542[key] = i5[key] + i42[key]


sections.append(section542)


section543 = {}
for key in i5.keys():
	if key == "trade":
		section543[key] = list(set(i5[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section543[key] = i5[key] + i43[key]


sections.append(section543)


section544 = {}
for key in i5.keys():
	if key == "trade":
		section544[key] = list(set(i5[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section544[key] = i5[key] + i44[key]


sections.append(section544)


section545 = {}
for key in i5.keys():
	if key == "trade":
		section545[key] = list(set(i5[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section545[key] = i5[key] + i45[key]


sections.append(section545)


section546 = {}
for key in i5.keys():
	if key == "trade":
		section546[key] = list(set(i5[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section546[key] = i5[key] + i46[key]


sections.append(section546)


section547 = {}
for key in i5.keys():
	if key == "trade":
		section547[key] = list(set(i5[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section547[key] = i5[key] + i47[key]


sections.append(section547)


section548 = {}
for key in i5.keys():
	if key == "trade":
		section548[key] = list(set(i5[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section548[key] = i5[key] + i48[key]


sections.append(section548)


section549 = {}
for key in i5.keys():
	if key == "trade":
		section549[key] = list(set(i5[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section549[key] = i5[key] + i49[key]


sections.append(section549)


section550 = {}
for key in i5.keys():
	if key == "trade":
		section550[key] = list(set(i5[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section550[key] = i5[key] + i50[key]


sections.append(section550)


section551 = {}
for key in i5.keys():
	if key == "trade":
		section551[key] = list(set(i5[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section551[key] = i5[key] + i51[key]


sections.append(section551)


section552 = {}
for key in i5.keys():
	if key == "trade":
		section552[key] = list(set(i5[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section552[key] = i5[key] + i52[key]


sections.append(section552)


section553 = {}
for key in i5.keys():
	if key == "trade":
		section553[key] = list(set(i5[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section553[key] = i5[key] + i53[key]


sections.append(section553)


section554 = {}
for key in i5.keys():
	if key == "trade":
		section554[key] = list(set(i5[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section554[key] = i5[key] + i54[key]


sections.append(section554)


section68 = {}
for key in i6.keys():
	if key == "trade":
		section68[key] = list(set(i6[key] + i8[key]))
	if key == "intersection":
		pass
	else:
		section68[key] = i6[key] + i8[key]


sections.append(section68)


section69 = {}
for key in i6.keys():
	if key == "trade":
		section69[key] = list(set(i6[key] + i9[key]))
	if key == "intersection":
		pass
	else:
		section69[key] = i6[key] + i9[key]


sections.append(section69)


section610 = {}
for key in i6.keys():
	if key == "trade":
		section610[key] = list(set(i6[key] + i10[key]))
	if key == "intersection":
		pass
	else:
		section610[key] = i6[key] + i10[key]


sections.append(section610)


section611 = {}
for key in i6.keys():
	if key == "trade":
		section611[key] = list(set(i6[key] + i11[key]))
	if key == "intersection":
		pass
	else:
		section611[key] = i6[key] + i11[key]


sections.append(section611)


section612 = {}
for key in i6.keys():
	if key == "trade":
		section612[key] = list(set(i6[key] + i12[key]))
	if key == "intersection":
		pass
	else:
		section612[key] = i6[key] + i12[key]


sections.append(section612)


section613 = {}
for key in i6.keys():
	if key == "trade":
		section613[key] = list(set(i6[key] + i13[key]))
	if key == "intersection":
		pass
	else:
		section613[key] = i6[key] + i13[key]


sections.append(section613)


section614 = {}
for key in i6.keys():
	if key == "trade":
		section614[key] = list(set(i6[key] + i14[key]))
	if key == "intersection":
		pass
	else:
		section614[key] = i6[key] + i14[key]


sections.append(section614)


section615 = {}
for key in i6.keys():
	if key == "trade":
		section615[key] = list(set(i6[key] + i15[key]))
	if key == "intersection":
		pass
	else:
		section615[key] = i6[key] + i15[key]


sections.append(section615)


section616 = {}
for key in i6.keys():
	if key == "trade":
		section616[key] = list(set(i6[key] + i16[key]))
	if key == "intersection":
		pass
	else:
		section616[key] = i6[key] + i16[key]


sections.append(section616)


section617 = {}
for key in i6.keys():
	if key == "trade":
		section617[key] = list(set(i6[key] + i17[key]))
	if key == "intersection":
		pass
	else:
		section617[key] = i6[key] + i17[key]


sections.append(section617)


section618 = {}
for key in i6.keys():
	if key == "trade":
		section618[key] = list(set(i6[key] + i18[key]))
	if key == "intersection":
		pass
	else:
		section618[key] = i6[key] + i18[key]


sections.append(section618)


section619 = {}
for key in i6.keys():
	if key == "trade":
		section619[key] = list(set(i6[key] + i19[key]))
	if key == "intersection":
		pass
	else:
		section619[key] = i6[key] + i19[key]


sections.append(section619)


section620 = {}
for key in i6.keys():
	if key == "trade":
		section620[key] = list(set(i6[key] + i20[key]))
	if key == "intersection":
		pass
	else:
		section620[key] = i6[key] + i20[key]


sections.append(section620)


section621 = {}
for key in i6.keys():
	if key == "trade":
		section621[key] = list(set(i6[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section621[key] = i6[key] + i21[key]


sections.append(section621)


section622 = {}
for key in i6.keys():
	if key == "trade":
		section622[key] = list(set(i6[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section622[key] = i6[key] + i22[key]


sections.append(section622)


section623 = {}
for key in i6.keys():
	if key == "trade":
		section623[key] = list(set(i6[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section623[key] = i6[key] + i23[key]


sections.append(section623)


section624 = {}
for key in i6.keys():
	if key == "trade":
		section624[key] = list(set(i6[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section624[key] = i6[key] + i24[key]


sections.append(section624)


section625 = {}
for key in i6.keys():
	if key == "trade":
		section625[key] = list(set(i6[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section625[key] = i6[key] + i25[key]


sections.append(section625)


section626 = {}
for key in i6.keys():
	if key == "trade":
		section626[key] = list(set(i6[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section626[key] = i6[key] + i26[key]


sections.append(section626)


section627 = {}
for key in i6.keys():
	if key == "trade":
		section627[key] = list(set(i6[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section627[key] = i6[key] + i27[key]


sections.append(section627)


section628 = {}
for key in i6.keys():
	if key == "trade":
		section628[key] = list(set(i6[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section628[key] = i6[key] + i28[key]


sections.append(section628)


section629 = {}
for key in i6.keys():
	if key == "trade":
		section629[key] = list(set(i6[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section629[key] = i6[key] + i29[key]


sections.append(section629)


section630 = {}
for key in i6.keys():
	if key == "trade":
		section630[key] = list(set(i6[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section630[key] = i6[key] + i30[key]


sections.append(section630)


section631 = {}
for key in i6.keys():
	if key == "trade":
		section631[key] = list(set(i6[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section631[key] = i6[key] + i31[key]


sections.append(section631)


section632 = {}
for key in i6.keys():
	if key == "trade":
		section632[key] = list(set(i6[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section632[key] = i6[key] + i32[key]


sections.append(section632)


section633 = {}
for key in i6.keys():
	if key == "trade":
		section633[key] = list(set(i6[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section633[key] = i6[key] + i33[key]


sections.append(section633)


section634 = {}
for key in i6.keys():
	if key == "trade":
		section634[key] = list(set(i6[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section634[key] = i6[key] + i34[key]


sections.append(section634)


section635 = {}
for key in i6.keys():
	if key == "trade":
		section635[key] = list(set(i6[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section635[key] = i6[key] + i35[key]


sections.append(section635)


section636 = {}
for key in i6.keys():
	if key == "trade":
		section636[key] = list(set(i6[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section636[key] = i6[key] + i36[key]


sections.append(section636)


section637 = {}
for key in i6.keys():
	if key == "trade":
		section637[key] = list(set(i6[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section637[key] = i6[key] + i37[key]


sections.append(section637)


section638 = {}
for key in i6.keys():
	if key == "trade":
		section638[key] = list(set(i6[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section638[key] = i6[key] + i38[key]


sections.append(section638)


section639 = {}
for key in i6.keys():
	if key == "trade":
		section639[key] = list(set(i6[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section639[key] = i6[key] + i39[key]


sections.append(section639)


section640 = {}
for key in i6.keys():
	if key == "trade":
		section640[key] = list(set(i6[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section640[key] = i6[key] + i40[key]


sections.append(section640)


section641 = {}
for key in i6.keys():
	if key == "trade":
		section641[key] = list(set(i6[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section641[key] = i6[key] + i41[key]


sections.append(section641)


section642 = {}
for key in i6.keys():
	if key == "trade":
		section642[key] = list(set(i6[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section642[key] = i6[key] + i42[key]


sections.append(section642)


section643 = {}
for key in i6.keys():
	if key == "trade":
		section643[key] = list(set(i6[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section643[key] = i6[key] + i43[key]


sections.append(section643)


section644 = {}
for key in i6.keys():
	if key == "trade":
		section644[key] = list(set(i6[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section644[key] = i6[key] + i44[key]


sections.append(section644)


section645 = {}
for key in i6.keys():
	if key == "trade":
		section645[key] = list(set(i6[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section645[key] = i6[key] + i45[key]


sections.append(section645)


section646 = {}
for key in i6.keys():
	if key == "trade":
		section646[key] = list(set(i6[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section646[key] = i6[key] + i46[key]


sections.append(section646)


section647 = {}
for key in i6.keys():
	if key == "trade":
		section647[key] = list(set(i6[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section647[key] = i6[key] + i47[key]


sections.append(section647)


section648 = {}
for key in i6.keys():
	if key == "trade":
		section648[key] = list(set(i6[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section648[key] = i6[key] + i48[key]


sections.append(section648)


section649 = {}
for key in i6.keys():
	if key == "trade":
		section649[key] = list(set(i6[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section649[key] = i6[key] + i49[key]


sections.append(section649)


section650 = {}
for key in i6.keys():
	if key == "trade":
		section650[key] = list(set(i6[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section650[key] = i6[key] + i50[key]


sections.append(section650)


section651 = {}
for key in i6.keys():
	if key == "trade":
		section651[key] = list(set(i6[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section651[key] = i6[key] + i51[key]


sections.append(section651)


section652 = {}
for key in i6.keys():
	if key == "trade":
		section652[key] = list(set(i6[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section652[key] = i6[key] + i52[key]


sections.append(section652)


section653 = {}
for key in i6.keys():
	if key == "trade":
		section653[key] = list(set(i6[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section653[key] = i6[key] + i53[key]


sections.append(section653)


section654 = {}
for key in i6.keys():
	if key == "trade":
		section654[key] = list(set(i6[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section654[key] = i6[key] + i54[key]


sections.append(section654)


section78 = {}
for key in i7.keys():
	if key == "trade":
		section78[key] = list(set(i7[key] + i8[key]))
	if key == "intersection":
		pass
	else:
		section78[key] = i7[key] + i8[key]


sections.append(section78)


section79 = {}
for key in i7.keys():
	if key == "trade":
		section79[key] = list(set(i7[key] + i9[key]))
	if key == "intersection":
		pass
	else:
		section79[key] = i7[key] + i9[key]


sections.append(section79)


section710 = {}
for key in i7.keys():
	if key == "trade":
		section710[key] = list(set(i7[key] + i10[key]))
	if key == "intersection":
		pass
	else:
		section710[key] = i7[key] + i10[key]


sections.append(section710)


section711 = {}
for key in i7.keys():
	if key == "trade":
		section711[key] = list(set(i7[key] + i11[key]))
	if key == "intersection":
		pass
	else:
		section711[key] = i7[key] + i11[key]


sections.append(section711)


section712 = {}
for key in i7.keys():
	if key == "trade":
		section712[key] = list(set(i7[key] + i12[key]))
	if key == "intersection":
		pass
	else:
		section712[key] = i7[key] + i12[key]


sections.append(section712)


section714 = {}
for key in i7.keys():
	if key == "trade":
		section714[key] = list(set(i7[key] + i14[key]))
	if key == "intersection":
		pass
	else:
		section714[key] = i7[key] + i14[key]


sections.append(section714)


section715 = {}
for key in i7.keys():
	if key == "trade":
		section715[key] = list(set(i7[key] + i15[key]))
	if key == "intersection":
		pass
	else:
		section715[key] = i7[key] + i15[key]


sections.append(section715)


section716 = {}
for key in i7.keys():
	if key == "trade":
		section716[key] = list(set(i7[key] + i16[key]))
	if key == "intersection":
		pass
	else:
		section716[key] = i7[key] + i16[key]


sections.append(section716)


section717 = {}
for key in i7.keys():
	if key == "trade":
		section717[key] = list(set(i7[key] + i17[key]))
	if key == "intersection":
		pass
	else:
		section717[key] = i7[key] + i17[key]


sections.append(section717)


section718 = {}
for key in i7.keys():
	if key == "trade":
		section718[key] = list(set(i7[key] + i18[key]))
	if key == "intersection":
		pass
	else:
		section718[key] = i7[key] + i18[key]


sections.append(section718)


section719 = {}
for key in i7.keys():
	if key == "trade":
		section719[key] = list(set(i7[key] + i19[key]))
	if key == "intersection":
		pass
	else:
		section719[key] = i7[key] + i19[key]


sections.append(section719)


section720 = {}
for key in i7.keys():
	if key == "trade":
		section720[key] = list(set(i7[key] + i20[key]))
	if key == "intersection":
		pass
	else:
		section720[key] = i7[key] + i20[key]


sections.append(section720)


section721 = {}
for key in i7.keys():
	if key == "trade":
		section721[key] = list(set(i7[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section721[key] = i7[key] + i21[key]


sections.append(section721)


section722 = {}
for key in i7.keys():
	if key == "trade":
		section722[key] = list(set(i7[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section722[key] = i7[key] + i22[key]


sections.append(section722)


section723 = {}
for key in i7.keys():
	if key == "trade":
		section723[key] = list(set(i7[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section723[key] = i7[key] + i23[key]


sections.append(section723)


section724 = {}
for key in i7.keys():
	if key == "trade":
		section724[key] = list(set(i7[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section724[key] = i7[key] + i24[key]


sections.append(section724)


section725 = {}
for key in i7.keys():
	if key == "trade":
		section725[key] = list(set(i7[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section725[key] = i7[key] + i25[key]


sections.append(section725)


section726 = {}
for key in i7.keys():
	if key == "trade":
		section726[key] = list(set(i7[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section726[key] = i7[key] + i26[key]


sections.append(section726)


section727 = {}
for key in i7.keys():
	if key == "trade":
		section727[key] = list(set(i7[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section727[key] = i7[key] + i27[key]


sections.append(section727)


section728 = {}
for key in i7.keys():
	if key == "trade":
		section728[key] = list(set(i7[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section728[key] = i7[key] + i28[key]


sections.append(section728)


section729 = {}
for key in i7.keys():
	if key == "trade":
		section729[key] = list(set(i7[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section729[key] = i7[key] + i29[key]


sections.append(section729)


section730 = {}
for key in i7.keys():
	if key == "trade":
		section730[key] = list(set(i7[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section730[key] = i7[key] + i30[key]


sections.append(section730)


section731 = {}
for key in i7.keys():
	if key == "trade":
		section731[key] = list(set(i7[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section731[key] = i7[key] + i31[key]


sections.append(section731)


section732 = {}
for key in i7.keys():
	if key == "trade":
		section732[key] = list(set(i7[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section732[key] = i7[key] + i32[key]


sections.append(section732)


section733 = {}
for key in i7.keys():
	if key == "trade":
		section733[key] = list(set(i7[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section733[key] = i7[key] + i33[key]


sections.append(section733)


section734 = {}
for key in i7.keys():
	if key == "trade":
		section734[key] = list(set(i7[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section734[key] = i7[key] + i34[key]


sections.append(section734)


section735 = {}
for key in i7.keys():
	if key == "trade":
		section735[key] = list(set(i7[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section735[key] = i7[key] + i35[key]


sections.append(section735)


section736 = {}
for key in i7.keys():
	if key == "trade":
		section736[key] = list(set(i7[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section736[key] = i7[key] + i36[key]


sections.append(section736)


section737 = {}
for key in i7.keys():
	if key == "trade":
		section737[key] = list(set(i7[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section737[key] = i7[key] + i37[key]


sections.append(section737)


section738 = {}
for key in i7.keys():
	if key == "trade":
		section738[key] = list(set(i7[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section738[key] = i7[key] + i38[key]


sections.append(section738)


section739 = {}
for key in i7.keys():
	if key == "trade":
		section739[key] = list(set(i7[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section739[key] = i7[key] + i39[key]


sections.append(section739)


section740 = {}
for key in i7.keys():
	if key == "trade":
		section740[key] = list(set(i7[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section740[key] = i7[key] + i40[key]


sections.append(section740)


section741 = {}
for key in i7.keys():
	if key == "trade":
		section741[key] = list(set(i7[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section741[key] = i7[key] + i41[key]


sections.append(section741)


section742 = {}
for key in i7.keys():
	if key == "trade":
		section742[key] = list(set(i7[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section742[key] = i7[key] + i42[key]


sections.append(section742)


section743 = {}
for key in i7.keys():
	if key == "trade":
		section743[key] = list(set(i7[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section743[key] = i7[key] + i43[key]


sections.append(section743)


section744 = {}
for key in i7.keys():
	if key == "trade":
		section744[key] = list(set(i7[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section744[key] = i7[key] + i44[key]


sections.append(section744)


section745 = {}
for key in i7.keys():
	if key == "trade":
		section745[key] = list(set(i7[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section745[key] = i7[key] + i45[key]


sections.append(section745)


section746 = {}
for key in i7.keys():
	if key == "trade":
		section746[key] = list(set(i7[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section746[key] = i7[key] + i46[key]


sections.append(section746)


section747 = {}
for key in i7.keys():
	if key == "trade":
		section747[key] = list(set(i7[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section747[key] = i7[key] + i47[key]


sections.append(section747)


section748 = {}
for key in i7.keys():
	if key == "trade":
		section748[key] = list(set(i7[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section748[key] = i7[key] + i48[key]


sections.append(section748)


section749 = {}
for key in i7.keys():
	if key == "trade":
		section749[key] = list(set(i7[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section749[key] = i7[key] + i49[key]


sections.append(section749)


section750 = {}
for key in i7.keys():
	if key == "trade":
		section750[key] = list(set(i7[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section750[key] = i7[key] + i50[key]


sections.append(section750)


section751 = {}
for key in i7.keys():
	if key == "trade":
		section751[key] = list(set(i7[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section751[key] = i7[key] + i51[key]


sections.append(section751)


section752 = {}
for key in i7.keys():
	if key == "trade":
		section752[key] = list(set(i7[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section752[key] = i7[key] + i52[key]


sections.append(section752)


section753 = {}
for key in i7.keys():
	if key == "trade":
		section753[key] = list(set(i7[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section753[key] = i7[key] + i53[key]


sections.append(section753)


section754 = {}
for key in i7.keys():
	if key == "trade":
		section754[key] = list(set(i7[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section754[key] = i7[key] + i54[key]


sections.append(section754)


section810 = {}
for key in i8.keys():
	if key == "trade":
		section810[key] = list(set(i8[key] + i10[key]))
	if key == "intersection":
		pass
	else:
		section810[key] = i8[key] + i10[key]


sections.append(section810)


section811 = {}
for key in i8.keys():
	if key == "trade":
		section811[key] = list(set(i8[key] + i11[key]))
	if key == "intersection":
		pass
	else:
		section811[key] = i8[key] + i11[key]


sections.append(section811)


section812 = {}
for key in i8.keys():
	if key == "trade":
		section812[key] = list(set(i8[key] + i12[key]))
	if key == "intersection":
		pass
	else:
		section812[key] = i8[key] + i12[key]


sections.append(section812)


section813 = {}
for key in i8.keys():
	if key == "trade":
		section813[key] = list(set(i8[key] + i13[key]))
	if key == "intersection":
		pass
	else:
		section813[key] = i8[key] + i13[key]


sections.append(section813)


section814 = {}
for key in i8.keys():
	if key == "trade":
		section814[key] = list(set(i8[key] + i14[key]))
	if key == "intersection":
		pass
	else:
		section814[key] = i8[key] + i14[key]


sections.append(section814)


section815 = {}
for key in i8.keys():
	if key == "trade":
		section815[key] = list(set(i8[key] + i15[key]))
	if key == "intersection":
		pass
	else:
		section815[key] = i8[key] + i15[key]


sections.append(section815)


section816 = {}
for key in i8.keys():
	if key == "trade":
		section816[key] = list(set(i8[key] + i16[key]))
	if key == "intersection":
		pass
	else:
		section816[key] = i8[key] + i16[key]


sections.append(section816)


section817 = {}
for key in i8.keys():
	if key == "trade":
		section817[key] = list(set(i8[key] + i17[key]))
	if key == "intersection":
		pass
	else:
		section817[key] = i8[key] + i17[key]


sections.append(section817)


section819 = {}
for key in i8.keys():
	if key == "trade":
		section819[key] = list(set(i8[key] + i19[key]))
	if key == "intersection":
		pass
	else:
		section819[key] = i8[key] + i19[key]


sections.append(section819)


section820 = {}
for key in i8.keys():
	if key == "trade":
		section820[key] = list(set(i8[key] + i20[key]))
	if key == "intersection":
		pass
	else:
		section820[key] = i8[key] + i20[key]


sections.append(section820)


section821 = {}
for key in i8.keys():
	if key == "trade":
		section821[key] = list(set(i8[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section821[key] = i8[key] + i21[key]


sections.append(section821)


section822 = {}
for key in i8.keys():
	if key == "trade":
		section822[key] = list(set(i8[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section822[key] = i8[key] + i22[key]


sections.append(section822)


section823 = {}
for key in i8.keys():
	if key == "trade":
		section823[key] = list(set(i8[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section823[key] = i8[key] + i23[key]


sections.append(section823)


section824 = {}
for key in i8.keys():
	if key == "trade":
		section824[key] = list(set(i8[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section824[key] = i8[key] + i24[key]


sections.append(section824)


section825 = {}
for key in i8.keys():
	if key == "trade":
		section825[key] = list(set(i8[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section825[key] = i8[key] + i25[key]


sections.append(section825)


section826 = {}
for key in i8.keys():
	if key == "trade":
		section826[key] = list(set(i8[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section826[key] = i8[key] + i26[key]


sections.append(section826)


section827 = {}
for key in i8.keys():
	if key == "trade":
		section827[key] = list(set(i8[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section827[key] = i8[key] + i27[key]


sections.append(section827)


section828 = {}
for key in i8.keys():
	if key == "trade":
		section828[key] = list(set(i8[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section828[key] = i8[key] + i28[key]


sections.append(section828)


section829 = {}
for key in i8.keys():
	if key == "trade":
		section829[key] = list(set(i8[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section829[key] = i8[key] + i29[key]


sections.append(section829)


section830 = {}
for key in i8.keys():
	if key == "trade":
		section830[key] = list(set(i8[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section830[key] = i8[key] + i30[key]


sections.append(section830)


section831 = {}
for key in i8.keys():
	if key == "trade":
		section831[key] = list(set(i8[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section831[key] = i8[key] + i31[key]


sections.append(section831)


section832 = {}
for key in i8.keys():
	if key == "trade":
		section832[key] = list(set(i8[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section832[key] = i8[key] + i32[key]


sections.append(section832)


section833 = {}
for key in i8.keys():
	if key == "trade":
		section833[key] = list(set(i8[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section833[key] = i8[key] + i33[key]


sections.append(section833)


section834 = {}
for key in i8.keys():
	if key == "trade":
		section834[key] = list(set(i8[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section834[key] = i8[key] + i34[key]


sections.append(section834)


section835 = {}
for key in i8.keys():
	if key == "trade":
		section835[key] = list(set(i8[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section835[key] = i8[key] + i35[key]


sections.append(section835)


section836 = {}
for key in i8.keys():
	if key == "trade":
		section836[key] = list(set(i8[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section836[key] = i8[key] + i36[key]


sections.append(section836)


section837 = {}
for key in i8.keys():
	if key == "trade":
		section837[key] = list(set(i8[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section837[key] = i8[key] + i37[key]


sections.append(section837)


section838 = {}
for key in i8.keys():
	if key == "trade":
		section838[key] = list(set(i8[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section838[key] = i8[key] + i38[key]


sections.append(section838)


section839 = {}
for key in i8.keys():
	if key == "trade":
		section839[key] = list(set(i8[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section839[key] = i8[key] + i39[key]


sections.append(section839)


section840 = {}
for key in i8.keys():
	if key == "trade":
		section840[key] = list(set(i8[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section840[key] = i8[key] + i40[key]


sections.append(section840)


section841 = {}
for key in i8.keys():
	if key == "trade":
		section841[key] = list(set(i8[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section841[key] = i8[key] + i41[key]


sections.append(section841)


section842 = {}
for key in i8.keys():
	if key == "trade":
		section842[key] = list(set(i8[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section842[key] = i8[key] + i42[key]


sections.append(section842)


section843 = {}
for key in i8.keys():
	if key == "trade":
		section843[key] = list(set(i8[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section843[key] = i8[key] + i43[key]


sections.append(section843)


section844 = {}
for key in i8.keys():
	if key == "trade":
		section844[key] = list(set(i8[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section844[key] = i8[key] + i44[key]


sections.append(section844)


section845 = {}
for key in i8.keys():
	if key == "trade":
		section845[key] = list(set(i8[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section845[key] = i8[key] + i45[key]


sections.append(section845)


section846 = {}
for key in i8.keys():
	if key == "trade":
		section846[key] = list(set(i8[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section846[key] = i8[key] + i46[key]


sections.append(section846)


section847 = {}
for key in i8.keys():
	if key == "trade":
		section847[key] = list(set(i8[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section847[key] = i8[key] + i47[key]


sections.append(section847)


section848 = {}
for key in i8.keys():
	if key == "trade":
		section848[key] = list(set(i8[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section848[key] = i8[key] + i48[key]


sections.append(section848)


section849 = {}
for key in i8.keys():
	if key == "trade":
		section849[key] = list(set(i8[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section849[key] = i8[key] + i49[key]


sections.append(section849)


section850 = {}
for key in i8.keys():
	if key == "trade":
		section850[key] = list(set(i8[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section850[key] = i8[key] + i50[key]


sections.append(section850)


section851 = {}
for key in i8.keys():
	if key == "trade":
		section851[key] = list(set(i8[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section851[key] = i8[key] + i51[key]


sections.append(section851)


section852 = {}
for key in i8.keys():
	if key == "trade":
		section852[key] = list(set(i8[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section852[key] = i8[key] + i52[key]


sections.append(section852)


section853 = {}
for key in i8.keys():
	if key == "trade":
		section853[key] = list(set(i8[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section853[key] = i8[key] + i53[key]


sections.append(section853)


section854 = {}
for key in i8.keys():
	if key == "trade":
		section854[key] = list(set(i8[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section854[key] = i8[key] + i54[key]


sections.append(section854)


section911 = {}
for key in i9.keys():
	if key == "trade":
		section911[key] = list(set(i9[key] + i11[key]))
	if key == "intersection":
		pass
	else:
		section911[key] = i9[key] + i11[key]


sections.append(section911)


section912 = {}
for key in i9.keys():
	if key == "trade":
		section912[key] = list(set(i9[key] + i12[key]))
	if key == "intersection":
		pass
	else:
		section912[key] = i9[key] + i12[key]


sections.append(section912)


section913 = {}
for key in i9.keys():
	if key == "trade":
		section913[key] = list(set(i9[key] + i13[key]))
	if key == "intersection":
		pass
	else:
		section913[key] = i9[key] + i13[key]


sections.append(section913)


section914 = {}
for key in i9.keys():
	if key == "trade":
		section914[key] = list(set(i9[key] + i14[key]))
	if key == "intersection":
		pass
	else:
		section914[key] = i9[key] + i14[key]


sections.append(section914)


section915 = {}
for key in i9.keys():
	if key == "trade":
		section915[key] = list(set(i9[key] + i15[key]))
	if key == "intersection":
		pass
	else:
		section915[key] = i9[key] + i15[key]


sections.append(section915)


section916 = {}
for key in i9.keys():
	if key == "trade":
		section916[key] = list(set(i9[key] + i16[key]))
	if key == "intersection":
		pass
	else:
		section916[key] = i9[key] + i16[key]


sections.append(section916)


section917 = {}
for key in i9.keys():
	if key == "trade":
		section917[key] = list(set(i9[key] + i17[key]))
	if key == "intersection":
		pass
	else:
		section917[key] = i9[key] + i17[key]


sections.append(section917)


section918 = {}
for key in i9.keys():
	if key == "trade":
		section918[key] = list(set(i9[key] + i18[key]))
	if key == "intersection":
		pass
	else:
		section918[key] = i9[key] + i18[key]


sections.append(section918)


section919 = {}
for key in i9.keys():
	if key == "trade":
		section919[key] = list(set(i9[key] + i19[key]))
	if key == "intersection":
		pass
	else:
		section919[key] = i9[key] + i19[key]


sections.append(section919)


section920 = {}
for key in i9.keys():
	if key == "trade":
		section920[key] = list(set(i9[key] + i20[key]))
	if key == "intersection":
		pass
	else:
		section920[key] = i9[key] + i20[key]


sections.append(section920)


section921 = {}
for key in i9.keys():
	if key == "trade":
		section921[key] = list(set(i9[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section921[key] = i9[key] + i21[key]


sections.append(section921)


section922 = {}
for key in i9.keys():
	if key == "trade":
		section922[key] = list(set(i9[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section922[key] = i9[key] + i22[key]


sections.append(section922)


section923 = {}
for key in i9.keys():
	if key == "trade":
		section923[key] = list(set(i9[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section923[key] = i9[key] + i23[key]


sections.append(section923)


section924 = {}
for key in i9.keys():
	if key == "trade":
		section924[key] = list(set(i9[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section924[key] = i9[key] + i24[key]


sections.append(section924)


section925 = {}
for key in i9.keys():
	if key == "trade":
		section925[key] = list(set(i9[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section925[key] = i9[key] + i25[key]


sections.append(section925)


section926 = {}
for key in i9.keys():
	if key == "trade":
		section926[key] = list(set(i9[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section926[key] = i9[key] + i26[key]


sections.append(section926)


section927 = {}
for key in i9.keys():
	if key == "trade":
		section927[key] = list(set(i9[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section927[key] = i9[key] + i27[key]


sections.append(section927)


section928 = {}
for key in i9.keys():
	if key == "trade":
		section928[key] = list(set(i9[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section928[key] = i9[key] + i28[key]


sections.append(section928)


section929 = {}
for key in i9.keys():
	if key == "trade":
		section929[key] = list(set(i9[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section929[key] = i9[key] + i29[key]


sections.append(section929)


section930 = {}
for key in i9.keys():
	if key == "trade":
		section930[key] = list(set(i9[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section930[key] = i9[key] + i30[key]


sections.append(section930)


section931 = {}
for key in i9.keys():
	if key == "trade":
		section931[key] = list(set(i9[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section931[key] = i9[key] + i31[key]


sections.append(section931)


section932 = {}
for key in i9.keys():
	if key == "trade":
		section932[key] = list(set(i9[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section932[key] = i9[key] + i32[key]


sections.append(section932)


section933 = {}
for key in i9.keys():
	if key == "trade":
		section933[key] = list(set(i9[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section933[key] = i9[key] + i33[key]


sections.append(section933)


section934 = {}
for key in i9.keys():
	if key == "trade":
		section934[key] = list(set(i9[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section934[key] = i9[key] + i34[key]


sections.append(section934)


section935 = {}
for key in i9.keys():
	if key == "trade":
		section935[key] = list(set(i9[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section935[key] = i9[key] + i35[key]


sections.append(section935)


section936 = {}
for key in i9.keys():
	if key == "trade":
		section936[key] = list(set(i9[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section936[key] = i9[key] + i36[key]


sections.append(section936)


section937 = {}
for key in i9.keys():
	if key == "trade":
		section937[key] = list(set(i9[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section937[key] = i9[key] + i37[key]


sections.append(section937)


section938 = {}
for key in i9.keys():
	if key == "trade":
		section938[key] = list(set(i9[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section938[key] = i9[key] + i38[key]


sections.append(section938)


section939 = {}
for key in i9.keys():
	if key == "trade":
		section939[key] = list(set(i9[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section939[key] = i9[key] + i39[key]


sections.append(section939)


section940 = {}
for key in i9.keys():
	if key == "trade":
		section940[key] = list(set(i9[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section940[key] = i9[key] + i40[key]


sections.append(section940)


section941 = {}
for key in i9.keys():
	if key == "trade":
		section941[key] = list(set(i9[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section941[key] = i9[key] + i41[key]


sections.append(section941)


section942 = {}
for key in i9.keys():
	if key == "trade":
		section942[key] = list(set(i9[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section942[key] = i9[key] + i42[key]


sections.append(section942)


section943 = {}
for key in i9.keys():
	if key == "trade":
		section943[key] = list(set(i9[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section943[key] = i9[key] + i43[key]


sections.append(section943)


section944 = {}
for key in i9.keys():
	if key == "trade":
		section944[key] = list(set(i9[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section944[key] = i9[key] + i44[key]


sections.append(section944)


section945 = {}
for key in i9.keys():
	if key == "trade":
		section945[key] = list(set(i9[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section945[key] = i9[key] + i45[key]


sections.append(section945)


section946 = {}
for key in i9.keys():
	if key == "trade":
		section946[key] = list(set(i9[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section946[key] = i9[key] + i46[key]


sections.append(section946)


section947 = {}
for key in i9.keys():
	if key == "trade":
		section947[key] = list(set(i9[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section947[key] = i9[key] + i47[key]


sections.append(section947)


section948 = {}
for key in i9.keys():
	if key == "trade":
		section948[key] = list(set(i9[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section948[key] = i9[key] + i48[key]


sections.append(section948)


section949 = {}
for key in i9.keys():
	if key == "trade":
		section949[key] = list(set(i9[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section949[key] = i9[key] + i49[key]


sections.append(section949)


section950 = {}
for key in i9.keys():
	if key == "trade":
		section950[key] = list(set(i9[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section950[key] = i9[key] + i50[key]


sections.append(section950)


section951 = {}
for key in i9.keys():
	if key == "trade":
		section951[key] = list(set(i9[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section951[key] = i9[key] + i51[key]


sections.append(section951)


section952 = {}
for key in i9.keys():
	if key == "trade":
		section952[key] = list(set(i9[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section952[key] = i9[key] + i52[key]


sections.append(section952)


section953 = {}
for key in i9.keys():
	if key == "trade":
		section953[key] = list(set(i9[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section953[key] = i9[key] + i53[key]


sections.append(section953)


section954 = {}
for key in i9.keys():
	if key == "trade":
		section954[key] = list(set(i9[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section954[key] = i9[key] + i54[key]


sections.append(section954)


section1012 = {}
for key in i10.keys():
	if key == "trade":
		section1012[key] = list(set(i10[key] + i12[key]))
	if key == "intersection":
		pass
	else:
		section1012[key] = i10[key] + i12[key]


sections.append(section1012)


section1013 = {}
for key in i10.keys():
	if key == "trade":
		section1013[key] = list(set(i10[key] + i13[key]))
	if key == "intersection":
		pass
	else:
		section1013[key] = i10[key] + i13[key]


sections.append(section1013)


section1014 = {}
for key in i10.keys():
	if key == "trade":
		section1014[key] = list(set(i10[key] + i14[key]))
	if key == "intersection":
		pass
	else:
		section1014[key] = i10[key] + i14[key]


sections.append(section1014)


section1015 = {}
for key in i10.keys():
	if key == "trade":
		section1015[key] = list(set(i10[key] + i15[key]))
	if key == "intersection":
		pass
	else:
		section1015[key] = i10[key] + i15[key]


sections.append(section1015)


section1016 = {}
for key in i10.keys():
	if key == "trade":
		section1016[key] = list(set(i10[key] + i16[key]))
	if key == "intersection":
		pass
	else:
		section1016[key] = i10[key] + i16[key]


sections.append(section1016)


section1017 = {}
for key in i10.keys():
	if key == "trade":
		section1017[key] = list(set(i10[key] + i17[key]))
	if key == "intersection":
		pass
	else:
		section1017[key] = i10[key] + i17[key]


sections.append(section1017)


section1018 = {}
for key in i10.keys():
	if key == "trade":
		section1018[key] = list(set(i10[key] + i18[key]))
	if key == "intersection":
		pass
	else:
		section1018[key] = i10[key] + i18[key]


sections.append(section1018)


section1019 = {}
for key in i10.keys():
	if key == "trade":
		section1019[key] = list(set(i10[key] + i19[key]))
	if key == "intersection":
		pass
	else:
		section1019[key] = i10[key] + i19[key]


sections.append(section1019)


section1021 = {}
for key in i10.keys():
	if key == "trade":
		section1021[key] = list(set(i10[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section1021[key] = i10[key] + i21[key]


sections.append(section1021)


section1022 = {}
for key in i10.keys():
	if key == "trade":
		section1022[key] = list(set(i10[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section1022[key] = i10[key] + i22[key]


sections.append(section1022)


section1023 = {}
for key in i10.keys():
	if key == "trade":
		section1023[key] = list(set(i10[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section1023[key] = i10[key] + i23[key]


sections.append(section1023)


section1024 = {}
for key in i10.keys():
	if key == "trade":
		section1024[key] = list(set(i10[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section1024[key] = i10[key] + i24[key]


sections.append(section1024)


section1025 = {}
for key in i10.keys():
	if key == "trade":
		section1025[key] = list(set(i10[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section1025[key] = i10[key] + i25[key]


sections.append(section1025)


section1026 = {}
for key in i10.keys():
	if key == "trade":
		section1026[key] = list(set(i10[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section1026[key] = i10[key] + i26[key]


sections.append(section1026)


section1027 = {}
for key in i10.keys():
	if key == "trade":
		section1027[key] = list(set(i10[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section1027[key] = i10[key] + i27[key]


sections.append(section1027)


section1028 = {}
for key in i10.keys():
	if key == "trade":
		section1028[key] = list(set(i10[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section1028[key] = i10[key] + i28[key]


sections.append(section1028)


section1029 = {}
for key in i10.keys():
	if key == "trade":
		section1029[key] = list(set(i10[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section1029[key] = i10[key] + i29[key]


sections.append(section1029)


section1030 = {}
for key in i10.keys():
	if key == "trade":
		section1030[key] = list(set(i10[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section1030[key] = i10[key] + i30[key]


sections.append(section1030)


section1031 = {}
for key in i10.keys():
	if key == "trade":
		section1031[key] = list(set(i10[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section1031[key] = i10[key] + i31[key]


sections.append(section1031)


section1032 = {}
for key in i10.keys():
	if key == "trade":
		section1032[key] = list(set(i10[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section1032[key] = i10[key] + i32[key]


sections.append(section1032)


section1033 = {}
for key in i10.keys():
	if key == "trade":
		section1033[key] = list(set(i10[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section1033[key] = i10[key] + i33[key]


sections.append(section1033)


section1034 = {}
for key in i10.keys():
	if key == "trade":
		section1034[key] = list(set(i10[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section1034[key] = i10[key] + i34[key]


sections.append(section1034)


section1035 = {}
for key in i10.keys():
	if key == "trade":
		section1035[key] = list(set(i10[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section1035[key] = i10[key] + i35[key]


sections.append(section1035)


section1036 = {}
for key in i10.keys():
	if key == "trade":
		section1036[key] = list(set(i10[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section1036[key] = i10[key] + i36[key]


sections.append(section1036)


section1037 = {}
for key in i10.keys():
	if key == "trade":
		section1037[key] = list(set(i10[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section1037[key] = i10[key] + i37[key]


sections.append(section1037)


section1038 = {}
for key in i10.keys():
	if key == "trade":
		section1038[key] = list(set(i10[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section1038[key] = i10[key] + i38[key]


sections.append(section1038)


section1039 = {}
for key in i10.keys():
	if key == "trade":
		section1039[key] = list(set(i10[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section1039[key] = i10[key] + i39[key]


sections.append(section1039)


section1040 = {}
for key in i10.keys():
	if key == "trade":
		section1040[key] = list(set(i10[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section1040[key] = i10[key] + i40[key]


sections.append(section1040)


section1041 = {}
for key in i10.keys():
	if key == "trade":
		section1041[key] = list(set(i10[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section1041[key] = i10[key] + i41[key]


sections.append(section1041)


section1042 = {}
for key in i10.keys():
	if key == "trade":
		section1042[key] = list(set(i10[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section1042[key] = i10[key] + i42[key]


sections.append(section1042)


section1043 = {}
for key in i10.keys():
	if key == "trade":
		section1043[key] = list(set(i10[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section1043[key] = i10[key] + i43[key]


sections.append(section1043)


section1044 = {}
for key in i10.keys():
	if key == "trade":
		section1044[key] = list(set(i10[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section1044[key] = i10[key] + i44[key]


sections.append(section1044)


section1045 = {}
for key in i10.keys():
	if key == "trade":
		section1045[key] = list(set(i10[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section1045[key] = i10[key] + i45[key]


sections.append(section1045)


section1046 = {}
for key in i10.keys():
	if key == "trade":
		section1046[key] = list(set(i10[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section1046[key] = i10[key] + i46[key]


sections.append(section1046)


section1047 = {}
for key in i10.keys():
	if key == "trade":
		section1047[key] = list(set(i10[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section1047[key] = i10[key] + i47[key]


sections.append(section1047)


section1048 = {}
for key in i10.keys():
	if key == "trade":
		section1048[key] = list(set(i10[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section1048[key] = i10[key] + i48[key]


sections.append(section1048)


section1049 = {}
for key in i10.keys():
	if key == "trade":
		section1049[key] = list(set(i10[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section1049[key] = i10[key] + i49[key]


sections.append(section1049)


section1050 = {}
for key in i10.keys():
	if key == "trade":
		section1050[key] = list(set(i10[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section1050[key] = i10[key] + i50[key]


sections.append(section1050)


section1051 = {}
for key in i10.keys():
	if key == "trade":
		section1051[key] = list(set(i10[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section1051[key] = i10[key] + i51[key]


sections.append(section1051)


section1052 = {}
for key in i10.keys():
	if key == "trade":
		section1052[key] = list(set(i10[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section1052[key] = i10[key] + i52[key]


sections.append(section1052)


section1053 = {}
for key in i10.keys():
	if key == "trade":
		section1053[key] = list(set(i10[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section1053[key] = i10[key] + i53[key]


sections.append(section1053)


section1054 = {}
for key in i10.keys():
	if key == "trade":
		section1054[key] = list(set(i10[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section1054[key] = i10[key] + i54[key]


sections.append(section1054)


section1113 = {}
for key in i11.keys():
	if key == "trade":
		section1113[key] = list(set(i11[key] + i13[key]))
	if key == "intersection":
		pass
	else:
		section1113[key] = i11[key] + i13[key]


sections.append(section1113)


section1114 = {}
for key in i11.keys():
	if key == "trade":
		section1114[key] = list(set(i11[key] + i14[key]))
	if key == "intersection":
		pass
	else:
		section1114[key] = i11[key] + i14[key]


sections.append(section1114)


section1115 = {}
for key in i11.keys():
	if key == "trade":
		section1115[key] = list(set(i11[key] + i15[key]))
	if key == "intersection":
		pass
	else:
		section1115[key] = i11[key] + i15[key]


sections.append(section1115)


section1116 = {}
for key in i11.keys():
	if key == "trade":
		section1116[key] = list(set(i11[key] + i16[key]))
	if key == "intersection":
		pass
	else:
		section1116[key] = i11[key] + i16[key]


sections.append(section1116)


section1117 = {}
for key in i11.keys():
	if key == "trade":
		section1117[key] = list(set(i11[key] + i17[key]))
	if key == "intersection":
		pass
	else:
		section1117[key] = i11[key] + i17[key]


sections.append(section1117)


section1118 = {}
for key in i11.keys():
	if key == "trade":
		section1118[key] = list(set(i11[key] + i18[key]))
	if key == "intersection":
		pass
	else:
		section1118[key] = i11[key] + i18[key]


sections.append(section1118)


section1119 = {}
for key in i11.keys():
	if key == "trade":
		section1119[key] = list(set(i11[key] + i19[key]))
	if key == "intersection":
		pass
	else:
		section1119[key] = i11[key] + i19[key]


sections.append(section1119)


section1120 = {}
for key in i11.keys():
	if key == "trade":
		section1120[key] = list(set(i11[key] + i20[key]))
	if key == "intersection":
		pass
	else:
		section1120[key] = i11[key] + i20[key]


sections.append(section1120)


section1121 = {}
for key in i11.keys():
	if key == "trade":
		section1121[key] = list(set(i11[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section1121[key] = i11[key] + i21[key]


sections.append(section1121)


section1122 = {}
for key in i11.keys():
	if key == "trade":
		section1122[key] = list(set(i11[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section1122[key] = i11[key] + i22[key]


sections.append(section1122)


section1123 = {}
for key in i11.keys():
	if key == "trade":
		section1123[key] = list(set(i11[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section1123[key] = i11[key] + i23[key]


sections.append(section1123)


section1124 = {}
for key in i11.keys():
	if key == "trade":
		section1124[key] = list(set(i11[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section1124[key] = i11[key] + i24[key]


sections.append(section1124)


section1125 = {}
for key in i11.keys():
	if key == "trade":
		section1125[key] = list(set(i11[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section1125[key] = i11[key] + i25[key]


sections.append(section1125)


section1126 = {}
for key in i11.keys():
	if key == "trade":
		section1126[key] = list(set(i11[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section1126[key] = i11[key] + i26[key]


sections.append(section1126)


section1127 = {}
for key in i11.keys():
	if key == "trade":
		section1127[key] = list(set(i11[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section1127[key] = i11[key] + i27[key]


sections.append(section1127)


section1128 = {}
for key in i11.keys():
	if key == "trade":
		section1128[key] = list(set(i11[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section1128[key] = i11[key] + i28[key]


sections.append(section1128)


section1129 = {}
for key in i11.keys():
	if key == "trade":
		section1129[key] = list(set(i11[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section1129[key] = i11[key] + i29[key]


sections.append(section1129)


section1130 = {}
for key in i11.keys():
	if key == "trade":
		section1130[key] = list(set(i11[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section1130[key] = i11[key] + i30[key]


sections.append(section1130)


section1131 = {}
for key in i11.keys():
	if key == "trade":
		section1131[key] = list(set(i11[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section1131[key] = i11[key] + i31[key]


sections.append(section1131)


section1132 = {}
for key in i11.keys():
	if key == "trade":
		section1132[key] = list(set(i11[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section1132[key] = i11[key] + i32[key]


sections.append(section1132)


section1133 = {}
for key in i11.keys():
	if key == "trade":
		section1133[key] = list(set(i11[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section1133[key] = i11[key] + i33[key]


sections.append(section1133)


section1134 = {}
for key in i11.keys():
	if key == "trade":
		section1134[key] = list(set(i11[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section1134[key] = i11[key] + i34[key]


sections.append(section1134)


section1135 = {}
for key in i11.keys():
	if key == "trade":
		section1135[key] = list(set(i11[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section1135[key] = i11[key] + i35[key]


sections.append(section1135)


section1136 = {}
for key in i11.keys():
	if key == "trade":
		section1136[key] = list(set(i11[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section1136[key] = i11[key] + i36[key]


sections.append(section1136)


section1137 = {}
for key in i11.keys():
	if key == "trade":
		section1137[key] = list(set(i11[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section1137[key] = i11[key] + i37[key]


sections.append(section1137)


section1138 = {}
for key in i11.keys():
	if key == "trade":
		section1138[key] = list(set(i11[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section1138[key] = i11[key] + i38[key]


sections.append(section1138)


section1139 = {}
for key in i11.keys():
	if key == "trade":
		section1139[key] = list(set(i11[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section1139[key] = i11[key] + i39[key]


sections.append(section1139)


section1140 = {}
for key in i11.keys():
	if key == "trade":
		section1140[key] = list(set(i11[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section1140[key] = i11[key] + i40[key]


sections.append(section1140)


section1141 = {}
for key in i11.keys():
	if key == "trade":
		section1141[key] = list(set(i11[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section1141[key] = i11[key] + i41[key]


sections.append(section1141)


section1142 = {}
for key in i11.keys():
	if key == "trade":
		section1142[key] = list(set(i11[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section1142[key] = i11[key] + i42[key]


sections.append(section1142)


section1143 = {}
for key in i11.keys():
	if key == "trade":
		section1143[key] = list(set(i11[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section1143[key] = i11[key] + i43[key]


sections.append(section1143)


section1144 = {}
for key in i11.keys():
	if key == "trade":
		section1144[key] = list(set(i11[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section1144[key] = i11[key] + i44[key]


sections.append(section1144)


section1145 = {}
for key in i11.keys():
	if key == "trade":
		section1145[key] = list(set(i11[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section1145[key] = i11[key] + i45[key]


sections.append(section1145)


section1146 = {}
for key in i11.keys():
	if key == "trade":
		section1146[key] = list(set(i11[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section1146[key] = i11[key] + i46[key]


sections.append(section1146)


section1147 = {}
for key in i11.keys():
	if key == "trade":
		section1147[key] = list(set(i11[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section1147[key] = i11[key] + i47[key]


sections.append(section1147)


section1148 = {}
for key in i11.keys():
	if key == "trade":
		section1148[key] = list(set(i11[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section1148[key] = i11[key] + i48[key]


sections.append(section1148)


section1149 = {}
for key in i11.keys():
	if key == "trade":
		section1149[key] = list(set(i11[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section1149[key] = i11[key] + i49[key]


sections.append(section1149)


section1150 = {}
for key in i11.keys():
	if key == "trade":
		section1150[key] = list(set(i11[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section1150[key] = i11[key] + i50[key]


sections.append(section1150)


section1151 = {}
for key in i11.keys():
	if key == "trade":
		section1151[key] = list(set(i11[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section1151[key] = i11[key] + i51[key]


sections.append(section1151)


section1152 = {}
for key in i11.keys():
	if key == "trade":
		section1152[key] = list(set(i11[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section1152[key] = i11[key] + i52[key]


sections.append(section1152)


section1153 = {}
for key in i11.keys():
	if key == "trade":
		section1153[key] = list(set(i11[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section1153[key] = i11[key] + i53[key]


sections.append(section1153)


section1154 = {}
for key in i11.keys():
	if key == "trade":
		section1154[key] = list(set(i11[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section1154[key] = i11[key] + i54[key]


sections.append(section1154)


section1214 = {}
for key in i12.keys():
	if key == "trade":
		section1214[key] = list(set(i12[key] + i14[key]))
	if key == "intersection":
		pass
	else:
		section1214[key] = i12[key] + i14[key]


sections.append(section1214)


section1215 = {}
for key in i12.keys():
	if key == "trade":
		section1215[key] = list(set(i12[key] + i15[key]))
	if key == "intersection":
		pass
	else:
		section1215[key] = i12[key] + i15[key]


sections.append(section1215)


section1216 = {}
for key in i12.keys():
	if key == "trade":
		section1216[key] = list(set(i12[key] + i16[key]))
	if key == "intersection":
		pass
	else:
		section1216[key] = i12[key] + i16[key]


sections.append(section1216)


section1217 = {}
for key in i12.keys():
	if key == "trade":
		section1217[key] = list(set(i12[key] + i17[key]))
	if key == "intersection":
		pass
	else:
		section1217[key] = i12[key] + i17[key]


sections.append(section1217)


section1218 = {}
for key in i12.keys():
	if key == "trade":
		section1218[key] = list(set(i12[key] + i18[key]))
	if key == "intersection":
		pass
	else:
		section1218[key] = i12[key] + i18[key]


sections.append(section1218)


section1219 = {}
for key in i12.keys():
	if key == "trade":
		section1219[key] = list(set(i12[key] + i19[key]))
	if key == "intersection":
		pass
	else:
		section1219[key] = i12[key] + i19[key]


sections.append(section1219)


section1220 = {}
for key in i12.keys():
	if key == "trade":
		section1220[key] = list(set(i12[key] + i20[key]))
	if key == "intersection":
		pass
	else:
		section1220[key] = i12[key] + i20[key]


sections.append(section1220)


section1221 = {}
for key in i12.keys():
	if key == "trade":
		section1221[key] = list(set(i12[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section1221[key] = i12[key] + i21[key]


sections.append(section1221)


section1223 = {}
for key in i12.keys():
	if key == "trade":
		section1223[key] = list(set(i12[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section1223[key] = i12[key] + i23[key]


sections.append(section1223)


section1224 = {}
for key in i12.keys():
	if key == "trade":
		section1224[key] = list(set(i12[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section1224[key] = i12[key] + i24[key]


sections.append(section1224)


section1225 = {}
for key in i12.keys():
	if key == "trade":
		section1225[key] = list(set(i12[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section1225[key] = i12[key] + i25[key]


sections.append(section1225)


section1226 = {}
for key in i12.keys():
	if key == "trade":
		section1226[key] = list(set(i12[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section1226[key] = i12[key] + i26[key]


sections.append(section1226)


section1227 = {}
for key in i12.keys():
	if key == "trade":
		section1227[key] = list(set(i12[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section1227[key] = i12[key] + i27[key]


sections.append(section1227)


section1228 = {}
for key in i12.keys():
	if key == "trade":
		section1228[key] = list(set(i12[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section1228[key] = i12[key] + i28[key]


sections.append(section1228)


section1229 = {}
for key in i12.keys():
	if key == "trade":
		section1229[key] = list(set(i12[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section1229[key] = i12[key] + i29[key]


sections.append(section1229)


section1230 = {}
for key in i12.keys():
	if key == "trade":
		section1230[key] = list(set(i12[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section1230[key] = i12[key] + i30[key]


sections.append(section1230)


section1231 = {}
for key in i12.keys():
	if key == "trade":
		section1231[key] = list(set(i12[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section1231[key] = i12[key] + i31[key]


sections.append(section1231)


section1232 = {}
for key in i12.keys():
	if key == "trade":
		section1232[key] = list(set(i12[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section1232[key] = i12[key] + i32[key]


sections.append(section1232)


section1233 = {}
for key in i12.keys():
	if key == "trade":
		section1233[key] = list(set(i12[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section1233[key] = i12[key] + i33[key]


sections.append(section1233)


section1234 = {}
for key in i12.keys():
	if key == "trade":
		section1234[key] = list(set(i12[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section1234[key] = i12[key] + i34[key]


sections.append(section1234)


section1235 = {}
for key in i12.keys():
	if key == "trade":
		section1235[key] = list(set(i12[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section1235[key] = i12[key] + i35[key]


sections.append(section1235)


section1236 = {}
for key in i12.keys():
	if key == "trade":
		section1236[key] = list(set(i12[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section1236[key] = i12[key] + i36[key]


sections.append(section1236)


section1237 = {}
for key in i12.keys():
	if key == "trade":
		section1237[key] = list(set(i12[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section1237[key] = i12[key] + i37[key]


sections.append(section1237)


section1238 = {}
for key in i12.keys():
	if key == "trade":
		section1238[key] = list(set(i12[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section1238[key] = i12[key] + i38[key]


sections.append(section1238)


section1239 = {}
for key in i12.keys():
	if key == "trade":
		section1239[key] = list(set(i12[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section1239[key] = i12[key] + i39[key]


sections.append(section1239)


section1240 = {}
for key in i12.keys():
	if key == "trade":
		section1240[key] = list(set(i12[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section1240[key] = i12[key] + i40[key]


sections.append(section1240)


section1241 = {}
for key in i12.keys():
	if key == "trade":
		section1241[key] = list(set(i12[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section1241[key] = i12[key] + i41[key]


sections.append(section1241)


section1242 = {}
for key in i12.keys():
	if key == "trade":
		section1242[key] = list(set(i12[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section1242[key] = i12[key] + i42[key]


sections.append(section1242)


section1243 = {}
for key in i12.keys():
	if key == "trade":
		section1243[key] = list(set(i12[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section1243[key] = i12[key] + i43[key]


sections.append(section1243)


section1244 = {}
for key in i12.keys():
	if key == "trade":
		section1244[key] = list(set(i12[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section1244[key] = i12[key] + i44[key]


sections.append(section1244)


section1245 = {}
for key in i12.keys():
	if key == "trade":
		section1245[key] = list(set(i12[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section1245[key] = i12[key] + i45[key]


sections.append(section1245)


section1246 = {}
for key in i12.keys():
	if key == "trade":
		section1246[key] = list(set(i12[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section1246[key] = i12[key] + i46[key]


sections.append(section1246)


section1247 = {}
for key in i12.keys():
	if key == "trade":
		section1247[key] = list(set(i12[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section1247[key] = i12[key] + i47[key]


sections.append(section1247)


section1248 = {}
for key in i12.keys():
	if key == "trade":
		section1248[key] = list(set(i12[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section1248[key] = i12[key] + i48[key]


sections.append(section1248)


section1249 = {}
for key in i12.keys():
	if key == "trade":
		section1249[key] = list(set(i12[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section1249[key] = i12[key] + i49[key]


sections.append(section1249)


section1250 = {}
for key in i12.keys():
	if key == "trade":
		section1250[key] = list(set(i12[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section1250[key] = i12[key] + i50[key]


sections.append(section1250)


section1251 = {}
for key in i12.keys():
	if key == "trade":
		section1251[key] = list(set(i12[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section1251[key] = i12[key] + i51[key]


sections.append(section1251)


section1252 = {}
for key in i12.keys():
	if key == "trade":
		section1252[key] = list(set(i12[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section1252[key] = i12[key] + i52[key]


sections.append(section1252)


section1253 = {}
for key in i12.keys():
	if key == "trade":
		section1253[key] = list(set(i12[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section1253[key] = i12[key] + i53[key]


sections.append(section1253)


section1254 = {}
for key in i12.keys():
	if key == "trade":
		section1254[key] = list(set(i12[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section1254[key] = i12[key] + i54[key]


sections.append(section1254)


section1315 = {}
for key in i13.keys():
	if key == "trade":
		section1315[key] = list(set(i13[key] + i15[key]))
	if key == "intersection":
		pass
	else:
		section1315[key] = i13[key] + i15[key]


sections.append(section1315)


section1316 = {}
for key in i13.keys():
	if key == "trade":
		section1316[key] = list(set(i13[key] + i16[key]))
	if key == "intersection":
		pass
	else:
		section1316[key] = i13[key] + i16[key]


sections.append(section1316)


section1317 = {}
for key in i13.keys():
	if key == "trade":
		section1317[key] = list(set(i13[key] + i17[key]))
	if key == "intersection":
		pass
	else:
		section1317[key] = i13[key] + i17[key]


sections.append(section1317)


section1318 = {}
for key in i13.keys():
	if key == "trade":
		section1318[key] = list(set(i13[key] + i18[key]))
	if key == "intersection":
		pass
	else:
		section1318[key] = i13[key] + i18[key]


sections.append(section1318)


section1319 = {}
for key in i13.keys():
	if key == "trade":
		section1319[key] = list(set(i13[key] + i19[key]))
	if key == "intersection":
		pass
	else:
		section1319[key] = i13[key] + i19[key]


sections.append(section1319)


section1320 = {}
for key in i13.keys():
	if key == "trade":
		section1320[key] = list(set(i13[key] + i20[key]))
	if key == "intersection":
		pass
	else:
		section1320[key] = i13[key] + i20[key]


sections.append(section1320)


section1321 = {}
for key in i13.keys():
	if key == "trade":
		section1321[key] = list(set(i13[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section1321[key] = i13[key] + i21[key]


sections.append(section1321)


section1322 = {}
for key in i13.keys():
	if key == "trade":
		section1322[key] = list(set(i13[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section1322[key] = i13[key] + i22[key]


sections.append(section1322)


section1323 = {}
for key in i13.keys():
	if key == "trade":
		section1323[key] = list(set(i13[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section1323[key] = i13[key] + i23[key]


sections.append(section1323)


section1324 = {}
for key in i13.keys():
	if key == "trade":
		section1324[key] = list(set(i13[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section1324[key] = i13[key] + i24[key]


sections.append(section1324)


section1325 = {}
for key in i13.keys():
	if key == "trade":
		section1325[key] = list(set(i13[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section1325[key] = i13[key] + i25[key]


sections.append(section1325)


section1326 = {}
for key in i13.keys():
	if key == "trade":
		section1326[key] = list(set(i13[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section1326[key] = i13[key] + i26[key]


sections.append(section1326)


section1327 = {}
for key in i13.keys():
	if key == "trade":
		section1327[key] = list(set(i13[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section1327[key] = i13[key] + i27[key]


sections.append(section1327)


section1328 = {}
for key in i13.keys():
	if key == "trade":
		section1328[key] = list(set(i13[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section1328[key] = i13[key] + i28[key]


sections.append(section1328)


section1329 = {}
for key in i13.keys():
	if key == "trade":
		section1329[key] = list(set(i13[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section1329[key] = i13[key] + i29[key]


sections.append(section1329)


section1330 = {}
for key in i13.keys():
	if key == "trade":
		section1330[key] = list(set(i13[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section1330[key] = i13[key] + i30[key]


sections.append(section1330)


section1331 = {}
for key in i13.keys():
	if key == "trade":
		section1331[key] = list(set(i13[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section1331[key] = i13[key] + i31[key]


sections.append(section1331)


section1332 = {}
for key in i13.keys():
	if key == "trade":
		section1332[key] = list(set(i13[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section1332[key] = i13[key] + i32[key]


sections.append(section1332)


section1333 = {}
for key in i13.keys():
	if key == "trade":
		section1333[key] = list(set(i13[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section1333[key] = i13[key] + i33[key]


sections.append(section1333)


section1334 = {}
for key in i13.keys():
	if key == "trade":
		section1334[key] = list(set(i13[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section1334[key] = i13[key] + i34[key]


sections.append(section1334)


section1335 = {}
for key in i13.keys():
	if key == "trade":
		section1335[key] = list(set(i13[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section1335[key] = i13[key] + i35[key]


sections.append(section1335)


section1336 = {}
for key in i13.keys():
	if key == "trade":
		section1336[key] = list(set(i13[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section1336[key] = i13[key] + i36[key]


sections.append(section1336)


section1337 = {}
for key in i13.keys():
	if key == "trade":
		section1337[key] = list(set(i13[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section1337[key] = i13[key] + i37[key]


sections.append(section1337)


section1338 = {}
for key in i13.keys():
	if key == "trade":
		section1338[key] = list(set(i13[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section1338[key] = i13[key] + i38[key]


sections.append(section1338)


section1339 = {}
for key in i13.keys():
	if key == "trade":
		section1339[key] = list(set(i13[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section1339[key] = i13[key] + i39[key]


sections.append(section1339)


section1340 = {}
for key in i13.keys():
	if key == "trade":
		section1340[key] = list(set(i13[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section1340[key] = i13[key] + i40[key]


sections.append(section1340)


section1341 = {}
for key in i13.keys():
	if key == "trade":
		section1341[key] = list(set(i13[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section1341[key] = i13[key] + i41[key]


sections.append(section1341)


section1342 = {}
for key in i13.keys():
	if key == "trade":
		section1342[key] = list(set(i13[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section1342[key] = i13[key] + i42[key]


sections.append(section1342)


section1343 = {}
for key in i13.keys():
	if key == "trade":
		section1343[key] = list(set(i13[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section1343[key] = i13[key] + i43[key]


sections.append(section1343)


section1344 = {}
for key in i13.keys():
	if key == "trade":
		section1344[key] = list(set(i13[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section1344[key] = i13[key] + i44[key]


sections.append(section1344)


section1345 = {}
for key in i13.keys():
	if key == "trade":
		section1345[key] = list(set(i13[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section1345[key] = i13[key] + i45[key]


sections.append(section1345)


section1346 = {}
for key in i13.keys():
	if key == "trade":
		section1346[key] = list(set(i13[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section1346[key] = i13[key] + i46[key]


sections.append(section1346)


section1347 = {}
for key in i13.keys():
	if key == "trade":
		section1347[key] = list(set(i13[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section1347[key] = i13[key] + i47[key]


sections.append(section1347)


section1348 = {}
for key in i13.keys():
	if key == "trade":
		section1348[key] = list(set(i13[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section1348[key] = i13[key] + i48[key]


sections.append(section1348)


section1349 = {}
for key in i13.keys():
	if key == "trade":
		section1349[key] = list(set(i13[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section1349[key] = i13[key] + i49[key]


sections.append(section1349)


section1350 = {}
for key in i13.keys():
	if key == "trade":
		section1350[key] = list(set(i13[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section1350[key] = i13[key] + i50[key]


sections.append(section1350)


section1351 = {}
for key in i13.keys():
	if key == "trade":
		section1351[key] = list(set(i13[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section1351[key] = i13[key] + i51[key]


sections.append(section1351)


section1352 = {}
for key in i13.keys():
	if key == "trade":
		section1352[key] = list(set(i13[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section1352[key] = i13[key] + i52[key]


sections.append(section1352)


section1353 = {}
for key in i13.keys():
	if key == "trade":
		section1353[key] = list(set(i13[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section1353[key] = i13[key] + i53[key]


sections.append(section1353)


section1354 = {}
for key in i13.keys():
	if key == "trade":
		section1354[key] = list(set(i13[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section1354[key] = i13[key] + i54[key]


sections.append(section1354)


section1416 = {}
for key in i14.keys():
	if key == "trade":
		section1416[key] = list(set(i14[key] + i16[key]))
	if key == "intersection":
		pass
	else:
		section1416[key] = i14[key] + i16[key]


sections.append(section1416)


section1417 = {}
for key in i14.keys():
	if key == "trade":
		section1417[key] = list(set(i14[key] + i17[key]))
	if key == "intersection":
		pass
	else:
		section1417[key] = i14[key] + i17[key]


sections.append(section1417)


section1418 = {}
for key in i14.keys():
	if key == "trade":
		section1418[key] = list(set(i14[key] + i18[key]))
	if key == "intersection":
		pass
	else:
		section1418[key] = i14[key] + i18[key]


sections.append(section1418)


section1419 = {}
for key in i14.keys():
	if key == "trade":
		section1419[key] = list(set(i14[key] + i19[key]))
	if key == "intersection":
		pass
	else:
		section1419[key] = i14[key] + i19[key]


sections.append(section1419)


section1420 = {}
for key in i14.keys():
	if key == "trade":
		section1420[key] = list(set(i14[key] + i20[key]))
	if key == "intersection":
		pass
	else:
		section1420[key] = i14[key] + i20[key]


sections.append(section1420)


section1421 = {}
for key in i14.keys():
	if key == "trade":
		section1421[key] = list(set(i14[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section1421[key] = i14[key] + i21[key]


sections.append(section1421)


section1422 = {}
for key in i14.keys():
	if key == "trade":
		section1422[key] = list(set(i14[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section1422[key] = i14[key] + i22[key]


sections.append(section1422)


section1423 = {}
for key in i14.keys():
	if key == "trade":
		section1423[key] = list(set(i14[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section1423[key] = i14[key] + i23[key]


sections.append(section1423)


section1425 = {}
for key in i14.keys():
	if key == "trade":
		section1425[key] = list(set(i14[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section1425[key] = i14[key] + i25[key]


sections.append(section1425)


section1426 = {}
for key in i14.keys():
	if key == "trade":
		section1426[key] = list(set(i14[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section1426[key] = i14[key] + i26[key]


sections.append(section1426)


section1427 = {}
for key in i14.keys():
	if key == "trade":
		section1427[key] = list(set(i14[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section1427[key] = i14[key] + i27[key]


sections.append(section1427)


section1428 = {}
for key in i14.keys():
	if key == "trade":
		section1428[key] = list(set(i14[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section1428[key] = i14[key] + i28[key]


sections.append(section1428)


section1429 = {}
for key in i14.keys():
	if key == "trade":
		section1429[key] = list(set(i14[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section1429[key] = i14[key] + i29[key]


sections.append(section1429)


section1430 = {}
for key in i14.keys():
	if key == "trade":
		section1430[key] = list(set(i14[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section1430[key] = i14[key] + i30[key]


sections.append(section1430)


section1431 = {}
for key in i14.keys():
	if key == "trade":
		section1431[key] = list(set(i14[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section1431[key] = i14[key] + i31[key]


sections.append(section1431)


section1432 = {}
for key in i14.keys():
	if key == "trade":
		section1432[key] = list(set(i14[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section1432[key] = i14[key] + i32[key]


sections.append(section1432)


section1433 = {}
for key in i14.keys():
	if key == "trade":
		section1433[key] = list(set(i14[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section1433[key] = i14[key] + i33[key]


sections.append(section1433)


section1434 = {}
for key in i14.keys():
	if key == "trade":
		section1434[key] = list(set(i14[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section1434[key] = i14[key] + i34[key]


sections.append(section1434)


section1435 = {}
for key in i14.keys():
	if key == "trade":
		section1435[key] = list(set(i14[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section1435[key] = i14[key] + i35[key]


sections.append(section1435)


section1436 = {}
for key in i14.keys():
	if key == "trade":
		section1436[key] = list(set(i14[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section1436[key] = i14[key] + i36[key]


sections.append(section1436)


section1437 = {}
for key in i14.keys():
	if key == "trade":
		section1437[key] = list(set(i14[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section1437[key] = i14[key] + i37[key]


sections.append(section1437)


section1438 = {}
for key in i14.keys():
	if key == "trade":
		section1438[key] = list(set(i14[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section1438[key] = i14[key] + i38[key]


sections.append(section1438)


section1439 = {}
for key in i14.keys():
	if key == "trade":
		section1439[key] = list(set(i14[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section1439[key] = i14[key] + i39[key]


sections.append(section1439)


section1440 = {}
for key in i14.keys():
	if key == "trade":
		section1440[key] = list(set(i14[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section1440[key] = i14[key] + i40[key]


sections.append(section1440)


section1441 = {}
for key in i14.keys():
	if key == "trade":
		section1441[key] = list(set(i14[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section1441[key] = i14[key] + i41[key]


sections.append(section1441)


section1442 = {}
for key in i14.keys():
	if key == "trade":
		section1442[key] = list(set(i14[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section1442[key] = i14[key] + i42[key]


sections.append(section1442)


section1443 = {}
for key in i14.keys():
	if key == "trade":
		section1443[key] = list(set(i14[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section1443[key] = i14[key] + i43[key]


sections.append(section1443)


section1444 = {}
for key in i14.keys():
	if key == "trade":
		section1444[key] = list(set(i14[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section1444[key] = i14[key] + i44[key]


sections.append(section1444)


section1445 = {}
for key in i14.keys():
	if key == "trade":
		section1445[key] = list(set(i14[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section1445[key] = i14[key] + i45[key]


sections.append(section1445)


section1446 = {}
for key in i14.keys():
	if key == "trade":
		section1446[key] = list(set(i14[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section1446[key] = i14[key] + i46[key]


sections.append(section1446)


section1447 = {}
for key in i14.keys():
	if key == "trade":
		section1447[key] = list(set(i14[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section1447[key] = i14[key] + i47[key]


sections.append(section1447)


section1448 = {}
for key in i14.keys():
	if key == "trade":
		section1448[key] = list(set(i14[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section1448[key] = i14[key] + i48[key]


sections.append(section1448)


section1449 = {}
for key in i14.keys():
	if key == "trade":
		section1449[key] = list(set(i14[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section1449[key] = i14[key] + i49[key]


sections.append(section1449)


section1450 = {}
for key in i14.keys():
	if key == "trade":
		section1450[key] = list(set(i14[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section1450[key] = i14[key] + i50[key]


sections.append(section1450)


section1451 = {}
for key in i14.keys():
	if key == "trade":
		section1451[key] = list(set(i14[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section1451[key] = i14[key] + i51[key]


sections.append(section1451)


section1452 = {}
for key in i14.keys():
	if key == "trade":
		section1452[key] = list(set(i14[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section1452[key] = i14[key] + i52[key]


sections.append(section1452)


section1453 = {}
for key in i14.keys():
	if key == "trade":
		section1453[key] = list(set(i14[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section1453[key] = i14[key] + i53[key]


sections.append(section1453)


section1454 = {}
for key in i14.keys():
	if key == "trade":
		section1454[key] = list(set(i14[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section1454[key] = i14[key] + i54[key]


sections.append(section1454)


section1517 = {}
for key in i15.keys():
	if key == "trade":
		section1517[key] = list(set(i15[key] + i17[key]))
	if key == "intersection":
		pass
	else:
		section1517[key] = i15[key] + i17[key]


sections.append(section1517)


section1518 = {}
for key in i15.keys():
	if key == "trade":
		section1518[key] = list(set(i15[key] + i18[key]))
	if key == "intersection":
		pass
	else:
		section1518[key] = i15[key] + i18[key]


sections.append(section1518)


section1519 = {}
for key in i15.keys():
	if key == "trade":
		section1519[key] = list(set(i15[key] + i19[key]))
	if key == "intersection":
		pass
	else:
		section1519[key] = i15[key] + i19[key]


sections.append(section1519)


section1520 = {}
for key in i15.keys():
	if key == "trade":
		section1520[key] = list(set(i15[key] + i20[key]))
	if key == "intersection":
		pass
	else:
		section1520[key] = i15[key] + i20[key]


sections.append(section1520)


section1521 = {}
for key in i15.keys():
	if key == "trade":
		section1521[key] = list(set(i15[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section1521[key] = i15[key] + i21[key]


sections.append(section1521)


section1522 = {}
for key in i15.keys():
	if key == "trade":
		section1522[key] = list(set(i15[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section1522[key] = i15[key] + i22[key]


sections.append(section1522)


section1523 = {}
for key in i15.keys():
	if key == "trade":
		section1523[key] = list(set(i15[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section1523[key] = i15[key] + i23[key]


sections.append(section1523)


section1524 = {}
for key in i15.keys():
	if key == "trade":
		section1524[key] = list(set(i15[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section1524[key] = i15[key] + i24[key]


sections.append(section1524)


section1525 = {}
for key in i15.keys():
	if key == "trade":
		section1525[key] = list(set(i15[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section1525[key] = i15[key] + i25[key]


sections.append(section1525)


section1526 = {}
for key in i15.keys():
	if key == "trade":
		section1526[key] = list(set(i15[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section1526[key] = i15[key] + i26[key]


sections.append(section1526)


section1527 = {}
for key in i15.keys():
	if key == "trade":
		section1527[key] = list(set(i15[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section1527[key] = i15[key] + i27[key]


sections.append(section1527)


section1528 = {}
for key in i15.keys():
	if key == "trade":
		section1528[key] = list(set(i15[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section1528[key] = i15[key] + i28[key]


sections.append(section1528)


section1529 = {}
for key in i15.keys():
	if key == "trade":
		section1529[key] = list(set(i15[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section1529[key] = i15[key] + i29[key]


sections.append(section1529)


section1530 = {}
for key in i15.keys():
	if key == "trade":
		section1530[key] = list(set(i15[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section1530[key] = i15[key] + i30[key]


sections.append(section1530)


section1531 = {}
for key in i15.keys():
	if key == "trade":
		section1531[key] = list(set(i15[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section1531[key] = i15[key] + i31[key]


sections.append(section1531)


section1532 = {}
for key in i15.keys():
	if key == "trade":
		section1532[key] = list(set(i15[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section1532[key] = i15[key] + i32[key]


sections.append(section1532)


section1533 = {}
for key in i15.keys():
	if key == "trade":
		section1533[key] = list(set(i15[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section1533[key] = i15[key] + i33[key]


sections.append(section1533)


section1534 = {}
for key in i15.keys():
	if key == "trade":
		section1534[key] = list(set(i15[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section1534[key] = i15[key] + i34[key]


sections.append(section1534)


section1535 = {}
for key in i15.keys():
	if key == "trade":
		section1535[key] = list(set(i15[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section1535[key] = i15[key] + i35[key]


sections.append(section1535)


section1536 = {}
for key in i15.keys():
	if key == "trade":
		section1536[key] = list(set(i15[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section1536[key] = i15[key] + i36[key]


sections.append(section1536)


section1537 = {}
for key in i15.keys():
	if key == "trade":
		section1537[key] = list(set(i15[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section1537[key] = i15[key] + i37[key]


sections.append(section1537)


section1538 = {}
for key in i15.keys():
	if key == "trade":
		section1538[key] = list(set(i15[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section1538[key] = i15[key] + i38[key]


sections.append(section1538)


section1539 = {}
for key in i15.keys():
	if key == "trade":
		section1539[key] = list(set(i15[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section1539[key] = i15[key] + i39[key]


sections.append(section1539)


section1540 = {}
for key in i15.keys():
	if key == "trade":
		section1540[key] = list(set(i15[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section1540[key] = i15[key] + i40[key]


sections.append(section1540)


section1541 = {}
for key in i15.keys():
	if key == "trade":
		section1541[key] = list(set(i15[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section1541[key] = i15[key] + i41[key]


sections.append(section1541)


section1542 = {}
for key in i15.keys():
	if key == "trade":
		section1542[key] = list(set(i15[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section1542[key] = i15[key] + i42[key]


sections.append(section1542)


section1543 = {}
for key in i15.keys():
	if key == "trade":
		section1543[key] = list(set(i15[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section1543[key] = i15[key] + i43[key]


sections.append(section1543)


section1544 = {}
for key in i15.keys():
	if key == "trade":
		section1544[key] = list(set(i15[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section1544[key] = i15[key] + i44[key]


sections.append(section1544)


section1545 = {}
for key in i15.keys():
	if key == "trade":
		section1545[key] = list(set(i15[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section1545[key] = i15[key] + i45[key]


sections.append(section1545)


section1546 = {}
for key in i15.keys():
	if key == "trade":
		section1546[key] = list(set(i15[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section1546[key] = i15[key] + i46[key]


sections.append(section1546)


section1547 = {}
for key in i15.keys():
	if key == "trade":
		section1547[key] = list(set(i15[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section1547[key] = i15[key] + i47[key]


sections.append(section1547)


section1548 = {}
for key in i15.keys():
	if key == "trade":
		section1548[key] = list(set(i15[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section1548[key] = i15[key] + i48[key]


sections.append(section1548)


section1549 = {}
for key in i15.keys():
	if key == "trade":
		section1549[key] = list(set(i15[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section1549[key] = i15[key] + i49[key]


sections.append(section1549)


section1550 = {}
for key in i15.keys():
	if key == "trade":
		section1550[key] = list(set(i15[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section1550[key] = i15[key] + i50[key]


sections.append(section1550)


section1551 = {}
for key in i15.keys():
	if key == "trade":
		section1551[key] = list(set(i15[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section1551[key] = i15[key] + i51[key]


sections.append(section1551)


section1552 = {}
for key in i15.keys():
	if key == "trade":
		section1552[key] = list(set(i15[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section1552[key] = i15[key] + i52[key]


sections.append(section1552)


section1553 = {}
for key in i15.keys():
	if key == "trade":
		section1553[key] = list(set(i15[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section1553[key] = i15[key] + i53[key]


sections.append(section1553)


section1554 = {}
for key in i15.keys():
	if key == "trade":
		section1554[key] = list(set(i15[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section1554[key] = i15[key] + i54[key]


sections.append(section1554)


section1617 = {}
for key in i16.keys():
	if key == "trade":
		section1617[key] = list(set(i16[key] + i17[key]))
	if key == "intersection":
		pass
	else:
		section1617[key] = i16[key] + i17[key]


sections.append(section1617)


section1618 = {}
for key in i16.keys():
	if key == "trade":
		section1618[key] = list(set(i16[key] + i18[key]))
	if key == "intersection":
		pass
	else:
		section1618[key] = i16[key] + i18[key]


sections.append(section1618)


section1619 = {}
for key in i16.keys():
	if key == "trade":
		section1619[key] = list(set(i16[key] + i19[key]))
	if key == "intersection":
		pass
	else:
		section1619[key] = i16[key] + i19[key]


sections.append(section1619)


section1620 = {}
for key in i16.keys():
	if key == "trade":
		section1620[key] = list(set(i16[key] + i20[key]))
	if key == "intersection":
		pass
	else:
		section1620[key] = i16[key] + i20[key]


sections.append(section1620)


section1621 = {}
for key in i16.keys():
	if key == "trade":
		section1621[key] = list(set(i16[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section1621[key] = i16[key] + i21[key]


sections.append(section1621)


section1622 = {}
for key in i16.keys():
	if key == "trade":
		section1622[key] = list(set(i16[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section1622[key] = i16[key] + i22[key]


sections.append(section1622)


section1623 = {}
for key in i16.keys():
	if key == "trade":
		section1623[key] = list(set(i16[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section1623[key] = i16[key] + i23[key]


sections.append(section1623)


section1624 = {}
for key in i16.keys():
	if key == "trade":
		section1624[key] = list(set(i16[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section1624[key] = i16[key] + i24[key]


sections.append(section1624)


section1625 = {}
for key in i16.keys():
	if key == "trade":
		section1625[key] = list(set(i16[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section1625[key] = i16[key] + i25[key]


sections.append(section1625)


section1627 = {}
for key in i16.keys():
	if key == "trade":
		section1627[key] = list(set(i16[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section1627[key] = i16[key] + i27[key]


sections.append(section1627)


section1628 = {}
for key in i16.keys():
	if key == "trade":
		section1628[key] = list(set(i16[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section1628[key] = i16[key] + i28[key]


sections.append(section1628)


section1629 = {}
for key in i16.keys():
	if key == "trade":
		section1629[key] = list(set(i16[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section1629[key] = i16[key] + i29[key]


sections.append(section1629)


section1630 = {}
for key in i16.keys():
	if key == "trade":
		section1630[key] = list(set(i16[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section1630[key] = i16[key] + i30[key]


sections.append(section1630)


section1631 = {}
for key in i16.keys():
	if key == "trade":
		section1631[key] = list(set(i16[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section1631[key] = i16[key] + i31[key]


sections.append(section1631)


section1632 = {}
for key in i16.keys():
	if key == "trade":
		section1632[key] = list(set(i16[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section1632[key] = i16[key] + i32[key]


sections.append(section1632)


section1633 = {}
for key in i16.keys():
	if key == "trade":
		section1633[key] = list(set(i16[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section1633[key] = i16[key] + i33[key]


sections.append(section1633)


section1634 = {}
for key in i16.keys():
	if key == "trade":
		section1634[key] = list(set(i16[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section1634[key] = i16[key] + i34[key]


sections.append(section1634)


section1635 = {}
for key in i16.keys():
	if key == "trade":
		section1635[key] = list(set(i16[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section1635[key] = i16[key] + i35[key]


sections.append(section1635)


section1636 = {}
for key in i16.keys():
	if key == "trade":
		section1636[key] = list(set(i16[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section1636[key] = i16[key] + i36[key]


sections.append(section1636)


section1637 = {}
for key in i16.keys():
	if key == "trade":
		section1637[key] = list(set(i16[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section1637[key] = i16[key] + i37[key]


sections.append(section1637)


section1638 = {}
for key in i16.keys():
	if key == "trade":
		section1638[key] = list(set(i16[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section1638[key] = i16[key] + i38[key]


sections.append(section1638)


section1639 = {}
for key in i16.keys():
	if key == "trade":
		section1639[key] = list(set(i16[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section1639[key] = i16[key] + i39[key]


sections.append(section1639)


section1640 = {}
for key in i16.keys():
	if key == "trade":
		section1640[key] = list(set(i16[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section1640[key] = i16[key] + i40[key]


sections.append(section1640)


section1641 = {}
for key in i16.keys():
	if key == "trade":
		section1641[key] = list(set(i16[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section1641[key] = i16[key] + i41[key]


sections.append(section1641)


section1642 = {}
for key in i16.keys():
	if key == "trade":
		section1642[key] = list(set(i16[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section1642[key] = i16[key] + i42[key]


sections.append(section1642)


section1643 = {}
for key in i16.keys():
	if key == "trade":
		section1643[key] = list(set(i16[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section1643[key] = i16[key] + i43[key]


sections.append(section1643)


section1644 = {}
for key in i16.keys():
	if key == "trade":
		section1644[key] = list(set(i16[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section1644[key] = i16[key] + i44[key]


sections.append(section1644)


section1645 = {}
for key in i16.keys():
	if key == "trade":
		section1645[key] = list(set(i16[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section1645[key] = i16[key] + i45[key]


sections.append(section1645)


section1646 = {}
for key in i16.keys():
	if key == "trade":
		section1646[key] = list(set(i16[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section1646[key] = i16[key] + i46[key]


sections.append(section1646)


section1647 = {}
for key in i16.keys():
	if key == "trade":
		section1647[key] = list(set(i16[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section1647[key] = i16[key] + i47[key]


sections.append(section1647)


section1648 = {}
for key in i16.keys():
	if key == "trade":
		section1648[key] = list(set(i16[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section1648[key] = i16[key] + i48[key]


sections.append(section1648)


section1649 = {}
for key in i16.keys():
	if key == "trade":
		section1649[key] = list(set(i16[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section1649[key] = i16[key] + i49[key]


sections.append(section1649)


section1650 = {}
for key in i16.keys():
	if key == "trade":
		section1650[key] = list(set(i16[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section1650[key] = i16[key] + i50[key]


sections.append(section1650)


section1651 = {}
for key in i16.keys():
	if key == "trade":
		section1651[key] = list(set(i16[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section1651[key] = i16[key] + i51[key]


sections.append(section1651)


section1652 = {}
for key in i16.keys():
	if key == "trade":
		section1652[key] = list(set(i16[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section1652[key] = i16[key] + i52[key]


sections.append(section1652)


section1653 = {}
for key in i16.keys():
	if key == "trade":
		section1653[key] = list(set(i16[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section1653[key] = i16[key] + i53[key]


sections.append(section1653)


section1654 = {}
for key in i16.keys():
	if key == "trade":
		section1654[key] = list(set(i16[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section1654[key] = i16[key] + i54[key]


sections.append(section1654)


section1719 = {}
for key in i17.keys():
	if key == "trade":
		section1719[key] = list(set(i17[key] + i19[key]))
	if key == "intersection":
		pass
	else:
		section1719[key] = i17[key] + i19[key]


sections.append(section1719)


section1720 = {}
for key in i17.keys():
	if key == "trade":
		section1720[key] = list(set(i17[key] + i20[key]))
	if key == "intersection":
		pass
	else:
		section1720[key] = i17[key] + i20[key]


sections.append(section1720)


section1721 = {}
for key in i17.keys():
	if key == "trade":
		section1721[key] = list(set(i17[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section1721[key] = i17[key] + i21[key]


sections.append(section1721)


section1722 = {}
for key in i17.keys():
	if key == "trade":
		section1722[key] = list(set(i17[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section1722[key] = i17[key] + i22[key]


sections.append(section1722)


section1723 = {}
for key in i17.keys():
	if key == "trade":
		section1723[key] = list(set(i17[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section1723[key] = i17[key] + i23[key]


sections.append(section1723)


section1724 = {}
for key in i17.keys():
	if key == "trade":
		section1724[key] = list(set(i17[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section1724[key] = i17[key] + i24[key]


sections.append(section1724)


section1725 = {}
for key in i17.keys():
	if key == "trade":
		section1725[key] = list(set(i17[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section1725[key] = i17[key] + i25[key]


sections.append(section1725)


section1726 = {}
for key in i17.keys():
	if key == "trade":
		section1726[key] = list(set(i17[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section1726[key] = i17[key] + i26[key]


sections.append(section1726)


section1727 = {}
for key in i17.keys():
	if key == "trade":
		section1727[key] = list(set(i17[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section1727[key] = i17[key] + i27[key]


sections.append(section1727)


section1729 = {}
for key in i17.keys():
	if key == "trade":
		section1729[key] = list(set(i17[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section1729[key] = i17[key] + i29[key]


sections.append(section1729)


section1730 = {}
for key in i17.keys():
	if key == "trade":
		section1730[key] = list(set(i17[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section1730[key] = i17[key] + i30[key]


sections.append(section1730)


section1731 = {}
for key in i17.keys():
	if key == "trade":
		section1731[key] = list(set(i17[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section1731[key] = i17[key] + i31[key]


sections.append(section1731)


section1732 = {}
for key in i17.keys():
	if key == "trade":
		section1732[key] = list(set(i17[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section1732[key] = i17[key] + i32[key]


sections.append(section1732)


section1733 = {}
for key in i17.keys():
	if key == "trade":
		section1733[key] = list(set(i17[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section1733[key] = i17[key] + i33[key]


sections.append(section1733)


section1734 = {}
for key in i17.keys():
	if key == "trade":
		section1734[key] = list(set(i17[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section1734[key] = i17[key] + i34[key]


sections.append(section1734)


section1735 = {}
for key in i17.keys():
	if key == "trade":
		section1735[key] = list(set(i17[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section1735[key] = i17[key] + i35[key]


sections.append(section1735)


section1736 = {}
for key in i17.keys():
	if key == "trade":
		section1736[key] = list(set(i17[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section1736[key] = i17[key] + i36[key]


sections.append(section1736)


section1737 = {}
for key in i17.keys():
	if key == "trade":
		section1737[key] = list(set(i17[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section1737[key] = i17[key] + i37[key]


sections.append(section1737)


section1738 = {}
for key in i17.keys():
	if key == "trade":
		section1738[key] = list(set(i17[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section1738[key] = i17[key] + i38[key]


sections.append(section1738)


section1739 = {}
for key in i17.keys():
	if key == "trade":
		section1739[key] = list(set(i17[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section1739[key] = i17[key] + i39[key]


sections.append(section1739)


section1740 = {}
for key in i17.keys():
	if key == "trade":
		section1740[key] = list(set(i17[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section1740[key] = i17[key] + i40[key]


sections.append(section1740)


section1741 = {}
for key in i17.keys():
	if key == "trade":
		section1741[key] = list(set(i17[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section1741[key] = i17[key] + i41[key]


sections.append(section1741)


section1742 = {}
for key in i17.keys():
	if key == "trade":
		section1742[key] = list(set(i17[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section1742[key] = i17[key] + i42[key]


sections.append(section1742)


section1743 = {}
for key in i17.keys():
	if key == "trade":
		section1743[key] = list(set(i17[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section1743[key] = i17[key] + i43[key]


sections.append(section1743)


section1744 = {}
for key in i17.keys():
	if key == "trade":
		section1744[key] = list(set(i17[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section1744[key] = i17[key] + i44[key]


sections.append(section1744)


section1745 = {}
for key in i17.keys():
	if key == "trade":
		section1745[key] = list(set(i17[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section1745[key] = i17[key] + i45[key]


sections.append(section1745)


section1746 = {}
for key in i17.keys():
	if key == "trade":
		section1746[key] = list(set(i17[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section1746[key] = i17[key] + i46[key]


sections.append(section1746)


section1747 = {}
for key in i17.keys():
	if key == "trade":
		section1747[key] = list(set(i17[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section1747[key] = i17[key] + i47[key]


sections.append(section1747)


section1748 = {}
for key in i17.keys():
	if key == "trade":
		section1748[key] = list(set(i17[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section1748[key] = i17[key] + i48[key]


sections.append(section1748)


section1749 = {}
for key in i17.keys():
	if key == "trade":
		section1749[key] = list(set(i17[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section1749[key] = i17[key] + i49[key]


sections.append(section1749)


section1750 = {}
for key in i17.keys():
	if key == "trade":
		section1750[key] = list(set(i17[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section1750[key] = i17[key] + i50[key]


sections.append(section1750)


section1751 = {}
for key in i17.keys():
	if key == "trade":
		section1751[key] = list(set(i17[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section1751[key] = i17[key] + i51[key]


sections.append(section1751)


section1752 = {}
for key in i17.keys():
	if key == "trade":
		section1752[key] = list(set(i17[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section1752[key] = i17[key] + i52[key]


sections.append(section1752)


section1753 = {}
for key in i17.keys():
	if key == "trade":
		section1753[key] = list(set(i17[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section1753[key] = i17[key] + i53[key]


sections.append(section1753)


section1754 = {}
for key in i17.keys():
	if key == "trade":
		section1754[key] = list(set(i17[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section1754[key] = i17[key] + i54[key]


sections.append(section1754)


section1820 = {}
for key in i18.keys():
	if key == "trade":
		section1820[key] = list(set(i18[key] + i20[key]))
	if key == "intersection":
		pass
	else:
		section1820[key] = i18[key] + i20[key]


sections.append(section1820)


section1821 = {}
for key in i18.keys():
	if key == "trade":
		section1821[key] = list(set(i18[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section1821[key] = i18[key] + i21[key]


sections.append(section1821)


section1822 = {}
for key in i18.keys():
	if key == "trade":
		section1822[key] = list(set(i18[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section1822[key] = i18[key] + i22[key]


sections.append(section1822)


section1823 = {}
for key in i18.keys():
	if key == "trade":
		section1823[key] = list(set(i18[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section1823[key] = i18[key] + i23[key]


sections.append(section1823)


section1824 = {}
for key in i18.keys():
	if key == "trade":
		section1824[key] = list(set(i18[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section1824[key] = i18[key] + i24[key]


sections.append(section1824)


section1825 = {}
for key in i18.keys():
	if key == "trade":
		section1825[key] = list(set(i18[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section1825[key] = i18[key] + i25[key]


sections.append(section1825)


section1826 = {}
for key in i18.keys():
	if key == "trade":
		section1826[key] = list(set(i18[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section1826[key] = i18[key] + i26[key]


sections.append(section1826)


section1827 = {}
for key in i18.keys():
	if key == "trade":
		section1827[key] = list(set(i18[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section1827[key] = i18[key] + i27[key]


sections.append(section1827)


section1828 = {}
for key in i18.keys():
	if key == "trade":
		section1828[key] = list(set(i18[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section1828[key] = i18[key] + i28[key]


sections.append(section1828)


section1829 = {}
for key in i18.keys():
	if key == "trade":
		section1829[key] = list(set(i18[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section1829[key] = i18[key] + i29[key]


sections.append(section1829)


section1830 = {}
for key in i18.keys():
	if key == "trade":
		section1830[key] = list(set(i18[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section1830[key] = i18[key] + i30[key]


sections.append(section1830)


section1831 = {}
for key in i18.keys():
	if key == "trade":
		section1831[key] = list(set(i18[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section1831[key] = i18[key] + i31[key]


sections.append(section1831)


section1832 = {}
for key in i18.keys():
	if key == "trade":
		section1832[key] = list(set(i18[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section1832[key] = i18[key] + i32[key]


sections.append(section1832)


section1833 = {}
for key in i18.keys():
	if key == "trade":
		section1833[key] = list(set(i18[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section1833[key] = i18[key] + i33[key]


sections.append(section1833)


section1834 = {}
for key in i18.keys():
	if key == "trade":
		section1834[key] = list(set(i18[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section1834[key] = i18[key] + i34[key]


sections.append(section1834)


section1835 = {}
for key in i18.keys():
	if key == "trade":
		section1835[key] = list(set(i18[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section1835[key] = i18[key] + i35[key]


sections.append(section1835)


section1836 = {}
for key in i18.keys():
	if key == "trade":
		section1836[key] = list(set(i18[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section1836[key] = i18[key] + i36[key]


sections.append(section1836)


section1837 = {}
for key in i18.keys():
	if key == "trade":
		section1837[key] = list(set(i18[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section1837[key] = i18[key] + i37[key]


sections.append(section1837)


section1838 = {}
for key in i18.keys():
	if key == "trade":
		section1838[key] = list(set(i18[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section1838[key] = i18[key] + i38[key]


sections.append(section1838)


section1839 = {}
for key in i18.keys():
	if key == "trade":
		section1839[key] = list(set(i18[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section1839[key] = i18[key] + i39[key]


sections.append(section1839)


section1840 = {}
for key in i18.keys():
	if key == "trade":
		section1840[key] = list(set(i18[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section1840[key] = i18[key] + i40[key]


sections.append(section1840)


section1841 = {}
for key in i18.keys():
	if key == "trade":
		section1841[key] = list(set(i18[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section1841[key] = i18[key] + i41[key]


sections.append(section1841)


section1842 = {}
for key in i18.keys():
	if key == "trade":
		section1842[key] = list(set(i18[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section1842[key] = i18[key] + i42[key]


sections.append(section1842)


section1843 = {}
for key in i18.keys():
	if key == "trade":
		section1843[key] = list(set(i18[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section1843[key] = i18[key] + i43[key]


sections.append(section1843)


section1844 = {}
for key in i18.keys():
	if key == "trade":
		section1844[key] = list(set(i18[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section1844[key] = i18[key] + i44[key]


sections.append(section1844)


section1845 = {}
for key in i18.keys():
	if key == "trade":
		section1845[key] = list(set(i18[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section1845[key] = i18[key] + i45[key]


sections.append(section1845)


section1846 = {}
for key in i18.keys():
	if key == "trade":
		section1846[key] = list(set(i18[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section1846[key] = i18[key] + i46[key]


sections.append(section1846)


section1847 = {}
for key in i18.keys():
	if key == "trade":
		section1847[key] = list(set(i18[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section1847[key] = i18[key] + i47[key]


sections.append(section1847)


section1848 = {}
for key in i18.keys():
	if key == "trade":
		section1848[key] = list(set(i18[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section1848[key] = i18[key] + i48[key]


sections.append(section1848)


section1849 = {}
for key in i18.keys():
	if key == "trade":
		section1849[key] = list(set(i18[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section1849[key] = i18[key] + i49[key]


sections.append(section1849)


section1850 = {}
for key in i18.keys():
	if key == "trade":
		section1850[key] = list(set(i18[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section1850[key] = i18[key] + i50[key]


sections.append(section1850)


section1851 = {}
for key in i18.keys():
	if key == "trade":
		section1851[key] = list(set(i18[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section1851[key] = i18[key] + i51[key]


sections.append(section1851)


section1852 = {}
for key in i18.keys():
	if key == "trade":
		section1852[key] = list(set(i18[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section1852[key] = i18[key] + i52[key]


sections.append(section1852)


section1853 = {}
for key in i18.keys():
	if key == "trade":
		section1853[key] = list(set(i18[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section1853[key] = i18[key] + i53[key]


sections.append(section1853)


section1854 = {}
for key in i18.keys():
	if key == "trade":
		section1854[key] = list(set(i18[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section1854[key] = i18[key] + i54[key]


sections.append(section1854)


section1921 = {}
for key in i19.keys():
	if key == "trade":
		section1921[key] = list(set(i19[key] + i21[key]))
	if key == "intersection":
		pass
	else:
		section1921[key] = i19[key] + i21[key]


sections.append(section1921)


section1922 = {}
for key in i19.keys():
	if key == "trade":
		section1922[key] = list(set(i19[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section1922[key] = i19[key] + i22[key]


sections.append(section1922)


section1923 = {}
for key in i19.keys():
	if key == "trade":
		section1923[key] = list(set(i19[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section1923[key] = i19[key] + i23[key]


sections.append(section1923)


section1924 = {}
for key in i19.keys():
	if key == "trade":
		section1924[key] = list(set(i19[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section1924[key] = i19[key] + i24[key]


sections.append(section1924)


section1925 = {}
for key in i19.keys():
	if key == "trade":
		section1925[key] = list(set(i19[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section1925[key] = i19[key] + i25[key]


sections.append(section1925)


section1926 = {}
for key in i19.keys():
	if key == "trade":
		section1926[key] = list(set(i19[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section1926[key] = i19[key] + i26[key]


sections.append(section1926)


section1927 = {}
for key in i19.keys():
	if key == "trade":
		section1927[key] = list(set(i19[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section1927[key] = i19[key] + i27[key]


sections.append(section1927)


section1928 = {}
for key in i19.keys():
	if key == "trade":
		section1928[key] = list(set(i19[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section1928[key] = i19[key] + i28[key]


sections.append(section1928)


section1929 = {}
for key in i19.keys():
	if key == "trade":
		section1929[key] = list(set(i19[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section1929[key] = i19[key] + i29[key]


sections.append(section1929)


section1931 = {}
for key in i19.keys():
	if key == "trade":
		section1931[key] = list(set(i19[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section1931[key] = i19[key] + i31[key]


sections.append(section1931)


section1932 = {}
for key in i19.keys():
	if key == "trade":
		section1932[key] = list(set(i19[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section1932[key] = i19[key] + i32[key]


sections.append(section1932)


section1933 = {}
for key in i19.keys():
	if key == "trade":
		section1933[key] = list(set(i19[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section1933[key] = i19[key] + i33[key]


sections.append(section1933)


section1934 = {}
for key in i19.keys():
	if key == "trade":
		section1934[key] = list(set(i19[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section1934[key] = i19[key] + i34[key]


sections.append(section1934)


section1935 = {}
for key in i19.keys():
	if key == "trade":
		section1935[key] = list(set(i19[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section1935[key] = i19[key] + i35[key]


sections.append(section1935)


section1936 = {}
for key in i19.keys():
	if key == "trade":
		section1936[key] = list(set(i19[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section1936[key] = i19[key] + i36[key]


sections.append(section1936)


section1937 = {}
for key in i19.keys():
	if key == "trade":
		section1937[key] = list(set(i19[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section1937[key] = i19[key] + i37[key]


sections.append(section1937)


section1938 = {}
for key in i19.keys():
	if key == "trade":
		section1938[key] = list(set(i19[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section1938[key] = i19[key] + i38[key]


sections.append(section1938)


section1939 = {}
for key in i19.keys():
	if key == "trade":
		section1939[key] = list(set(i19[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section1939[key] = i19[key] + i39[key]


sections.append(section1939)


section1940 = {}
for key in i19.keys():
	if key == "trade":
		section1940[key] = list(set(i19[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section1940[key] = i19[key] + i40[key]


sections.append(section1940)


section1941 = {}
for key in i19.keys():
	if key == "trade":
		section1941[key] = list(set(i19[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section1941[key] = i19[key] + i41[key]


sections.append(section1941)


section1942 = {}
for key in i19.keys():
	if key == "trade":
		section1942[key] = list(set(i19[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section1942[key] = i19[key] + i42[key]


sections.append(section1942)


section1943 = {}
for key in i19.keys():
	if key == "trade":
		section1943[key] = list(set(i19[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section1943[key] = i19[key] + i43[key]


sections.append(section1943)


section1944 = {}
for key in i19.keys():
	if key == "trade":
		section1944[key] = list(set(i19[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section1944[key] = i19[key] + i44[key]


sections.append(section1944)


section1945 = {}
for key in i19.keys():
	if key == "trade":
		section1945[key] = list(set(i19[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section1945[key] = i19[key] + i45[key]


sections.append(section1945)


section1946 = {}
for key in i19.keys():
	if key == "trade":
		section1946[key] = list(set(i19[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section1946[key] = i19[key] + i46[key]


sections.append(section1946)


section1947 = {}
for key in i19.keys():
	if key == "trade":
		section1947[key] = list(set(i19[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section1947[key] = i19[key] + i47[key]


sections.append(section1947)


section1948 = {}
for key in i19.keys():
	if key == "trade":
		section1948[key] = list(set(i19[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section1948[key] = i19[key] + i48[key]


sections.append(section1948)


section1949 = {}
for key in i19.keys():
	if key == "trade":
		section1949[key] = list(set(i19[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section1949[key] = i19[key] + i49[key]


sections.append(section1949)


section1950 = {}
for key in i19.keys():
	if key == "trade":
		section1950[key] = list(set(i19[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section1950[key] = i19[key] + i50[key]


sections.append(section1950)


section1951 = {}
for key in i19.keys():
	if key == "trade":
		section1951[key] = list(set(i19[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section1951[key] = i19[key] + i51[key]


sections.append(section1951)


section1952 = {}
for key in i19.keys():
	if key == "trade":
		section1952[key] = list(set(i19[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section1952[key] = i19[key] + i52[key]


sections.append(section1952)


section1953 = {}
for key in i19.keys():
	if key == "trade":
		section1953[key] = list(set(i19[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section1953[key] = i19[key] + i53[key]


sections.append(section1953)


section1954 = {}
for key in i19.keys():
	if key == "trade":
		section1954[key] = list(set(i19[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section1954[key] = i19[key] + i54[key]


sections.append(section1954)


section2022 = {}
for key in i20.keys():
	if key == "trade":
		section2022[key] = list(set(i20[key] + i22[key]))
	if key == "intersection":
		pass
	else:
		section2022[key] = i20[key] + i22[key]


sections.append(section2022)


section2023 = {}
for key in i20.keys():
	if key == "trade":
		section2023[key] = list(set(i20[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section2023[key] = i20[key] + i23[key]


sections.append(section2023)


section2024 = {}
for key in i20.keys():
	if key == "trade":
		section2024[key] = list(set(i20[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section2024[key] = i20[key] + i24[key]


sections.append(section2024)


section2025 = {}
for key in i20.keys():
	if key == "trade":
		section2025[key] = list(set(i20[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section2025[key] = i20[key] + i25[key]


sections.append(section2025)


section2026 = {}
for key in i20.keys():
	if key == "trade":
		section2026[key] = list(set(i20[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section2026[key] = i20[key] + i26[key]


sections.append(section2026)


section2027 = {}
for key in i20.keys():
	if key == "trade":
		section2027[key] = list(set(i20[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section2027[key] = i20[key] + i27[key]


sections.append(section2027)


section2028 = {}
for key in i20.keys():
	if key == "trade":
		section2028[key] = list(set(i20[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section2028[key] = i20[key] + i28[key]


sections.append(section2028)


section2029 = {}
for key in i20.keys():
	if key == "trade":
		section2029[key] = list(set(i20[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section2029[key] = i20[key] + i29[key]


sections.append(section2029)


section2030 = {}
for key in i20.keys():
	if key == "trade":
		section2030[key] = list(set(i20[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section2030[key] = i20[key] + i30[key]


sections.append(section2030)


section2031 = {}
for key in i20.keys():
	if key == "trade":
		section2031[key] = list(set(i20[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section2031[key] = i20[key] + i31[key]


sections.append(section2031)


section2032 = {}
for key in i20.keys():
	if key == "trade":
		section2032[key] = list(set(i20[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section2032[key] = i20[key] + i32[key]


sections.append(section2032)


section2033 = {}
for key in i20.keys():
	if key == "trade":
		section2033[key] = list(set(i20[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section2033[key] = i20[key] + i33[key]


sections.append(section2033)


section2034 = {}
for key in i20.keys():
	if key == "trade":
		section2034[key] = list(set(i20[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section2034[key] = i20[key] + i34[key]


sections.append(section2034)


section2035 = {}
for key in i20.keys():
	if key == "trade":
		section2035[key] = list(set(i20[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section2035[key] = i20[key] + i35[key]


sections.append(section2035)


section2036 = {}
for key in i20.keys():
	if key == "trade":
		section2036[key] = list(set(i20[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section2036[key] = i20[key] + i36[key]


sections.append(section2036)


section2037 = {}
for key in i20.keys():
	if key == "trade":
		section2037[key] = list(set(i20[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section2037[key] = i20[key] + i37[key]


sections.append(section2037)


section2038 = {}
for key in i20.keys():
	if key == "trade":
		section2038[key] = list(set(i20[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section2038[key] = i20[key] + i38[key]


sections.append(section2038)


section2039 = {}
for key in i20.keys():
	if key == "trade":
		section2039[key] = list(set(i20[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section2039[key] = i20[key] + i39[key]


sections.append(section2039)


section2040 = {}
for key in i20.keys():
	if key == "trade":
		section2040[key] = list(set(i20[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section2040[key] = i20[key] + i40[key]


sections.append(section2040)


section2041 = {}
for key in i20.keys():
	if key == "trade":
		section2041[key] = list(set(i20[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section2041[key] = i20[key] + i41[key]


sections.append(section2041)


section2042 = {}
for key in i20.keys():
	if key == "trade":
		section2042[key] = list(set(i20[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section2042[key] = i20[key] + i42[key]


sections.append(section2042)


section2043 = {}
for key in i20.keys():
	if key == "trade":
		section2043[key] = list(set(i20[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section2043[key] = i20[key] + i43[key]


sections.append(section2043)


section2044 = {}
for key in i20.keys():
	if key == "trade":
		section2044[key] = list(set(i20[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section2044[key] = i20[key] + i44[key]


sections.append(section2044)


section2045 = {}
for key in i20.keys():
	if key == "trade":
		section2045[key] = list(set(i20[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section2045[key] = i20[key] + i45[key]


sections.append(section2045)


section2046 = {}
for key in i20.keys():
	if key == "trade":
		section2046[key] = list(set(i20[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section2046[key] = i20[key] + i46[key]


sections.append(section2046)


section2047 = {}
for key in i20.keys():
	if key == "trade":
		section2047[key] = list(set(i20[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section2047[key] = i20[key] + i47[key]


sections.append(section2047)


section2048 = {}
for key in i20.keys():
	if key == "trade":
		section2048[key] = list(set(i20[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section2048[key] = i20[key] + i48[key]


sections.append(section2048)


section2049 = {}
for key in i20.keys():
	if key == "trade":
		section2049[key] = list(set(i20[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section2049[key] = i20[key] + i49[key]


sections.append(section2049)


section2050 = {}
for key in i20.keys():
	if key == "trade":
		section2050[key] = list(set(i20[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section2050[key] = i20[key] + i50[key]


sections.append(section2050)


section2051 = {}
for key in i20.keys():
	if key == "trade":
		section2051[key] = list(set(i20[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section2051[key] = i20[key] + i51[key]


sections.append(section2051)


section2052 = {}
for key in i20.keys():
	if key == "trade":
		section2052[key] = list(set(i20[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section2052[key] = i20[key] + i52[key]


sections.append(section2052)


section2053 = {}
for key in i20.keys():
	if key == "trade":
		section2053[key] = list(set(i20[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section2053[key] = i20[key] + i53[key]


sections.append(section2053)


section2054 = {}
for key in i20.keys():
	if key == "trade":
		section2054[key] = list(set(i20[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section2054[key] = i20[key] + i54[key]


sections.append(section2054)


section2123 = {}
for key in i21.keys():
	if key == "trade":
		section2123[key] = list(set(i21[key] + i23[key]))
	if key == "intersection":
		pass
	else:
		section2123[key] = i21[key] + i23[key]


sections.append(section2123)


section2124 = {}
for key in i21.keys():
	if key == "trade":
		section2124[key] = list(set(i21[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section2124[key] = i21[key] + i24[key]


sections.append(section2124)


section2125 = {}
for key in i21.keys():
	if key == "trade":
		section2125[key] = list(set(i21[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section2125[key] = i21[key] + i25[key]


sections.append(section2125)


section2126 = {}
for key in i21.keys():
	if key == "trade":
		section2126[key] = list(set(i21[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section2126[key] = i21[key] + i26[key]


sections.append(section2126)


section2127 = {}
for key in i21.keys():
	if key == "trade":
		section2127[key] = list(set(i21[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section2127[key] = i21[key] + i27[key]


sections.append(section2127)


section2128 = {}
for key in i21.keys():
	if key == "trade":
		section2128[key] = list(set(i21[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section2128[key] = i21[key] + i28[key]


sections.append(section2128)


section2129 = {}
for key in i21.keys():
	if key == "trade":
		section2129[key] = list(set(i21[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section2129[key] = i21[key] + i29[key]


sections.append(section2129)


section2130 = {}
for key in i21.keys():
	if key == "trade":
		section2130[key] = list(set(i21[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section2130[key] = i21[key] + i30[key]


sections.append(section2130)


section2131 = {}
for key in i21.keys():
	if key == "trade":
		section2131[key] = list(set(i21[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section2131[key] = i21[key] + i31[key]


sections.append(section2131)


section2133 = {}
for key in i21.keys():
	if key == "trade":
		section2133[key] = list(set(i21[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section2133[key] = i21[key] + i33[key]


sections.append(section2133)


section2134 = {}
for key in i21.keys():
	if key == "trade":
		section2134[key] = list(set(i21[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section2134[key] = i21[key] + i34[key]


sections.append(section2134)


section2135 = {}
for key in i21.keys():
	if key == "trade":
		section2135[key] = list(set(i21[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section2135[key] = i21[key] + i35[key]


sections.append(section2135)


section2136 = {}
for key in i21.keys():
	if key == "trade":
		section2136[key] = list(set(i21[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section2136[key] = i21[key] + i36[key]


sections.append(section2136)


section2137 = {}
for key in i21.keys():
	if key == "trade":
		section2137[key] = list(set(i21[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section2137[key] = i21[key] + i37[key]


sections.append(section2137)


section2138 = {}
for key in i21.keys():
	if key == "trade":
		section2138[key] = list(set(i21[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section2138[key] = i21[key] + i38[key]


sections.append(section2138)


section2139 = {}
for key in i21.keys():
	if key == "trade":
		section2139[key] = list(set(i21[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section2139[key] = i21[key] + i39[key]


sections.append(section2139)


section2140 = {}
for key in i21.keys():
	if key == "trade":
		section2140[key] = list(set(i21[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section2140[key] = i21[key] + i40[key]


sections.append(section2140)


section2141 = {}
for key in i21.keys():
	if key == "trade":
		section2141[key] = list(set(i21[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section2141[key] = i21[key] + i41[key]


sections.append(section2141)


section2142 = {}
for key in i21.keys():
	if key == "trade":
		section2142[key] = list(set(i21[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section2142[key] = i21[key] + i42[key]


sections.append(section2142)


section2143 = {}
for key in i21.keys():
	if key == "trade":
		section2143[key] = list(set(i21[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section2143[key] = i21[key] + i43[key]


sections.append(section2143)


section2144 = {}
for key in i21.keys():
	if key == "trade":
		section2144[key] = list(set(i21[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section2144[key] = i21[key] + i44[key]


sections.append(section2144)


section2145 = {}
for key in i21.keys():
	if key == "trade":
		section2145[key] = list(set(i21[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section2145[key] = i21[key] + i45[key]


sections.append(section2145)


section2146 = {}
for key in i21.keys():
	if key == "trade":
		section2146[key] = list(set(i21[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section2146[key] = i21[key] + i46[key]


sections.append(section2146)


section2147 = {}
for key in i21.keys():
	if key == "trade":
		section2147[key] = list(set(i21[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section2147[key] = i21[key] + i47[key]


sections.append(section2147)


section2148 = {}
for key in i21.keys():
	if key == "trade":
		section2148[key] = list(set(i21[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section2148[key] = i21[key] + i48[key]


sections.append(section2148)


section2149 = {}
for key in i21.keys():
	if key == "trade":
		section2149[key] = list(set(i21[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section2149[key] = i21[key] + i49[key]


sections.append(section2149)


section2150 = {}
for key in i21.keys():
	if key == "trade":
		section2150[key] = list(set(i21[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section2150[key] = i21[key] + i50[key]


sections.append(section2150)


section2151 = {}
for key in i21.keys():
	if key == "trade":
		section2151[key] = list(set(i21[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section2151[key] = i21[key] + i51[key]


sections.append(section2151)


section2152 = {}
for key in i21.keys():
	if key == "trade":
		section2152[key] = list(set(i21[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section2152[key] = i21[key] + i52[key]


sections.append(section2152)


section2153 = {}
for key in i21.keys():
	if key == "trade":
		section2153[key] = list(set(i21[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section2153[key] = i21[key] + i53[key]


sections.append(section2153)


section2154 = {}
for key in i21.keys():
	if key == "trade":
		section2154[key] = list(set(i21[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section2154[key] = i21[key] + i54[key]


sections.append(section2154)


section2224 = {}
for key in i22.keys():
	if key == "trade":
		section2224[key] = list(set(i22[key] + i24[key]))
	if key == "intersection":
		pass
	else:
		section2224[key] = i22[key] + i24[key]


sections.append(section2224)


section2225 = {}
for key in i22.keys():
	if key == "trade":
		section2225[key] = list(set(i22[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section2225[key] = i22[key] + i25[key]


sections.append(section2225)


section2226 = {}
for key in i22.keys():
	if key == "trade":
		section2226[key] = list(set(i22[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section2226[key] = i22[key] + i26[key]


sections.append(section2226)


section2227 = {}
for key in i22.keys():
	if key == "trade":
		section2227[key] = list(set(i22[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section2227[key] = i22[key] + i27[key]


sections.append(section2227)


section2228 = {}
for key in i22.keys():
	if key == "trade":
		section2228[key] = list(set(i22[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section2228[key] = i22[key] + i28[key]


sections.append(section2228)


section2229 = {}
for key in i22.keys():
	if key == "trade":
		section2229[key] = list(set(i22[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section2229[key] = i22[key] + i29[key]


sections.append(section2229)


section2230 = {}
for key in i22.keys():
	if key == "trade":
		section2230[key] = list(set(i22[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section2230[key] = i22[key] + i30[key]


sections.append(section2230)


section2231 = {}
for key in i22.keys():
	if key == "trade":
		section2231[key] = list(set(i22[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section2231[key] = i22[key] + i31[key]


sections.append(section2231)


section2232 = {}
for key in i22.keys():
	if key == "trade":
		section2232[key] = list(set(i22[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section2232[key] = i22[key] + i32[key]


sections.append(section2232)


section2233 = {}
for key in i22.keys():
	if key == "trade":
		section2233[key] = list(set(i22[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section2233[key] = i22[key] + i33[key]


sections.append(section2233)


section2234 = {}
for key in i22.keys():
	if key == "trade":
		section2234[key] = list(set(i22[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section2234[key] = i22[key] + i34[key]


sections.append(section2234)


section2235 = {}
for key in i22.keys():
	if key == "trade":
		section2235[key] = list(set(i22[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section2235[key] = i22[key] + i35[key]


sections.append(section2235)


section2236 = {}
for key in i22.keys():
	if key == "trade":
		section2236[key] = list(set(i22[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section2236[key] = i22[key] + i36[key]


sections.append(section2236)


section2237 = {}
for key in i22.keys():
	if key == "trade":
		section2237[key] = list(set(i22[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section2237[key] = i22[key] + i37[key]


sections.append(section2237)


section2238 = {}
for key in i22.keys():
	if key == "trade":
		section2238[key] = list(set(i22[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section2238[key] = i22[key] + i38[key]


sections.append(section2238)


section2239 = {}
for key in i22.keys():
	if key == "trade":
		section2239[key] = list(set(i22[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section2239[key] = i22[key] + i39[key]


sections.append(section2239)


section2240 = {}
for key in i22.keys():
	if key == "trade":
		section2240[key] = list(set(i22[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section2240[key] = i22[key] + i40[key]


sections.append(section2240)


section2241 = {}
for key in i22.keys():
	if key == "trade":
		section2241[key] = list(set(i22[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section2241[key] = i22[key] + i41[key]


sections.append(section2241)


section2242 = {}
for key in i22.keys():
	if key == "trade":
		section2242[key] = list(set(i22[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section2242[key] = i22[key] + i42[key]


sections.append(section2242)


section2243 = {}
for key in i22.keys():
	if key == "trade":
		section2243[key] = list(set(i22[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section2243[key] = i22[key] + i43[key]


sections.append(section2243)


section2244 = {}
for key in i22.keys():
	if key == "trade":
		section2244[key] = list(set(i22[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section2244[key] = i22[key] + i44[key]


sections.append(section2244)


section2245 = {}
for key in i22.keys():
	if key == "trade":
		section2245[key] = list(set(i22[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section2245[key] = i22[key] + i45[key]


sections.append(section2245)


section2246 = {}
for key in i22.keys():
	if key == "trade":
		section2246[key] = list(set(i22[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section2246[key] = i22[key] + i46[key]


sections.append(section2246)


section2247 = {}
for key in i22.keys():
	if key == "trade":
		section2247[key] = list(set(i22[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section2247[key] = i22[key] + i47[key]


sections.append(section2247)


section2248 = {}
for key in i22.keys():
	if key == "trade":
		section2248[key] = list(set(i22[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section2248[key] = i22[key] + i48[key]


sections.append(section2248)


section2249 = {}
for key in i22.keys():
	if key == "trade":
		section2249[key] = list(set(i22[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section2249[key] = i22[key] + i49[key]


sections.append(section2249)


section2250 = {}
for key in i22.keys():
	if key == "trade":
		section2250[key] = list(set(i22[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section2250[key] = i22[key] + i50[key]


sections.append(section2250)


section2251 = {}
for key in i22.keys():
	if key == "trade":
		section2251[key] = list(set(i22[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section2251[key] = i22[key] + i51[key]


sections.append(section2251)


section2252 = {}
for key in i22.keys():
	if key == "trade":
		section2252[key] = list(set(i22[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section2252[key] = i22[key] + i52[key]


sections.append(section2252)


section2253 = {}
for key in i22.keys():
	if key == "trade":
		section2253[key] = list(set(i22[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section2253[key] = i22[key] + i53[key]


sections.append(section2253)


section2254 = {}
for key in i22.keys():
	if key == "trade":
		section2254[key] = list(set(i22[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section2254[key] = i22[key] + i54[key]


sections.append(section2254)


section2325 = {}
for key in i23.keys():
	if key == "trade":
		section2325[key] = list(set(i23[key] + i25[key]))
	if key == "intersection":
		pass
	else:
		section2325[key] = i23[key] + i25[key]


sections.append(section2325)


section2326 = {}
for key in i23.keys():
	if key == "trade":
		section2326[key] = list(set(i23[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section2326[key] = i23[key] + i26[key]


sections.append(section2326)


section2327 = {}
for key in i23.keys():
	if key == "trade":
		section2327[key] = list(set(i23[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section2327[key] = i23[key] + i27[key]


sections.append(section2327)


section2328 = {}
for key in i23.keys():
	if key == "trade":
		section2328[key] = list(set(i23[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section2328[key] = i23[key] + i28[key]


sections.append(section2328)


section2329 = {}
for key in i23.keys():
	if key == "trade":
		section2329[key] = list(set(i23[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section2329[key] = i23[key] + i29[key]


sections.append(section2329)


section2330 = {}
for key in i23.keys():
	if key == "trade":
		section2330[key] = list(set(i23[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section2330[key] = i23[key] + i30[key]


sections.append(section2330)


section2331 = {}
for key in i23.keys():
	if key == "trade":
		section2331[key] = list(set(i23[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section2331[key] = i23[key] + i31[key]


sections.append(section2331)


section2332 = {}
for key in i23.keys():
	if key == "trade":
		section2332[key] = list(set(i23[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section2332[key] = i23[key] + i32[key]


sections.append(section2332)


section2333 = {}
for key in i23.keys():
	if key == "trade":
		section2333[key] = list(set(i23[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section2333[key] = i23[key] + i33[key]


sections.append(section2333)


section2335 = {}
for key in i23.keys():
	if key == "trade":
		section2335[key] = list(set(i23[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section2335[key] = i23[key] + i35[key]


sections.append(section2335)


section2336 = {}
for key in i23.keys():
	if key == "trade":
		section2336[key] = list(set(i23[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section2336[key] = i23[key] + i36[key]


sections.append(section2336)


section2337 = {}
for key in i23.keys():
	if key == "trade":
		section2337[key] = list(set(i23[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section2337[key] = i23[key] + i37[key]


sections.append(section2337)


section2338 = {}
for key in i23.keys():
	if key == "trade":
		section2338[key] = list(set(i23[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section2338[key] = i23[key] + i38[key]


sections.append(section2338)


section2339 = {}
for key in i23.keys():
	if key == "trade":
		section2339[key] = list(set(i23[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section2339[key] = i23[key] + i39[key]


sections.append(section2339)


section2340 = {}
for key in i23.keys():
	if key == "trade":
		section2340[key] = list(set(i23[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section2340[key] = i23[key] + i40[key]


sections.append(section2340)


section2341 = {}
for key in i23.keys():
	if key == "trade":
		section2341[key] = list(set(i23[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section2341[key] = i23[key] + i41[key]


sections.append(section2341)


section2342 = {}
for key in i23.keys():
	if key == "trade":
		section2342[key] = list(set(i23[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section2342[key] = i23[key] + i42[key]


sections.append(section2342)


section2343 = {}
for key in i23.keys():
	if key == "trade":
		section2343[key] = list(set(i23[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section2343[key] = i23[key] + i43[key]


sections.append(section2343)


section2344 = {}
for key in i23.keys():
	if key == "trade":
		section2344[key] = list(set(i23[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section2344[key] = i23[key] + i44[key]


sections.append(section2344)


section2345 = {}
for key in i23.keys():
	if key == "trade":
		section2345[key] = list(set(i23[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section2345[key] = i23[key] + i45[key]


sections.append(section2345)


section2346 = {}
for key in i23.keys():
	if key == "trade":
		section2346[key] = list(set(i23[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section2346[key] = i23[key] + i46[key]


sections.append(section2346)


section2347 = {}
for key in i23.keys():
	if key == "trade":
		section2347[key] = list(set(i23[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section2347[key] = i23[key] + i47[key]


sections.append(section2347)


section2348 = {}
for key in i23.keys():
	if key == "trade":
		section2348[key] = list(set(i23[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section2348[key] = i23[key] + i48[key]


sections.append(section2348)


section2349 = {}
for key in i23.keys():
	if key == "trade":
		section2349[key] = list(set(i23[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section2349[key] = i23[key] + i49[key]


sections.append(section2349)


section2350 = {}
for key in i23.keys():
	if key == "trade":
		section2350[key] = list(set(i23[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section2350[key] = i23[key] + i50[key]


sections.append(section2350)


section2351 = {}
for key in i23.keys():
	if key == "trade":
		section2351[key] = list(set(i23[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section2351[key] = i23[key] + i51[key]


sections.append(section2351)


section2352 = {}
for key in i23.keys():
	if key == "trade":
		section2352[key] = list(set(i23[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section2352[key] = i23[key] + i52[key]


sections.append(section2352)


section2353 = {}
for key in i23.keys():
	if key == "trade":
		section2353[key] = list(set(i23[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section2353[key] = i23[key] + i53[key]


sections.append(section2353)


section2354 = {}
for key in i23.keys():
	if key == "trade":
		section2354[key] = list(set(i23[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section2354[key] = i23[key] + i54[key]


sections.append(section2354)


section2426 = {}
for key in i24.keys():
	if key == "trade":
		section2426[key] = list(set(i24[key] + i26[key]))
	if key == "intersection":
		pass
	else:
		section2426[key] = i24[key] + i26[key]


sections.append(section2426)


section2427 = {}
for key in i24.keys():
	if key == "trade":
		section2427[key] = list(set(i24[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section2427[key] = i24[key] + i27[key]


sections.append(section2427)


section2428 = {}
for key in i24.keys():
	if key == "trade":
		section2428[key] = list(set(i24[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section2428[key] = i24[key] + i28[key]


sections.append(section2428)


section2429 = {}
for key in i24.keys():
	if key == "trade":
		section2429[key] = list(set(i24[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section2429[key] = i24[key] + i29[key]


sections.append(section2429)


section2430 = {}
for key in i24.keys():
	if key == "trade":
		section2430[key] = list(set(i24[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section2430[key] = i24[key] + i30[key]


sections.append(section2430)


section2431 = {}
for key in i24.keys():
	if key == "trade":
		section2431[key] = list(set(i24[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section2431[key] = i24[key] + i31[key]


sections.append(section2431)


section2432 = {}
for key in i24.keys():
	if key == "trade":
		section2432[key] = list(set(i24[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section2432[key] = i24[key] + i32[key]


sections.append(section2432)


section2433 = {}
for key in i24.keys():
	if key == "trade":
		section2433[key] = list(set(i24[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section2433[key] = i24[key] + i33[key]


sections.append(section2433)


section2434 = {}
for key in i24.keys():
	if key == "trade":
		section2434[key] = list(set(i24[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section2434[key] = i24[key] + i34[key]


sections.append(section2434)


section2435 = {}
for key in i24.keys():
	if key == "trade":
		section2435[key] = list(set(i24[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section2435[key] = i24[key] + i35[key]


sections.append(section2435)


section2436 = {}
for key in i24.keys():
	if key == "trade":
		section2436[key] = list(set(i24[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section2436[key] = i24[key] + i36[key]


sections.append(section2436)


section2437 = {}
for key in i24.keys():
	if key == "trade":
		section2437[key] = list(set(i24[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section2437[key] = i24[key] + i37[key]


sections.append(section2437)


section2438 = {}
for key in i24.keys():
	if key == "trade":
		section2438[key] = list(set(i24[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section2438[key] = i24[key] + i38[key]


sections.append(section2438)


section2439 = {}
for key in i24.keys():
	if key == "trade":
		section2439[key] = list(set(i24[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section2439[key] = i24[key] + i39[key]


sections.append(section2439)


section2440 = {}
for key in i24.keys():
	if key == "trade":
		section2440[key] = list(set(i24[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section2440[key] = i24[key] + i40[key]


sections.append(section2440)


section2441 = {}
for key in i24.keys():
	if key == "trade":
		section2441[key] = list(set(i24[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section2441[key] = i24[key] + i41[key]


sections.append(section2441)


section2442 = {}
for key in i24.keys():
	if key == "trade":
		section2442[key] = list(set(i24[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section2442[key] = i24[key] + i42[key]


sections.append(section2442)


section2443 = {}
for key in i24.keys():
	if key == "trade":
		section2443[key] = list(set(i24[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section2443[key] = i24[key] + i43[key]


sections.append(section2443)


section2444 = {}
for key in i24.keys():
	if key == "trade":
		section2444[key] = list(set(i24[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section2444[key] = i24[key] + i44[key]


sections.append(section2444)


section2445 = {}
for key in i24.keys():
	if key == "trade":
		section2445[key] = list(set(i24[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section2445[key] = i24[key] + i45[key]


sections.append(section2445)


section2446 = {}
for key in i24.keys():
	if key == "trade":
		section2446[key] = list(set(i24[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section2446[key] = i24[key] + i46[key]


sections.append(section2446)


section2447 = {}
for key in i24.keys():
	if key == "trade":
		section2447[key] = list(set(i24[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section2447[key] = i24[key] + i47[key]


sections.append(section2447)


section2448 = {}
for key in i24.keys():
	if key == "trade":
		section2448[key] = list(set(i24[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section2448[key] = i24[key] + i48[key]


sections.append(section2448)


section2449 = {}
for key in i24.keys():
	if key == "trade":
		section2449[key] = list(set(i24[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section2449[key] = i24[key] + i49[key]


sections.append(section2449)


section2450 = {}
for key in i24.keys():
	if key == "trade":
		section2450[key] = list(set(i24[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section2450[key] = i24[key] + i50[key]


sections.append(section2450)


section2451 = {}
for key in i24.keys():
	if key == "trade":
		section2451[key] = list(set(i24[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section2451[key] = i24[key] + i51[key]


sections.append(section2451)


section2452 = {}
for key in i24.keys():
	if key == "trade":
		section2452[key] = list(set(i24[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section2452[key] = i24[key] + i52[key]


sections.append(section2452)


section2453 = {}
for key in i24.keys():
	if key == "trade":
		section2453[key] = list(set(i24[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section2453[key] = i24[key] + i53[key]


sections.append(section2453)


section2454 = {}
for key in i24.keys():
	if key == "trade":
		section2454[key] = list(set(i24[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section2454[key] = i24[key] + i54[key]


sections.append(section2454)


section2527 = {}
for key in i25.keys():
	if key == "trade":
		section2527[key] = list(set(i25[key] + i27[key]))
	if key == "intersection":
		pass
	else:
		section2527[key] = i25[key] + i27[key]


sections.append(section2527)


section2528 = {}
for key in i25.keys():
	if key == "trade":
		section2528[key] = list(set(i25[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section2528[key] = i25[key] + i28[key]


sections.append(section2528)


section2529 = {}
for key in i25.keys():
	if key == "trade":
		section2529[key] = list(set(i25[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section2529[key] = i25[key] + i29[key]


sections.append(section2529)


section2530 = {}
for key in i25.keys():
	if key == "trade":
		section2530[key] = list(set(i25[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section2530[key] = i25[key] + i30[key]


sections.append(section2530)


section2531 = {}
for key in i25.keys():
	if key == "trade":
		section2531[key] = list(set(i25[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section2531[key] = i25[key] + i31[key]


sections.append(section2531)


section2532 = {}
for key in i25.keys():
	if key == "trade":
		section2532[key] = list(set(i25[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section2532[key] = i25[key] + i32[key]


sections.append(section2532)


section2533 = {}
for key in i25.keys():
	if key == "trade":
		section2533[key] = list(set(i25[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section2533[key] = i25[key] + i33[key]


sections.append(section2533)


section2534 = {}
for key in i25.keys():
	if key == "trade":
		section2534[key] = list(set(i25[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section2534[key] = i25[key] + i34[key]


sections.append(section2534)


section2536 = {}
for key in i25.keys():
	if key == "trade":
		section2536[key] = list(set(i25[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section2536[key] = i25[key] + i36[key]


sections.append(section2536)


section2537 = {}
for key in i25.keys():
	if key == "trade":
		section2537[key] = list(set(i25[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section2537[key] = i25[key] + i37[key]


sections.append(section2537)


section2538 = {}
for key in i25.keys():
	if key == "trade":
		section2538[key] = list(set(i25[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section2538[key] = i25[key] + i38[key]


sections.append(section2538)


section2539 = {}
for key in i25.keys():
	if key == "trade":
		section2539[key] = list(set(i25[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section2539[key] = i25[key] + i39[key]


sections.append(section2539)


section2540 = {}
for key in i25.keys():
	if key == "trade":
		section2540[key] = list(set(i25[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section2540[key] = i25[key] + i40[key]


sections.append(section2540)


section2541 = {}
for key in i25.keys():
	if key == "trade":
		section2541[key] = list(set(i25[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section2541[key] = i25[key] + i41[key]


sections.append(section2541)


section2542 = {}
for key in i25.keys():
	if key == "trade":
		section2542[key] = list(set(i25[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section2542[key] = i25[key] + i42[key]


sections.append(section2542)


section2543 = {}
for key in i25.keys():
	if key == "trade":
		section2543[key] = list(set(i25[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section2543[key] = i25[key] + i43[key]


sections.append(section2543)


section2544 = {}
for key in i25.keys():
	if key == "trade":
		section2544[key] = list(set(i25[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section2544[key] = i25[key] + i44[key]


sections.append(section2544)


section2545 = {}
for key in i25.keys():
	if key == "trade":
		section2545[key] = list(set(i25[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section2545[key] = i25[key] + i45[key]


sections.append(section2545)


section2546 = {}
for key in i25.keys():
	if key == "trade":
		section2546[key] = list(set(i25[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section2546[key] = i25[key] + i46[key]


sections.append(section2546)


section2547 = {}
for key in i25.keys():
	if key == "trade":
		section2547[key] = list(set(i25[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section2547[key] = i25[key] + i47[key]


sections.append(section2547)


section2548 = {}
for key in i25.keys():
	if key == "trade":
		section2548[key] = list(set(i25[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section2548[key] = i25[key] + i48[key]


sections.append(section2548)


section2549 = {}
for key in i25.keys():
	if key == "trade":
		section2549[key] = list(set(i25[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section2549[key] = i25[key] + i49[key]


sections.append(section2549)


section2550 = {}
for key in i25.keys():
	if key == "trade":
		section2550[key] = list(set(i25[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section2550[key] = i25[key] + i50[key]


sections.append(section2550)


section2551 = {}
for key in i25.keys():
	if key == "trade":
		section2551[key] = list(set(i25[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section2551[key] = i25[key] + i51[key]


sections.append(section2551)


section2552 = {}
for key in i25.keys():
	if key == "trade":
		section2552[key] = list(set(i25[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section2552[key] = i25[key] + i52[key]


sections.append(section2552)


section2553 = {}
for key in i25.keys():
	if key == "trade":
		section2553[key] = list(set(i25[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section2553[key] = i25[key] + i53[key]


sections.append(section2553)


section2554 = {}
for key in i25.keys():
	if key == "trade":
		section2554[key] = list(set(i25[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section2554[key] = i25[key] + i54[key]


sections.append(section2554)


section2628 = {}
for key in i26.keys():
	if key == "trade":
		section2628[key] = list(set(i26[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section2628[key] = i26[key] + i28[key]


sections.append(section2628)


section2629 = {}
for key in i26.keys():
	if key == "trade":
		section2629[key] = list(set(i26[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section2629[key] = i26[key] + i29[key]


sections.append(section2629)


section2630 = {}
for key in i26.keys():
	if key == "trade":
		section2630[key] = list(set(i26[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section2630[key] = i26[key] + i30[key]


sections.append(section2630)


section2631 = {}
for key in i26.keys():
	if key == "trade":
		section2631[key] = list(set(i26[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section2631[key] = i26[key] + i31[key]


sections.append(section2631)


section2632 = {}
for key in i26.keys():
	if key == "trade":
		section2632[key] = list(set(i26[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section2632[key] = i26[key] + i32[key]


sections.append(section2632)


section2633 = {}
for key in i26.keys():
	if key == "trade":
		section2633[key] = list(set(i26[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section2633[key] = i26[key] + i33[key]


sections.append(section2633)


section2634 = {}
for key in i26.keys():
	if key == "trade":
		section2634[key] = list(set(i26[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section2634[key] = i26[key] + i34[key]


sections.append(section2634)


section2635 = {}
for key in i26.keys():
	if key == "trade":
		section2635[key] = list(set(i26[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section2635[key] = i26[key] + i35[key]


sections.append(section2635)


section2636 = {}
for key in i26.keys():
	if key == "trade":
		section2636[key] = list(set(i26[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section2636[key] = i26[key] + i36[key]


sections.append(section2636)


section2637 = {}
for key in i26.keys():
	if key == "trade":
		section2637[key] = list(set(i26[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section2637[key] = i26[key] + i37[key]


sections.append(section2637)


section2638 = {}
for key in i26.keys():
	if key == "trade":
		section2638[key] = list(set(i26[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section2638[key] = i26[key] + i38[key]


sections.append(section2638)


section2639 = {}
for key in i26.keys():
	if key == "trade":
		section2639[key] = list(set(i26[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section2639[key] = i26[key] + i39[key]


sections.append(section2639)


section2640 = {}
for key in i26.keys():
	if key == "trade":
		section2640[key] = list(set(i26[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section2640[key] = i26[key] + i40[key]


sections.append(section2640)


section2641 = {}
for key in i26.keys():
	if key == "trade":
		section2641[key] = list(set(i26[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section2641[key] = i26[key] + i41[key]


sections.append(section2641)


section2642 = {}
for key in i26.keys():
	if key == "trade":
		section2642[key] = list(set(i26[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section2642[key] = i26[key] + i42[key]


sections.append(section2642)


section2643 = {}
for key in i26.keys():
	if key == "trade":
		section2643[key] = list(set(i26[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section2643[key] = i26[key] + i43[key]


sections.append(section2643)


section2644 = {}
for key in i26.keys():
	if key == "trade":
		section2644[key] = list(set(i26[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section2644[key] = i26[key] + i44[key]


sections.append(section2644)


section2645 = {}
for key in i26.keys():
	if key == "trade":
		section2645[key] = list(set(i26[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section2645[key] = i26[key] + i45[key]


sections.append(section2645)


section2646 = {}
for key in i26.keys():
	if key == "trade":
		section2646[key] = list(set(i26[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section2646[key] = i26[key] + i46[key]


sections.append(section2646)


section2647 = {}
for key in i26.keys():
	if key == "trade":
		section2647[key] = list(set(i26[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section2647[key] = i26[key] + i47[key]


sections.append(section2647)


section2648 = {}
for key in i26.keys():
	if key == "trade":
		section2648[key] = list(set(i26[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section2648[key] = i26[key] + i48[key]


sections.append(section2648)


section2649 = {}
for key in i26.keys():
	if key == "trade":
		section2649[key] = list(set(i26[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section2649[key] = i26[key] + i49[key]


sections.append(section2649)


section2650 = {}
for key in i26.keys():
	if key == "trade":
		section2650[key] = list(set(i26[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section2650[key] = i26[key] + i50[key]


sections.append(section2650)


section2651 = {}
for key in i26.keys():
	if key == "trade":
		section2651[key] = list(set(i26[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section2651[key] = i26[key] + i51[key]


sections.append(section2651)


section2652 = {}
for key in i26.keys():
	if key == "trade":
		section2652[key] = list(set(i26[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section2652[key] = i26[key] + i52[key]


sections.append(section2652)


section2653 = {}
for key in i26.keys():
	if key == "trade":
		section2653[key] = list(set(i26[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section2653[key] = i26[key] + i53[key]


sections.append(section2653)


section2654 = {}
for key in i26.keys():
	if key == "trade":
		section2654[key] = list(set(i26[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section2654[key] = i26[key] + i54[key]


sections.append(section2654)


section2728 = {}
for key in i27.keys():
	if key == "trade":
		section2728[key] = list(set(i27[key] + i28[key]))
	if key == "intersection":
		pass
	else:
		section2728[key] = i27[key] + i28[key]


sections.append(section2728)


section2729 = {}
for key in i27.keys():
	if key == "trade":
		section2729[key] = list(set(i27[key] + i29[key]))
	if key == "intersection":
		pass
	else:
		section2729[key] = i27[key] + i29[key]


sections.append(section2729)


section2730 = {}
for key in i27.keys():
	if key == "trade":
		section2730[key] = list(set(i27[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section2730[key] = i27[key] + i30[key]


sections.append(section2730)


section2731 = {}
for key in i27.keys():
	if key == "trade":
		section2731[key] = list(set(i27[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section2731[key] = i27[key] + i31[key]


sections.append(section2731)


section2732 = {}
for key in i27.keys():
	if key == "trade":
		section2732[key] = list(set(i27[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section2732[key] = i27[key] + i32[key]


sections.append(section2732)


section2733 = {}
for key in i27.keys():
	if key == "trade":
		section2733[key] = list(set(i27[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section2733[key] = i27[key] + i33[key]


sections.append(section2733)


section2734 = {}
for key in i27.keys():
	if key == "trade":
		section2734[key] = list(set(i27[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section2734[key] = i27[key] + i34[key]


sections.append(section2734)


section2735 = {}
for key in i27.keys():
	if key == "trade":
		section2735[key] = list(set(i27[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section2735[key] = i27[key] + i35[key]


sections.append(section2735)


section2736 = {}
for key in i27.keys():
	if key == "trade":
		section2736[key] = list(set(i27[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section2736[key] = i27[key] + i36[key]


sections.append(section2736)


section2737 = {}
for key in i27.keys():
	if key == "trade":
		section2737[key] = list(set(i27[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section2737[key] = i27[key] + i37[key]


sections.append(section2737)


section2739 = {}
for key in i27.keys():
	if key == "trade":
		section2739[key] = list(set(i27[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section2739[key] = i27[key] + i39[key]


sections.append(section2739)


section2740 = {}
for key in i27.keys():
	if key == "trade":
		section2740[key] = list(set(i27[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section2740[key] = i27[key] + i40[key]


sections.append(section2740)


section2741 = {}
for key in i27.keys():
	if key == "trade":
		section2741[key] = list(set(i27[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section2741[key] = i27[key] + i41[key]


sections.append(section2741)


section2742 = {}
for key in i27.keys():
	if key == "trade":
		section2742[key] = list(set(i27[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section2742[key] = i27[key] + i42[key]


sections.append(section2742)


section2743 = {}
for key in i27.keys():
	if key == "trade":
		section2743[key] = list(set(i27[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section2743[key] = i27[key] + i43[key]


sections.append(section2743)


section2744 = {}
for key in i27.keys():
	if key == "trade":
		section2744[key] = list(set(i27[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section2744[key] = i27[key] + i44[key]


sections.append(section2744)


section2745 = {}
for key in i27.keys():
	if key == "trade":
		section2745[key] = list(set(i27[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section2745[key] = i27[key] + i45[key]


sections.append(section2745)


section2746 = {}
for key in i27.keys():
	if key == "trade":
		section2746[key] = list(set(i27[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section2746[key] = i27[key] + i46[key]


sections.append(section2746)


section2747 = {}
for key in i27.keys():
	if key == "trade":
		section2747[key] = list(set(i27[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section2747[key] = i27[key] + i47[key]


sections.append(section2747)


section2748 = {}
for key in i27.keys():
	if key == "trade":
		section2748[key] = list(set(i27[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section2748[key] = i27[key] + i48[key]


sections.append(section2748)


section2749 = {}
for key in i27.keys():
	if key == "trade":
		section2749[key] = list(set(i27[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section2749[key] = i27[key] + i49[key]


sections.append(section2749)


section2750 = {}
for key in i27.keys():
	if key == "trade":
		section2750[key] = list(set(i27[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section2750[key] = i27[key] + i50[key]


sections.append(section2750)


section2751 = {}
for key in i27.keys():
	if key == "trade":
		section2751[key] = list(set(i27[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section2751[key] = i27[key] + i51[key]


sections.append(section2751)


section2752 = {}
for key in i27.keys():
	if key == "trade":
		section2752[key] = list(set(i27[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section2752[key] = i27[key] + i52[key]


sections.append(section2752)


section2753 = {}
for key in i27.keys():
	if key == "trade":
		section2753[key] = list(set(i27[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section2753[key] = i27[key] + i53[key]


sections.append(section2753)


section2754 = {}
for key in i27.keys():
	if key == "trade":
		section2754[key] = list(set(i27[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section2754[key] = i27[key] + i54[key]


sections.append(section2754)


section2830 = {}
for key in i28.keys():
	if key == "trade":
		section2830[key] = list(set(i28[key] + i30[key]))
	if key == "intersection":
		pass
	else:
		section2830[key] = i28[key] + i30[key]


sections.append(section2830)


section2831 = {}
for key in i28.keys():
	if key == "trade":
		section2831[key] = list(set(i28[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section2831[key] = i28[key] + i31[key]


sections.append(section2831)


section2832 = {}
for key in i28.keys():
	if key == "trade":
		section2832[key] = list(set(i28[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section2832[key] = i28[key] + i32[key]


sections.append(section2832)


section2833 = {}
for key in i28.keys():
	if key == "trade":
		section2833[key] = list(set(i28[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section2833[key] = i28[key] + i33[key]


sections.append(section2833)


section2834 = {}
for key in i28.keys():
	if key == "trade":
		section2834[key] = list(set(i28[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section2834[key] = i28[key] + i34[key]


sections.append(section2834)


section2835 = {}
for key in i28.keys():
	if key == "trade":
		section2835[key] = list(set(i28[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section2835[key] = i28[key] + i35[key]


sections.append(section2835)


section2836 = {}
for key in i28.keys():
	if key == "trade":
		section2836[key] = list(set(i28[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section2836[key] = i28[key] + i36[key]


sections.append(section2836)


section2837 = {}
for key in i28.keys():
	if key == "trade":
		section2837[key] = list(set(i28[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section2837[key] = i28[key] + i37[key]


sections.append(section2837)


section2838 = {}
for key in i28.keys():
	if key == "trade":
		section2838[key] = list(set(i28[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section2838[key] = i28[key] + i38[key]


sections.append(section2838)


section2839 = {}
for key in i28.keys():
	if key == "trade":
		section2839[key] = list(set(i28[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section2839[key] = i28[key] + i39[key]


sections.append(section2839)


section2840 = {}
for key in i28.keys():
	if key == "trade":
		section2840[key] = list(set(i28[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section2840[key] = i28[key] + i40[key]


sections.append(section2840)


section2841 = {}
for key in i28.keys():
	if key == "trade":
		section2841[key] = list(set(i28[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section2841[key] = i28[key] + i41[key]


sections.append(section2841)


section2842 = {}
for key in i28.keys():
	if key == "trade":
		section2842[key] = list(set(i28[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section2842[key] = i28[key] + i42[key]


sections.append(section2842)


section2843 = {}
for key in i28.keys():
	if key == "trade":
		section2843[key] = list(set(i28[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section2843[key] = i28[key] + i43[key]


sections.append(section2843)


section2844 = {}
for key in i28.keys():
	if key == "trade":
		section2844[key] = list(set(i28[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section2844[key] = i28[key] + i44[key]


sections.append(section2844)


section2845 = {}
for key in i28.keys():
	if key == "trade":
		section2845[key] = list(set(i28[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section2845[key] = i28[key] + i45[key]


sections.append(section2845)


section2846 = {}
for key in i28.keys():
	if key == "trade":
		section2846[key] = list(set(i28[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section2846[key] = i28[key] + i46[key]


sections.append(section2846)


section2847 = {}
for key in i28.keys():
	if key == "trade":
		section2847[key] = list(set(i28[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section2847[key] = i28[key] + i47[key]


sections.append(section2847)


section2848 = {}
for key in i28.keys():
	if key == "trade":
		section2848[key] = list(set(i28[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section2848[key] = i28[key] + i48[key]


sections.append(section2848)


section2849 = {}
for key in i28.keys():
	if key == "trade":
		section2849[key] = list(set(i28[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section2849[key] = i28[key] + i49[key]


sections.append(section2849)


section2850 = {}
for key in i28.keys():
	if key == "trade":
		section2850[key] = list(set(i28[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section2850[key] = i28[key] + i50[key]


sections.append(section2850)


section2851 = {}
for key in i28.keys():
	if key == "trade":
		section2851[key] = list(set(i28[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section2851[key] = i28[key] + i51[key]


sections.append(section2851)


section2852 = {}
for key in i28.keys():
	if key == "trade":
		section2852[key] = list(set(i28[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section2852[key] = i28[key] + i52[key]


sections.append(section2852)


section2853 = {}
for key in i28.keys():
	if key == "trade":
		section2853[key] = list(set(i28[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section2853[key] = i28[key] + i53[key]


sections.append(section2853)


section2854 = {}
for key in i28.keys():
	if key == "trade":
		section2854[key] = list(set(i28[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section2854[key] = i28[key] + i54[key]


sections.append(section2854)


section2931 = {}
for key in i29.keys():
	if key == "trade":
		section2931[key] = list(set(i29[key] + i31[key]))
	if key == "intersection":
		pass
	else:
		section2931[key] = i29[key] + i31[key]


sections.append(section2931)


section2932 = {}
for key in i29.keys():
	if key == "trade":
		section2932[key] = list(set(i29[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section2932[key] = i29[key] + i32[key]


sections.append(section2932)


section2933 = {}
for key in i29.keys():
	if key == "trade":
		section2933[key] = list(set(i29[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section2933[key] = i29[key] + i33[key]


sections.append(section2933)


section2934 = {}
for key in i29.keys():
	if key == "trade":
		section2934[key] = list(set(i29[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section2934[key] = i29[key] + i34[key]


sections.append(section2934)


section2935 = {}
for key in i29.keys():
	if key == "trade":
		section2935[key] = list(set(i29[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section2935[key] = i29[key] + i35[key]


sections.append(section2935)


section2936 = {}
for key in i29.keys():
	if key == "trade":
		section2936[key] = list(set(i29[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section2936[key] = i29[key] + i36[key]


sections.append(section2936)


section2937 = {}
for key in i29.keys():
	if key == "trade":
		section2937[key] = list(set(i29[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section2937[key] = i29[key] + i37[key]


sections.append(section2937)


section2938 = {}
for key in i29.keys():
	if key == "trade":
		section2938[key] = list(set(i29[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section2938[key] = i29[key] + i38[key]


sections.append(section2938)


section2940 = {}
for key in i29.keys():
	if key == "trade":
		section2940[key] = list(set(i29[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section2940[key] = i29[key] + i40[key]


sections.append(section2940)


section2941 = {}
for key in i29.keys():
	if key == "trade":
		section2941[key] = list(set(i29[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section2941[key] = i29[key] + i41[key]


sections.append(section2941)


section2942 = {}
for key in i29.keys():
	if key == "trade":
		section2942[key] = list(set(i29[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section2942[key] = i29[key] + i42[key]


sections.append(section2942)


section2943 = {}
for key in i29.keys():
	if key == "trade":
		section2943[key] = list(set(i29[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section2943[key] = i29[key] + i43[key]


sections.append(section2943)


section2944 = {}
for key in i29.keys():
	if key == "trade":
		section2944[key] = list(set(i29[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section2944[key] = i29[key] + i44[key]


sections.append(section2944)


section2945 = {}
for key in i29.keys():
	if key == "trade":
		section2945[key] = list(set(i29[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section2945[key] = i29[key] + i45[key]


sections.append(section2945)


section2946 = {}
for key in i29.keys():
	if key == "trade":
		section2946[key] = list(set(i29[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section2946[key] = i29[key] + i46[key]


sections.append(section2946)


section2947 = {}
for key in i29.keys():
	if key == "trade":
		section2947[key] = list(set(i29[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section2947[key] = i29[key] + i47[key]


sections.append(section2947)


section2948 = {}
for key in i29.keys():
	if key == "trade":
		section2948[key] = list(set(i29[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section2948[key] = i29[key] + i48[key]


sections.append(section2948)


section2949 = {}
for key in i29.keys():
	if key == "trade":
		section2949[key] = list(set(i29[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section2949[key] = i29[key] + i49[key]


sections.append(section2949)


section2950 = {}
for key in i29.keys():
	if key == "trade":
		section2950[key] = list(set(i29[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section2950[key] = i29[key] + i50[key]


sections.append(section2950)


section2951 = {}
for key in i29.keys():
	if key == "trade":
		section2951[key] = list(set(i29[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section2951[key] = i29[key] + i51[key]


sections.append(section2951)


section2952 = {}
for key in i29.keys():
	if key == "trade":
		section2952[key] = list(set(i29[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section2952[key] = i29[key] + i52[key]


sections.append(section2952)


section2953 = {}
for key in i29.keys():
	if key == "trade":
		section2953[key] = list(set(i29[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section2953[key] = i29[key] + i53[key]


sections.append(section2953)


section2954 = {}
for key in i29.keys():
	if key == "trade":
		section2954[key] = list(set(i29[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section2954[key] = i29[key] + i54[key]


sections.append(section2954)


section3032 = {}
for key in i30.keys():
	if key == "trade":
		section3032[key] = list(set(i30[key] + i32[key]))
	if key == "intersection":
		pass
	else:
		section3032[key] = i30[key] + i32[key]


sections.append(section3032)


section3033 = {}
for key in i30.keys():
	if key == "trade":
		section3033[key] = list(set(i30[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section3033[key] = i30[key] + i33[key]


sections.append(section3033)


section3034 = {}
for key in i30.keys():
	if key == "trade":
		section3034[key] = list(set(i30[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section3034[key] = i30[key] + i34[key]


sections.append(section3034)


section3035 = {}
for key in i30.keys():
	if key == "trade":
		section3035[key] = list(set(i30[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section3035[key] = i30[key] + i35[key]


sections.append(section3035)


section3036 = {}
for key in i30.keys():
	if key == "trade":
		section3036[key] = list(set(i30[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section3036[key] = i30[key] + i36[key]


sections.append(section3036)


section3037 = {}
for key in i30.keys():
	if key == "trade":
		section3037[key] = list(set(i30[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section3037[key] = i30[key] + i37[key]


sections.append(section3037)


section3038 = {}
for key in i30.keys():
	if key == "trade":
		section3038[key] = list(set(i30[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section3038[key] = i30[key] + i38[key]


sections.append(section3038)


section3039 = {}
for key in i30.keys():
	if key == "trade":
		section3039[key] = list(set(i30[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section3039[key] = i30[key] + i39[key]


sections.append(section3039)


section3040 = {}
for key in i30.keys():
	if key == "trade":
		section3040[key] = list(set(i30[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section3040[key] = i30[key] + i40[key]


sections.append(section3040)


section3041 = {}
for key in i30.keys():
	if key == "trade":
		section3041[key] = list(set(i30[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section3041[key] = i30[key] + i41[key]


sections.append(section3041)


section3042 = {}
for key in i30.keys():
	if key == "trade":
		section3042[key] = list(set(i30[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section3042[key] = i30[key] + i42[key]


sections.append(section3042)


section3043 = {}
for key in i30.keys():
	if key == "trade":
		section3043[key] = list(set(i30[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section3043[key] = i30[key] + i43[key]


sections.append(section3043)


section3044 = {}
for key in i30.keys():
	if key == "trade":
		section3044[key] = list(set(i30[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section3044[key] = i30[key] + i44[key]


sections.append(section3044)


section3045 = {}
for key in i30.keys():
	if key == "trade":
		section3045[key] = list(set(i30[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section3045[key] = i30[key] + i45[key]


sections.append(section3045)


section3046 = {}
for key in i30.keys():
	if key == "trade":
		section3046[key] = list(set(i30[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section3046[key] = i30[key] + i46[key]


sections.append(section3046)


section3047 = {}
for key in i30.keys():
	if key == "trade":
		section3047[key] = list(set(i30[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section3047[key] = i30[key] + i47[key]


sections.append(section3047)


section3048 = {}
for key in i30.keys():
	if key == "trade":
		section3048[key] = list(set(i30[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section3048[key] = i30[key] + i48[key]


sections.append(section3048)


section3049 = {}
for key in i30.keys():
	if key == "trade":
		section3049[key] = list(set(i30[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section3049[key] = i30[key] + i49[key]


sections.append(section3049)


section3050 = {}
for key in i30.keys():
	if key == "trade":
		section3050[key] = list(set(i30[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section3050[key] = i30[key] + i50[key]


sections.append(section3050)


section3051 = {}
for key in i30.keys():
	if key == "trade":
		section3051[key] = list(set(i30[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section3051[key] = i30[key] + i51[key]


sections.append(section3051)


section3052 = {}
for key in i30.keys():
	if key == "trade":
		section3052[key] = list(set(i30[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section3052[key] = i30[key] + i52[key]


sections.append(section3052)


section3053 = {}
for key in i30.keys():
	if key == "trade":
		section3053[key] = list(set(i30[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section3053[key] = i30[key] + i53[key]


sections.append(section3053)


section3054 = {}
for key in i30.keys():
	if key == "trade":
		section3054[key] = list(set(i30[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section3054[key] = i30[key] + i54[key]


sections.append(section3054)


section3133 = {}
for key in i31.keys():
	if key == "trade":
		section3133[key] = list(set(i31[key] + i33[key]))
	if key == "intersection":
		pass
	else:
		section3133[key] = i31[key] + i33[key]


sections.append(section3133)


section3134 = {}
for key in i31.keys():
	if key == "trade":
		section3134[key] = list(set(i31[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section3134[key] = i31[key] + i34[key]


sections.append(section3134)


section3135 = {}
for key in i31.keys():
	if key == "trade":
		section3135[key] = list(set(i31[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section3135[key] = i31[key] + i35[key]


sections.append(section3135)


section3136 = {}
for key in i31.keys():
	if key == "trade":
		section3136[key] = list(set(i31[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section3136[key] = i31[key] + i36[key]


sections.append(section3136)


section3137 = {}
for key in i31.keys():
	if key == "trade":
		section3137[key] = list(set(i31[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section3137[key] = i31[key] + i37[key]


sections.append(section3137)


section3138 = {}
for key in i31.keys():
	if key == "trade":
		section3138[key] = list(set(i31[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section3138[key] = i31[key] + i38[key]


sections.append(section3138)


section3139 = {}
for key in i31.keys():
	if key == "trade":
		section3139[key] = list(set(i31[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section3139[key] = i31[key] + i39[key]


sections.append(section3139)


section3140 = {}
for key in i31.keys():
	if key == "trade":
		section3140[key] = list(set(i31[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section3140[key] = i31[key] + i40[key]


sections.append(section3140)


section3142 = {}
for key in i31.keys():
	if key == "trade":
		section3142[key] = list(set(i31[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section3142[key] = i31[key] + i42[key]


sections.append(section3142)


section3143 = {}
for key in i31.keys():
	if key == "trade":
		section3143[key] = list(set(i31[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section3143[key] = i31[key] + i43[key]


sections.append(section3143)


section3144 = {}
for key in i31.keys():
	if key == "trade":
		section3144[key] = list(set(i31[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section3144[key] = i31[key] + i44[key]


sections.append(section3144)


section3145 = {}
for key in i31.keys():
	if key == "trade":
		section3145[key] = list(set(i31[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section3145[key] = i31[key] + i45[key]


sections.append(section3145)


section3146 = {}
for key in i31.keys():
	if key == "trade":
		section3146[key] = list(set(i31[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section3146[key] = i31[key] + i46[key]


sections.append(section3146)


section3147 = {}
for key in i31.keys():
	if key == "trade":
		section3147[key] = list(set(i31[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section3147[key] = i31[key] + i47[key]


sections.append(section3147)


section3148 = {}
for key in i31.keys():
	if key == "trade":
		section3148[key] = list(set(i31[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section3148[key] = i31[key] + i48[key]


sections.append(section3148)


section3149 = {}
for key in i31.keys():
	if key == "trade":
		section3149[key] = list(set(i31[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section3149[key] = i31[key] + i49[key]


sections.append(section3149)


section3150 = {}
for key in i31.keys():
	if key == "trade":
		section3150[key] = list(set(i31[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section3150[key] = i31[key] + i50[key]


sections.append(section3150)


section3151 = {}
for key in i31.keys():
	if key == "trade":
		section3151[key] = list(set(i31[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section3151[key] = i31[key] + i51[key]


sections.append(section3151)


section3152 = {}
for key in i31.keys():
	if key == "trade":
		section3152[key] = list(set(i31[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section3152[key] = i31[key] + i52[key]


sections.append(section3152)


section3153 = {}
for key in i31.keys():
	if key == "trade":
		section3153[key] = list(set(i31[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section3153[key] = i31[key] + i53[key]


sections.append(section3153)


section3154 = {}
for key in i31.keys():
	if key == "trade":
		section3154[key] = list(set(i31[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section3154[key] = i31[key] + i54[key]


sections.append(section3154)


section3234 = {}
for key in i32.keys():
	if key == "trade":
		section3234[key] = list(set(i32[key] + i34[key]))
	if key == "intersection":
		pass
	else:
		section3234[key] = i32[key] + i34[key]


sections.append(section3234)


section3235 = {}
for key in i32.keys():
	if key == "trade":
		section3235[key] = list(set(i32[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section3235[key] = i32[key] + i35[key]


sections.append(section3235)


section3236 = {}
for key in i32.keys():
	if key == "trade":
		section3236[key] = list(set(i32[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section3236[key] = i32[key] + i36[key]


sections.append(section3236)


section3237 = {}
for key in i32.keys():
	if key == "trade":
		section3237[key] = list(set(i32[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section3237[key] = i32[key] + i37[key]


sections.append(section3237)


section3238 = {}
for key in i32.keys():
	if key == "trade":
		section3238[key] = list(set(i32[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section3238[key] = i32[key] + i38[key]


sections.append(section3238)


section3239 = {}
for key in i32.keys():
	if key == "trade":
		section3239[key] = list(set(i32[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section3239[key] = i32[key] + i39[key]


sections.append(section3239)


section3240 = {}
for key in i32.keys():
	if key == "trade":
		section3240[key] = list(set(i32[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section3240[key] = i32[key] + i40[key]


sections.append(section3240)


section3241 = {}
for key in i32.keys():
	if key == "trade":
		section3241[key] = list(set(i32[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section3241[key] = i32[key] + i41[key]


sections.append(section3241)


section3242 = {}
for key in i32.keys():
	if key == "trade":
		section3242[key] = list(set(i32[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section3242[key] = i32[key] + i42[key]


sections.append(section3242)


section3243 = {}
for key in i32.keys():
	if key == "trade":
		section3243[key] = list(set(i32[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section3243[key] = i32[key] + i43[key]


sections.append(section3243)


section3244 = {}
for key in i32.keys():
	if key == "trade":
		section3244[key] = list(set(i32[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section3244[key] = i32[key] + i44[key]


sections.append(section3244)


section3245 = {}
for key in i32.keys():
	if key == "trade":
		section3245[key] = list(set(i32[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section3245[key] = i32[key] + i45[key]


sections.append(section3245)


section3246 = {}
for key in i32.keys():
	if key == "trade":
		section3246[key] = list(set(i32[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section3246[key] = i32[key] + i46[key]


sections.append(section3246)


section3247 = {}
for key in i32.keys():
	if key == "trade":
		section3247[key] = list(set(i32[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section3247[key] = i32[key] + i47[key]


sections.append(section3247)


section3248 = {}
for key in i32.keys():
	if key == "trade":
		section3248[key] = list(set(i32[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section3248[key] = i32[key] + i48[key]


sections.append(section3248)


section3249 = {}
for key in i32.keys():
	if key == "trade":
		section3249[key] = list(set(i32[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section3249[key] = i32[key] + i49[key]


sections.append(section3249)


section3250 = {}
for key in i32.keys():
	if key == "trade":
		section3250[key] = list(set(i32[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section3250[key] = i32[key] + i50[key]


sections.append(section3250)


section3251 = {}
for key in i32.keys():
	if key == "trade":
		section3251[key] = list(set(i32[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section3251[key] = i32[key] + i51[key]


sections.append(section3251)


section3252 = {}
for key in i32.keys():
	if key == "trade":
		section3252[key] = list(set(i32[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section3252[key] = i32[key] + i52[key]


sections.append(section3252)


section3253 = {}
for key in i32.keys():
	if key == "trade":
		section3253[key] = list(set(i32[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section3253[key] = i32[key] + i53[key]


sections.append(section3253)


section3254 = {}
for key in i32.keys():
	if key == "trade":
		section3254[key] = list(set(i32[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section3254[key] = i32[key] + i54[key]


sections.append(section3254)


section3335 = {}
for key in i33.keys():
	if key == "trade":
		section3335[key] = list(set(i33[key] + i35[key]))
	if key == "intersection":
		pass
	else:
		section3335[key] = i33[key] + i35[key]


sections.append(section3335)


section3336 = {}
for key in i33.keys():
	if key == "trade":
		section3336[key] = list(set(i33[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section3336[key] = i33[key] + i36[key]


sections.append(section3336)


section3337 = {}
for key in i33.keys():
	if key == "trade":
		section3337[key] = list(set(i33[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section3337[key] = i33[key] + i37[key]


sections.append(section3337)


section3338 = {}
for key in i33.keys():
	if key == "trade":
		section3338[key] = list(set(i33[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section3338[key] = i33[key] + i38[key]


sections.append(section3338)


section3339 = {}
for key in i33.keys():
	if key == "trade":
		section3339[key] = list(set(i33[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section3339[key] = i33[key] + i39[key]


sections.append(section3339)


section3340 = {}
for key in i33.keys():
	if key == "trade":
		section3340[key] = list(set(i33[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section3340[key] = i33[key] + i40[key]


sections.append(section3340)


section3341 = {}
for key in i33.keys():
	if key == "trade":
		section3341[key] = list(set(i33[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section3341[key] = i33[key] + i41[key]


sections.append(section3341)


section3342 = {}
for key in i33.keys():
	if key == "trade":
		section3342[key] = list(set(i33[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section3342[key] = i33[key] + i42[key]


sections.append(section3342)


section3344 = {}
for key in i33.keys():
	if key == "trade":
		section3344[key] = list(set(i33[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section3344[key] = i33[key] + i44[key]


sections.append(section3344)


section3345 = {}
for key in i33.keys():
	if key == "trade":
		section3345[key] = list(set(i33[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section3345[key] = i33[key] + i45[key]


sections.append(section3345)


section3346 = {}
for key in i33.keys():
	if key == "trade":
		section3346[key] = list(set(i33[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section3346[key] = i33[key] + i46[key]


sections.append(section3346)


section3347 = {}
for key in i33.keys():
	if key == "trade":
		section3347[key] = list(set(i33[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section3347[key] = i33[key] + i47[key]


sections.append(section3347)


section3348 = {}
for key in i33.keys():
	if key == "trade":
		section3348[key] = list(set(i33[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section3348[key] = i33[key] + i48[key]


sections.append(section3348)


section3349 = {}
for key in i33.keys():
	if key == "trade":
		section3349[key] = list(set(i33[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section3349[key] = i33[key] + i49[key]


sections.append(section3349)


section3350 = {}
for key in i33.keys():
	if key == "trade":
		section3350[key] = list(set(i33[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section3350[key] = i33[key] + i50[key]


sections.append(section3350)


section3351 = {}
for key in i33.keys():
	if key == "trade":
		section3351[key] = list(set(i33[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section3351[key] = i33[key] + i51[key]


sections.append(section3351)


section3352 = {}
for key in i33.keys():
	if key == "trade":
		section3352[key] = list(set(i33[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section3352[key] = i33[key] + i52[key]


sections.append(section3352)


section3353 = {}
for key in i33.keys():
	if key == "trade":
		section3353[key] = list(set(i33[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section3353[key] = i33[key] + i53[key]


sections.append(section3353)


section3354 = {}
for key in i33.keys():
	if key == "trade":
		section3354[key] = list(set(i33[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section3354[key] = i33[key] + i54[key]


sections.append(section3354)


section3436 = {}
for key in i34.keys():
	if key == "trade":
		section3436[key] = list(set(i34[key] + i36[key]))
	if key == "intersection":
		pass
	else:
		section3436[key] = i34[key] + i36[key]


sections.append(section3436)


section3437 = {}
for key in i34.keys():
	if key == "trade":
		section3437[key] = list(set(i34[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section3437[key] = i34[key] + i37[key]


sections.append(section3437)


section3438 = {}
for key in i34.keys():
	if key == "trade":
		section3438[key] = list(set(i34[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section3438[key] = i34[key] + i38[key]


sections.append(section3438)


section3439 = {}
for key in i34.keys():
	if key == "trade":
		section3439[key] = list(set(i34[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section3439[key] = i34[key] + i39[key]


sections.append(section3439)


section3440 = {}
for key in i34.keys():
	if key == "trade":
		section3440[key] = list(set(i34[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section3440[key] = i34[key] + i40[key]


sections.append(section3440)


section3441 = {}
for key in i34.keys():
	if key == "trade":
		section3441[key] = list(set(i34[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section3441[key] = i34[key] + i41[key]


sections.append(section3441)


section3442 = {}
for key in i34.keys():
	if key == "trade":
		section3442[key] = list(set(i34[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section3442[key] = i34[key] + i42[key]


sections.append(section3442)


section3443 = {}
for key in i34.keys():
	if key == "trade":
		section3443[key] = list(set(i34[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section3443[key] = i34[key] + i43[key]


sections.append(section3443)


section3444 = {}
for key in i34.keys():
	if key == "trade":
		section3444[key] = list(set(i34[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section3444[key] = i34[key] + i44[key]


sections.append(section3444)


section3445 = {}
for key in i34.keys():
	if key == "trade":
		section3445[key] = list(set(i34[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section3445[key] = i34[key] + i45[key]


sections.append(section3445)


section3446 = {}
for key in i34.keys():
	if key == "trade":
		section3446[key] = list(set(i34[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section3446[key] = i34[key] + i46[key]


sections.append(section3446)


section3447 = {}
for key in i34.keys():
	if key == "trade":
		section3447[key] = list(set(i34[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section3447[key] = i34[key] + i47[key]


sections.append(section3447)


section3448 = {}
for key in i34.keys():
	if key == "trade":
		section3448[key] = list(set(i34[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section3448[key] = i34[key] + i48[key]


sections.append(section3448)


section3449 = {}
for key in i34.keys():
	if key == "trade":
		section3449[key] = list(set(i34[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section3449[key] = i34[key] + i49[key]


sections.append(section3449)


section3450 = {}
for key in i34.keys():
	if key == "trade":
		section3450[key] = list(set(i34[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section3450[key] = i34[key] + i50[key]


sections.append(section3450)


section3451 = {}
for key in i34.keys():
	if key == "trade":
		section3451[key] = list(set(i34[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section3451[key] = i34[key] + i51[key]


sections.append(section3451)


section3452 = {}
for key in i34.keys():
	if key == "trade":
		section3452[key] = list(set(i34[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section3452[key] = i34[key] + i52[key]


sections.append(section3452)


section3453 = {}
for key in i34.keys():
	if key == "trade":
		section3453[key] = list(set(i34[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section3453[key] = i34[key] + i53[key]


sections.append(section3453)


section3454 = {}
for key in i34.keys():
	if key == "trade":
		section3454[key] = list(set(i34[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section3454[key] = i34[key] + i54[key]


sections.append(section3454)


section3537 = {}
for key in i35.keys():
	if key == "trade":
		section3537[key] = list(set(i35[key] + i37[key]))
	if key == "intersection":
		pass
	else:
		section3537[key] = i35[key] + i37[key]


sections.append(section3537)


section3538 = {}
for key in i35.keys():
	if key == "trade":
		section3538[key] = list(set(i35[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section3538[key] = i35[key] + i38[key]


sections.append(section3538)


section3539 = {}
for key in i35.keys():
	if key == "trade":
		section3539[key] = list(set(i35[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section3539[key] = i35[key] + i39[key]


sections.append(section3539)


section3540 = {}
for key in i35.keys():
	if key == "trade":
		section3540[key] = list(set(i35[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section3540[key] = i35[key] + i40[key]


sections.append(section3540)


section3541 = {}
for key in i35.keys():
	if key == "trade":
		section3541[key] = list(set(i35[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section3541[key] = i35[key] + i41[key]


sections.append(section3541)


section3542 = {}
for key in i35.keys():
	if key == "trade":
		section3542[key] = list(set(i35[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section3542[key] = i35[key] + i42[key]


sections.append(section3542)


section3543 = {}
for key in i35.keys():
	if key == "trade":
		section3543[key] = list(set(i35[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section3543[key] = i35[key] + i43[key]


sections.append(section3543)


section3544 = {}
for key in i35.keys():
	if key == "trade":
		section3544[key] = list(set(i35[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section3544[key] = i35[key] + i44[key]


sections.append(section3544)


section3546 = {}
for key in i35.keys():
	if key == "trade":
		section3546[key] = list(set(i35[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section3546[key] = i35[key] + i46[key]


sections.append(section3546)


section3547 = {}
for key in i35.keys():
	if key == "trade":
		section3547[key] = list(set(i35[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section3547[key] = i35[key] + i47[key]


sections.append(section3547)


section3548 = {}
for key in i35.keys():
	if key == "trade":
		section3548[key] = list(set(i35[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section3548[key] = i35[key] + i48[key]


sections.append(section3548)


section3549 = {}
for key in i35.keys():
	if key == "trade":
		section3549[key] = list(set(i35[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section3549[key] = i35[key] + i49[key]


sections.append(section3549)


section3550 = {}
for key in i35.keys():
	if key == "trade":
		section3550[key] = list(set(i35[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section3550[key] = i35[key] + i50[key]


sections.append(section3550)


section3551 = {}
for key in i35.keys():
	if key == "trade":
		section3551[key] = list(set(i35[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section3551[key] = i35[key] + i51[key]


sections.append(section3551)


section3552 = {}
for key in i35.keys():
	if key == "trade":
		section3552[key] = list(set(i35[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section3552[key] = i35[key] + i52[key]


sections.append(section3552)


section3553 = {}
for key in i35.keys():
	if key == "trade":
		section3553[key] = list(set(i35[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section3553[key] = i35[key] + i53[key]


sections.append(section3553)


section3554 = {}
for key in i35.keys():
	if key == "trade":
		section3554[key] = list(set(i35[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section3554[key] = i35[key] + i54[key]


sections.append(section3554)


section3638 = {}
for key in i36.keys():
	if key == "trade":
		section3638[key] = list(set(i36[key] + i38[key]))
	if key == "intersection":
		pass
	else:
		section3638[key] = i36[key] + i38[key]


sections.append(section3638)


section3639 = {}
for key in i36.keys():
	if key == "trade":
		section3639[key] = list(set(i36[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section3639[key] = i36[key] + i39[key]


sections.append(section3639)


section3640 = {}
for key in i36.keys():
	if key == "trade":
		section3640[key] = list(set(i36[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section3640[key] = i36[key] + i40[key]


sections.append(section3640)


section3641 = {}
for key in i36.keys():
	if key == "trade":
		section3641[key] = list(set(i36[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section3641[key] = i36[key] + i41[key]


sections.append(section3641)


section3642 = {}
for key in i36.keys():
	if key == "trade":
		section3642[key] = list(set(i36[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section3642[key] = i36[key] + i42[key]


sections.append(section3642)


section3643 = {}
for key in i36.keys():
	if key == "trade":
		section3643[key] = list(set(i36[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section3643[key] = i36[key] + i43[key]


sections.append(section3643)


section3644 = {}
for key in i36.keys():
	if key == "trade":
		section3644[key] = list(set(i36[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section3644[key] = i36[key] + i44[key]


sections.append(section3644)


section3645 = {}
for key in i36.keys():
	if key == "trade":
		section3645[key] = list(set(i36[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section3645[key] = i36[key] + i45[key]


sections.append(section3645)


section3646 = {}
for key in i36.keys():
	if key == "trade":
		section3646[key] = list(set(i36[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section3646[key] = i36[key] + i46[key]


sections.append(section3646)


section3647 = {}
for key in i36.keys():
	if key == "trade":
		section3647[key] = list(set(i36[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section3647[key] = i36[key] + i47[key]


sections.append(section3647)


section3648 = {}
for key in i36.keys():
	if key == "trade":
		section3648[key] = list(set(i36[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section3648[key] = i36[key] + i48[key]


sections.append(section3648)


section3649 = {}
for key in i36.keys():
	if key == "trade":
		section3649[key] = list(set(i36[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section3649[key] = i36[key] + i49[key]


sections.append(section3649)


section3650 = {}
for key in i36.keys():
	if key == "trade":
		section3650[key] = list(set(i36[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section3650[key] = i36[key] + i50[key]


sections.append(section3650)


section3651 = {}
for key in i36.keys():
	if key == "trade":
		section3651[key] = list(set(i36[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section3651[key] = i36[key] + i51[key]


sections.append(section3651)


section3652 = {}
for key in i36.keys():
	if key == "trade":
		section3652[key] = list(set(i36[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section3652[key] = i36[key] + i52[key]


sections.append(section3652)


section3653 = {}
for key in i36.keys():
	if key == "trade":
		section3653[key] = list(set(i36[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section3653[key] = i36[key] + i53[key]


sections.append(section3653)


section3654 = {}
for key in i36.keys():
	if key == "trade":
		section3654[key] = list(set(i36[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section3654[key] = i36[key] + i54[key]


sections.append(section3654)


section3739 = {}
for key in i37.keys():
	if key == "trade":
		section3739[key] = list(set(i37[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section3739[key] = i37[key] + i39[key]


sections.append(section3739)


section3740 = {}
for key in i37.keys():
	if key == "trade":
		section3740[key] = list(set(i37[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section3740[key] = i37[key] + i40[key]


sections.append(section3740)


section3741 = {}
for key in i37.keys():
	if key == "trade":
		section3741[key] = list(set(i37[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section3741[key] = i37[key] + i41[key]


sections.append(section3741)


section3742 = {}
for key in i37.keys():
	if key == "trade":
		section3742[key] = list(set(i37[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section3742[key] = i37[key] + i42[key]


sections.append(section3742)


section3743 = {}
for key in i37.keys():
	if key == "trade":
		section3743[key] = list(set(i37[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section3743[key] = i37[key] + i43[key]


sections.append(section3743)


section3744 = {}
for key in i37.keys():
	if key == "trade":
		section3744[key] = list(set(i37[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section3744[key] = i37[key] + i44[key]


sections.append(section3744)


section3745 = {}
for key in i37.keys():
	if key == "trade":
		section3745[key] = list(set(i37[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section3745[key] = i37[key] + i45[key]


sections.append(section3745)


section3746 = {}
for key in i37.keys():
	if key == "trade":
		section3746[key] = list(set(i37[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section3746[key] = i37[key] + i46[key]


sections.append(section3746)


section3748 = {}
for key in i37.keys():
	if key == "trade":
		section3748[key] = list(set(i37[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section3748[key] = i37[key] + i48[key]


sections.append(section3748)


section3749 = {}
for key in i37.keys():
	if key == "trade":
		section3749[key] = list(set(i37[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section3749[key] = i37[key] + i49[key]


sections.append(section3749)


section3750 = {}
for key in i37.keys():
	if key == "trade":
		section3750[key] = list(set(i37[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section3750[key] = i37[key] + i50[key]


sections.append(section3750)


section3751 = {}
for key in i37.keys():
	if key == "trade":
		section3751[key] = list(set(i37[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section3751[key] = i37[key] + i51[key]


sections.append(section3751)


section3752 = {}
for key in i37.keys():
	if key == "trade":
		section3752[key] = list(set(i37[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section3752[key] = i37[key] + i52[key]


sections.append(section3752)


section3753 = {}
for key in i37.keys():
	if key == "trade":
		section3753[key] = list(set(i37[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section3753[key] = i37[key] + i53[key]


sections.append(section3753)


section3754 = {}
for key in i37.keys():
	if key == "trade":
		section3754[key] = list(set(i37[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section3754[key] = i37[key] + i54[key]


sections.append(section3754)


section3839 = {}
for key in i38.keys():
	if key == "trade":
		section3839[key] = list(set(i38[key] + i39[key]))
	if key == "intersection":
		pass
	else:
		section3839[key] = i38[key] + i39[key]


sections.append(section3839)


section3840 = {}
for key in i38.keys():
	if key == "trade":
		section3840[key] = list(set(i38[key] + i40[key]))
	if key == "intersection":
		pass
	else:
		section3840[key] = i38[key] + i40[key]


sections.append(section3840)


section3841 = {}
for key in i38.keys():
	if key == "trade":
		section3841[key] = list(set(i38[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section3841[key] = i38[key] + i41[key]


sections.append(section3841)


section3842 = {}
for key in i38.keys():
	if key == "trade":
		section3842[key] = list(set(i38[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section3842[key] = i38[key] + i42[key]


sections.append(section3842)


section3843 = {}
for key in i38.keys():
	if key == "trade":
		section3843[key] = list(set(i38[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section3843[key] = i38[key] + i43[key]


sections.append(section3843)


section3844 = {}
for key in i38.keys():
	if key == "trade":
		section3844[key] = list(set(i38[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section3844[key] = i38[key] + i44[key]


sections.append(section3844)


section3845 = {}
for key in i38.keys():
	if key == "trade":
		section3845[key] = list(set(i38[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section3845[key] = i38[key] + i45[key]


sections.append(section3845)


section3846 = {}
for key in i38.keys():
	if key == "trade":
		section3846[key] = list(set(i38[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section3846[key] = i38[key] + i46[key]


sections.append(section3846)


section3847 = {}
for key in i38.keys():
	if key == "trade":
		section3847[key] = list(set(i38[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section3847[key] = i38[key] + i47[key]


sections.append(section3847)


section3848 = {}
for key in i38.keys():
	if key == "trade":
		section3848[key] = list(set(i38[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section3848[key] = i38[key] + i48[key]


sections.append(section3848)


section3849 = {}
for key in i38.keys():
	if key == "trade":
		section3849[key] = list(set(i38[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section3849[key] = i38[key] + i49[key]


sections.append(section3849)


section3850 = {}
for key in i38.keys():
	if key == "trade":
		section3850[key] = list(set(i38[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section3850[key] = i38[key] + i50[key]


sections.append(section3850)


section3851 = {}
for key in i38.keys():
	if key == "trade":
		section3851[key] = list(set(i38[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section3851[key] = i38[key] + i51[key]


sections.append(section3851)


section3852 = {}
for key in i38.keys():
	if key == "trade":
		section3852[key] = list(set(i38[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section3852[key] = i38[key] + i52[key]


sections.append(section3852)


section3853 = {}
for key in i38.keys():
	if key == "trade":
		section3853[key] = list(set(i38[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section3853[key] = i38[key] + i53[key]


sections.append(section3853)


section3854 = {}
for key in i38.keys():
	if key == "trade":
		section3854[key] = list(set(i38[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section3854[key] = i38[key] + i54[key]


sections.append(section3854)


section3941 = {}
for key in i39.keys():
	if key == "trade":
		section3941[key] = list(set(i39[key] + i41[key]))
	if key == "intersection":
		pass
	else:
		section3941[key] = i39[key] + i41[key]


sections.append(section3941)


section3942 = {}
for key in i39.keys():
	if key == "trade":
		section3942[key] = list(set(i39[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section3942[key] = i39[key] + i42[key]


sections.append(section3942)


section3943 = {}
for key in i39.keys():
	if key == "trade":
		section3943[key] = list(set(i39[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section3943[key] = i39[key] + i43[key]


sections.append(section3943)


section3944 = {}
for key in i39.keys():
	if key == "trade":
		section3944[key] = list(set(i39[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section3944[key] = i39[key] + i44[key]


sections.append(section3944)


section3945 = {}
for key in i39.keys():
	if key == "trade":
		section3945[key] = list(set(i39[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section3945[key] = i39[key] + i45[key]


sections.append(section3945)


section3946 = {}
for key in i39.keys():
	if key == "trade":
		section3946[key] = list(set(i39[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section3946[key] = i39[key] + i46[key]


sections.append(section3946)


section3947 = {}
for key in i39.keys():
	if key == "trade":
		section3947[key] = list(set(i39[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section3947[key] = i39[key] + i47[key]


sections.append(section3947)


section3948 = {}
for key in i39.keys():
	if key == "trade":
		section3948[key] = list(set(i39[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section3948[key] = i39[key] + i48[key]


sections.append(section3948)


section3949 = {}
for key in i39.keys():
	if key == "trade":
		section3949[key] = list(set(i39[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section3949[key] = i39[key] + i49[key]


sections.append(section3949)


section3950 = {}
for key in i39.keys():
	if key == "trade":
		section3950[key] = list(set(i39[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section3950[key] = i39[key] + i50[key]


sections.append(section3950)


section3951 = {}
for key in i39.keys():
	if key == "trade":
		section3951[key] = list(set(i39[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section3951[key] = i39[key] + i51[key]


sections.append(section3951)


section3952 = {}
for key in i39.keys():
	if key == "trade":
		section3952[key] = list(set(i39[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section3952[key] = i39[key] + i52[key]


sections.append(section3952)


section3953 = {}
for key in i39.keys():
	if key == "trade":
		section3953[key] = list(set(i39[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section3953[key] = i39[key] + i53[key]


sections.append(section3953)


section3954 = {}
for key in i39.keys():
	if key == "trade":
		section3954[key] = list(set(i39[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section3954[key] = i39[key] + i54[key]


sections.append(section3954)


section4042 = {}
for key in i40.keys():
	if key == "trade":
		section4042[key] = list(set(i40[key] + i42[key]))
	if key == "intersection":
		pass
	else:
		section4042[key] = i40[key] + i42[key]


sections.append(section4042)


section4043 = {}
for key in i40.keys():
	if key == "trade":
		section4043[key] = list(set(i40[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section4043[key] = i40[key] + i43[key]


sections.append(section4043)


section4044 = {}
for key in i40.keys():
	if key == "trade":
		section4044[key] = list(set(i40[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section4044[key] = i40[key] + i44[key]


sections.append(section4044)


section4045 = {}
for key in i40.keys():
	if key == "trade":
		section4045[key] = list(set(i40[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section4045[key] = i40[key] + i45[key]


sections.append(section4045)


section4046 = {}
for key in i40.keys():
	if key == "trade":
		section4046[key] = list(set(i40[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section4046[key] = i40[key] + i46[key]


sections.append(section4046)


section4047 = {}
for key in i40.keys():
	if key == "trade":
		section4047[key] = list(set(i40[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section4047[key] = i40[key] + i47[key]


sections.append(section4047)


section4049 = {}
for key in i40.keys():
	if key == "trade":
		section4049[key] = list(set(i40[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section4049[key] = i40[key] + i49[key]


sections.append(section4049)


section4050 = {}
for key in i40.keys():
	if key == "trade":
		section4050[key] = list(set(i40[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section4050[key] = i40[key] + i50[key]


sections.append(section4050)


section4051 = {}
for key in i40.keys():
	if key == "trade":
		section4051[key] = list(set(i40[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section4051[key] = i40[key] + i51[key]


sections.append(section4051)


section4052 = {}
for key in i40.keys():
	if key == "trade":
		section4052[key] = list(set(i40[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section4052[key] = i40[key] + i52[key]


sections.append(section4052)


section4053 = {}
for key in i40.keys():
	if key == "trade":
		section4053[key] = list(set(i40[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section4053[key] = i40[key] + i53[key]


sections.append(section4053)


section4054 = {}
for key in i40.keys():
	if key == "trade":
		section4054[key] = list(set(i40[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section4054[key] = i40[key] + i54[key]


sections.append(section4054)


section4143 = {}
for key in i41.keys():
	if key == "trade":
		section4143[key] = list(set(i41[key] + i43[key]))
	if key == "intersection":
		pass
	else:
		section4143[key] = i41[key] + i43[key]


sections.append(section4143)


section4144 = {}
for key in i41.keys():
	if key == "trade":
		section4144[key] = list(set(i41[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section4144[key] = i41[key] + i44[key]


sections.append(section4144)


section4145 = {}
for key in i41.keys():
	if key == "trade":
		section4145[key] = list(set(i41[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section4145[key] = i41[key] + i45[key]


sections.append(section4145)


section4146 = {}
for key in i41.keys():
	if key == "trade":
		section4146[key] = list(set(i41[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section4146[key] = i41[key] + i46[key]


sections.append(section4146)


section4147 = {}
for key in i41.keys():
	if key == "trade":
		section4147[key] = list(set(i41[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section4147[key] = i41[key] + i47[key]


sections.append(section4147)


section4148 = {}
for key in i41.keys():
	if key == "trade":
		section4148[key] = list(set(i41[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section4148[key] = i41[key] + i48[key]


sections.append(section4148)


section4149 = {}
for key in i41.keys():
	if key == "trade":
		section4149[key] = list(set(i41[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section4149[key] = i41[key] + i49[key]


sections.append(section4149)


section4150 = {}
for key in i41.keys():
	if key == "trade":
		section4150[key] = list(set(i41[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section4150[key] = i41[key] + i50[key]


sections.append(section4150)


section4151 = {}
for key in i41.keys():
	if key == "trade":
		section4151[key] = list(set(i41[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section4151[key] = i41[key] + i51[key]


sections.append(section4151)


section4152 = {}
for key in i41.keys():
	if key == "trade":
		section4152[key] = list(set(i41[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section4152[key] = i41[key] + i52[key]


sections.append(section4152)


section4153 = {}
for key in i41.keys():
	if key == "trade":
		section4153[key] = list(set(i41[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section4153[key] = i41[key] + i53[key]


sections.append(section4153)


section4154 = {}
for key in i41.keys():
	if key == "trade":
		section4154[key] = list(set(i41[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section4154[key] = i41[key] + i54[key]


sections.append(section4154)


section4244 = {}
for key in i42.keys():
	if key == "trade":
		section4244[key] = list(set(i42[key] + i44[key]))
	if key == "intersection":
		pass
	else:
		section4244[key] = i42[key] + i44[key]


sections.append(section4244)


section4245 = {}
for key in i42.keys():
	if key == "trade":
		section4245[key] = list(set(i42[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section4245[key] = i42[key] + i45[key]


sections.append(section4245)


section4246 = {}
for key in i42.keys():
	if key == "trade":
		section4246[key] = list(set(i42[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section4246[key] = i42[key] + i46[key]


sections.append(section4246)


section4247 = {}
for key in i42.keys():
	if key == "trade":
		section4247[key] = list(set(i42[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section4247[key] = i42[key] + i47[key]


sections.append(section4247)


section4248 = {}
for key in i42.keys():
	if key == "trade":
		section4248[key] = list(set(i42[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section4248[key] = i42[key] + i48[key]


sections.append(section4248)


section4249 = {}
for key in i42.keys():
	if key == "trade":
		section4249[key] = list(set(i42[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section4249[key] = i42[key] + i49[key]


sections.append(section4249)


section4251 = {}
for key in i42.keys():
	if key == "trade":
		section4251[key] = list(set(i42[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section4251[key] = i42[key] + i51[key]


sections.append(section4251)


section4252 = {}
for key in i42.keys():
	if key == "trade":
		section4252[key] = list(set(i42[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section4252[key] = i42[key] + i52[key]


sections.append(section4252)


section4253 = {}
for key in i42.keys():
	if key == "trade":
		section4253[key] = list(set(i42[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section4253[key] = i42[key] + i53[key]


sections.append(section4253)


section4254 = {}
for key in i42.keys():
	if key == "trade":
		section4254[key] = list(set(i42[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section4254[key] = i42[key] + i54[key]


sections.append(section4254)


section4345 = {}
for key in i43.keys():
	if key == "trade":
		section4345[key] = list(set(i43[key] + i45[key]))
	if key == "intersection":
		pass
	else:
		section4345[key] = i43[key] + i45[key]


sections.append(section4345)


section4346 = {}
for key in i43.keys():
	if key == "trade":
		section4346[key] = list(set(i43[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section4346[key] = i43[key] + i46[key]


sections.append(section4346)


section4347 = {}
for key in i43.keys():
	if key == "trade":
		section4347[key] = list(set(i43[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section4347[key] = i43[key] + i47[key]


sections.append(section4347)


section4348 = {}
for key in i43.keys():
	if key == "trade":
		section4348[key] = list(set(i43[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section4348[key] = i43[key] + i48[key]


sections.append(section4348)


section4349 = {}
for key in i43.keys():
	if key == "trade":
		section4349[key] = list(set(i43[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section4349[key] = i43[key] + i49[key]


sections.append(section4349)


section4350 = {}
for key in i43.keys():
	if key == "trade":
		section4350[key] = list(set(i43[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section4350[key] = i43[key] + i50[key]


sections.append(section4350)


section4351 = {}
for key in i43.keys():
	if key == "trade":
		section4351[key] = list(set(i43[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section4351[key] = i43[key] + i51[key]


sections.append(section4351)


section4352 = {}
for key in i43.keys():
	if key == "trade":
		section4352[key] = list(set(i43[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section4352[key] = i43[key] + i52[key]


sections.append(section4352)


section4353 = {}
for key in i43.keys():
	if key == "trade":
		section4353[key] = list(set(i43[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section4353[key] = i43[key] + i53[key]


sections.append(section4353)


section4354 = {}
for key in i43.keys():
	if key == "trade":
		section4354[key] = list(set(i43[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section4354[key] = i43[key] + i54[key]


sections.append(section4354)


section4446 = {}
for key in i44.keys():
	if key == "trade":
		section4446[key] = list(set(i44[key] + i46[key]))
	if key == "intersection":
		pass
	else:
		section4446[key] = i44[key] + i46[key]


sections.append(section4446)


section4447 = {}
for key in i44.keys():
	if key == "trade":
		section4447[key] = list(set(i44[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section4447[key] = i44[key] + i47[key]


sections.append(section4447)


section4448 = {}
for key in i44.keys():
	if key == "trade":
		section4448[key] = list(set(i44[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section4448[key] = i44[key] + i48[key]


sections.append(section4448)


section4449 = {}
for key in i44.keys():
	if key == "trade":
		section4449[key] = list(set(i44[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section4449[key] = i44[key] + i49[key]


sections.append(section4449)


section4450 = {}
for key in i44.keys():
	if key == "trade":
		section4450[key] = list(set(i44[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section4450[key] = i44[key] + i50[key]


sections.append(section4450)


section4451 = {}
for key in i44.keys():
	if key == "trade":
		section4451[key] = list(set(i44[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section4451[key] = i44[key] + i51[key]


sections.append(section4451)


section4453 = {}
for key in i44.keys():
	if key == "trade":
		section4453[key] = list(set(i44[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section4453[key] = i44[key] + i53[key]


sections.append(section4453)


section4454 = {}
for key in i44.keys():
	if key == "trade":
		section4454[key] = list(set(i44[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section4454[key] = i44[key] + i54[key]


sections.append(section4454)


section4547 = {}
for key in i45.keys():
	if key == "trade":
		section4547[key] = list(set(i45[key] + i47[key]))
	if key == "intersection":
		pass
	else:
		section4547[key] = i45[key] + i47[key]


sections.append(section4547)


section4548 = {}
for key in i45.keys():
	if key == "trade":
		section4548[key] = list(set(i45[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section4548[key] = i45[key] + i48[key]


sections.append(section4548)


section4549 = {}
for key in i45.keys():
	if key == "trade":
		section4549[key] = list(set(i45[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section4549[key] = i45[key] + i49[key]


sections.append(section4549)


section4550 = {}
for key in i45.keys():
	if key == "trade":
		section4550[key] = list(set(i45[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section4550[key] = i45[key] + i50[key]


sections.append(section4550)


section4551 = {}
for key in i45.keys():
	if key == "trade":
		section4551[key] = list(set(i45[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section4551[key] = i45[key] + i51[key]


sections.append(section4551)


section4552 = {}
for key in i45.keys():
	if key == "trade":
		section4552[key] = list(set(i45[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section4552[key] = i45[key] + i52[key]


sections.append(section4552)


section4553 = {}
for key in i45.keys():
	if key == "trade":
		section4553[key] = list(set(i45[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section4553[key] = i45[key] + i53[key]


sections.append(section4553)


section4554 = {}
for key in i45.keys():
	if key == "trade":
		section4554[key] = list(set(i45[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section4554[key] = i45[key] + i54[key]


sections.append(section4554)


section4648 = {}
for key in i46.keys():
	if key == "trade":
		section4648[key] = list(set(i46[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section4648[key] = i46[key] + i48[key]


sections.append(section4648)


section4649 = {}
for key in i46.keys():
	if key == "trade":
		section4649[key] = list(set(i46[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section4649[key] = i46[key] + i49[key]


sections.append(section4649)


section4650 = {}
for key in i46.keys():
	if key == "trade":
		section4650[key] = list(set(i46[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section4650[key] = i46[key] + i50[key]


sections.append(section4650)


section4651 = {}
for key in i46.keys():
	if key == "trade":
		section4651[key] = list(set(i46[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section4651[key] = i46[key] + i51[key]


sections.append(section4651)


section4652 = {}
for key in i46.keys():
	if key == "trade":
		section4652[key] = list(set(i46[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section4652[key] = i46[key] + i52[key]


sections.append(section4652)


section4653 = {}
for key in i46.keys():
	if key == "trade":
		section4653[key] = list(set(i46[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section4653[key] = i46[key] + i53[key]


sections.append(section4653)


section4748 = {}
for key in i47.keys():
	if key == "trade":
		section4748[key] = list(set(i47[key] + i48[key]))
	if key == "intersection":
		pass
	else:
		section4748[key] = i47[key] + i48[key]


sections.append(section4748)


section4749 = {}
for key in i47.keys():
	if key == "trade":
		section4749[key] = list(set(i47[key] + i49[key]))
	if key == "intersection":
		pass
	else:
		section4749[key] = i47[key] + i49[key]


sections.append(section4749)


section4750 = {}
for key in i47.keys():
	if key == "trade":
		section4750[key] = list(set(i47[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section4750[key] = i47[key] + i50[key]


sections.append(section4750)


section4751 = {}
for key in i47.keys():
	if key == "trade":
		section4751[key] = list(set(i47[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section4751[key] = i47[key] + i51[key]


sections.append(section4751)


section4752 = {}
for key in i47.keys():
	if key == "trade":
		section4752[key] = list(set(i47[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section4752[key] = i47[key] + i52[key]


sections.append(section4752)


section4753 = {}
for key in i47.keys():
	if key == "trade":
		section4753[key] = list(set(i47[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section4753[key] = i47[key] + i53[key]


sections.append(section4753)


section4754 = {}
for key in i47.keys():
	if key == "trade":
		section4754[key] = list(set(i47[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section4754[key] = i47[key] + i54[key]


sections.append(section4754)


section4850 = {}
for key in i48.keys():
	if key == "trade":
		section4850[key] = list(set(i48[key] + i50[key]))
	if key == "intersection":
		pass
	else:
		section4850[key] = i48[key] + i50[key]


sections.append(section4850)


section4851 = {}
for key in i48.keys():
	if key == "trade":
		section4851[key] = list(set(i48[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section4851[key] = i48[key] + i51[key]


sections.append(section4851)


section4852 = {}
for key in i48.keys():
	if key == "trade":
		section4852[key] = list(set(i48[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section4852[key] = i48[key] + i52[key]


sections.append(section4852)


section4853 = {}
for key in i48.keys():
	if key == "trade":
		section4853[key] = list(set(i48[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section4853[key] = i48[key] + i53[key]


sections.append(section4853)


section4854 = {}
for key in i48.keys():
	if key == "trade":
		section4854[key] = list(set(i48[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section4854[key] = i48[key] + i54[key]


sections.append(section4854)


section4951 = {}
for key in i49.keys():
	if key == "trade":
		section4951[key] = list(set(i49[key] + i51[key]))
	if key == "intersection":
		pass
	else:
		section4951[key] = i49[key] + i51[key]


sections.append(section4951)


section4952 = {}
for key in i49.keys():
	if key == "trade":
		section4952[key] = list(set(i49[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section4952[key] = i49[key] + i52[key]


sections.append(section4952)


section4953 = {}
for key in i49.keys():
	if key == "trade":
		section4953[key] = list(set(i49[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section4953[key] = i49[key] + i53[key]


sections.append(section4953)


section4954 = {}
for key in i49.keys():
	if key == "trade":
		section4954[key] = list(set(i49[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section4954[key] = i49[key] + i54[key]


sections.append(section4954)


section5052 = {}
for key in i50.keys():
	if key == "trade":
		section5052[key] = list(set(i50[key] + i52[key]))
	if key == "intersection":
		pass
	else:
		section5052[key] = i50[key] + i52[key]


sections.append(section5052)


section5053 = {}
for key in i50.keys():
	if key == "trade":
		section5053[key] = list(set(i50[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section5053[key] = i50[key] + i53[key]


sections.append(section5053)


section5054 = {}
for key in i50.keys():
	if key == "trade":
		section5054[key] = list(set(i50[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section5054[key] = i50[key] + i54[key]


sections.append(section5054)


section5153 = {}
for key in i51.keys():
	if key == "trade":
		section5153[key] = list(set(i51[key] + i53[key]))
	if key == "intersection":
		pass
	else:
		section5153[key] = i51[key] + i53[key]


sections.append(section5153)


section5154 = {}
for key in i51.keys():
	if key == "trade":
		section5154[key] = list(set(i51[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section5154[key] = i51[key] + i54[key]


sections.append(section5154)


section5254 = {}
for key in i52.keys():
	if key == "trade":
		section5254[key] = list(set(i52[key] + i54[key]))
	if key == "intersection":
		pass
	else:
		section5254[key] = i52[key] + i54[key]


sections.append(section5254)




# %%
