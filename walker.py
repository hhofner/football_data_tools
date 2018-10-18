# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 10:49:56 2018

@author: h_hof
"""
import os
import csv

class Walker(object):
    '''
    Walker object to parse the data collected and return 
    '''
    def __init__(self):
        self.data_dir   = os.path.join(os.getcwd(), 'data')
        self.values_dir = os.path.join(self.data_dir, 'values') 
    
    def fetch_total_value(self, team, year='0000', path='0000'):
        '''
        Fetches the total market value of a team for specified year. If no year
        is specified, then the '0000' is used indicating all years in the values
        directory.
        '''
        if path=='0000':
            path = self.values_dir
        if not os.path.exists(path):
            raise Exception('path {{%s}} does not exist' % path)
        if year=="0000":
            years  = []
            values = []
            for file_name in os.listdir(path):
                if team in file_name:
                    file_path = os.path.join(path, file_name)
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
                        values.append(total)
            return (years, values)
        else:
            try:
                year = int(year)
            except ValueError:
                print('Something is wrong with specified year: %s' % year)
            years  = [year]
            values = []
            for file_name in os.listdir(path):
                if (team in file_name) and (str(year) in file_name):
                    file_path = os.path.join(path, file_name)
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
                                    print('Cant convert %s value: {{%s}} to float' %  (row[1], row[2]))
                                    val = 0
                                    total += val
                                line_count += 1
                        values.append(total)
                    break
            # Double check the values and years have same length
            if len(years) != len(values):
                raise Exception('Years: {{%s}} and values: {{%s}} need to have same' 
                                'length' % (years, values))
            return (years, values)
        
if __name__ == '__main__':
    # Testing
    walker = Walker()
    years, values = walker.fetch_total_value('fc-bayern-munchen', '2010')
    print(years)
    print(values)