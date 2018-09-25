# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 18:23:15 2018

@author: h_hof
"""

import parsers
import requests
from bs4 import BeautifulSoup

import pandas as pd

base = 'https://www.transfermarkt.de'

league_page = 'https://www.transfermarkt.de/jumplist/startseite/wettbewerb/GB1'
header = parsers.headers

pageTree = requests.get(league_page, headers=header)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

teams = pageSoup.find_all("td", {"class":"hauptlink no-border-links hide-for-small hide-for-pad"})
team_pages = {}
for team in teams:
    name = team.text
    team_pages[name] = team.a['href']

#print(team_pages)

test = ('mancity', team_pages['Manchester City '])

cityTree = requests.get(base+league_page, headers=header)
citySoup = BeautifulSoup(cityTree.content, 'html.parser')

stuff = citySoup.find_all("a", {"name":"SubNavi", "text":"Kader im Detail"})
print(stuff)