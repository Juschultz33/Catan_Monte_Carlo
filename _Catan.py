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

Intersections_used = [20]

taken_section = []
for i in range(len(Intersections_used)):
	taken_section.extend(dicts[Intersections_used[i]-1]['intersection'])
# %%
# def sectionCombo(dicts, taken_section):
# 	for i in range(0,54):
# 		if (i + 1) not in taken_section:
# 			for j in range(1,55):
# 				if (i + 1) < j and j not in taken_section:
# 					if j in dicts[i]['intersection']:
# 						pass
# 					else: 
# 						section_name = f'section{i+1}<>{j}'
# 						print(f'{section_name} = {{}}')
# 						print(f'for key in i{i+1}.keys():')
# 						print('\tif key == "trade":')
# 						print(f'\t\t{section_name}[key] = list(set(i{i+1}[key] + i{j}[key]))')
# 						print('\tif key == "intersection":')
# 						print(f'\t\tpass')
# 						print('\telse:')
# 						print(f'\t\t{section_name}[key] = i{i+1}[key] + i{j}[key]')
# 						print('\n')
# 						print(f'sections.append({section_name})')
# 						print('\n')


sections = []

code_to_execute = ""

for i in range(0,54):
		if (i + 1) not in taken_section:
			for j in range(1,55):
				if ((i + 1) < j) and (j not in taken_section):
					if j in dicts[i]['intersection']:
						pass
					else:
						section_name = f'section{i+1}{j}'
						code_to_execute += f'{section_name} = {{}}\n'
						code_to_execute += f'for key in i{i+1}.keys():\n'
						code_to_execute += '\tif key == "trade":\n'
						code_to_execute += f'\t\t{section_name}[key] = list(set(i{i+1}[key] + i{j}[key]))\n'
						code_to_execute += '\tif key == "intersection":\n'
						code_to_execute += '\t\tpass\n'
						code_to_execute += '\telse:\n'
						code_to_execute += f'\t\t{section_name}[key] = i{i+1}[key] + i{j}[key]\n'
						code_to_execute += '\n'
						code_to_execute += f'sections.append({section_name})\n'
						code_to_execute += '\n'
                		# Add a print statement to debug
						print(f"Generated code for section {section_name}")

# Check the content of code_to_execute
print(code_to_execute)

# Now execute the generated code if it is not empty
if code_to_execute:
    exec(code_to_execute)
else:
    print("No code to execute")


# %%
mycode = sectionCombo(dicts, taken_section)
# %%
exec(sectionCombo(dicts, taken_section))
# %%
