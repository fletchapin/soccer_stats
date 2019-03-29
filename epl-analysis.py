import pandas as pd
import plotly as plt
from tabulate import tabulate


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
for j in range(poi_count):
    filepath = './Results/' + str(j) + '/epl-table-final.csv'
    table_csv = pd.read_csv(filepath)
    table_csv.drop(table_csv.columns[0], axis=1)
    winner = table_csv[table_csv['Position'] == 1]['Club'][0]
    if winner in winners:
        winners[winner] += 1
    else:
        winners[winner] = 1

    if j == 0:
        table_df = pd.read_csv(filepath)
        table_df = table_df.drop(table_df.columns[0], axis=1)
    else:
        table_df = agg_table(table_df, table_csv)

table_df = avg_table(table_df, poi_count)
table_df.to_csv('./Results/epl-table-agg.csv')

print(winners)
print(tabulate(table_df, headers='keys', tablefmt='psql', showindex=False))
