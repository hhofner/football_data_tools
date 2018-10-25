# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:31:44 2018

@author: h_hof

Plot past years total team worth (value).
"""
import os
import csv
import matplotlib.pyplot as plt


teams = ['arsenal-fc', 'manchester-city', 'tottenham-hotspur', 'liverpool-fc']

cwd = os.getcwd()
data_dir = os.path.join(cwd, 'data')
values_dir = os.path.join(data_dir, 'values')

years = []
total_values = []
fig, ax = plt.subplots()
fig.legend(prop={'size':4})

for team in teams:
    years = []
    total_values = []
    for file_name in os.listdir(values_dir):
        if team in file_name:
            file_path = os.path.join(values_dir, file_name)
            year = file_name[-8:-4]
            years.append(int(year))
            with open(file_path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                total = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        try:
                            val = float(row[2])
                            total += val
                        except ValueError:
                            print('Cant convert %s value: %s to float' % (row[1], row[2]))
                            val = 0
                            total += val
                        line_count+=1
                total_values.append(total)

    print('Processed')
    ax.plot(years, total_values, label=team)

ax.legend()
ax.set(xlabel='Year', ylabel='Total Team Market Value', title='Top 4 EPL Teams\nMarket Values Over the Years')
ax.grid()

fig.savefig("top_4_epl_mark_vals.png")
plt.show()
