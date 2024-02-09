# example of classes
from pandas import DataFrame
# from sklearn.linear_model import LinearRegression
# from sklearn.ensemble import RandomForestClassifier

# all the class names have no spaces or underscores, 
# and a new word begins with a capital letter!
# classes in green color

# example of a function (no uppercase letters and can have underscores)
# function in yellow
# from sklearn.metrics import mean_absolute_error

# demonstrate how DataFrame is a class
import pandas as pd 

# Build my class of type DataFrame
# df holds a DataFrame "object"
# object is something made from a class and stored in a variable
# When I create a new object, I have "instantiated" that object, like below
# I create an instance after I run the line of code below

df = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6]})

if __name__ == '__main__':
# We have a class function aka constructor that allows us to instantiate
#   a dataframe object and save it to a variable df
    
# Attributes = Variables that form part of an "object" and are accessed
#   using dot-notation
#   Just to look up some values, no code invovled
    print(df.shape)
    print(df.dtypes)
    print(df.index)
    print(df.columns)

# Methods = functions that form part of an object (sometimes just called functions)
#   will run a code to perform these functions
    print(df.head())
    print(df.describe())
    print(df.isnull().sum())
    df['a'].value_counts()