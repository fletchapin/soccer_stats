During the Int’l Break, I simulated the remainder of the EPL season and found Liverpool had a 51% chance of winning the title:

* Obtained data from every match in the EPL this season
* Calculated average GF/GA both home and away for each team
* For each match remaining, averaged the home team’s GF and away team’s GA for expected goals for home team, and combined with similarly derived expected away goals to get an expected scoreline
* Ran 100 simulations of each match using a Poisson distribution of the expected goals\*
   * For a legitimate study there would be more trials, but this is just for fun anyway
* Calculated 100 league tables. Here's the results:

&#x200B;

**Aggregate Table:**

&#x200B;

Position | Club | Matches | Wins | Draws | Losses | GF | GA | GD | Points
:-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :--
1.49 | Liverpool | 38 | 27.11 | 8.64 | 2.25 | 83.07 | 24.32 | 58.75 | 89.97
1.51 | Man City | 38 | 28.33 | 3.96 | 5.71 | 93.81 | 29.3 | 64.51 | 88.95
3.88 | Tottenham | 38 | 23.69 | 3.01 | 11.3 | 70 | 42.24 | 27.76 | 74.08 
4.29 | Arsenal | 38 | 21.56 | 7.89 | 8.55 | 76.37 | 50.15 | 26.22 | 72.57
4.55 | Man Utd | 38 | 20.97 | 8.97 | 8.06 | 72.04 | 49.71 | 22.33 | 71.88
5.28 | Chelsea | 38 | 20.51 | 7.9 | 9.59 | 62.64 | 43.07 | 19.57 | 69.43
8.08 | Wolves| 38 | 15.11 | 9.85 | 13.04 | 48.93 | 46.47 |   2.46 | 55.18
8.09 | Watford | 38 | 15.48 | 8.81 | 13.71 | 54.05 | 54.13 | -0.08 | 55.25
9.46 | Leicester City | 38 | 15.1 | 6.7 | 16.2 | 50.42 | 51.86 | -1.44 | 52.00
10.32 | Everton| 38 | 13.74 | 8.66 | 15.6 | 53.03 | 51.89 | 1.14 | 49.88
10.55 | West Ham| 38 | 14.00 | 7.66 | 16.34 | 48.94 | 57.09 | -8.15 | 49.66 
12.74 | Bournemouth | 38 | 13.11 | 6.71 | 18.18 | 52.58 | 67.48 | -14.9 | 46.04 
13.36 | Crystal Palace| 38 | 12.02 | 7.97 | 18.01 | 46.85 | 51.54 | -4.69 | 44.03
13.38 | Brighton | 38 | 12.1 | 8.19 | 17.71 | 42.63 | 54.13 | -11.5 | 44.49 
14.26 | Newcastle | 38 | 10.96 | 9.77 | 17.27 | 38.15 | 49.86 | -11.71 | 42.65 
15.67 | Southampton | 38 | 9.59 | 11.14 | 17.27 | 44.25 | 61.88 | -17.63 | 39.91
16.48 | Burnley | 38 | 10.25 | 7.64 | 20.11 | 43.95 | 70.38 | -26.43 | 38.39
17.63 | Cardiff City | 38 | 9.57 | 5.92 | 22.51 | 35.09 | 72.11 | -37.02 | 34.63
19.14 | Fulham | 38 | 6.09 | 6.57 | 25.34 | 36.83 | 81.08 | -44.25 | 24.84
19.84 | Huddersfield | 38 | 4.46 | 6.54 | 27.00 | 24.1 | 69.04 | -44.94 | 19.92 

&#x200B;

**Final Position (%):**

&#x200B;

