import pandas as pd
import plotly as plt
from tabulate import tabulate


def add_to_dict(dict, entry):
    if entry in dict:
        dict[entry] += 1
    else:
        dict[entry] = 1


def agg_table(orig_df, add_df):
    #for team in orig_df['Club']:
        #team_stats = add_df[add_df['Club'] == team]
    orig_df['Position'] += add_df['Position']
    orig_df['Wins'] += add_df['Wins']
    orig_df['Draws'] += add_df['Draws']
    orig_df['Losses'] += add_df['Losses']
    orig_df['GA'] += add_df['GA']
    orig_df['GF'] += add_df['GF']
    orig_df['GD'] += add_df['GD']
    orig_df['Pts'] += add_df['Pts']

    return orig_df


def avg_table(orig_df, count):
    #for team in orig_df['Club']:
        #team_stats = add_df[add_df['Club'] == team]
    orig_df['Position'] = orig_df['Position'] / count
    orig_df['Wins'] = orig_df['Wins'] / count
    orig_df['Draws'] = orig_df['Draws'] / count
    orig_df['Losses'] = orig_df['Losses'] / count
    orig_df['GA'] = orig_df['GA'] / count
    orig_df['GF'] = orig_df['GF'] / count
    orig_df['GD'] = orig_df['GD'] / count
    orig_df['Pts'] = orig_df['Pts'] / count

    return orig_df


poi_count = 100
winners = {}
pos_dict = {}
for j in range(poi_count):
    filepath = './Results/' + str(j) + '/epl-table-final.csv'
    table_csv = pd.read_csv(filepath)
    table_csv.drop(table_csv.columns[0], axis=1)
    winner = table_csv.loc[table_csv['Position'] == 1, 'Club'].values[0]
    add_to_dict(winners, winner)

    if j == 0:
        table_df = pd.read_csv(filepath)
        table_df = table_df.drop(table_df.columns[0], axis=1)
    else:
        table_df = agg_table(table_df, table_csv)

    for team in table_csv['Club']:
        if j == 0:
            pos_dict[team] = {}
        pos = table_csv.loc[table_csv['Club'] == team, 'Position'].values[0]
        add_to_dict(pos_dict[team], pos)

table_df = avg_table(table_df, poi_count)
table_df.to_csv('./Results/epl-table-agg.csv')

# add in percentages, and convert NaN to ''
pos_df = pd.DataFrame(pos_dict).T
pos_df = pos_df.fillna('')
pos_df.to_csv('./Results/epl-pos-percent.csv')

print(winners)
print(tabulate(table_df, headers='keys', tablefmt='psql', showindex=False))
print(tabulate(pos_df, headers='keys', tablefmt='psql', showindex=True))
