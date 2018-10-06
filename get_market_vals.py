# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 18:59:53 2018

@author: h_hof

Web Scraping Transfermarkt for ManCity v Cardiff City
"""

import requests
from bs4 import BeautifulSoup

import pandas as pd

# Header variable not to be blocked as scraping tool
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

def convertValueStringToInteger(value_string):
    ''' Convert a web-scraped string of a value into integer
        Example: 3,50 Mio. € ==> 3500000
    '''
    if len(value_string) < 2:
        return ''
    else:
        multipliers = {'Mio.': 1000000, 'Tsd.': 1000}
        try:
            exp = multipliers[value_string[1]]
        except KeyError:
            raise Exception('Unknown exponent: %s' % value_string[1])

        value = float(value_string[0].replace(',','.')) * exp
        return value

def getPlayerValues(page, headers):
    pageTree = requests.get(page, headers=headers)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    Players = pageSoup.find_all("a", {"class":"spielprofil_tooltip"})

    Values = pageSoup.find_all("td", {"class":"rechts hauptlink"})

    PlayersList = []
    ValuesList = []

    # TODO: assert len(Players) == len(Values), 'Non-matching Players and Values sizes'

#    for i in range(len(Players)):
#        PlayersList.append(Players[i].text)
#        ValuesList.append(Values[i].text)

    i=0;j=0
    while(j<len(Values)):
        PlayersList.append(Players[i].text)
        value_string = Values[j].text.split(' ')
        value = convertValueStringToInteger(value_string)
        ValuesList.append(value)
        i += 2; j += 1

    # Create Pandas dataframe
    df = pd.DataFrame({"Players":PlayersList, "Values":ValuesList})

    return df


if __name__ == '__main__':
    # Cardiff City
    cardiff_city_url = 'https://www.transfermarkt.de/cardiff-city/kader/verein/603'
    cardiffcity_df   = getPlayerValues(cardiff_city_url, headers)
    print(cardiffcity_df.head())

    # Man City
    man_city_url = 'https://www.transfermarkt.de/manchester-city/kader/verein/281'
    mancity_df = getPlayerValues(man_city_url, headers)
    print(mancity_df.head())
