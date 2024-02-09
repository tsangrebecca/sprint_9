"""Part 2:
The exercise of writing these functions in Part 2 is helpful practice in learning how to geenrate random values.
The data structure of having tuples inside of a list is one that we'll see multiple times throughout Unit 3
so it's helpful to get familiar with it and to also be able to simulate our own versions of lists of tuples with fake data in them."""
# to follow pep 8 guidelines, we need to include doc strings '''xxx'''

import pandas as pd
import numpy as np
import random

# df = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6]})

# print(df.head())

adj = ['badass', 'delirious', 'mindnumbing', 'nuclear']
nou = ['butt', 'bread', 'sloth', 'fart', 'face']

def random_phrase():
    """Randomly select an adjective from a list of adjectives, a noun from a list of nouns, 
    then concatenate them returning them as a single string"""
    # random.choice returns 1 elements, random.sample can return more than 1!
    random_adjective = random.choice(adj)

    # random_noun = np.random.choice(nouns) # if we don't import random
    # OR
    # random_index = random.randint(0, len(nouns)-1)
    # random_noun = nouns[random_index]
    # OR
    # random_noun = random.sample(nouns, 1)[0] # return a list so we need to index[0] to choose the string
    random_noun = random.choice(nou)

    # return f"{random_adjective} {random_noun}"
    # OR
    return random_adjective + ' ' + random_noun

def random_float(min_val, max_val):
    """Returns a random float uniformly distributed between some min and max values."""
    return random.uniform(min_val, max_val)

def random_bowling_score():
    return random.randint(0, 300)

def random_rating_1dec(min_val, max_val):
    return round(random.uniform(min_val, max_val), 1)

def silly_tuple():  # that contains all 3 smaller functions
    # random_string = random_phrase(adj, nou)
    # rating = random_rating_1dec(1, 5)
    # bowling_score = random_bowling_score(0,300)
    return (random_phrase(), random_rating_1dec(1,5), random_bowling_score())

# list filled with silly tuples of a certain number
def silly_tuple_list(num_tuples):

    result = []
    for _ in range(num_tuples):
        result.append(silly_tuple())
    return result

if __name__ == '__main__':
    print(random_phrase())
    print(random_float(1, 100))
    print(random_bowling_score())
    print(random_rating_1dec(1,5))
    print(silly_tuple())
    print(silly_tuple_list(3))

"""Part 3:
Part 3 is a practice in writing functions that might truly be useful within a published Python package. We're writing functions that
we could theoretically import into other projects to help us do our work.

Remeber that it's only required that you implement 1 of the functions from part 3."""

# PART 3 FUNCTIONS ===========================================================================================================
    
# create a random dataframe
test_df = pd.DataFrame(np.array([[1,2,3], [4,5,6], [7,8,9]])) # these are the rows
null_df = pd.DataFrame(np.array([[1,2,np.nan], [4,5,np.nan], [7,8,9]]))

#-----------------------------------------------------------------------------------------------------------------------------
# check a dataframe for nulls and return the number of missing values
def null_count(df):
    '''Check a dataframe for nulls and return the number of missing values.'''
    return df.isnull().sum().sum()  # 1st .sum() is to sum up by the column, 2nd sum is sum up the columns
null_count(test_df)

#--------------------------------------------------------------------------------------------------------------------
# train test split
# Frac is the percent of data to set aside for training.
def train_test_split(df, frac=0.8):
    '''Create a train/test split function for a dataframe and returns both the training and testing sets
    '''
    # if the train test data split is not time-sensitive, we should shuffle them, otherwise, turn the shuffle off
    shuffled_df = df.sample(frac=1, random_state=42)

    # index to split the df
    split_index = int(frac * len(df))

    train_set = shuffled_df.iloc[:split_index] # everything up till the index. If time-sensitive, use df not shuffled_df
    test_set = shuffled_df.iloc[split_index:] # everything after the index
    return train_set, test_set

#-----------------------------------------------------------------------------------------------------------------------------------
# mix everything up in a dataframe with a random seed for reproducible randomization
def randomize(df, seed):
    """Develop a randomization function that randomizes all of a dataframes cells then returns that randomized dataframe
    """
    return df.sample(frac=1.0, random_state=seed)
    
#-----------------------------------------------------------------------------------------------------------------------------------
# split addresses into cities, states and zip codes
address_df = pd.DataFrame({'address':['890 Jennifer Brooks\nNorth Janet, WY 23785',
                                      '8394 Kim Meadow\nDarrenville, AK 27389',
                                      '379 Cain Plaza\nJosephburgh, WY 06332',
                                      '5303 Tina Hill\nAudreychester, VA 97036']}) # a single column dataframe
    
