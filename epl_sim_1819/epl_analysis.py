import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate


def add_to_dict(dict, entry):
    if entry in dict:
        dict[entry] += 1
    else:
        dict[entry] = 1


def agg_table(orig_df, add_df, j):
    add_df = add_df.sort_values('Unnamed: 0', 0, True)
    add_df = add_df.drop(add_df.columns[0], axis=1)

    orig_df['Position'] = orig_df['Position'].values + add_df['Position'].values
    orig_df['Wins'] = orig_df['Wins'].values + add_df['Wins'].values
    orig_df['Draws'] = orig_df['Draws'].values  + add_df['Draws'].values
    orig_df['Losses'] = orig_df['Losses'].values + add_df['Losses'].values
    orig_df['GA'] = orig_df['GA'].values + add_df['GA'].values
    orig_df['GF'] = orig_df['GF'].values + add_df['GF'].values
    orig_df['GD'] = orig_df['GD'].values + add_df['GD'].values
    orig_df['Pts'] = orig_df['Pts'].values + add_df['Pts'].values

    return orig_df


def avg_table(orig_df, count):
    orig_df['Position'] = orig_df['Position'] / count
    orig_df['Wins'] = orig_df['Wins'] / count
    orig_df['Draws'] = orig_df['Draws'] / count
    orig_df['Losses'] = orig_df['Losses'] / count
    orig_df['GA'] = orig_df['GA'] / count
    orig_df['GF'] = orig_df['GF'] / count
    orig_df['GD'] = orig_df['GD'] / count
    orig_df['Pts'] = orig_df['Pts'] / count

    return orig_df


pos_dict = {}
for team in pd.read_csv('epl-table.csv')['Club']:
    pos_dict[team] = {}

poi_count = 100
winners = {}
for j in range(poi_count):
    filepath = './Results/' + str(j) + '/epl-table-final.csv'
    table_csv = pd.read_csv(filepath)
    winner = table_csv.loc[table_csv['Position'] == 1, 'Club'].values[0]
    add_to_dict(winners, winner)

    if j == 0:
        table_df = pd.read_csv(filepath)
        table_df = table_df.sort_values('Unnamed: 0', 0, True)
        table_df = table_df.drop(table_df.columns[0], axis=1)
    else:
        table_df = agg_table(table_df, table_csv, j)

    for team in table_csv['Club']:
        pos = table_csv.loc[table_csv['Club'] == team, 'Position'].values[0]
        add_to_dict(pos_dict[team], pos)

table_df = avg_table(table_df, poi_count)
table_df = table_df.sort_values(['Position'], 0, True)
table_df.to_csv('./Results/epl-table-agg.csv')

pos_df = pd.DataFrame(pos_dict).T
pos_df = pos_df.fillna('')
pos_df.to_csv('./Results/epl-pos-percent.csv')

print(winners)
print(tabulate(table_df, headers='keys', tablefmt='psql', showindex=False))
print(tabulate(pos_df, headers='keys', tablefmt='psql', showindex=True))
