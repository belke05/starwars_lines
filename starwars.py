# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 10:01:37 2019

@author: henri
"""

import pandas as pd, matplotlib.pyplot as plt, numpy as np
import matplotlib.pyplot as plt

script = open("data/SW_EpisodeVI.txt", "r").read()
script_list = script.split('\n')

print(*script_list,sep="\n")

script_list2 = [["id","character","dialogue"]]

for line in script_list[1:]:
    script_list2.append(line.split("\" \""))
    
print(*script_list2, sep="\n")

scriptlist3 = []
for x in script_list2:
    line = []
    for y in x:
        line.append(y.replace("\"", ''))
    scriptlist3.append(line)
    
print(*scriptlist3, sep="\n")


spoken_by = {}

for line in scriptlist3:
    if len(line) < 2:
        scriptlist3.remove(line)
        
        
# =============================================================================
for line in scriptlist3:
    if line[1] in spoken_by.keys():
        spoken_by[line[1]] += 1
    else:
         spoken_by[line[1]] = 1
         

print(spoken_by)

names = list(spoken_by.keys())
values = list(spoken_by.values())

df_starwars = pd.DataFrame(list(spoken_by.items()), columns=["characters", "Count"])
print(df_starwars)

df_starwars = df_starwars.sort_values('Count')
df_starwars.plot.bar(x='characters', y='Count')

charachter_list = df_starwars['characters'].tolist()[26:]
count_list = df_starwars['Count'].tolist()[26:]
print(charachter_list)
print(count_list)


 
index = np.arange(len(charachter_list))
plt.bar(index, count_list)
plt.xlabel('Character', fontsize=3)
plt.ylabel('No of lines', fontsize=3)
plt.xticks(index, charachter_list, fontsize=5, rotation=30)
plt.title('Lines per character')
plt.show()
# =============================================================================



plt.bar(range(len(spoken_by)),values,tick_label=names, width=0.3,align='center',color='skyblue')
plt.show()

plt.bar(list(spoken_by.keys()), spoken_by.values(), color='g')
plt.show()

np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
y_pos = np.arange(len(charachter_list))
line_count = count_list


ax.barh(y_pos, line_count ,align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(charachter_list, fontsize=6)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('line count')
ax.set_title('star wars episode 6 line counter')

for i in ax.patches:
    # get_width pulls left or right; get_y pushes up or down
    ax.text(i.get_width()+.1, i.get_y()+.31, \
            str(round((i.get_width()), 2)), fontsize=5, color='dimgrey')
plt.show()

#============================


