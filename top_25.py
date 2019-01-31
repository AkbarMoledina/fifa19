# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 19:42:14 2019

@author: akbar
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


data = pd.read_csv('data.csv')
top25_data = data.head(25)

print('The top 25 players in Fifa 19 are:')
print(top25_data['Name'])
mean_overall = np.mean(top25_data['Overall'])
median_overall = np.median(top25_data['Overall'])
print('the mean Overall rating is', mean_overall)
print('the median Overall rating is', median_overall)

plt.xlabel('Player Name')
plt.ylabel('Overall Rating')
bar = plt.bar(top25_data['Name'], top25_data['Overall'])
plt.xticks(rotation='vertical')
plt.ylim(88, 95)
plt.show()

plt.xlabel('Age')
plt.ylabel('Number of Players')
ax = plt.hist(top25_data['Age'], bins=10)
plt.show()

print('27 year old players:')
print(top25_data['Name'][top25_data['Age'] == 27], '\n')
print('33 year old players:')
print(top25_data['Name'][top25_data['Age'] == 32], '\n')


columns_to_drop = ['ID', 'Age', 'Photo', 'Nationality', 'Flag', 'Overall', 'Potential', 'Club', 
                   'Club Logo', 'Value', 'Wage', 'Special', 'Preferred Foot',
                   'International Reputation', 'Weak Foot', 'Skill Moves', 'Work Rate', 'Body Type', 'Real Face', 
                   'Jersey Number', 'Joined', 'Loaned From', 
                   'Contract Valid Until', 'Height', 'Weight', 'Release Clause',
                   'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW', 'LAM', 
                   'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
                   'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB']
attributes = top25_data.drop(labels=columns_to_drop, axis=1)

gk = attributes[attributes.Position == 'GK'].drop(labels='Position', axis=1)
cb = attributes[(attributes.Position == 'CB') | (attributes.Position == 'LCB') | (attributes.Position == 'RCB')].drop(labels='Position', axis=1)
fb = attributes[(attributes.Position == 'RB') | (attributes.Position == 'LB')].drop(labels='Position', axis=1)
cm = attributes[(attributes.Position == 'CM') | (attributes.Position == 'RCM') | (attributes.Position == 'LCM') | (attributes.Position == 'CDM') | (attributes.Position == 'CAM') | (attributes.Position == 'RDM') | (attributes.Position == 'LDM')].drop(labels='Position', axis=1)
wf = attributes[(attributes.Position == 'RW') | (attributes.Position == 'LW') | (attributes.Position == 'RF') | (attributes.Position == 'LF')].drop(labels='Position', axis=1)
st = attributes[(attributes.Position == 'ST') | (attributes.Position == 'RS') | (attributes.Position == 'LS')].drop(labels='Position', axis=1)

total = len(gk) + len(cb) + len(fb) + len(cm) + len(wf) + len(st)


def get_best_stats(data, threshold=85):
    all_stats = data.max().drop(labels='Name')
    best_columns = ['Name'] + list(all_stats[all_stats >= threshold].index)
    best_stats = data[best_columns]
    return best_stats


gk_best_stats = get_best_stats(gk)
print(gk_best_stats)
print(gk_best_stats.mean().round(1))

cb_best_stats = get_best_stats(cb)
print(cb_best_stats)
print(cb_best_stats.mean().round(1))

cm_best_stats = get_best_stats(cm)
print(cm_best_stats)
print(cm_best_stats.mean().round(1))

wf_best_stats = get_best_stats(wf)
print(wf_best_stats)
print(wf_best_stats.mean().round(1))

st_best_stats = get_best_stats(st)
print(st_best_stats)
print(st_best_stats.mean().round(1))
