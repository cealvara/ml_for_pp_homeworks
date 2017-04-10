import pandas as pd
import numpy as np

# 1. Read Data: For this assignment, assume input is CSV and write a function 
# that can read a csv into python

def read_data(filename):
    data = pd.read_csv(filename)

    return data

# 2. Explore Data: You can use the code you wrote for assignment 1 here to 
# generate distributions and data summaries.

def varnames(df):
    print(df.columns)

def explore(df):
    df.describe()
    pass

# 3. Pre-Process Data: For this assignment, you can limit this to filling in 
# missing values for the variables that have missing values. You can use any 
# simple method to do it (use mean to fill in missing values).

def fill_miss(df):
    pass

# 4. Generate Features/Predictors: For this assignment, you should write one 
# function that can discretize a continuous variable and one function that can 
# take a categorical variable and create binary/dummy variables from it. Apply 
# them to at least one variable each in this data.

def discretize(df, varname, nbins, cut_type='quantile'):
    '''
    Discretizes given "varname" into "nbins".

    Inputs:
            - df: name of pandas DataFrame
            - varname: name of variable to be discretized
            - nbins: number of categories to create
            - cut_type: can be 'quantile', 'uniform', 'linspace' or 'logspace'

    Returns: nothing. Modifies "df" in place
    '''
    accepted_cut_types = ['quantile', 'uniform', 'linspace', 'logspace']

    assert varname in df.columns, "Column '{}' not found in DataFrame".format(varname)

    assert len(df[varname].value_counts()) > nbins, "Number of bins too large"

    assert cut_type in accepted_cut_types, "Given cut_type not allowed"


    if cut_type == 'quantile':
        df[varname+'_cat'] = pd.qcut(df[varname], nbins)
    elif cut_type == 'uniform':
        df[varname+'_cat'] = pd.cut(df[varname], nbins)
    elif cut_type == 'linspace':
        minval = min(df[varname])
        maxval = max(df[varname])
        bins = np.linspace(minval, maxval, nbins+1)
        df[varname+'_cat'] = pd.cut(df[varname], bins, include_lowest=True)
    elif cut_type == 'logspace':
        minval = min(df[varname])
        maxval = max(df[varname])
        
        assert maxval > 0, 'Column {} has only negative or zero numbers'.format(varname)

        if minval <= 0:
            print('Warning, {} has negative or zero values'.format(varname))
            minval = 0.0001

        bins = np.logspace(np.log10(minval), np.log10(maxval), num = nbins+1)
        df[varname+'_cat'] = pd.cut(df[varname], bins, include_lowest=True)


def make_dummies(df, varname):
    '''
    Creates a set of dummies out of "varname"
    '''
    for i, value in enumerate(df[varname].unique()):
        print(type(value), value)
        df[varname+'_{}'.format(value)] = df[varname] == value


# 5. Build Classifier: For this assignment, select any classifier you feel 
# comfortable with (Logistic Regression for example)

def classify(df, var):
    pass
# 6. Evaluate Classifier: you can use any metric you choose for this assignment 
# (accuracy is the easiest one). Feel free to evaluate it on the same data you 
# built the model on (this is not a good idea in general but for this assignment, 
#     it is fine). We haven't covered models and evaluation yet, so don't worry 
# about creating validation sets or cross-validation. 

def evaluate(df, var):
    pass