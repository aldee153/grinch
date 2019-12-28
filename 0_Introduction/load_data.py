#0. Introduction
# This the grinch script, Jim Carrey version, it will be utilizing movie scripts.
# We will attempt to do the following:

# Derive metrics from raw text, visualize distributions.
# Tell stories though visuals.
# Sentiment analysis.
# Random script generator with Markov Chains.
# Extract themes automatically aka topic modelling.
# Dependencies: Pandas, Numpy, Seaborn, NLTK, scikit-learn.

# Load data
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(context='talk', style='ticks')
%matplotlib inline

# Read in data
df = pd.read_csv("data/grinch_script.csv")

# Check first lines of data frame.
df.head()

# Take a closer look
df.loc[0, 'script']