def addy_split(addy_series):
    """
    Split addresses into 3 columns (df['city], df['state'], and df['zip']). 
    You can use regexes to detect the format and pull out important pieces.
    """
    df = pd.DataFrame()
    city_list = []
    state_list = []
    zip_list = []

    for addy in addy_series:
        # break up the address into strings
        second_half = addy.split('\n')[1] # grab the 2nd item after the split which contains the city, state and zip code
        city = second_half.split(',')[0]
        state = second_half.split(' ')[-2]
        zip = second_half.split(' ')[-1]

        # add the strings to the lists
        city_list.append(city)
        state_list.append(state)
        zip_list.append(zip)

    # add the lists as new columns on the df
    df['city'] = city_list
    df['state'] = state_list
    df['zip'] = zip_list

    return df

#---------------------------------------------------------------------------------------------------------------------------------
# Turn abbreviations to state names spelled out
state_dict = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

# extract the state column in the addy dataframe
addy_states = addy_split(address_df['address'])['state'] # 1st part is the new df we created with 3 columns of city, state and zip, and we're calling the state column

def abbr_2_st(state_series, abbr_2_st=True): # toggle between name to abbrev and abbrev to name based on Boolean
    """
    Return a new column with the full name from a state abbreviation column eg input of FL will return Florida
    """
    # functions within a function
    def abbrev_replace(abbrev):
        return state_dict[abbrev]  # go to dictionary to get the state name
    def state_replace(state_name): # do the opposite
        reverse_state_dict = dict((v, k) for k, v in state_dict.items()) # swapping key values pairs in dict
        return reverse_state_dict[state_name]
    
    if abbr_2_st:
        return state_series.apply(abbrev_replace) # go to the column and apply that function row by row
    else:
        return state_series.apply(state_replace)

# to test the reverse we need a column of state names
full_state_names_column = abbr_2_st(addy_states)
#---------------------------------------------------------------------------------------------------------------------------------
# take a list and df and turn list into a series as a new column in the df
def list_2_series(list_2_series, df):
    """
    Single function to take a list and dataframe, turn it into a series and add it to a dataframe as a new column.
    """
    new_column = pd.Series(list_2_series)
    return pd.concat([df, new_column], axis=1) # specify axis to make sure it's column not row

#---------------------------------------------------------------------------------------------------------------------------------
outlier_df = pd.DataFrame(
    {'a': [1,2,3,4,5,6],
     'b': [4,5,6,7,8,9],
     'c': [7,1000,9,10,11,12]})

def rm_outliers(df): # according to 1.5 interquartile rule
    """
    A 1.5*interquartile range outlier detection/removal function that gets rid of outlying rows
    and returns the outlier-cleaned dataframe.
    """
    cleaned_df = pd.DataFrame()
    for (columnName, columnData) in df.iteritems():
        Q1 = columnData.quantile(0.25)
        Q3 = columnData.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5*IQR 
        upper_bound = Q3 + 1.5*IQR     
        # print(lower_bound, upper_bound)    

        mask = columnData.between(lower_bound, upper_bound, inclusive='both')       
        cleaned = columnData.loc[mask]
        # print(columnName, cleaned)
        cleaned_df[columnName] = cleaned
    return cleaned_df

#------------------------------------------------------------------------------------------------------------------------------
dates_column = pd.Series(['01/13/2016', '02/14/2017', '03/15/2018', '04/16/2019'])         
def split_dates(date_series):
    """
    Function to split dates of forma 'MM/DD/YYYY' into multiple columns 
    (df['month'], df['day'], df['year']) then return the same dataframe with those additional columns"""
    # assume it's MM/DD/YYYY
    df = pd.DataFrame()
    
    month_list = []
    day_list = []
    year_list = []

    for date in date_series:
        month_list.append(date.split('/')[0])
        day_list.append(date.split('/')[1])
        year_list.append(date.split('/')[2])

    df['month'] = month_list
    df['day'] = day_list
    df['year'] = year_list

    return df
  
#=============================================================================================================================
# section below only for printing outcomes when run as scripts but not run as modules
if __name__ == '__main__':
    print(null_count(null_df))
    print(train_test_split(test_df))
    print(randomize(test_df, 10))
    print(addy_split(address_df['address']))
    print(abbr_2_st(addy_states))
    print(abbr_2_st(full_state_names_column, abbr_2_st=False))
    print(list_2_series([10,11,12], test_df))
    print(rm_outliers(outlier_df))
    print(split_dates(dates_column))