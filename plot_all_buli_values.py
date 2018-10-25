import walker
import os
import matplotlib.pyplot as plt

from_data = walker.Walker()

fig, ax = plt.subplots()
fig.legend(prop={'size':18})

team_names = ['fc-schalke-04', 'tsg-1899-hoffenheim', 'borussia-dortmund', 'bayer-04-leverkusen',
              'rasenballsport-leipzig', 'vfb-stuttgart', 'eintracht-frankfurt', 'borussia-monchengladbach',
              'hertha-bsc', 'sv-werder-bremen', 'fc-augsburg', 'hannover-96', '1-fsv-mainz-05',
              'sc-freiburg', 'vfl-wolfsburg', 'fortuna-dusseldorf', '1-fc-nurnberg', 'fc-bayern-munchen']

for team in team_names:
    years, values = from_data.fetch_total_value(team, verbose=True)
    ax.plot(years, values, label=team)

ax.legend()
ax.set(xlabel='Year', ylabel='Total Team Market Value', title='Bundesliga\nMarket Values Over the Years')
ax.grid()

#fig.savefig("top_4_epl_mark_vals.png")
plt.show()
