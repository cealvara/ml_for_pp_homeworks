import pandas as pd

# 1. Read Data: For this assignment, assume input is CSV and write a function 
# that can read a csv into python

def read_data(filename):
    if '.csv' in filename:
        data = pd.read_csv(filename)
    elif '.dta':
        data = pd.read_stata(filename)

    return data

# 2. Explore Data: You can use the code you wrote for assignment 1 here to 
# generate distributions and data summaries.

def describe_column(df, columnname):
    print(df[columnname].describe)
    #add number of unique values, missing values, other interesting stats

def tabular(df, columnname):
    #number of complaints by type
    ctcounts = df[columnname].value_counts().to_frame()
    total = sum(ctcounts[columnname])
    ctcounts['Percent'] = ctcounts[columnname]/total
    print(ctcounts.sort)

def histogram(df, columnname):
    #create histogram

# 3. Pre-Process Data: For this assignment, you can limit this to filling in 
# missing values for the variables that have missing values. You can use any 
# simple method to do it (use mean to fill in missing values).

def fill_miss(df):
    pass

# 4. Generate Features/Predictors: For this assignment, you should write one 
# function that can discretize a continuous variable and one function that can 
# take a categorical variable and create binary/dummy variables from it. Apply 
# them to at least one variable each in this data.

def discretize(df, var):
    pass

def make_dummies(df, var):
    pass

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