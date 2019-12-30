# Now that we have text metrics, a quick histogram spread on all metrics.

# Most script lines are under X characters, X lines, X words.
# Most script lines use around X unique words
# Lexical density is spread across, mostly curved up between X and X.

# Lexical density is pretty high considering how other singer's lyrics usually are.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df.hist(sharey=True, layout=(2, 3), figsize=(15, 8));

# Plot violin plots for distributions
cols_metrics = df.select_dtypes(include=[np.number]).columns
fig, axs = plt.subplots(ncols=len(cols_metrics), figsize=(16, 5))

# Word Length Distribution
pd.Series(len(x) for x in ' '.join(df.script).split()).value_counts().sort_index().plot(kind='bar', figsize=(12, 3))

# Looking at the word lengths, median length is 4 letters. But there exists decent long tail of longer length words.

# Most common script words without removing any stops works.
pd.Series(' '.join(df.script).lower().split()).value_counts()[:20][::-1].plot(kind='barh')

# Single words do not give much insight --the, a, you, i, and are most common

# Most common longer words
pd.Series([w for w in ' '.join(df.script).lower().split() if len(w) > 7]).value_counts()[:20][::-1].plot(kind = 'barh')

# Among the longer words (length > 7), combination of (christmas|welcome|grinch|whobilation) are most common.

# Most common n-grams
from nltk import ngrams

def get_ngrams_from_series(series, n=2):
    """Collocations, called n-grams, where we look aat collated phrases"""
    # using nltk.ngrams
    lines = ' '.join(series).lower().split('\n')
    lgrams = [ngrams(l.split(), n) for l in lines]
    grams = [[' '.join(g) for g in list(lg)] for lg in lgrams]
    return [item for sublist in grams for item in sublist]

pd.Series(get_ngrams_from_series(df.script, 2)).value_counts()[:20][::-1].plot(kind='barh')

# `the grinch` is the most common bi-gram with 17 occurrences.

# Top tri-grams
pd.Series(get_ngrams_from_series(df.script, 3)).value_counts()[:20][::-1].plot(kind='barh')

# Common tri-grams are the chair of, and now it's, and are also not very insightful.