Club | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20
:-- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-:
Liverpool | 51 | 49 | | | | | | | | | | | | | | | | | |
Man City | 49 | 51 | | | | | | | | | | | | | | | | | |
Tottenham | | | 47| 27 | 17 | 9 | | | | | | | | | | | | | |
Arsenal | | | 25 | 33 | 30 | 12 | | | | | | | | | | | | | |
Man U | | | 20 | 28 | 29 | 23 | | | | | | | | | | | | | |
Chelsea | | | 8 | 12 | 24 | 56 | | | | | | | | | | | | | |
Wolves | | | | | | | 41 | 28 | 21 | 5 | 4 | | | 1 | | | | | |
Watford | | | | | | | 40 | 33 | 11 | 11 | 4 | 1 | | | | | | | |
West Ham | | | | | | | 2 | 5 | 17 | 27 | 22 | 18 | 6 | 3 | | | | | |
Leicester City | | | | | | | 12 | 21 | 23 | 22 | 8 | 6 | 5 | 3 | | | | | |
Everton | | | | | | | 5 | 11 | 19 | 20 | 18 | 16 | 8 | 1 | 2 | | | | |
Bournemouth | | | | | | | | 1 | 3 | 4 | 16 | 23 | 19 | 15 | 14 | 5 | | | |
Newcastle | | | | | | | | | 2 | 3 | 5 | 7 | 13 | 17 | 24 | 22 | 6 | 1 | |
Crystal Palace | | | | | | | | 1 | 3 | 2 | 13 | 12 | 19 | 22 | 12 | 13 | 3 | | |
Brighton | | | | | | | | | 1 | 5 | 9 | 15 | 25 | 18 | 14 | 10 | 1 | 2 | |
Southampton | | | | | | | | | | 1 | 1 | 2 | 3 | 14 | 16 | 29 | 29 | 5 | |
Burnley | | | | | | | | | | | | | 1 | 5 | 15 | 18 | 46 | 15 | |
Cardiff City | | | | | | | | | | | | | 1 | 1 | 3 | 3 | 15 | 75 | 2 |
Fulham | | | | | | | | | | | | | | | | | | 2 | 82 | 16
Huddersfield | | | | | | | | | | | | | | | | | | | 16 | 84

&#x200B;

Before discussing these a bit, I just wanted to point out that the **Final Position** table is in the order the table was in before the simulation, i.e. how it looked during the international break. The **Aggregate Table** is the average of Position, Record (W-L-D), Goals, and Points over the 100 simulations for each team, and is sorted by average position (e.g. note that Brighton has a higher average points total but worse average position so is lower. This interesting situation is most likely due to goal difference).

&#x200B;

As  I said before, this is obviously not scientific, especially due to the relatively small number of trials I performed, but I think it could start an interesting discussion. It gives a general idea of the the different "packs" that make up the table:

* Title Race: Liverpool and Man City. Essentially a coin flip
* Top 4 Tussle: Man United, Arsenal, Tottenham, Chelsea are all within 5 points of each other in the aggregate table, and the results over the weekend have only made that closer
* Fight for Europa League: This only applies if Man City wins the FA cup, but the fight for 7th and the possible final Europa League spot is tight between Watford and Wolves with Leicester and Everton having an outside chance.
* Midtable: West Ham and Bournemouth are comfortably clear of relegation, while Newcastle, Crystal Palace, and Brighton are closer but they look to be safe as well
* Relegation Battle: Huddersfield and Fulham are locks to go down. Southampton, Burnley, and Cardiff are all fighting not to be the third

I'd like to check back on this at the end of the season to see how accurate it is. Since it's using a relatively simple method to determine the expected goals and therefore scoreline, I'm interested in if more factors need to be incorporated to make accurate predictions.

&#x200B;

\*Based on *The Numbers Game: Why Everything You Know About Soccer Is Wrong*, goals in soccer are sufficiently independent and occur at constant enough rate to follow a Poisson distribution

Other references: 

[https://medium.com/@adamfreymiller/a-monte-carlo-simulation-of-the-2017-18-premier-league-season-3b7bbe8b8a13](https://medium.com/@adamfreymiller/a-monte-carlo-simulation-of-the-2017-18-premier-league-season-3b7bbe8b8a13)

[https://github.com/openfootball](https://github.com/openfootball)
