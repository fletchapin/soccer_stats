import pandas as pd
import plotly as plt
import numpy as np
import numpy.random as rd

season_csv = pd.read_csv('epl-2018.csv')
table_csv = pd.read_csv('epl-table.csv')
goals_df = pd.DataFrame(columns=['Club', 'Avg GF Home', 'Avg GF Away',
                                 'Avg GA Home', 'Avg GA Away'])


# parses the score and returns goals for and against
def score_parser(index, awayFlag, df=season_csv):
    score = df['Result'][index]
    scoreArr = score.split("-")
    if awayFlag:
        goalsFor = int(scoreArr[1])
        goalsAgainst = int(scoreArr[0])
    else:
        goalsFor = int(scoreArr[0])
        goalsAgainst = int(scoreArr[1])
    return goalsFor, goalsAgainst


# get avg home/away goals for/against for each team
played_matches = season_csv[season_csv['Result'].notna()]
num_rows = played_matches['Date'].count()
for team in table_csv['Club']:
    gf_home = 0
    gf_away = 0
    ga_home = 0
    ga_away = 0
    i = 0
    while i < num_rows:
        if team == season_csv['Home Team'][i]:
            try:
                gf, ga = score_parser(i, False, played_matches)
                gf_home = gf_home + gf
                ga_home = ga_home + ga
            except:
                break
        elif team == season_csv['Away Team'][i]:
            try:
                gf, ga = score_parser(i, True, played_matches)
                gf_away = gf_away + gf
                ga_away = ga_away + ga
            except:
                break
        i = i + 1

    num_home = table_csv['Home Matches'][table_csv['Club'] == team].iloc[0]
    num_away = table_csv['Away Matches'][table_csv['Club'] == team].iloc[0]
    avg_gf_home = gf_home / num_home
    avg_gf_away = gf_away / num_home
    avg_ga_home = ga_home / num_away
    avg_ga_away = ga_away / num_away

    goals_df = goals_df.append({'Club': team, 'Avg GF Home': avg_gf_home,
                                'Avg GF Away': avg_gf_away,
                                'Avg GA Home': avg_ga_home,
                                'Avg GA Away': avg_ga_away}, ignore_index=True)

# get list of matches remaining which need to be predicted
calc_df = pd.DataFrame(columns=['Home Team', 'Away Team', 'Ex HG', 'Ex AG'])
remaining_matches = season_csv[season_csv['Result'].isna()]
for i in range(remaining_matches['Date'].count()):
    home_team = remaining_matches['Home Team'].iloc[i]
    away_team = remaining_matches['Away Team'].iloc[i]

    ex_hgf = goals_df[goals_df['Club'] == home_team]['Avg GF Home'].iloc[0]
    ex_hga = goals_df[goals_df['Club'] == home_team]['Avg GA Home'].iloc[0]

    ex_agf = goals_df[goals_df['Club'] == away_team]['Avg GF Away'].iloc[0]
    ex_aga = goals_df[goals_df['Club'] == away_team]['Avg GA Away'].iloc[0]

    # TODO: fancier weighted average here
    exg_home = (ex_hgf + ex_aga) / 2
    exg_away = (ex_agf + ex_hga) / 2

    # run poisson 1000 times per match, round avg score to nearest whole number
    poi_home = np.mean(rd.poisson(exg_home, 1000))
    poi_away = np.mean(rd.poisson(exg_away, 1000))

    calc_df = calc_df.append({'Home Team': home_team, 'Away Team': away_team,
                              'Ex HG': exg_home, 'Ex AG': exg_away,
                              'Poisson HG': poi_home, 'Poisson AG': poi_away},
                             ignore_index=True)

    score = str(int(np.round(poi_home))) + ' - ' + str(int(np.round(poi_away)))
    remaining_matches['Result'].iloc[i] = score

remaining_matches.to_csv('epl-results-1819')

# TODO: update table based on these results

# references:
# https://medium.com/@adamfreymiller/a-monte-carlo-simulation-of-the-2017-18-premier-league-season-3b7bbe8b8a13
# https://github.com/openfootball
