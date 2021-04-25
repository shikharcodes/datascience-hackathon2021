import pandas as pd

# read data from csv file into a pandas dataFrame
with open('.//ipl csv2//all_matches.csv') as f: 
    ipl_data = pd.read_csv(f)

# print all columns
# print (data.columns)
# all columns

# ['match_id', 'season', 'start_date', 'venue', 'innings', 'ball', 'batting_team, bowling_team', 'striker', 'non_striker', 'bowler', 'runs_off_bat', 'extras', 'wides', 'noballs', 'byes', 'legbyes', 'penalty', 'wicket_type', 'player_dismissed', 'other_wicket_type', 'other player_dismissed']

relevantColumns= ['match_id', 'venue', 'innings', 'ball','batting_team', 'bowling_team', 'striker', 'non_striker','bowler', 'runs_off_bat', 'extras', 'wides', 'noballs', 'byes', 'legbyes', 'penalty']

ipl data ipl_data[relevantColumns]

# create another column that tells number of runs scored, including off the bat and
# extra runs conceded by bowling team 
ipl_data['total_runs']=ipl_data['runs_off_bat']+ipl_data['extras']

# now drop the columns runs off bat and extras as they are not required anymore. 

ipl_data= ipl_data.drop(columns=['runs_off_bat', 'extras'])

# only select rows belonging to first 6 overs

ipl_data = ipl_data[ipl_data['ball'] <= 5.6]

ipl_data = ipl_data[ipl_data[innings] <= 2]

# preprocess the data so that we get a tuple of following kind in each row: # 
# ('match_id', 'venue, 'innings', 'batting_team", "bowling team', 'total_runs

ipl_data= ipl_data.groupby(['match_id','venue', 'innings','batting team','bowling team']).total_runs.sum()

# convert back to dataframe
ipl_data= ipl_data.reset_index()

ipl_data=ipl_data.drop(columns=['match_id'])

ipl_data.to_csv ("myPreprocessed.csv", index=False)

# print('ts type is ipl data.columns)
