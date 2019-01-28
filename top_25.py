# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 19:42:14 2019

@author: akbar
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#with open('data.csv', 'rb') as f:
 #   reader = uc.DictReader(f)
  #  data = list(reader)

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

gk = top25_data[top25_data.Position == 'GK']
cb = top25_data[(top25_data.Position == 'CB') | (top25_data.Position == 'LCB') | (top25_data.Position == 'RCB')]
fb = top25_data[(top25_data.Position == 'RB') | (top25_data.Position == 'LB')]
cm = top25_data[(top25_data.Position == 'CM') | (top25_data.Position == 'RCM') | (top25_data.Position == 'LCM') | (top25_data.Position == 'CDM') | (top25_data.Position == 'CAM') | (top25_data.Position == 'RDM') | (top25_data.Position == 'LDM')]
wf = top25_data[(top25_data.Position == 'RW') | (top25_data.Position == 'LW') | (top25_data.Position == 'RF') | (top25_data.Position == 'LF')]
st = top25_data[(top25_data.Position == 'ST') | (top25_data.Position == 'RS') | (top25_data.Position == 'LS')]

total = len(gk) + len(cb) + len(fb) + len(cm) + len(wf) + len(st)
