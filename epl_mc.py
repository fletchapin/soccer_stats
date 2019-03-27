import pandas as pd
import plotly as plt

season_csv = pd.read_csv('epl-2018.csv')
table_csv = pd.read_csv('epl-table.csv')
output = pd.DataFrame(columns=['Club', 'GF Home', 'GF Away', 'GA Home', 'GA Away'])

def score_parser(index, awayFlag):
    score = season_csv['Result'][index]
    scoreArr = score.split("-")
    if awayFlag:
        goalsFor = int(scoreArr[1])
        goalsAgainst = int(scoreArr[0])
    else:
        goalsFor = int(scoreArr[0])
        goalsAgainst = int(scoreArr[1])
    return goalsFor, goalsAgainst


num_rows = season_csv['Date'].count()
for team in table_csv['Club']:
    gf_home = 0
    gf_away = 0
    ga_home = 0
    ga_away = 0
    i = 0
    while i < num_rows:
        if team == season_csv['Home Team'][i]:
            try:
                gf, ga = score_parser(i, False)
                gf_home = gf_home + gf
                ga_home = ga_home + ga
            except:
                break
        elif team == season_csv['Away Team'][i]:
            try:
                gf, ga = score_parser(i, True)
                gf_away = gf_away + gf
                ga_away = ga_away + ga
            except:
                break
        i = i + 1

    output = output.append({'Club': team, 'GF Home': gf_home,
                            'GF Away': gf_away, 'GA Home': ga_home,
                            'GA Away': ga_away}, ignore_index=True)


# create a Poisson distribution of expected goals
# conduct Monte Carlo simulation to determine remaining league results

# references:
# https://medium.com/@adamfreymiller/a-monte-carlo-simulation-of-the-2017-18-premier-league-season-3b7bbe8b8a13
# https://github.com/openfootball
